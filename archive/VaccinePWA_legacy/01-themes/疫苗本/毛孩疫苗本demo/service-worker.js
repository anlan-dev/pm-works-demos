// 缓存名称，每次更新代码可以改版本号让旧缓存失效
const CACHE_NAME = 'vaccine-pwa-v1';
// 需要缓存的文件列表
const urlsToCache = [
  '.',
  'index.html',
  'manifest.json',
  'icon.png'
  // 如果你有外部的 CSS 或 JS 文件，也可以加在这里
];

// 安装事件：预缓存关键资源
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('缓存已打开');
        return cache.addAll(urlsToCache);
      })
  );
});

// 激活事件：清理旧版本缓存
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.filter(cacheName => cacheName !== CACHE_NAME)
          .map(cacheName => caches.delete(cacheName))
      );
    })
  );
});

// 拦截网络请求：优先使用缓存，提升加载速度
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // 缓存中有就直接返回，否则去网络请求
        return response || fetch(event.request);
      })
  );
});