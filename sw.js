const CACHE_NAME = 'pet-vaccine-cache-v1';
// 本应用(宠伴)专属缓存前缀：activate 只清理本应用自己的历史缓存，不清除创作舱/demo 的缓存
const CACHE_PREFIX = 'pet-vaccine-cache';

const CORE_ASSETS = [
  './pet-vaccine.html',
  './manifest.json',
  './icon.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(CORE_ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k.startsWith(CACHE_PREFIX) && k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// 简单缓存策略：优先网络，失败回退缓存（适合 demo）
self.addEventListener('fetch', (event) => {
  const req = event.request;
  event.respondWith(
    fetch(req).then((res) => {
      const copy = res.clone();
      caches.open(CACHE_NAME).then((cache) => cache.put(req, copy)).catch(() => {});
      return res;
    }).catch(() => caches.match(req).then((c) => {
      if (c) return c;
      // 导航请求离线且缓存无命中时才回退到本应用(宠伴)入口页，避免回退成其它应用的页面；非导航未缓存资源交回浏览器处理
      if (req.mode === 'navigate') return caches.match('./pet-vaccine.html');
    }))
  );
});

// 兼容“推送/通知”展示：真实 push 需要后端，这里提供 showNotification 能力
self.addEventListener('push', (event) => {
  let data = {};
  try { data = event.data ? event.data.json() : {}; } catch { data = { body: event.data?.text?.() }; }
  const title = data.title || '宠伴·健康台账';
  const body = data.body || '你有新的提醒';
  event.waitUntil(self.registration.showNotification(title, { body, icon: './icon.svg' }));
});

