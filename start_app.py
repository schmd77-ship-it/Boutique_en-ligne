from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / "guitar_shop"
VENV_PYTHON = PROJECT / ".venv" / "Scripts" / "python.exe"


def main() -> None:
    if VENV_PYTHON.exists():
        env = os.environ.copy()
        env["PYTHONPATH"] = str(PROJECT) + os.pathsep + env.get("PYTHONPATH", "")
        subprocess.run([str(VENV_PYTHON), "-m", "client.main"], cwd=str(PROJECT), env=env)
        return

    project_root = str(PROJECT)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    from client.main import GuitarShopApp

    GuitarShopApp().run()


if __name__ == "__main__":
    main()
