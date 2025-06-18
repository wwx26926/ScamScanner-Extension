(async () => {
  const API = "https://<codespace>-8000.preview.app.github.dev/analyze";
  const text = (document.querySelector("article")||document.body).innerText.substring(0,5000);

  // Pobierz ustawienia
  const { force_rag } = await chrome.storage.sync.get(["force_rag"]);

  // Wstrzyknij panel ładowania
  injectPanel("Trwa analiza…");

  try {
    const resp = await fetch(API, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ text, force_rag })
    });
    const { result } = await resp.json();
    injectPanel(result);
  } catch (e) {
    injectPanel("Błąd: " + e.message);
  }

  function injectPanel(html) {
    const old = document.getElementById("scanscanner-panel");
    if (old) old.remove();
    const panel = document.createElement("div");
    panel.id = "scamscanner-panel";
    panel.innerHTML = `<h3>ScamScanner</h3><div class="result">${html}</div>`;
    (document.querySelector("article")||document.body).prepend(panel);
  }
})();
