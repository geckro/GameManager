# LICENSE: MIT
import argparse
import sys
import src

from PyQt6.QtWidgets import QApplication

from core.log import log
from ui.app import MainWindow


def argparser():
    """
    Parse arguments using the python standard library argparse.
    """
    parser = argparse.ArgumentParser(prog='gamemanager', description=src.description)
    parser.add_argument('-v', '--version', help='Show app version')
    return parser


def main():
    """
    Start the application.
    """
    try:
        parser = argparser()
        argv = sys.argv[1:]
        args = parser.parse_args(argv)
        gui_app = QApplication([])
        window = MainWindow()
        window.show()
        log('info', "Executing window...")
        sys.exit(gui_app.exec())

    except Exception as e:
        log('error', e)


if __name__ == "__main__":
    main()
