from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableView, QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import pyqtSignal

class GameView(QDialog):
    # Define a custom pyqtSignal for when a row is selected using the mouse
    row_selected = pyqtSignal(list)

    def __init__(self, df):
        super().__init__()
        self.setWindowTitle(f"Search Results")
        
        # Creat a QVBoxLayout to hold the table view
        layout = QVBoxLayout(self)

        # Create a QTableView widget and sort the table and disallow editing the table.
        self.table_view = QTableView(self)
        self.table_view.setSortingEnabled(True)
        self.table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
        # Create a QStandardItemModel to hold the data
        self.table_model = QStandardItemModel()

        # Set column header names
        self.table_model.setHorizontalHeaderLabels(['Title', 'System'])

        # Add data to the table from the search results
        for i in range(df.shape[0]):
            items = [QStandardItem(str(df.iloc[i,j])) for j in [0, 7]]
            self.table_model.appendRow(items)

        # Set the table model for the table view
        self.table_view.setModel(self.table_model)
        
        # Add the table view to the layout
        layout.addWidget(self.table_view)

        # Connect the table view's selectionChanged signal to the handle_selection method
        self.table_view.selectionModel().selectionChanged.connect(self.handle_selection)

    def handle_selection(self, selected):
        if selected.indexes():
            rows = set()
            for index in selected.indexes():
                rows.add(index.row())

            selected_rows = []
            for row in rows:
                row_data = []
                for column in range(self.table_model.columnCount()):
                    cell_data = self.table_model.index(row, column).data()
                    row_data.append(cell_data)
                selected_rows.append(row_data)

            # Emit the row_selected signal with the selected row data
            self.row_selected.emit(selected_rows)
            
            # Close the dialog once you have selected a row
            self.close()
