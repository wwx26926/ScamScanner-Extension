import os
import platform
import shutil
import subprocess
from pathlib import Path

PROJECT = "ScamScanner"
BACKEND_DIR = Path(__file__).resolve().parents[1] / "backend"
DIST_DIR = Path(__file__).resolve().parents[1] / "dist"
DIST_DIR.mkdir(exist_ok=True)


def run(cmd, check=True):
    print(f"$ {cmd}")
    return subprocess.run(cmd, shell=True, check=check)


def check_tool(name, install_hint):
    if shutil.which(name) is None:
        print(f"[WARN] Missing {name}. Install via: {install_hint}")
        return False
    return True


def ensure_env():
    os_name = platform.system()
    print(f"Detected OS: {os_name}")
    py_ok = check_tool("python3", "https://www.python.org/downloads")
    pip_ok = check_tool("pip", "python -m ensurepip --upgrade")
    node_ok = check_tool("node", "https://nodejs.org/")
    return py_ok and pip_ok and node_ok


def build_backend():
    venv = BACKEND_DIR / ".venv"
    run(f"python3 -m venv {venv}")
    pip = venv / ("Scripts" if platform.system() == "Windows" else "bin") / "pip"
    run(f"{pip} install -r {BACKEND_DIR / 'requirements1.txt'} pyinstaller")
    pyinstaller = venv / ("Scripts" if platform.system() == "Windows" else "bin") / "pyinstaller"
    run(
        f"{pyinstaller} --onefile {BACKEND_DIR / 'server.py'} "
        f"--name {PROJECT}Backend"
    )
    exe = BACKEND_DIR / "dist" / (f"{PROJECT}Backend.exe" if platform.system() == "Windows" else f"{PROJECT}Backend")
    target = DIST_DIR / exe.name
    if exe.exists():
        shutil.move(str(exe), target)
    return target


def create_nsis_installer(exe_path):
    script = DIST_DIR / "installer.nsi"
    script.write_text(
        f"""Name \"{PROJECT}\"\nOutFile \"{DIST_DIR / (PROJECT + '_Setup.exe')}\"\nInstallDir $PROGRAMFILES\\{PROJECT}\nPage directory\nPage instfiles\nSection\n  SetOutPath $INSTDIR\n  File \"{exe_path}\"\n  CreateShortcut $DESKTOP\\{PROJECT}.lnk $INSTDIR\\{exe_path.name}\nSectionEnd\n"""
    )
    if check_tool("makensis", "choco install nsis" if platform.system()=="Windows" else "brew install nsis"):
        run(f"makensis {script}")
    return script


def main():
    if not ensure_env():
        print("Missing tools. See warnings above.")
        return
    exe = build_backend()
    if platform.system() == "Windows":
        create_nsis_installer(exe)
    print("Build complete. Files in", DIST_DIR)


if __name__ == "__main__":
    main()
