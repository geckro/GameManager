from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableView, QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import pyqtSignal

class GameView(QDialog):
    row_selected = pyqtSignal(list)

    def __init__(self, df):
        super().__init__()
        self.setWindowTitle(f"Search Results")
        layout = QVBoxLayout(self)

        self.table_view = QTableView(self)
        self.table_view.setSortingEnabled(True)
        self.table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_model = QStandardItemModel()

        self.table_model.setHorizontalHeaderLabels(['Title', 'System'])

        for i in range(df.shape[0]):
            items = [QStandardItem(str(df.iloc[i,j])) for j in [0, 7]]
            self.table_model.appendRow(items)

        self.table_view.setModel(self.table_model)
        layout.addWidget(self.table_view)

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

            self.row_selected.emit(selected_rows)
            self.close()
