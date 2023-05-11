from PyQt6.QtWidgets import QApplication
from app import MainWindow
import logging
from sys import exit, argv

def main():
    # Try to create and show the main application window
    try:
        # Create a QApplication object with CLI arguments passed to it
        app = QApplication(argv)
        
        # Create a MainWindow object and show the window
        window = MainWindow()
        window.show()
        
        # Start the event loop. exit() is used to cleanly exit the application.
        exit(app.exec())
        
    # If there are issues, log any exceptions with the logging module
    except Exception as e:
        logging.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    main()