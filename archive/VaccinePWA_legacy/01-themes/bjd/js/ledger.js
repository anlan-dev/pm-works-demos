/**
 * 账本汇总：妆面、衣橱、娃价/运费（记在娃娃档案上）
 */
(function (global) {
  function parseMoney(v) {
    if (v == null || v === '') return 0;
    var n = Number(String(v).replace(/[^\d.-]/g, ''));
    return isFinite(n) ? n : 0;
  }

  function monthKeyFromDate(dateStr) {
    if (!dateStr || typeof dateStr !== 'string') return '未填日期';
    var m = dateStr.match(/^(\d{4}-\d{2})/);
    return m ? m[1] : '未填日期';
  }

  /**
   * @returns {Array<{kind:string,id:string,dollId:string,dollName:string,amount:number,label:string,detail:string,date:string,monthKey:string}>}
   */
  function buildExpenseEntries(dolls, makeups, wardrobes) {
    var entries = [];
    var nameById = {};
    for (var i = 0; i < dolls.length; i++) {
      nameById[dolls[i].id] = dolls[i].name;
    }
    for (var di = 0; di < dolls.length; di++) {
      var d = dolls[di];
      var p = parseMoney(d.purchasePrice);
      var s = parseMoney(d.shippingCost);
      if (p > 0 || s > 0) {
        var parts = [];
        if (p > 0) parts.push('娃价 ¥' + p);
        if (s > 0) parts.push('运费 ¥' + s);
        entries.push({
          kind: 'doll',
          id: 'doll-cost-' + d.id,
          dollId: d.id,
          dollName: d.name,
          amount: p + s,
          label: '娃价/运费',
          detail: parts.join(' · '),
          date: d.arrival || '',
          monthKey: d.arrival ? monthKeyFromDate(d.arrival) : '未填日期',
        });
      }
    }
    for (var mi = 0; mi < makeups.length; mi++) {
      var m = makeups[mi];
      entries.push({
        kind: 'makeup',
        id: m.id,
        dollId: m.dollId,
        dollName: nameById[m.dollId] || '',
        amount: parseMoney(m.price),
        label: '妆面',
        detail: [m.name, m.artist].filter(Boolean).join(' · '),
        date: m.date || '',
        monthKey: m.date ? monthKeyFromDate(m.date) : '未填日期',
      });
    }
    for (var wi = 0; wi < wardrobes.length; wi++) {
      var w = wardrobes[wi];
      entries.push({
        kind: 'wardrobe',
        id: w.id,
        dollId: w.dollId,
        dollName: nameById[w.dollId] || '',
        amount: parseMoney(w.price),
        label: '衣橱 · ' + (w.type || ''),
        detail: w.name + (w.brand ? ' · ' + w.brand : ''),
        date: w.purchaseDate || '',
        monthKey: w.purchaseDate ? monthKeyFromDate(w.purchaseDate) : '未填日期',
      });
    }
    return entries;
  }

  function grandTotal(entries) {
    var s = 0;
    for (var i = 0; i < entries.length; i++) s += entries[i].amount;
    return s;
  }

  function byDoll(entries, dolls) {
    var nameById = {};
    for (var i = 0; i < dolls.length; i++) nameById[dolls[i].id] = dolls[i].name;
    var map = {};
    for (var j = 0; j < entries.length; j++) {
      var e = entries[j];
      var key = e.dollId || '_none';
      if (!map[key]) {
        map[key] = {
          dollId: key,
          name: nameById[key] || e.dollName || '未关联娃娃',
          total: 0,
          lines: [],
        };
      }
      if (nameById[key]) map[key].name = nameById[key];
      map[key].total += e.amount;
      map[key].lines.push(e);
    }
    var arr = [];
    for (var k in map) arr.push(map[k]);
    arr.sort(function (a, b) {
      return b.total - a.total;
    });
    return arr;
  }

  function byMonth(entries) {
    var map = {};
    for (var i = 0; i < entries.length; i++) {
      var e = entries[i];
      var mk = e.monthKey || '未填日期';
      if (!map[mk]) map[mk] = { month: mk, total: 0, lines: [] };
      map[mk].total += e.amount;
      map[mk].lines.push(e);
    }
    var arr = [];
    for (var k in map) arr.push(map[k]);
    arr.sort(function (a, b) {
      return String(b.month).localeCompare(String(a.month));
    });
    return arr;
  }

  /** 某娃最近一次有日期的妆面 */
  function latestMakeupDateForDoll(makeups, dollId) {
    var best = null;
    for (var i = 0; i < makeups.length; i++) {
      var m = makeups[i];
      if (m.dollId !== dollId || !m.date) continue;
      if (!best || m.date > best) best = m.date;
    }
    return best;
  }

  function addDays(isoDate, days) {
    var d = new Date(isoDate + 'T12:00:00');
    d.setDate(d.getDate() + Number(days));
    return d.toISOString().slice(0, 10);
  }

  global.BJDLedger = {
    parseMoney: parseMoney,
    buildExpenseEntries: buildExpenseEntries,
    grandTotal: grandTotal,
    byDoll: byDoll,
    byMonth: byMonth,
    latestMakeupDateForDoll: latestMakeupDateForDoll,
    addDays: addDays,
    monthKeyFromDate: monthKeyFromDate,
  };
})(typeof window !== 'undefined' ? window : this);
