import os
import sys


def resource_path(relative_path: str) -> str:
    """Return absolute path to a bundled resource.

    Works both when running from source and when packaged with PyInstaller
    (--onefile extracts assets to a temporary folder exposed via sys._MEIPASS).
    """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)