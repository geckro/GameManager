from PyQt6.QtWidgets import QMainWindow

from src.core.log import log
from src.ui.initui import InitUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        log('info', 'Executing InitUI()')
        self.init_ui = InitUI(self)

        self.setWindowTitle("GameManager")

        self.resize(800, 300)
