/**
 * 娃娘手帐 — 主程序（与 storage / ledger 解耦，便于以后接后端）
 */
(function () {
  var dolls = [];
  var inspirations = [];
  var wardrobes = [];
  var makeups = [];
  var reminders = [];

  var sizeFilter = '';
  var artistFilter = '';
  var tagFilter = '';
  var searchKeyword = '';
  var ledgerSeg = 'doll';

  var currentGalleryDoll = null;
  var secondaryView = null;
  var mainTab = 'inventory';

  var pendingInspoImg = null;

  var LS_LAST_BACKUP_MS = 'bjd_last_backup_export_ms';
  var BACKUP_NUDGE_AFTER_DAYS = 14;

  function showToast(msg) {
    var t = document.createElement('div');
    t.className = 'toast';
    t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(function () {
      t.remove();
    }, 2200);
  }

  function escapeHtml(str) {
    return String(str || '').replace(/[&<>]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c];
    });
  }

  function moneyDisplay(n) {
    var v = Number(n) || 0;
    return '¥' + v.toLocaleString('zh-CN', { maximumFractionDigits: 2 });
  }

  function formatBytes(n) {
    if (n < 1024) return n + ' B';
    if (n < 1024 * 1024) return (n / 1024).toFixed(1) + ' KB';
    return (n / (1024 * 1024)).toFixed(2) + ' MB';
  }

  function todayISODate() {
    return new Date().toISOString().slice(0, 10);
  }

  function compressImage(file, maxSize, quality) {
    return new Promise(function (res, rej) {
      var reader = new FileReader();
      reader.onload = function (e) {
        var img = new Image();
        img.onload = function () {
          var w = img.width;
          var h = img.height;
          if (w > maxSize) {
            h = (h * maxSize) / w;
            w = maxSize;
          }
          var c = document.createElement('canvas');
          c.width = w;
          c.height = h;
          c.getContext('2d').drawImage(img, 0, 0, w, h);
          res(c.toDataURL('image/jpeg', quality));
        };
        img.onerror = rej;
        img.src = e.target.result;
      };
      reader.onerror = rej;
      reader.readAsDataURL(file);
    });
  }

  function dollDeletionImpact(dollId) {
    var doll = dolls.find(function (d) {
      return d.id === dollId;
    });
    var photoN = doll && doll.photos ? doll.photos.length : 0;
    return {
      makeups: makeups.filter(function (m) {
        return m.dollId === dollId;
      }).length,
      wardrobes: wardrobes.filter(function (w) {
        return w.dollId === dollId;
      }).length,
      reminders: reminders.filter(function (r) {
        return r.dollId === dollId;
      }).length,
      inspirations: inspirations.filter(function (i) {
        return i.dollId === dollId;
      }).length,
      photos: photoN,
    };
  }

  function dollDeletionConfirmMessage(dollId) {
    var imp = dollDeletionImpact(dollId);
    var parts = [];
    if (imp.makeups) parts.push('妆面 ' + imp.makeups + ' 条');
    if (imp.wardrobes) parts.push('衣橱 ' + imp.wardrobes + ' 条');
    if (imp.reminders) parts.push('日程 ' + imp.reminders + ' 条');
    if (imp.inspirations) parts.push('灵感关联 ' + imp.inspirations + ' 条（将改为未关联）');
    if (imp.photos) parts.push('相册照片约 ' + imp.photos + ' 张');
    var head =
      parts.length > 0
        ? '删除后将移除与该娃关联的数据：\n' + parts.join('，') + '。\n\n'
        : '';
    return head + '确定删除这只娃娃？此操作不可撤销。';
  }

  async function removeDollCascade(dollId) {
    var mids = makeups
      .filter(function (m) {
        return m.dollId === dollId;
      })
      .map(function (m) {
        return m.id;
      });
    var wids = wardrobes
      .filter(function (w) {
        return w.dollId === dollId;
      })
      .map(function (w) {
        return w.id;
      });
    var rids = reminders
      .filter(function (r) {
        return r.dollId === dollId;
      })
      .map(function (r) {
        return r.id;
      });
    dolls = dolls.filter(function (d) {
      return d.id !== dollId;
    });
    makeups = makeups.filter(function (m) {
      return m.dollId !== dollId;
    });
    wardrobes = wardrobes.filter(function (w) {
      return w.dollId !== dollId;
    });
    reminders = reminders.filter(function (r) {
      return r.dollId !== dollId;
    });
    for (var ii = 0; ii < inspirations.length; ii++) {
      if (inspirations[ii].dollId === dollId) inspirations[ii].dollId = '';
    }
    await BJDStorage.deleteItem('dolls', dollId);
    for (var mi = 0; mi < mids.length; mi++) await BJDStorage.deleteItem('makeupHistory', mids[mi]);
    for (var wi = 0; wi < wids.length; wi++) await BJDStorage.deleteItem('wardrobe', wids[wi]);
    for (var ri = 0; ri < rids.length; ri++) await BJDStorage.deleteItem('reminders', rids[ri]);
    await saveAllAndRender();
  }

  function touchBackupExported() {
    try {
      localStorage.setItem(LS_LAST_BACKUP_MS, String(Date.now()));
    } catch (e) {}
    updateBackupNudge();
  }

  function updateBackupNudge() {
    var el = document.getElementById('backupNudge');
    if (!el) return;
    var last = null;
    try {
      last = localStorage.getItem(LS_LAST_BACKUP_MS);
    } catch (e) {}
    if (!last) {
      el.textContent = '建议导出备份';
      el.hidden = false;
      return;
    }
    var ms = parseInt(last, 10);
    if (!isFinite(ms)) {
      el.textContent = '建议导出备份';
      el.hidden = false;
      return;
    }
    var days = (Date.now() - ms) / 86400000;
    if (days >= BACKUP_NUDGE_AFTER_DAYS) {
      el.textContent = '已约 ' + Math.floor(days) + ' 天未导出，建议备份';
      el.hidden = false;
    } else {
      el.hidden = true;
      el.textContent = '';
    }
  }

  async function loadAll() {
    try {
      dolls = (await BJDStorage.getAll('dolls')) || [];
      inspirations = (await BJDStorage.getAll('inspirations')) || [];
      wardrobes = (await BJDStorage.getAll('wardrobe')) || [];
      makeups = (await BJDStorage.getAll('makeupHistory')) || [];
      reminders = (await BJDStorage.getAll('reminders')) || [];
    } catch (e) {
      showToast('读取数据失败：' + (e && e.message ? e.message : e));
      throw e;
    }
    if (dolls.length === 0) {
      var demo = {
        id: 'd1',
        name: '小荔枝',
        sculpt: 'MYou-眠娜',
        brand: 'napi',
        size: '4分',
        artist: '荔枝壮士',
        arrival: '2025-03-12',
        avatarImage: '',
        avatarEmoji: '🍓',
        tags: '有妆',
        photos: [],
        purchasePrice: '',
        shippingCost: '',
        maintenanceDays: '',
      };
      try {
        await BJDStorage.putItem('dolls', demo);
      } catch (e) {
        showToast(e.message || '初始化示例数据失败');
        throw e;
      }
      dolls.push(demo);
    }
    renderAll();
  }

  async function saveAllAndRender() {
    try {
      for (var i = 0; i < dolls.length; i++) await BJDStorage.putItem('dolls', dolls[i]);
      for (var a = 0; a < inspirations.length; a++) await BJDStorage.putItem('inspirations', inspirations[a]);
      for (var b = 0; b < wardrobes.length; b++) await BJDStorage.putItem('wardrobe', wardrobes[b]);
      for (var c = 0; c < makeups.length; c++) await BJDStorage.putItem('makeupHistory', makeups[c]);
      for (var d = 0; d < reminders.length; d++) await BJDStorage.putItem('reminders', reminders[d]);
    } catch (e) {
      showToast(e.message || '保存失败');
      throw e;
    }
    renderAll();
  }

  function getFilteredDolls() {
    return dolls.filter(function (d) {
      if (sizeFilter && d.size !== sizeFilter) return false;
      if (artistFilter && d.artist !== artistFilter) return false;
      if (tagFilter && !(d.tags || '').includes(tagFilter)) return false;
      if (
        searchKeyword &&
        !('' + d.name + ' ' + (d.sculpt || '') + ' ' + (d.brand || ''))
          .toLowerCase()
          .includes(searchKeyword.toLowerCase())
      )
        return false;
      return true;
    });
  }

  function expenseEntries() {
    return BJDLedger.buildExpenseEntries(dolls, makeups, wardrobes);
  }

  function dollTotalsMap() {
    var entries = expenseEntries();
    var byDoll = BJDLedger.byDoll(entries, dolls);
    var map = {};
    for (var i = 0; i < byDoll.length; i++) {
      map[byDoll[i].dollId] = byDoll[i].total;
    }
    return map;
  }

  function renderInventory() {
    var filtered = getFilteredDolls();
    var totals = dollTotalsMap();
    var container = document.getElementById('dollListContainer');
    container.innerHTML = filtered
      .map(function (d) {
        var dt = totals[d.id];
        var moneyLine =
          dt > 0 ? '<div class="doll-ledger-mini">账本 ' + moneyDisplay(dt) + '</div>' : '';
        return (
          '<div class="doll-card" data-doll-id="' +
          d.id +
          '"><div class="doll-avatar">' +
          (d.avatarImage ? '<img src="' + d.avatarImage + '" alt="">' : d.avatarEmoji || '🧸') +
          '</div><div class="doll-name">' +
          escapeHtml(d.name) +
          '</div><div class="doll-meta">' +
          escapeHtml(d.sculpt || '') +
          ' · ' +
          escapeHtml(d.size) +
          '</div><div class="doll-meta">🎨 ' +
          escapeHtml(d.artist || '?') +
          '</div>' +
          moneyLine +
          '<div class="delete-btn" data-delete="' +
          d.id +
          '">🗑️ 删除</div></div>'
        );
      })
      .join('');
    document.getElementById('dollStats').textContent =
      '共 ' + dolls.length + ' 只（筛选后 ' + filtered.length + ' 只）';

    var entries = expenseEntries();
    var grand = BJDLedger.grandTotal(entries);
    document.getElementById('homeQuickStats').innerHTML =
      '账本合计约 <strong>' +
      moneyDisplay(grand) +
      '</strong> · 妆面 ' +
      makeups.length +
      ' 条 · 衣橱 ' +
      wardrobes.length +
      ' 条 · 灵感 ' +
      inspirations.length +
      ' 条';

    updateFilterOptions();
  }

  function updateFilterOptions() {
    var sizeSel = document.getElementById('filterSize');
    sizeSel.innerHTML =
      '<option value="">全部尺寸</option>' +
      [...new Set(dolls.map(function (d) { return d.size; }))]
        .map(function (s) {
          return '<option>' + s + '</option>';
        })
        .join('');
    var artistSel = document.getElementById('filterArtist');
    artistSel.innerHTML =
      '<option value="">全部壮士</option>' +
      [...new Set(dolls.map(function (d) { return d.artist; }).filter(Boolean))]
        .map(function (a) {
          return '<option>' + escapeHtml(a) + '</option>';
        })
        .join('');
    var tagSel = document.getElementById('filterTag');
    tagSel.innerHTML =
      '<option value="">全部标签</option>' +
      [
        ...new Set(
          dolls.flatMap(function (d) {
            return (d.tags || '').split(',').filter(function (t) { return t; });
          })
        ),
      ]
        .map(function (t) {
          return '<option>' + t + '</option>';
        })
        .join('');
    if (sizeFilter && [...sizeSel.options].some(function (o) { return o.value === sizeFilter; }))
      sizeSel.value = sizeFilter;
    if (artistFilter && [...artistSel.options].some(function (o) { return o.value === artistFilter; }))
      artistSel.value = artistFilter;
    if (tagFilter && [...tagSel.options].some(function (o) { return o.value === tagFilter; }))
      tagSel.value = tagFilter;
  }

  function renderLedger() {
    var entries = expenseEntries();
    var grand = BJDLedger.grandTotal(entries);
    document.getElementById('ledgerGrandTotal').textContent = '合计 ' + moneyDisplay(grand);

    var byDoll = BJDLedger.byDoll(entries, dolls);
    document.getElementById('ledgerByDollPanel').innerHTML = byDoll
      .map(function (row) {
        return (
          '<details class="ledger-group"><summary><span>' +
          escapeHtml(row.name) +
          '</span><span>' +
          moneyDisplay(row.total) +
          '</span></summary><ul class="ledger-lines">' +
          row.lines
            .map(function (e) {
              return (
                '<li><span><span class="ledger-kind">' +
                escapeHtml(e.label) +
                '</span> ' +
                escapeHtml(e.detail) +
                ' · ' +
                (e.date || '无日期') +
                '</span><span>' +
                moneyDisplay(e.amount) +
                '</span></li>'
              );
            })
            .join('') +
          '</ul></details>'
        );
      })
      .join('');

    var byMonth = BJDLedger.byMonth(entries);
    document.getElementById('ledgerByMonthPanel').innerHTML = byMonth
      .map(function (row) {
        return (
          '<details class="ledger-group"><summary><span>' +
          escapeHtml(row.month) +
          '</span><span>' +
          moneyDisplay(row.total) +
          '</span></summary><ul class="ledger-lines">' +
          row.lines
            .map(function (e) {
              return (
                '<li><span><span class="ledger-kind">' +
                escapeHtml(e.label) +
                '</span> ' +
                escapeHtml(e.detail) +
                ' · ' +
                escapeHtml(e.dollName || '') +
                ' · ' +
                (e.date || '无日期') +
                '</span><span>' +
                moneyDisplay(e.amount) +
                '</span></li>'
              );
            })
            .join('') +
          '</ul></details>'
        );
      })
      .join('');

    document.getElementById('ledgerByDollPanel').style.display = ledgerSeg === 'doll' ? 'block' : 'none';
    document.getElementById('ledgerByMonthPanel').style.display = ledgerSeg === 'month' ? 'block' : 'none';

    var ledgerGuide = document.getElementById('ledgerEmptyGuide');
    if (ledgerGuide) {
      if (grand <= 0) {
        ledgerGuide.style.display = 'block';
        ledgerGuide.innerHTML =
          '<strong>账本还是空的。</strong>可先点上方「+ 妆面支出」「+ 衣橱支出」记一笔；或在「娃娃」页点开娃娃<strong>编辑档案</strong>填写娃价/运费，汇总会自动出现在这里。';
      } else {
        ledgerGuide.style.display = 'none';
      }
    }

    renderWardrobeManageList();
  }

  function renderWardrobeManageList() {
    var el = document.getElementById('wardrobeManageList');
    if (!el) return;
    if (wardrobes.length === 0) {
      el.innerHTML = '<p class="small-note">暂无衣橱记录。可在上方点「+ 衣橱支出」添加。</p>';
      return;
    }
    el.innerHTML = wardrobes
      .map(function (w) {
        var dname = (dolls.find(function (d) { return d.id === w.dollId; }) || {}).name || '';
        return (
          '<div class="rem-card" style="margin-bottom:8px">' +
          '<div><strong>' +
          escapeHtml(w.name) +
          '</strong> · ' +
          escapeHtml(w.type) +
          ' · ' +
          moneyDisplay(w.price) +
          (w.purchaseDate ? ' · ' + escapeHtml(w.purchaseDate) : '') +
          (dname ? ' · 娃：' + escapeHtml(dname) : '') +
          '</div><div class="makeup-actions" style="margin-top:6px">' +
          '<button type="button" class="btn btn-sm" data-edit-wardrobe="' +
          w.id +
          '">编辑</button> ' +
          '<button type="button" class="btn btn-sm" data-del-wardrobe="' +
          w.id +
          '">删除</button></div></div>'
        );
      })
      .join('');
  }

  function renderMaintenanceHints() {
    var card = document.getElementById('maintenanceHintsCard');
    var list = document.getElementById('maintenanceHintsList');
    if (!card || !list) return;
    var rows = [];
    for (var i = 0; i < dolls.length; i++) {
      var d = dolls[i];
      var days = parseInt(d.maintenanceDays, 10);
      if (!isFinite(days) || days <= 0) continue;
      var last = BJDLedger.latestMakeupDateForDoll(makeups, d.id);
      if (!last) {
        rows.push(
          '<div class="small-note"><strong>' +
            escapeHtml(d.name) +
            '</strong>：已填保养周期，但暂无带日期的妆面记录。</div>'
        );
        continue;
      }
      var suggest = BJDLedger.addDays(last, days);
      var delta = Math.ceil(
        (new Date(suggest + 'T12:00:00') - new Date(todayISODate() + 'T12:00:00')) / 86400000
      );
      var tail =
        delta >= 0
          ? '还有约 <strong>' + delta + '</strong> 天'
          : '已超过约 <strong>' + Math.abs(delta) + '</strong> 天';
      rows.push(
        '<div class="rem-card rem-upcoming"><strong>' +
          escapeHtml(d.name) +
          '</strong><br>上次妆面 ' +
          escapeHtml(last) +
          ' · 建议留意约 <strong>' +
          escapeHtml(suggest) +
          '</strong> · ' +
          tail +
          '</div>'
      );
    }
    if (rows.length === 0) {
      card.style.display = 'none';
      return;
    }
    card.style.display = 'block';
    list.innerHTML = rows.join('');
  }

  function sortMakeupsForDisplay() {
    return makeups.slice().sort(function (a, b) {
      if (!a.date && !b.date) return 0;
      if (!a.date) return 1;
      if (!b.date) return -1;
      return b.date.localeCompare(a.date);
    });
  }

  function renderMakeup() {
    var container = document.getElementById('makeupList');
    var sel = document.getElementById('makeupDollId');
    if (sel) {
      sel.innerHTML = dolls
        .map(function (d) {
          return '<option value="' + d.id + '">' + escapeHtml(d.name) + '</option>';
        })
        .join('');
    }
    if (dolls.length === 0) {
      container.innerHTML = '<p class="small-note">请先添加娃娃。</p>';
      renderMaintenanceHints();
      return;
    }
    var sorted = sortMakeupsForDisplay();
    if (sorted.length === 0) {
      container.innerHTML = '<p class="small-note">还没有妆面记录。</p>';
      renderMaintenanceHints();
      return;
    }
    container.innerHTML = sorted
      .map(function (m) {
        var dn = (dolls.find(function (d) { return d.id === m.dollId; }) || {}).name || '';
        return (
          '<div class="makeup-row" data-makeup-id="' +
          m.id +
          '"><div class="makeup-row-head"><span class="makeup-date">' +
          escapeHtml(m.date || '未填日期') +
          '</span><span class="makeup-actions">' +
          '<button type="button" class="btn btn-sm" data-edit-makeup="' +
          m.id +
          '">编辑</button> ' +
          '<button type="button" class="btn btn-sm" data-del-makeup="' +
          m.id +
          '">删除</button></span></div><div class="makeup-body">' +
          escapeHtml(m.name || '') +
          ' · 妆师 ' +
          escapeHtml(m.artist || '') +
          ' · 娃 ' +
          escapeHtml(dn) +
          ' · ' +
          moneyDisplay(m.price) +
          '</div></div>'
        );
      })
      .join('');
    renderMaintenanceHints();
  }

  function parseLocalDate(iso) {
    if (!iso) return null;
    var p = iso.split('-').map(Number);
    if (p.length !== 3) return null;
    return new Date(p[0], p[1] - 1, p[2]);
  }

  function openReminderModal(prefill) {
    var sel = document.getElementById('reminderDollId');
    sel.innerHTML =
      '<option value="">无</option>' +
      dolls
        .map(function (d) {
          return '<option value="' + d.id + '">' + escapeHtml(d.name) + '</option>';
        })
        .join('');
    document.getElementById('editReminderId').value = prefill ? prefill.id : '';
    document.getElementById('reminderModalTitle').textContent = prefill ? '编辑提醒' : '添加提醒';
    if (prefill) {
      document.getElementById('reminderTitle').value = prefill.title || '';
      document.getElementById('reminderDollId').value = prefill.dollId || '';
      document.getElementById('reminderDate').value = prefill.date || todayISODate();
      document.getElementById('reminderType').value = prefill.type || '送妆提醒';
    } else {
      document.getElementById('reminderTitle').value = '';
      document.getElementById('reminderDollId').value = '';
      document.getElementById('reminderDate').value = todayISODate();
      document.getElementById('reminderType').selectedIndex = 0;
    }
    document.getElementById('reminderModal').style.display = 'flex';
  }

  function innerReminderBody(r) {
    var dname = (dolls.find(function (d) { return d.id === r.dollId; }) || {}).name || '';
    return (
      '<strong>' +
      escapeHtml(r.title || '') +
      '</strong> · ' +
      escapeHtml(r.type || '') +
      ' · ' +
      escapeHtml(r.date || '') +
      (dname ? ' · 娃：' + escapeHtml(dname) : '') +
      ' <button type="button" class="btn btn-sm" data-edit-rem="' +
      r.id +
      '">编辑</button> <button type="button" class="btn btn-sm" data-del-rem="' +
      r.id +
      '">删除</button>'
    );
  }

  function renderReminders() {
    var container = document.getElementById('reminderList');
    var sel = document.getElementById('reminderDollId');
    if (sel) {
      sel.innerHTML =
        '<option value="">无</option>' +
        dolls
          .map(function (d) {
            return '<option value="' + d.id + '">' + escapeHtml(d.name) + '</option>';
          })
          .join('');
    }
    if (reminders.length === 0) {
      container.innerHTML =
        '<div class="hint-text">' +
        '<strong>还没有日程。</strong>点右上角「+ 添加」记下送妆截止、娃聚、补尾款等；新建时<strong>日期默认为今天</strong>，可随时改掉。</div>';
      return;
    }
    var today = parseLocalDate(todayISODate());
    var upcoming = [];
    var past = [];
    for (var i = 0; i < reminders.length; i++) {
      var r = reminders[i];
      var rd = parseLocalDate(r.date);
      if (rd && today && rd >= today) upcoming.push(r);
      else past.push(r);
    }
    upcoming.sort(function (a, b) {
      return (a.date || '').localeCompare(b.date || '');
    });
    past.sort(function (a, b) {
      return (b.date || '').localeCompare(a.date || '');
    });
    var html = '';
    if (upcoming.length) {
      html += '<div class="rem-section-title">即将到来（含今天）</div>';
      for (var u = 0; u < upcoming.length; u++) {
        html += '<div class="rem-card rem-upcoming">' + innerReminderBody(upcoming[u]) + '</div>';
      }
    }
    if (past.length) {
      html += '<div class="rem-section-title">已过期 / 无日期</div>';
      for (var p = 0; p < past.length; p++) {
        html += '<div class="rem-card rem-past">' + innerReminderBody(past[p]) + '</div>';
      }
    }
    container.innerHTML = html;
  }

  function openSecondary(which) {
    secondaryView = which;
    document.getElementById('mainShell').classList.add('hidden');
    document.getElementById('mainTabBar').classList.add('hidden');
    document.getElementById('secondaryShell').style.display = 'block';
    document.getElementById('headerBackBtn').style.display = 'inline-block';
    document.getElementById('page-gallery').classList.toggle('active', which === 'gallery');
    document.getElementById('page-inspo').classList.toggle('active', which === 'inspo');
    document.getElementById('headerTitle').textContent =
      which === 'gallery' ? '📸 娃娃相册' : '🎨 灵感日记';
    if (which === 'gallery') renderGallery();
    else renderInspo();
  }

  function closeSecondary() {
    secondaryView = null;
    document.getElementById('secondaryShell').style.display = 'none';
    document.getElementById('mainShell').classList.remove('hidden');
    document.getElementById('mainTabBar').classList.remove('hidden');
    document.getElementById('headerBackBtn').style.display = 'none';
    document.getElementById('headerTitle').textContent = '🍼 娃娘手帐';
    renderAll();
  }

  function setMainTab(name) {
    mainTab = name;
    document.querySelectorAll('.page').forEach(function (p) {
      p.classList.remove('active');
    });
    var pageEl = document.getElementById('page-' + name);
    if (pageEl) pageEl.classList.add('active');
    document.querySelectorAll('.tab-item').forEach(function (t) {
      var on = t.dataset.page === name;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    renderAll();
  }

  function renderGallery() {
    var selDiv = document.getElementById('galleryDollSelect');
    if (dolls.length === 0) {
      selDiv.innerHTML = '<p class="small-note">暂无娃娃。</p>';
      document.getElementById('galleryPhotos').innerHTML = '';
      return;
    }
    selDiv.innerHTML =
      '<select id="galleryDollSelectInner" aria-label="选择娃娃">' +
      dolls
        .map(function (d) {
          return '<option value="' + d.id + '">' + escapeHtml(d.name) + '</option>';
        })
        .join('') +
      '</select>';
    var inner = document.getElementById('galleryDollSelectInner');
    inner.onchange = function (e) {
      currentGalleryDoll = dolls.find(function (d) {
        return d.id === e.target.value;
      });
      showGalleryPhotos();
    };
    currentGalleryDoll = dolls[0];
    showGalleryPhotos();
  }

  function showGalleryPhotos() {
    var container = document.getElementById('galleryPhotos');
    if (!currentGalleryDoll) return;
    var photos = currentGalleryDoll.photos || [];
    container.innerHTML = photos
      .map(function (p, idx) {
        return '<img src="' + p + '" class="photo-item" alt="" data-idx="' + idx + '">';
      })
      .join('');
    document.getElementById('addPhotoBtn').onclick = function () {
      document.getElementById('photoUploadInput').click();
    };
    document.getElementById('photoUploadInput').onchange = async function (e) {
      var files = e.target.files;
      if (!files || !files.length) return;
      try {
        for (var fi = 0; fi < files.length; fi++) {
          var base64 = await compressImage(files[fi], 800, 0.7);
          if (!currentGalleryDoll.photos) currentGalleryDoll.photos = [];
          currentGalleryDoll.photos.push(base64);
          await BJDStorage.putItem('dolls', currentGalleryDoll);
        }
        showGalleryPhotos();
        await saveAllAndRender();
      } catch (err) {
        showToast(err.message || '上传失败');
      }
      e.target.value = '';
    };
  }

  function renderInspo() {
    var container = document.getElementById('inspoListContainer');
    container.innerHTML = inspirations
      .map(function (i) {
        var dn = i.dollId ? (dolls.find(function (d) { return d.id === i.dollId; }) || {}).name : '';
        return (
          '<div class="inspo-item"><div><b>' +
          escapeHtml(i.title) +
          '</b> ' +
          (dn ? '[关联: ' + escapeHtml(dn) + ']' : '') +
          '</div><div>' +
          escapeHtml(i.description || '') +
          '</div>' +
          (i.imageBase64 ? '<img src="' + i.imageBase64 + '" class="inspo-img" alt="">' : '') +
          '<div class="small-note">' +
          escapeHtml(i.source || '') +
          ' ' +
          new Date(i.createdAt).toLocaleDateString() +
          '</div><button type="button" data-del-inspo="' +
          i.id +
          '" class="btn btn-sm">删除</button></div>'
        );
      })
      .join('');
    var dollSelect = document.getElementById('inspoDollId');
    dollSelect.innerHTML =
      '<option value="">无关联</option>' +
      dolls
        .map(function (d) {
          return '<option value="' + d.id + '">' + escapeHtml(d.name) + '</option>';
        })
        .join('');
  }

  function exportPayload() {
    return { dolls: dolls, inspirations: inspirations, wardrobes: wardrobes, makeups: makeups, reminders: reminders };
  }

  async function exportFullBackup() {
    var data = exportPayload();
    var json = JSON.stringify(data);
    var bytes = new Blob([json]).size;
    if (bytes > 1.5 * 1024 * 1024) {
      if (
        !confirm(
          '导出约 ' +
            formatBytes(bytes) +
            '，体积较大。建议改用电脑浏览器或确保有足够空间。是否继续下载？'
        )
      ) {
        return;
      }
    }
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([json], { type: 'application/json' }));
    a.download = 'bjd_hand_backup_' + Date.now() + '.json';
    a.click();
    URL.revokeObjectURL(a.href);
    showToast('已开始下载');
    touchBackupExported();
    document.getElementById('backupModal').style.display = 'none';
  }

  async function exportCopy() {
    var json = JSON.stringify(exportPayload());
    if (json.length > 800000) {
      showToast('数据太大，请使用文件导出');
      return;
    }
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(json);
        showToast('已复制到剪贴板');
        touchBackupExported();
      } else {
        throw new Error('no-clipboard');
      }
    } catch (e) {
      prompt('请手动全选并复制：', json.slice(0, 5000) + (json.length > 5000 ? '…' : ''));
    }
    document.getElementById('backupModal').style.display = 'none';
  }

  async function importBackup(file, mode) {
    var reader = new FileReader();
    reader.onload = async function (e) {
      try {
        var data = JSON.parse(e.target.result);
        if (mode === 'overwrite') {
          await BJDStorage.clearStore('dolls');
          await BJDStorage.clearStore('inspirations');
          await BJDStorage.clearStore('wardrobe');
          await BJDStorage.clearStore('makeupHistory');
          await BJDStorage.clearStore('reminders');
          if (data.dolls) for (var i = 0; i < data.dolls.length; i++) await BJDStorage.putItem('dolls', data.dolls[i]);
          if (data.inspirations)
            for (var j = 0; j < data.inspirations.length; j++)
              await BJDStorage.putItem('inspirations', data.inspirations[j]);
          if (data.wardrobes)
            for (var k = 0; k < data.wardrobes.length; k++)
              await BJDStorage.putItem('wardrobe', data.wardrobes[k]);
          if (data.makeups)
            for (var m = 0; m < data.makeups.length; m++)
              await BJDStorage.putItem('makeupHistory', data.makeups[m]);
          if (data.reminders)
            for (var r = 0; r < data.reminders.length; r++)
              await BJDStorage.putItem('reminders', data.reminders[r]);
        } else {
          var nd;
          for (nd = 0; nd < (data.dolls || []).length; nd++) {
            var newD = data.dolls[nd];
            var dix = dolls.findIndex(function (d) {
              return d.id === newD.id;
            });
            if (dix !== -1) dolls[dix] = newD;
            else dolls.push(newD);
          }
          for (nd = 0; nd < (data.inspirations || []).length; nd++) {
            var newI = data.inspirations[nd];
            var iix = inspirations.findIndex(function (i) {
              return i.id === newI.id;
            });
            if (iix !== -1) inspirations[iix] = newI;
            else inspirations.push(newI);
          }
          for (nd = 0; nd < (data.wardrobes || []).length; nd++) {
            var newW = data.wardrobes[nd];
            var wix = wardrobes.findIndex(function (w) {
              return w.id === newW.id;
            });
            if (wix !== -1) wardrobes[wix] = newW;
            else wardrobes.push(newW);
          }
          for (nd = 0; nd < (data.makeups || []).length; nd++) {
            var newM = data.makeups[nd];
            var mix = makeups.findIndex(function (m) {
              return m.id === newM.id;
            });
            if (mix !== -1) makeups[mix] = newM;
            else makeups.push(newM);
          }
          for (nd = 0; nd < (data.reminders || []).length; nd++) {
            var newR = data.reminders[nd];
            var rix = reminders.findIndex(function (r) {
              return r.id === newR.id;
            });
            if (rix !== -1) reminders[rix] = newR;
            else reminders.push(newR);
          }
          await saveAllAndRender();
        }
        await loadAll();
        showToast('导入成功');
        document.getElementById('backupModal').style.display = 'none';
      } catch (err) {
        alert('导入失败：' + (err.message || err));
      }
    };
    reader.readAsText(file);
  }

  function openMakeupModal(prefill) {
    var modal = document.getElementById('makeupModal');
    document.getElementById('makeupDollId').innerHTML = dolls
      .map(function (d) {
        return '<option value="' + d.id + '">' + escapeHtml(d.name) + '</option>';
      })
      .join('');
    document.getElementById('editMakeupId').value = prefill ? prefill.id : '';
    document.getElementById('makeupModalTitle').textContent = prefill ? '编辑妆面' : '妆面记录';
    if (prefill) {
      document.getElementById('makeupDollId').value = prefill.dollId || '';
      document.getElementById('makeupArtist').value = prefill.artist || '';
      document.getElementById('makeupName').value = prefill.name || '';
      document.getElementById('makeupDate').value = prefill.date || '';
      document.getElementById('makeupPrice').value = prefill.price || '';
    } else {
      document.getElementById('makeupArtist').value = '';
      document.getElementById('makeupName').value = '';
      document.getElementById('makeupDate').value = todayISODate();
      document.getElementById('makeupPrice').value = '';
    }
    modal.style.display = 'flex';
  }

  function openWardrobeModal(prefill) {
    document.getElementById('wardrobeDollId').innerHTML =
      '<option value="">关联娃娃</option>' +
      dolls
        .map(function (d) {
          return '<option value="' + d.id + '">' + escapeHtml(d.name) + '</option>';
        })
        .join('');
    document.getElementById('editWardrobeId').value = prefill ? prefill.id : '';
    document.getElementById('wardrobeModalTitle').textContent = prefill ? '编辑衣橱' : '添加配件';
    if (prefill) {
      document.getElementById('wardrobeName').value = prefill.name || '';
      document.getElementById('wardrobeType').value = prefill.type || '衣服';
      document.getElementById('wardrobePrice').value = prefill.price || '';
      document.getElementById('wardrobePurchaseDate').value = prefill.purchaseDate || '';
      document.getElementById('wardrobeBrand').value = prefill.brand || '';
      document.getElementById('wardrobeDollId').value = prefill.dollId || '';
    } else {
      document.getElementById('wardrobeName').value = '';
      document.getElementById('wardrobePrice').value = '';
      document.getElementById('wardrobePurchaseDate').value = '';
      document.getElementById('wardrobeBrand').value = '';
      document.getElementById('wardrobeDollId').value = '';
    }
    document.getElementById('wardrobeModal').style.display = 'flex';
  }

  function setTheme(theme) {
    document.body.classList.remove('theme-pink', 'theme-blue', 'theme-purple', 'theme-green', 'theme-cream');
    if (theme === 'pink') document.body.classList.add('theme-pink');
    else if (theme === 'blue') document.body.classList.add('theme-blue');
    else if (theme === 'purple') document.body.classList.add('theme-purple');
    else if (theme === 'green') document.body.classList.add('theme-green');
    else if (theme === 'cream') document.body.classList.add('theme-cream');
    localStorage.setItem('bjd_theme', theme);
  }

  function renderAll() {
    renderInventory();
    renderLedger();
    renderMakeup();
    renderReminders();
    if (secondaryView === 'gallery') renderGallery();
    else if (secondaryView === 'inspo') renderInspo();
    updateBackupNudge();
  }

  function bindEvents() {
    document.querySelectorAll('.tab-item').forEach(function (tab) {
      tab.onclick = function () {
        setMainTab(tab.dataset.page);
      };
    });

    document.getElementById('headerBackBtn').onclick = function () {
      closeSecondary();
    };

    document.querySelectorAll('[data-ledger-seg]').forEach(function (btn) {
      btn.onclick = function () {
        ledgerSeg = btn.dataset.ledgerSeg;
        document.querySelectorAll('[data-ledger-seg]').forEach(function (b) {
          b.classList.toggle('active', b.dataset.ledgerSeg === ledgerSeg);
          b.setAttribute('aria-selected', b.dataset.ledgerSeg === ledgerSeg ? 'true' : 'false');
        });
        document.getElementById('ledgerByDollPanel').style.display =
          ledgerSeg === 'doll' ? 'block' : 'none';
        document.getElementById('ledgerByMonthPanel').style.display =
          ledgerSeg === 'month' ? 'block' : 'none';
      };
    });

    document.getElementById('ledgerAddMakeupBtn').onclick = function () {
      if (dolls.length === 0) {
        showToast('请先添加娃娃');
        return;
      }
      openMakeupModal(null);
    };
    document.getElementById('ledgerAddWardrobeBtn').onclick = function () {
      openWardrobeModal(null);
    };

    document.getElementById('openGalleryBtn').onclick = function () {
      openSecondary('gallery');
    };
    document.getElementById('openInspoBtn').onclick = function () {
      openSecondary('inspo');
    };

    document.getElementById('filterSize').onchange = function (e) {
      sizeFilter = e.target.value;
      renderInventory();
    };
    document.getElementById('filterArtist').onchange = function (e) {
      artistFilter = e.target.value;
      renderInventory();
    };
    document.getElementById('filterTag').onchange = function (e) {
      tagFilter = e.target.value;
      renderInventory();
    };
    document.getElementById('searchInput').oninput = function (e) {
      searchKeyword = e.target.value;
      renderInventory();
    };
    document.getElementById('resetFilter').onclick = function () {
      sizeFilter = '';
      artistFilter = '';
      tagFilter = '';
      searchKeyword = '';
      document.getElementById('filterSize').value = '';
      document.getElementById('filterArtist').value = '';
      document.getElementById('filterTag').value = '';
      document.getElementById('searchInput').value = '';
      renderInventory();
    };

    var pendingAvatar = null;
    document.getElementById('showAddDollForm').onclick = function () {
      document.getElementById('addDollForm').style.display = 'block';
    };
    document.getElementById('cancelAddDoll').onclick = function () {
      document.getElementById('addDollForm').style.display = 'none';
    };
    document.getElementById('addSelectAvatarBtn').onclick = function () {
      document.getElementById('addAvatarInput').click();
    };
    document.getElementById('addAvatarInput').onchange = async function (e) {
      var f = e.target.files[0];
      if (!f) return;
      try {
        pendingAvatar = await compressImage(f, 200, 0.7);
        document.getElementById('addAvatarPreview').innerHTML = '<img src="' + pendingAvatar + '" alt="">';
      } catch (err) {
        showToast(err.message || '图片处理失败');
      }
    };
    document.getElementById('saveDollBtn').onclick = async function () {
      var name = document.getElementById('dollName').value.trim();
      if (!name) return;
      var newDoll = {
        id: Date.now() + '' + Math.random(),
        name: name,
        sculpt: document.getElementById('dollSculpt').value,
        brand: document.getElementById('dollBrand').value,
        size: document.getElementById('dollSize').value,
        artist: document.getElementById('dollArtist').value,
        arrival: document.getElementById('dollArrival').value,
        purchasePrice: document.getElementById('dollPurchasePrice').value,
        shippingCost: document.getElementById('dollShipping').value,
        avatarImage: pendingAvatar || '',
        avatarEmoji: '🧸',
        tags: '',
        photos: [],
        maintenanceDays: '',
      };
      dolls.push(newDoll);
      try {
        await saveAllAndRender();
        document.getElementById('addDollForm').style.display = 'none';
        pendingAvatar = null;
        document.getElementById('addAvatarPreview').innerHTML = '🧸';
      } catch (err) {}
    };

    document.getElementById('dollListContainer').addEventListener('click', async function (e) {
      if (e.target.dataset.delete) {
        var delId = e.target.dataset.delete;
        if (!confirm(dollDeletionConfirmMessage(delId))) return;
        try {
          await removeDollCascade(delId);
        } catch (err) {
          showToast(err.message || '删除失败');
        }
        return;
      }
      var card = e.target.closest('[data-doll-id]');
      if (card) {
        var doll = dolls.find(function (d) {
          return d.id === card.dataset.dollId;
        });
        if (doll) openEditModal(doll);
      }
    });

    window.openEditModal = function (doll) {
      document.getElementById('editDollId').value = doll.id;
      document.getElementById('editName').value = doll.name;
      document.getElementById('editSculpt').value = doll.sculpt || '';
      document.getElementById('editBrand').value = doll.brand || '';
      document.getElementById('editSize').value = doll.size;
      document.getElementById('editArtist').value = doll.artist || '';
      document.getElementById('editArrival').value = doll.arrival || '';
      document.getElementById('editPurchasePrice').value = doll.purchasePrice || '';
      document.getElementById('editShipping').value = doll.shippingCost || '';
      document.getElementById('editMaintenanceDays').value = doll.maintenanceDays || '';
      document.getElementById('editTags').value = doll.tags || '';
      var previewDiv = document.getElementById('editAvatarPreview');
      previewDiv.innerHTML = doll.avatarImage
        ? '<img src="' + doll.avatarImage + '" alt="">'
        : doll.avatarEmoji || '🧸';
      window.editPendingAvatar = null;
      document.getElementById('editDollModal').style.display = 'flex';
    };

    document.getElementById('editAvatarBtn').onclick = function () {
      document.getElementById('editAvatarInput').click();
    };
    document.getElementById('editAvatarInput').onchange = async function (e) {
      var f = e.target.files[0];
      if (!f) return;
      try {
        window.editPendingAvatar = await compressImage(f, 200, 0.7);
        document.getElementById('editAvatarPreview').innerHTML =
          '<img src="' + window.editPendingAvatar + '" alt="">';
      } catch (err) {
        showToast(err.message || '图片处理失败');
      }
    };
    document.getElementById('saveEditDollBtn').onclick = async function () {
      var id = document.getElementById('editDollId').value;
      var doll = dolls.find(function (d) {
        return d.id === id;
      });
      if (doll) {
        doll.name = document.getElementById('editName').value;
        doll.sculpt = document.getElementById('editSculpt').value;
        doll.brand = document.getElementById('editBrand').value;
        doll.size = document.getElementById('editSize').value;
        doll.artist = document.getElementById('editArtist').value;
        doll.arrival = document.getElementById('editArrival').value;
        doll.purchasePrice = document.getElementById('editPurchasePrice').value;
        doll.shippingCost = document.getElementById('editShipping').value;
        doll.maintenanceDays = document.getElementById('editMaintenanceDays').value;
        doll.tags = document.getElementById('editTags').value;
        if (window.editPendingAvatar) {
          doll.avatarImage = window.editPendingAvatar;
          doll.avatarEmoji = '';
        }
        try {
          await saveAllAndRender();
        } catch (err) {}
      }
      document.getElementById('editDollModal').style.display = 'none';
    };
    document.getElementById('cancelEditBtn').onclick = function () {
      document.getElementById('editDollModal').style.display = 'none';
    };

    document.getElementById('batchOperateBtn').onclick = function () {
      var listDiv = document.getElementById('batchSelectList');
      listDiv.innerHTML = dolls
        .map(function (d) {
          return (
            '<label><input type="checkbox" value="' +
            d.id +
            '"> ' +
            escapeHtml(d.name) +
            '</label><br>'
          );
        })
        .join('');
      document.getElementById('batchModal').style.display = 'flex';
    };
    document.getElementById('closeBatchBtn').onclick = function () {
      document.getElementById('batchModal').style.display = 'none';
    };
    document.getElementById('batchDeleteBtn').onclick = async function () {
      var checks = document.querySelectorAll('#batchSelectList input:checked');
      if (!checks.length) return;
      if (
        !confirm(
          '将删除选中的 ' +
            checks.length +
            ' 只娃娃，并移除关联的妆面、衣橱与日程；灵感日记中的关联会断开。相册照片随娃娃删除。确定？'
        )
      )
        return;
      try {
        for (var bi = 0; bi < checks.length; bi++) {
          await removeDollCascade(checks[bi].value);
        }
      } catch (err) {
        showToast(err.message || '批量删除失败');
      }
      document.getElementById('batchModal').style.display = 'none';
    };

    var backupModal = document.getElementById('backupModal');
    document.getElementById('showBackupModalBtn').onclick = function () {
      backupModal.style.display = 'flex';
    };
    document.getElementById('closeBackupModal').onclick = function () {
      backupModal.style.display = 'none';
      document.getElementById('importArea').style.display = 'none';
    };
    document.getElementById('exportBackupBtn').onclick = function () {
      exportFullBackup();
    };
    document.getElementById('exportCopyBtn').onclick = function () {
      exportCopy();
    };
    document.getElementById('importBackupTrigger').onclick = function () {
      document.getElementById('importArea').style.display = 'block';
    };
    document.getElementById('cancelImportBtn').onclick = function () {
      document.getElementById('importArea').style.display = 'none';
    };
    document.getElementById('confirmImportBtn').onclick = function () {
      var mode = document.querySelector('input[name="importMode"]:checked').value;
      var fileInput = document.getElementById('importFileInput');
      fileInput.click();
      fileInput.onchange = function (e) {
        if (e.target.files[0]) importBackup(e.target.files[0], mode);
        fileInput.value = '';
      };
    };

    document.getElementById('addMakeupBtn').onclick = function () {
      if (dolls.length === 0) {
        showToast('请先添加娃娃');
        return;
      }
      openMakeupModal(null);
    };
    document.getElementById('closeMakeupBtn').onclick = function () {
      document.getElementById('makeupModal').style.display = 'none';
    };
    document.getElementById('saveMakeupBtn').onclick = async function () {
      var mid = document.getElementById('editMakeupId').value;
      var payload = {
        dollId: document.getElementById('makeupDollId').value,
        artist: document.getElementById('makeupArtist').value,
        name: document.getElementById('makeupName').value,
        date: document.getElementById('makeupDate').value,
        price: document.getElementById('makeupPrice').value,
      };
      try {
        if (mid) {
          var exist = makeups.find(function (m) {
            return m.id === mid;
          });
          if (exist) Object.assign(exist, payload);
        } else {
          makeups.push({
            id: Date.now() + '' + Math.random(),
            dollId: payload.dollId,
            artist: payload.artist,
            name: payload.name,
            date: payload.date,
            price: payload.price,
          });
        }
        await saveAllAndRender();
        document.getElementById('makeupModal').style.display = 'none';
      } catch (err) {}
    };

    document.getElementById('makeupList').addEventListener('click', async function (e) {
      var editId = e.target.getAttribute('data-edit-makeup');
      if (editId) {
        var mm = makeups.find(function (m) {
          return m.id === editId;
        });
        if (mm) openMakeupModal(mm);
        return;
      }
      var delId = e.target.getAttribute('data-del-makeup');
      if (delId) {
        if (!confirm('删除这条妆面记录？')) return;
        makeups = makeups.filter(function (m) {
          return m.id !== delId;
        });
        try {
          await saveAllAndRender();
        } catch (err) {}
      }
    });

    document.getElementById('closeWardrobeBtn').onclick = function () {
      document.getElementById('wardrobeModal').style.display = 'none';
    };
    document.getElementById('saveWardrobeBtn').onclick = async function () {
      var wid = document.getElementById('editWardrobeId').value;
      var name = document.getElementById('wardrobeName').value.trim();
      if (!name) {
        showToast('请填写名称');
        return;
      }
      var payload = {
        name: name,
        type: document.getElementById('wardrobeType').value,
        price: document.getElementById('wardrobePrice').value,
        purchaseDate: document.getElementById('wardrobePurchaseDate').value,
        brand: document.getElementById('wardrobeBrand').value,
        dollId: document.getElementById('wardrobeDollId').value,
      };
      try {
        if (wid) {
          var wo = wardrobes.find(function (w) {
            return w.id === wid;
          });
          if (wo) Object.assign(wo, payload);
        } else {
          wardrobes.push({
            id: Date.now() + '' + Math.random(),
            name: payload.name,
            type: payload.type,
            price: payload.price,
            purchaseDate: payload.purchaseDate,
            brand: payload.brand,
            dollId: payload.dollId,
          });
        }
        await saveAllAndRender();
        document.getElementById('wardrobeModal').style.display = 'none';
      } catch (err) {}
    };

    document.getElementById('wardrobeManageList').addEventListener('click', async function (e) {
      var eid = e.target.getAttribute('data-edit-wardrobe');
      if (eid) {
        var ww = wardrobes.find(function (w) {
          return w.id === eid;
        });
        if (ww) openWardrobeModal(ww);
        return;
      }
      var did = e.target.getAttribute('data-del-wardrobe');
      if (did) {
        if (!confirm('删除这条衣橱记录？')) return;
        wardrobes = wardrobes.filter(function (w) {
          return w.id !== did;
        });
        try {
          await saveAllAndRender();
        } catch (err) {}
      }
    });

    document.getElementById('addReminderBtn').onclick = function () {
      openReminderModal(null);
    };
    document.getElementById('closeReminderBtn').onclick = function () {
      document.getElementById('editReminderId').value = '';
      document.getElementById('reminderModal').style.display = 'none';
    };
    document.getElementById('saveReminderBtn').onclick = async function () {
      var title = document.getElementById('reminderTitle').value.trim();
      if (!title) return;
      var editR = document.getElementById('editReminderId').value;
      var payload = {
        title: title,
        dollId: document.getElementById('reminderDollId').value,
        date: document.getElementById('reminderDate').value,
        type: document.getElementById('reminderType').value,
      };
      try {
        if (editR) {
          var existR = reminders.find(function (r) {
            return r.id === editR;
          });
          if (existR) {
            existR.title = payload.title;
            existR.dollId = payload.dollId;
            existR.date = payload.date;
            existR.type = payload.type;
          }
        } else {
          reminders.push({
            id: Date.now() + '' + Math.random(),
            title: payload.title,
            dollId: payload.dollId,
            date: payload.date,
            type: payload.type,
          });
        }
        await saveAllAndRender();
        document.getElementById('editReminderId').value = '';
        document.getElementById('reminderModal').style.display = 'none';
      } catch (err) {}
    };

    document.getElementById('reminderList').addEventListener('click', async function (e) {
      var erid = e.target.getAttribute('data-edit-rem');
      if (erid) {
        var ed = reminders.find(function (r) {
          return r.id === erid;
        });
        if (ed) openReminderModal(ed);
        return;
      }
      var rid = e.target.getAttribute('data-del-rem');
      if (rid) {
        reminders = reminders.filter(function (r) {
          return r.id !== rid;
        });
        try {
          await saveAllAndRender();
        } catch (err) {}
      }
    });

    document.getElementById('showAddInspoForm').onclick = function () {
      document.getElementById('addInspoForm').style.display = 'block';
    };
    document.getElementById('cancelAddInspo').onclick = function () {
      document.getElementById('addInspoForm').style.display = 'none';
    };
    document.getElementById('inspoSelectImageBtn').onclick = function () {
      document.getElementById('inspoImageInput').click();
    };
    document.getElementById('inspoImageInput').onchange = async function (e) {
      if (e.target.files[0])
        try {
          pendingInspoImg = await compressImage(e.target.files[0], 600, 0.7);
        } catch (err) {
          showToast(err.message || '图片处理失败');
        }
    };
    document.getElementById('saveInspoBtn').onclick = async function () {
      var title = document.getElementById('inspoTitle').value.trim();
      if (!title) return;
      inspirations.push({
        id: Date.now() + '' + Math.random(),
        title: title,
        description: document.getElementById('inspoDesc').value,
        source: document.getElementById('inspoSource').value,
        dollId: document.getElementById('inspoDollId').value,
        imageBase64: pendingInspoImg || '',
        createdAt: new Date().toISOString(),
      });
      try {
        await saveAllAndRender();
        document.getElementById('addInspoForm').style.display = 'none';
        pendingInspoImg = null;
      } catch (err) {}
    };
    document.getElementById('inspoListContainer').addEventListener('click', async function (e) {
      var iid = e.target.getAttribute('data-del-inspo');
      if (iid) {
        inspirations = inspirations.filter(function (i) {
          return i.id !== iid;
        });
        try {
          await saveAllAndRender();
        } catch (err) {}
      }
    });

    document.querySelectorAll('.theme-dot').forEach(function (dot) {
      dot.addEventListener('click', function () {
        setTheme(dot.dataset.theme);
      });
    });
    setTheme(localStorage.getItem('bjd_theme') || 'pink');
  }

  (async function init() {
    try {
      await BJDStorage.openDB();
      await loadAll();
    } catch (e) {
      alert('应用无法启动：' + (e && e.message ? e.message : e));
      return;
    }
    bindEvents();
    if (typeof Notification !== 'undefined' && Notification.permission !== 'granted') {
      Notification.requestPermission();
    }
  })();
})();
