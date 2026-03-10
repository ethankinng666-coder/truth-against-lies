var CACHE_NAME = 'tal-v1';
var ASSETS = [
    './',
    'index.html',
    'lies.html',
    'october7.html',
    'antisemitism.html',
    'facts.html',
    'facts-command.html',
    'facts-court.html',
    'facts-iran.html',
    'facts-knesset.html',
    'facts-media.html',
    'facts-money.html',
    'facts-myths.html',
    'facts-netanyahu.html',
    'facts-orgs.html',
    'facts-policies.html',
    'facts-west.html',
    'gallery.html',
    'videos.html',
    'action.html',
    'regions.html',
    'glossary.html',
    'statistics.html',
    'holocaust-denial.html',
    'shared.css',
    'common.js',
    'search.js',
    'search-index.js',
    'favicon.png',
    'favicon.ico'
];

// Install: cache all assets
self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            return cache.addAll(ASSETS);
        })
    );
    self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', function(e) {
    e.waitUntil(
        caches.keys().then(function(names) {
            return Promise.all(
                names.filter(function(n) { return n !== CACHE_NAME; })
                    .map(function(n) { return caches.delete(n); })
            );
        })
    );
    self.clients.claim();
});

// Fetch: cache-first, fallback to network
self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(cached) {
            if (cached) return cached;
            return fetch(e.request).then(function(response) {
                if (response && response.status === 200 && response.type === 'basic') {
                    var clone = response.clone();
                    caches.open(CACHE_NAME).then(function(cache) {
                        cache.put(e.request, clone);
                    });
                }
                return response;
            });
        })
    );
});
