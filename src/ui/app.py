from PyQt6.QtWidgets import QMainWindow

from src.ui.initui import InitUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui = InitUI(self)

        self.setWindowTitle("GameManager")

        self.resize(800, 300)
