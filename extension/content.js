// Tworzy (lub aktualizuje) panel z wynikiem na stronie
function ensurePanel() {
  if (!document.getElementById('scamscanner-style')) {
    const link = document.createElement('link');
    link.id = 'scamscanner-style';
    link.rel = 'stylesheet';
    link.href = chrome.runtime.getURL('inject.css');
    document.head.appendChild(link);
  }

  let panel = document.getElementById('scamscanner-panel');
  if (!panel) {
    panel = document.createElement('div');
    panel.id = 'scamscanner-panel';
    panel.innerHTML = '<h3>ScamScanner</h3><div class="status"></div><div class="result"></div>';
    document.body.prepend(panel);
  }
  return panel;
}

// Pobranie tekstu (np. zaznaczonego przez użytkownika) i wysłanie do API
async function analyzeSelectedText(model = 'gpt2') {
  const selectedText = window.getSelection().toString() || document.body.innerText;

  const panel = ensurePanel();
  const statusEl = panel.querySelector('.status');
  const resultEl = panel.querySelector('.result');
  resultEl.textContent = '';
  statusEl.innerHTML = '<span class="spinner"></span> Analiza w toku...';
  const start = performance.now();

  try {
    const response = await fetch('http://127.0.0.1:8000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: selectedText, model })
    });

    if (!response.ok) throw new Error(`Błąd serwera: ${response.status}`);
    const data = await response.json();
    const time = ((performance.now() - start) / 1000).toFixed(1);
    statusEl.textContent = `Gotowe w ${time}s`;
    resultEl.textContent = data.result;
  } catch (err) {
    console.error(err);
    statusEl.textContent = 'Błąd połączenia';
    alert(`Nie udało się połączyć: ${err.message}`);
  }
}

// Nasłuchiwanie komunikatu z background/popup
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.command === 'analyze') {
    analyzeSelectedText(msg.model);
    sendResponse({ status: 'started' });
  }
});

// Dla popup.html: wysłanie komendy
// W popup.js wystarczy:
// document.getElementById('scan').onclick = () => chrome.runtime.sendMessage({ command: 'analyze' });
