import wikipedia
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QAbstractItemView


class Search:
    def __init__(self, table_view):
        # Reference to QTableView Widget
        self.table_view = table_view

        # Create a new QStandardItemModel and set it as the model for the QTableView widget
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        # Enable sorting and disable editing
        self.table_view.setSortingEnabled(True)
        self.table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        # Set the last section of the horizontal header of the QTableView widget to stretch
        header = self.table_view.horizontalHeader()
        header.setStretchLastSection(True)

        # Connect the clicked signal of the QTableView widget to the on_table_clicked slot
        self.table_view.clicked.connect(self.on_table_clicked)

    def search(self, search_text):
        # Clear QStandardItemModel
        self.model.clear()
        self.table_view.show()

        # Set the horizontal header label for the QStandardItemModel
        self.model.setHorizontalHeaderLabels(['Search Results'])

        # Search for results on Wikipedia
        results = wikipedia.search(search_text)

        # Begin resetting the QStandardItemModel
        self.model.beginResetModel()

        # Loop through the search results and add them as QStandardItems to the QStandardItemModel
        for result in results:
            item = QStandardItem(result)
            self.model.appendRow(item)  # Append the QStandardItem to the QStandardItemModel

            # If the search_text matches a Wikipedia result perfectly, return that result
            if search_text.lower() == result.lower():
                self.table_view.hide()
                return result

        # End resetting the QStandardItemModel
        self.model.endResetModel()

    def on_table_clicked(self):
        selected_indexes = self.table_view.selectedIndexes()
        if not selected_indexes:
            return

        selected_index = selected_indexes[0]
        selected_row = selected_index.row()

        # Get the result from the selected row
        result_index = self.model.index(selected_row, 0)
        result = self.model.data(result_index)

        self.table_view.hide()

        return result
