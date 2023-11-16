from src.ui.new import New
from src.ui.add import Add

class Triggers:
    def __init__(self, main_window):
        self.main_window = main_window

    @staticmethod
    def new_action_triggered(self):
        new = New()
        new.exec()

    @staticmethod
    def add_action_triggered(self):
        add = Add()
        add.exec()
