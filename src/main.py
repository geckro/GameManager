import logging
import sys

from PyQt6.QtWidgets import QApplication

from ui.app import MainWindow


def main():
    try:
        gui_app = QApplication([])
        gui_app.setStyle('Fusion')
        window = MainWindow()
        window.show()
        sys.exit(gui_app.exec())

    except Exception as e:
        logging.exception(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
