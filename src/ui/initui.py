import os

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QVBoxLayout, QToolBar, QTableWidget, QTableView, QWidget, QTableWidgetItem, QMenu, \
    QSizePolicy

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
        self.toolbar = QToolBar(central_widget)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.main_window.addToolBar(self.toolbar)

        new_action = QAction(QIcon('src/img/icons/actions/window-new.svg'), 'New Title', self.main_window)
        new_action.triggered.connect(self.triggers.new_action_triggered)

        add_action = QAction(QIcon('src/img/icons/actions/text-field.svg'), 'Add Data', self.main_window)
        add_action.triggered.connect(self.triggers.add_action_triggered)

        spacer = QWidget()
        spacer_policy = QSizePolicy()
        spacer_policy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        spacer.setSizePolicy(spacer_policy)

        options_action = QAction(QIcon('src/img/icons/actions/configure.svg'), 'Options', self.main_window)
        options_action.triggered.connect(self.triggers.options_triggered)

        self.toolbar.addAction(new_action)
        self.toolbar.addAction(add_action)
        self.toolbar.addWidget(spacer)
        self.toolbar.addAction(options_action)

        self.toolbar.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.toolbar.customContextMenuRequested.connect(self.on_toolbar_context_menu)

    def on_toolbar_context_menu(self, position):
        context_menu = QMenu()
        actions = ('Lock Toolbar', 'Hide Toolbar')
        action_objs = {}

        for action_text in actions:
            action = context_menu.addAction(action_text)
            action_objs[action_text] = action

        selected_action = context_menu.exec(self.main_window.table_widget.viewport().mapToGlobal(position))
        if selected_action:
            if selected_action == action_objs['Lock Toolbar']:
                if self.toolbar.isMovable():
                    self.toolbar.setMovable(False)
                elif not self.toolbar.isMovable():
                    self.toolbar.setMovable(True)
            if selected_action == action_objs['Hide Toolbar']:
                if not self.toolbar.isHidden():
                    self.toolbar.setHidden(True)
                elif self.toolbar.isHidden():
                    self.toolbar.setHidden(False)

    def init_table(self, layout):
        self.main_window.table_widget = QTableWidget()
        self.main_window.table_widget.setShowGrid(False)
        self.main_window.table_widget.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.main_window.table_widget.setAlternatingRowColors(True)
        self.main_window.table_widget.setSortingEnabled(True)
        self.main_window.table_widget.setTabKeyNavigation(False)
        self.main_window.table_widget.verticalHeader().setVisible(False)
        self.main_window.table_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.main_window.table_widget.customContextMenuRequested.connect(self.on_context_menu)

        layout.addWidget(self.main_window.table_widget)

    def on_context_menu(self, position):
        context_menu = QMenu()
        actions = ('Modify Entry', 'Delete Entry')
        action_objs = {}

        for action_text in actions:
            action = context_menu.addAction(action_text)
            action_objs[action_text] = action

        item = self.main_window.table_widget.itemAt(position)

        if item is not None:
            row = item.row()
            data = []
            num_columns = self.main_window.table_widget.columnCount()

            for column in range(num_columns):
                cell_item = self.main_window.table_widget.item(row, column)
                if cell_item:
                    data.append(cell_item.text())
                else:
                    data.append("")

            selected_action = context_menu.exec(self.main_window.table_widget.viewport().mapToGlobal(position))
            if selected_action:
                if selected_action == action_objs['Modify Entry']:
                    # TODO: ModifyEntry
                    pass
                elif selected_action == action_objs['Delete Entry']:
                    self.game_data.delete_game_entry(data)

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
