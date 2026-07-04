/**
 * IndexedDB 封装：统一错误处理，供 UI 层提示用户。
 */
(function (global) {
  var DB_NAME = 'BJD_Vault_Complete';
  var DB_VERSION = 5;

  var db = null;

  function openDB() {
    return new Promise(function (resolve, reject) {
      var req = indexedDB.open(DB_NAME, DB_VERSION);
      req.onupgradeneeded = function (e) {
        var database = e.target.result;
        if (!database.objectStoreNames.contains('dolls')) {
          database.createObjectStore('dolls', { keyPath: 'id' });
        }
        if (!database.objectStoreNames.contains('inspirations')) {
          database.createObjectStore('inspirations', { keyPath: 'id' });
        }
        if (!database.objectStoreNames.contains('wardrobe')) {
          database.createObjectStore('wardrobe', { keyPath: 'id' });
        }
        if (!database.objectStoreNames.contains('makeupHistory')) {
          database.createObjectStore('makeupHistory', { keyPath: 'id' });
        }
        if (!database.objectStoreNames.contains('reminders')) {
          database.createObjectStore('reminders', { keyPath: 'id' });
        }
      };
      req.onsuccess = function (e) {
        db = e.target.result;
        resolve(db);
      };
      req.onerror = function () {
        reject(req.error || new Error('无法打开本地数据库'));
      };
      req.onblocked = function () {
        reject(new Error('数据库被其他标签页占用，请关闭其它打开本应用的分页后重试。'));
      };
    });
  }

  async function getStore(storeName, mode) {
    if (!db) await openDB();
    return db.transaction(storeName, mode || 'readonly').objectStore(storeName);
  }

  async function getAll(storeName) {
    try {
      var store = await getStore(storeName);
      return await new Promise(function (res, rej) {
        var r = store.getAll();
        r.onsuccess = function () {
          res(r.result || []);
        };
        r.onerror = function () {
          rej(r.error);
        };
      });
    } catch (err) {
      throw wrapErr(err, '读取失败');
    }
  }

  async function putItem(storeName, item) {
    try {
      var store = await getStore(storeName, 'readwrite');
      await new Promise(function (res, rej) {
        var r = store.put(item);
        r.onsuccess = res;
        r.onerror = function () {
          rej(r.error);
        };
      });
    } catch (err) {
      var msg = mapQuotaError(err);
      throw new Error(msg);
    }
  }

  async function deleteItem(storeName, id) {
    try {
      var store = await getStore(storeName, 'readwrite');
      await new Promise(function (res, rej) {
        var r = store.delete(id);
        r.onsuccess = res;
        r.onerror = function () {
          rej(r.error);
        };
      });
    } catch (err) {
      throw wrapErr(err, '删除失败');
    }
  }

  async function clearStore(storeName) {
    try {
      var store = await getStore(storeName, 'readwrite');
      await new Promise(function (res, rej) {
        var r = store.clear();
        r.onsuccess = res;
        r.onerror = function () {
          rej(r.error);
        };
      });
    } catch (err) {
      throw wrapErr(err, '清空数据失败');
    }
  }

  function mapQuotaError(err) {
    if (!err) return '保存失败';
    var name = err.name || '';
    if (name === 'QuotaExceededError') {
      return '存储空间已满（图片过多）。请导出备份后删除部分相册图片，或使用「备份」清理后重装。';
    }
    return err.message || '保存失败';
  }

  function wrapErr(err, prefix) {
    if (err && err.name === 'QuotaExceededError') {
      return new Error(mapQuotaError(err));
    }
    return new Error((prefix || '') + '：' + (err && err.message ? err.message : String(err)));
  }

  global.BJDStorage = {
    DB_NAME: DB_NAME,
    openDB: openDB,
    getAll: getAll,
    putItem: putItem,
    deleteItem: deleteItem,
    clearStore: clearStore,
  };
})(typeof window !== 'undefined' ? window : this);
