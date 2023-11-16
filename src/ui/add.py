from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QComboBox, QPushButton

from src.core.data.platform_data import PlatformData


class Add(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Data")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.data_edit = QLineEdit(self)
        layout.addWidget(QLabel("Data Entry"))
        layout.addWidget(self.data_edit)

        self.data_type_button = QComboBox()
        self.data_type_button.addItems(["Platform", "Genre"])
        layout.addWidget(self.data_type_button)

        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit(self):
        data = self.data_edit.text()

        json_data = PlatformData()
        json_data.append_to_json(data)
        self.close()
