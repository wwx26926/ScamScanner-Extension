import os
import subprocess
import sys
import platform
from pathlib import Path
import importlib

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / '.venv'


def run(cmd):
    print('$', ' '.join(cmd))
    return subprocess.run(cmd, check=True)


def ensure_venv():
    if not VENV_DIR.exists():
        run([sys.executable, '-m', 'venv', str(VENV_DIR)])
    if platform.system() == 'Windows':
        python = VENV_DIR / 'Scripts' / 'python.exe'
        pip = VENV_DIR / 'Scripts' / 'pip.exe'
    else:
        python = VENV_DIR / 'bin' / 'python'
        pip = VENV_DIR / 'bin' / 'pip'
    run([str(pip), 'install', '--upgrade', 'pip'])
    run([str(pip), 'install', '-r', str(ROOT / 'backend' / 'requirements1.txt')])
    run([str(pip), 'install', 'pydantic-settings'])
    try:
        importlib.import_module('tkinter')
    except ImportError:
        if platform.system() == 'Linux':
            subprocess.call(['sudo', 'apt', 'update'])
            subprocess.call(['sudo', 'apt', 'install', '-y', 'python3-tk'])
    return python


def main():
    python = ensure_venv()
    backend_cmd = [str(python), '-m', 'uvicorn', 'backend.server:app', '--reload', '--host', '127.0.0.1', '--port', '8000']
    backend = subprocess.Popen(backend_cmd)
    try:
        subprocess.call([str(python), 'gui.py'])
    finally:
        backend.terminate()
        backend.wait()


if __name__ == '__main__':
    main()
