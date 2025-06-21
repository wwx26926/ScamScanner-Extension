import os
import sys
import shutil
import subprocess
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXT_DIR = ROOT / "extension"

BACKEND_CMD = [sys.executable, "-m", "uvicorn", "backend.server:app", "--host", "127.0.0.1", "--port", "8000"]


def find_browser():
    for name in ["google-chrome", "chrome", "chromium", "msedge"]:
        path = shutil.which(name)
        if path:
            return [path, f"--load-extension={EXT_DIR}"]
    if shutil.which("firefox"):
        return ["firefox"]
    return None


def main():
    print("Starting backend server...")
    backend = subprocess.Popen(BACKEND_CMD)
    browser_cmd = find_browser()
    if browser_cmd:
        if "firefox" in browser_cmd[0]:
            print("Firefox detected. Open about:debugging and load the extension manually from:", EXT_DIR)
            webbrowser.open("about:debugging#/runtime/this-firefox")
        else:
            print("Launching browser with extension...")
            subprocess.Popen(browser_cmd)
    else:
        print("No supported browser found. Please open Chrome/Edge with developer mode and load the extension from:", EXT_DIR)

    try:
        backend.wait()
    except KeyboardInterrupt:
        backend.terminate()
        backend.wait()


if __name__ == "__main__":
    main()

