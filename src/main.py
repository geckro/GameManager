import sys

from PyQt6.QtWidgets import QApplication

from src.core.log import log
from ui.app import MainWindow


def main():
    try:
        gui_app = QApplication([])
        window = MainWindow()
        window.show()
        log('info', "Executing window...")
        sys.exit(gui_app.exec())

    except Exception as e:
        log('error', e)


if __name__ == "__main__":
    main()
