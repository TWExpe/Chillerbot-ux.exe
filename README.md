# muff1n 📱

Eine schicke, installierbare **Web-App (PWA)** fürs Handy. Du öffnest sie im
Handy-Browser, fügst sie über „Zum Startbildschirm hinzufügen" hinzu und hast
danach ein App-Icon wie eine echte App (Vollbild, ohne Browserleiste).

## Design & Funktionen

- ✨ Modernes Design: animierter Aurora-Hintergrund, Glas-Effekte (Glassmorphism)
- 📲 Installierbar als App (PWA, Vollbild, eigenes Icon)
- ⟳ Neu laden · ↗ Im Browser öffnen
- 🛡️ **Popup-Ad-Schutz**: Der iframe läuft in einer `sandbox` ohne
  `allow-popups` – die typischen Popup-/Popunder- und Auto-Weiterleitungs-Ads
  werden dadurch blockiert.
- 🔒 **Security-Härtung**: strenge Content-Security-Policy, `strict-origin`
  Referrer-Policy, kein Tracking, keine Drittanbieter-Skripte.

## So bekommst du die App aufs Handy

### Variante A – über GitHub Pages (empfohlen)

1. Repo-**Settings → Pages → Source = „GitHub Actions"**.
2. Der Workflow (`.github/workflows/deploy.yml`) veröffentlicht die App bei
   jedem Push. Die URL findest du danach unter **Settings → Pages**.
3. URL auf dem **Handy** öffnen.
4. **Android (Chrome):** Menü ⋮ → „App installieren".
   **iPhone (Safari):** Teilen → „Zum Home-Bildschirm".

### Variante B – lokal testen

```bash
node serve.js   # -> http://localhost:8080
```

## Zur Werbung / zum Adblocking – ehrlich erklärt

Eine reine Web-App kann **nur Popup-Ads** blockieren (über die iframe-Sandbox,
siehe oben). **Banner-/Overlay-Ads innerhalb** der eingebetteten Seite kann sie
nicht filtern – das verbietet die Same-Origin-Policy des Browsers, und ohne
einen Inhalts-Proxy (den dieses Projekt bewusst nicht enthält) gibt es keinen
Zugriff auf den iframe-Inhalt.

Für vollständiges Ad-/Malware-Blocking gibt es legitime Wege:

- **Geräteweiter DNS-Filter**, z. B. AdGuard DNS oder NextDNS – blockt Ad-/
  Tracker-Domains für alle Apps inkl. dieser.
- **Native Android-App (WebView)** mit Request-Interception, die bekannte
  Werbe-/Malware-Domains blockiert. (Auf Wunsch baue ich das Projekt dafür.)

> Hinweis: muff1n ist eine App-Hülle/ein Starter für eine Webseite. Welche
> Inhalte du aufrufst und ob das in deinem Land erlaubt ist, liegt in deiner
> Verantwortung.

## Dateien

```
index.html              App-Hülle (Kopfzeile + Frame + Hero/Fallback)
styles.css              Modernes, mobiles Design (Aurora + Glas)
app.js                  Lade-/Fallback-Logik, Service-Worker-Registrierung
manifest.webmanifest    PWA-Manifest
sw.js                   Service Worker (installierbar / offline-startfähig)
icons/                  App-Icons (m1-Monogramm, 192/512 + maskable)
serve.js                Mini-Testserver ohne Abhängigkeiten
.github/workflows/      Automatisches Deployment zu GitHub Pages
```

## Zielseite ändern

Oben in `app.js`:

```js
const HOME_URL = 'https://huhu.to/';
```
