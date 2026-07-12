from pathlib import Path

from .main import main


if __name__ == "__main__":
    raise SystemExit(main(repository_root=Path.cwd()))
