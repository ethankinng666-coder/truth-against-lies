/* ============================================
   SHARED JS — Truth Against Lies
   Used by: lies, october7, gallery, videos, action, regions
   ============================================ */

// ========== CLOSE NAV ON OUTSIDE CLICK ==========
document.addEventListener('click', function(e) {
    var nav = document.querySelector('.nav-links');
    var hamburger = document.querySelector('.hamburger');
    if (nav && nav.classList.contains('open') && !nav.contains(e.target) && e.target !== hamburger) {
        nav.classList.remove('open');
    }
});

// ========== FLOATING SHARE ==========
function fabShare(platform) {
    var url = window.location.href;
    var title = document.title;
    var text = title + '\n' + url;
    var encoded = encodeURIComponent(text);
    if (platform === 'whatsapp') window.open('https://wa.me/?text=' + encoded, '_blank');
    else if (platform === 'telegram') window.open('https://t.me/share/url?url=' + encodeURIComponent(url) + '&text=' + encodeURIComponent(title), '_blank');
    else if (platform === 'twitter') window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(title) + '&url=' + encodeURIComponent(url), '_blank');
    else if (platform === 'facebook') window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url), '_blank');
    else if (platform === 'copy') {
        navigator.clipboard.writeText(url);
        var btn = document.querySelector('.sfab-cp');
        btn.textContent = '\u2713';
        setTimeout(function() { btn.innerHTML = '&#128203;'; }, 2000);
    }
    document.getElementById('shareFab').classList.remove('open');
}
document.addEventListener('click', function(e) {
    var fab = document.getElementById('shareFab');
    if (fab && !fab.contains(e.target)) fab.classList.remove('open');
});

// ========== LANGUAGE PICKER ==========
function setPageLang(lang) {
    document.querySelector('.nav-lang-menu').classList.remove('open');
    if (lang === 'he') {
        localStorage.removeItem('siteLang');
        document.cookie = 'googtrans=;path=/;expires=Thu, 01 Jan 1970 00:00:00 GMT';
        document.cookie = 'googtrans=;path=/;domain=.github.io;expires=Thu, 01 Jan 1970 00:00:00 GMT';
    } else {
        localStorage.setItem('siteLang', lang);
        document.cookie = 'googtrans=/he/' + lang + ';path=/';
        document.cookie = 'googtrans=/he/' + lang + ';path=/;domain=.github.io';
    }
    location.reload();
    return false;
}
document.addEventListener('click', function(e) {
    var lm = document.querySelector('.nav-lang-menu');
    var lb = document.querySelector('.nav-lang-btn');
    if (lm && !lm.contains(e.target) && e.target !== lb) lm.classList.remove('open');
});

// ========== GOOGLE TRANSLATE ==========
function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage:'he',autoDisplay:false}, 'google_translate_element');
}
(function(){
    var lang = localStorage.getItem('siteLang');
    if (lang && lang !== 'he') {
        document.cookie = 'googtrans=/he/' + lang + ';path=/';
        document.cookie = 'googtrans=/he/' + lang + ';path=/;domain=.github.io';
    }
    if (!document.getElementById('gt-script')) {
        var s = document.createElement('script');
        s.id = 'gt-script';
        s.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
        document.body.appendChild(s);
    }
})();
