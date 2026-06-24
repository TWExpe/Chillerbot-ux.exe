// Zielseite, die gestreamt werden soll
const HOME_URL = 'https://huhu.to/';

const frame = document.getElementById('frame');
const loader = document.getElementById('loader');
const fallback = document.getElementById('fallback');
const reloadBtn = document.getElementById('reload');
const openExtBtn = document.getElementById('open-ext');
const retryBtn = document.getElementById('retry');
const launchBtn = document.getElementById('launch');

let loadTimer = null;
let loaded = false;

function showLoader() {
  loaded = false;
  loader.classList.remove('hidden');
  fallback.classList.add('hidden');
}

function showFrame() {
  loaded = true;
  loader.classList.add('hidden');
  fallback.classList.add('hidden');
}

// Viele Streaming-Seiten verbieten das Einbetten (X-Frame-Options / CSP).
// Cross-Origin lässt sich der Fehler nicht direkt abfangen, daher Fallback
// nach einer Frist: Hero mit Direkt-Öffnen-Button.
function showFallback() {
  if (loaded) return;
  loader.classList.add('hidden');
  fallback.classList.remove('hidden');
}

function loadSite() {
  showLoader();
  clearTimeout(loadTimer);
  frame.src = HOME_URL;
  loadTimer = setTimeout(showFallback, 6000);
}

frame.addEventListener('load', () => {
  clearTimeout(loadTimer);
  showFrame();
});

reloadBtn.addEventListener('click', loadSite);
retryBtn.addEventListener('click', loadSite);
openExtBtn.addEventListener('click', () => window.open(HOME_URL, '_blank', 'noopener,noreferrer'));
launchBtn.setAttribute('href', HOME_URL);

// Service Worker registrieren (macht die App installierbar / offline-startfähig)
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('sw.js').catch(() => { /* nicht kritisch */ });
  });
}

loadSite();
