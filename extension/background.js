// Gdy klikniesz ikonę wtyczki – wstrzykujemy content.js
chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ["content.js"]
  });
});
