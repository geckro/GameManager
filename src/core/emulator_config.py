import pathlib
import sys
import os

from core.config import add_to_config


def get_default_emulator_paths():
    if sys.platform.startswith('win32'):
        drive = str(os.getenv('SystemDrive'))
        home = str(pathlib.Path.home())

        files_to_check = (
            f'{drive}\\RetroArch-Win64\\retroarch.exe',
            f'{home}\\AppData\\Local\\yuzu\\yuzu-windows-msvc\\yuzu.exe'
        )
        # Check for executables because some programs may just leave folders behind
        for file in files_to_check:
            if pathlib.Path(file).is_file():
                print(f'{file} true')
