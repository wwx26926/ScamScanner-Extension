import subprocess
import sys

BACKEND_CMD = [sys.executable, '-m', 'uvicorn', 'backend.server:app', '--host', '127.0.0.1', '--port', '8000']


def main() -> None:
    backend = subprocess.Popen(BACKEND_CMD)
    try:
        subprocess.call([sys.executable, 'gui.py'])
    finally:
        backend.terminate()
        backend.wait()


if __name__ == '__main__':
    main()
