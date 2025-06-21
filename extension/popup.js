document.getElementById("analyze").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const model = document.getElementById("model").value;
  chrome.tabs.sendMessage(tab.id, { command: "analyze", model });
});
