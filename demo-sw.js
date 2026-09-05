const CACHE_NAME = 'demo-cache-v1';
// demo 页缓存前缀：activate 只清理 demo 自身的历史缓存，不清除宠伴/创作舱的缓存
const CACHE_PREFIX = 'demo-cache';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k.startsWith(CACHE_PREFIX) && k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  
  event.respondWith(
    fetch(req).then((res) => {
      if (res.status === 200) {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(req, copy)).catch(() => {});
      }
      return res;
    }).catch(() => 
      caches.match(req).then((cached) => {
        if (cached) return cached;
        if (req.mode === 'navigate') {
          return caches.match('./index.html');
        }
        return new Response('Offline', { status: 503, statusText: 'Offline' });
      })
    )
  );
});
