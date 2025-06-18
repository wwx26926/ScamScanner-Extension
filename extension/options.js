const chk = document.getElementById("force_rag");
const status = document.getElementById("status");

chrome.storage.sync.get(["force_rag"], data => {
  chk.checked = data.force_rag || false;
});

document.getElementById("save").addEventListener("click", () => {
  chrome.storage.sync.set({ force_rag: chk.checked }, () => {
    status.textContent = "Zapisano!";
    setTimeout(() => status.textContent = "", 2000);
  });
});
