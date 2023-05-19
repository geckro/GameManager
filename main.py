import logging
import argparse
from sys import exit, argv

from PyQt6.QtWidgets import QApplication

from src.ui.app import MainWindow
from src.core.app import app


def main():
    try:
        parser = argparse.ArgumentParser(description="Practically a wikipedia client")
        parser.add_argument('--tui', action='store_true', help='Launch TUI')
        args = parser.parse_args()

        if args.tui:
            app()
        elif not args.tui:
            # Create a QApplication object with CLI arguments passed to it
            gui_app = QApplication(argv)

            # Create a MainWindow object and show the window
            window = MainWindow()
            window.show()

            # exit() is used to cleanly exit the application.
            exit(gui_app.exec())
        
    except Exception as e:
        logging.exception(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
