# Huhu Stream 📱

Eine installierbare **Web-App (PWA)** fürs Handy, mit der du **huhu.to**
streamen kannst. Du öffnest sie im Handy-Browser, fügst sie über „Zum
Startbildschirm hinzufügen" hinzu – und hast danach ein App-Icon wie eine
echte App (Vollbild, ohne Browserleiste).

> **Hinweis:** Die App ist ein Wrapper/Starter für die Webseite huhu.to. Viele
> Streaming-Seiten verbieten das direkte Einbetten – in dem Fall zeigt die App
> einen Button „Jetzt streamen", der huhu.to öffnet. Welche Inhalte du
> streamst und ob das in deinem Land erlaubt ist, liegt in deiner
> Verantwortung.

## So bekommst du die App aufs Handy

### Variante A – über GitHub Pages (empfohlen, nichts zu installieren)

1. In den Repo-Einstellungen **Settings → Pages** öffnen und als Quelle
   **„GitHub Actions"** wählen.
2. Der enthaltene Workflow (`.github/workflows/deploy.yml`) veröffentlicht die
   App automatisch bei jedem Push. Nach dem ersten Lauf findest du die URL
   unter **Settings → Pages** (z. B. `https://<dein-name>.github.io/<repo>/`).
3. Diese URL auf dem **Handy im Browser** öffnen.
4. **Android (Chrome):** Menü ⋮ → „App installieren" / „Zum Startbildschirm
   hinzufügen".
   **iPhone (Safari):** Teilen-Symbol → „Zum Home-Bildschirm".
5. Fertig – das Huhu-Stream-Icon liegt jetzt auf dem Startbildschirm.

### Variante B – lokal testen (am PC)

```bash
node serve.js
# -> http://localhost:8080
```

Im selben WLAN kannst du die App auch direkt vom Handy aufrufen, indem du die
lokale IP des PCs nutzt (z. B. `http://192.168.x.x:8080`). Für „App
installieren" verlangen Browser allerdings HTTPS – dafür ist Variante A
(GitHub Pages) gedacht.

## Funktionen

- 📲 Installierbar als App (PWA, Vollbild, eigenes Icon)
- ▶ Lädt huhu.to direkt beim Start
- ⟳ Neu-Laden-Button
- ↗ „Im Browser öffnen", falls die Einbettung blockiert ist
- 🌙 Dunkles Design, für Handys optimiert (Safe-Areas, kein Zoom-Wackeln)

## Dateien

```
index.html              App-Hülle (Kopfzeile + Streaming-Frame + Fallback)
styles.css              Dunkles, mobiles Design
app.js                  Lade-/Fallback-Logik, Service-Worker-Registrierung
manifest.webmanifest    PWA-Manifest (Name, Icon, Vollbild)
sw.js                   Service Worker (App installierbar / offline-fähig)
icons/                  App-Icons (192/512 px + maskable)
serve.js                Mini-Testserver ohne Abhängigkeiten
.github/workflows/      Automatisches Deployment zu GitHub Pages
```

## Startseite ändern

Die Adresse steht oben in `app.js`:

```js
const HOME_URL = 'https://huhu.to/';
```
