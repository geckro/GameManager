import pathlib
import sys
import os

from core.config import add_to_config


def get_default_emulator_paths():
    if sys.platform.startswith('win32'):
        drive = str(os.getenv('SystemDrive'))
        home = str(pathlib.Path.home())

        _emulator_files = (
            (f'{drive}\\RetroArch-Win64\\retroarch.exe', 'retroarch'),  # RetroArch
            (f'{home}\\AppData\\Local\\yuzu\\yuzu-windows-msvc\\yuzu.exe', 'yuzu'),  # Yuzu
            (f'{home}\\AppData\\Local\\Citra\\nightly\\citra.exe', 'citra')  # Citra
        )

        # Check for executables because some programs may just leave folders behind
        for file, emulator in _emulator_files:
            if pathlib.Path(file).is_file():
                add_to_config(f"{emulator}_directory", file)

        add_to_config("has_not_checked_emulator_paths", False)
