import subprocess
import sys

from pathlib import Path

BACKEND_DIR = Path.cwd() / "backend"
VENV_PYTHON = BACKEND_DIR / ".venv" / "Scripts" / "python.exe"


def run(cmd_args):
    subprocess.run([VENV_PYTHON] + cmd_args, cwd=BACKEND_DIR, check=True)


def start_server():
    run(["-m", "uvicorn", "main:app"])


def test():
    run(["-m", "pytest", "tests"])


def lint():
    run(["-m", "flake8", ".", "--exclude=.venv,__pycache__,build,dist"])


def sort_imports():
    run(["-m", "isort", ".", "--skip", ".venv"])


def format_all():
    sort_imports()
    lint()


ACTIONS = {
    "start-server": start_server,
    "test": test,
    "lint": lint,
    "sort-imports": sort_imports,
    "format": format_all,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ACTIONS:
        print("Usage:")
        print("  py tasks.py start-server  # Start FastAPI server")
        print("  py tasks.py test          # Run all tests in backend/tests")
        print("  py tasks.py lint          # Lint with flake8")
        print("  py tasks.py sort-imports  # Sort imports with isort")
        print("  py tasks.py format        # Sort imports and lint")
        sys.exit(1)
    ACTIONS[sys.argv[1]]()
