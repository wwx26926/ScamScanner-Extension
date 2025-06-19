// Pobranie tekstu (np. zaznaczonego przez użytkownika) i wysłanie do API
async function analyzeSelectedText() {
  // Przykładowy sposób pobrania tekstu z aktywnej strony:
  const selectedText = window.getSelection().toString() || document.body.innerText;

  try {
    const response = await fetch('http://127.0.0.1:8000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: selectedText })
    });

    if (!response.ok) throw new Error(`Błąd serwera: ${response.status}`);
    const data = await response.json();
    console.log('Wynik analizy:', data);
    alert(`Wynik: ${data.result}`);
  } catch (err) {
    console.error(err);
    alert(`Nie udało się połączyć: ${err.message}`);
  }
}

// Nasłuchiwanie komunikatu z background/popup
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.command === 'analyze') {
    analyzeSelectedText();
    sendResponse({ status: 'started' });
  }
});

// Dla popup.html: wysłanie komendy
// W popup.js wystarczy:
// document.getElementById('scan').onclick = () => chrome.runtime.sendMessage({ command: 'analyze' });