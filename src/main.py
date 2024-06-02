# LICENSE: MIT
import sys

from PyQt6.QtWidgets import QApplication

from core.log import log
from ui.app import MainWindow


def main():
    """
    Start the application.
    """
    try:
        gui_app = QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(gui_app.exec())

    except Exception as e:
        log('error', e)


if __name__ == "__main__":
    main()
