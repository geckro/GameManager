from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QVBoxLayout, QToolBar, QTableWidget, QTableView, QWidget, QTableWidgetItem

from src.core.data.common_data import CommonData
from src.core.data.game_data import GameData
from src.ui.triggers import Triggers


class InitUI:
    def __init__(self, main_window):
        self.common_data = CommonData('data/data.json')
        self.game_data = GameData()
        self.keys = self.game_data.get_game_keys()
        self.main_window = main_window
        self.triggers = Triggers(self)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self.main_window)
        self.main_window.setCentralWidget(central_widget)

        self.init_toolbar(central_widget)

        layout = QVBoxLayout(central_widget)

        self.init_table(layout)

        self.load_data()

    def init_toolbar(self, central_widget):
        toolbar = QToolBar(central_widget)
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.main_window.addToolBar(toolbar)

        new_action = QAction(QIcon.fromTheme("list-new"), 'New Title', self.main_window)
        new_action.triggered.connect(self.triggers.new_action_triggered)

        add_action = QAction(QIcon.fromTheme("list-add"), 'Add Data', self.main_window)
        add_action.triggered.connect(self.triggers.add_action_triggered)

        toolbar.addAction(new_action)
        toolbar.addAction(add_action)

    def init_table(self, layout):
        self.main_window.table_widget = QTableWidget()
        self.main_window.table_widget.setShowGrid(False)
        self.main_window.table_widget.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.main_window.table_widget.setAlternatingRowColors(True)
        self.main_window.table_widget.setSortingEnabled(True)
        self.main_window.table_widget.setTabKeyNavigation(False)
        self.main_window.table_widget.verticalHeader().setVisible(False)

        layout.addWidget(self.main_window.table_widget)

    def load_data(self):
        # Read the JSON data
        data = self.common_data.open_json()

        # Set up the table
        self.main_window.table_widget.setRowCount(len(data))
        self.main_window.table_widget.setColumnCount(len(self.keys))
        self.main_window.table_widget.setHorizontalHeaderLabels(self.keys)
        for row, entry in enumerate(data):
            for column, key in enumerate(self.keys):
                # Join the list into a string for list-type fields, else just use the value
                value = ", ".join(entry[key]) if isinstance(entry[key], list) else entry[key]
                table_item = QTableWidgetItem(value)
                table_item.setFlags(table_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.main_window.table_widget.setItem(row, column, table_item)
