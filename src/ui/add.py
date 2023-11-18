from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QComboBox, QPushButton

from src.core.data.developer_data import DeveloperData
from src.core.data.genre_data import GenreData
from src.core.data.platform_data import PlatformData
from src.core.data.publisher_data import PublisherData
from src.core.log import log


class Add(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameManager - Add Data")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.data_edit = QLineEdit(self)
        layout.addWidget(QLabel("Data Entry"))
        layout.addWidget(self.data_edit)

        self.data_type_button = QComboBox()
        self.data_type_button.addItems(["Platform", "Genre", "Developer", "Publisher"])
        layout.addWidget(self.data_type_button)

        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit(self):
        """
        Submits data from the data entry field. If data is not whitespace, it appends it to the respective JSON file and
        then closes the window.
        """
        data = self.data_edit.text().strip()
        data_type = self.data_type_button.currentText()
        if data:
            try:
                if data_type == 'Platform':
                    json_data = PlatformData()
                    json_data.append_to_json(data)
                elif data_type == 'Genre':
                    json_data = GenreData()
                    json_data.append_to_json(data)
                elif data_type == 'Developer':
                    json_data = DeveloperData()
                    json_data.append_to_json(data)
                elif data_type == 'Publisher':
                    json_data = PublisherData()
                    json_data.append_to_json(data)
            except Exception as e:
                log('error', e)

        self.close()
