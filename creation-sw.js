const CACHE_NAME = 'creation-cabin-cache-v1';
// 本应用(创作舱)专属缓存前缀：activate 只清理本应用自己的历史缓存，不清除宠伴/demo 的缓存
const CACHE_PREFIX = 'creation-cabin-cache';
const ASSETS = [
  './creation-cabin.html',
  './creation-manifest.json',
  './creation-icon.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k.startsWith(CACHE_PREFIX) && k !== CACHE_NAME).map((k) => caches.delete(k)))).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(event.request).then((r) => {
        if (r) return r;
        // 导航请求离线且缓存无命中时才回退到本应用(创作舱)入口页，避免回退成其它应用的页面；非导航未缓存资源交回浏览器处理
        if (event.request.mode === 'navigate') return caches.match('./creation-cabin.html');
      }))
  );
});

