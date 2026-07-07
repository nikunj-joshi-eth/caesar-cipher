"""
Caesar Cipher — entry point.

Author: Nikunj Joshi (B.Tech Student)
"""
import sys
from pathlib import Path

# Allow running `python main.py` without installing the package.
sys.path.insert(0, str(Path(__file__).parent / "src"))

from caesar_cipher.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
