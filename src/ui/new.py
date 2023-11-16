from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QDateEdit, QLabel, QHBoxLayout, \
    QTreeWidget, QTreeWidgetItem

from src.core.data.game_data import GameData


class New(QDialog):
    def __init__(self):
        super().__init__()

        self.genre_list = ["Action", "Adventure", "Puzzle", "RPG", "Strategy"]
        self.developer_list = ["Nintendo EAD", "Nintendo EPD"]
        self.publisher_list = ["Nintendo", "Sony"]
        self.platform_list = ["Wii", "3DS"]

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout_encapsulation = QHBoxLayout()
        basic_info_layout = QVBoxLayout()
        advanced_info_layout = QVBoxLayout()
        submit_layout = QHBoxLayout()

        self.title_edit = QLineEdit(self)
        basic_info_layout.addWidget(QLabel("Title"))
        basic_info_layout.addWidget(self.title_edit)

        self.date_edit = QDateEdit(self)
        self.date_edit.setDisplayFormat('yyyy-MMM-dd')
        self.date_edit.setCalendarPopup(True)
        basic_info_layout.addWidget(QLabel("Date"))
        basic_info_layout.addWidget(self.date_edit)

        self.platform_field = QTreeWidget()
        self.platform_field.setHeaderHidden(True)
        platform_tree = QTreeWidgetItem(self.platform_field)
        platform_tree.setText(0, "Platform")
        for platform in self.platform_list:
            platform_item = QTreeWidgetItem(platform_tree)
            platform_item.setFlags(platform_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            platform_item.setText(0, platform)
            platform_item.setCheckState(0, Qt.CheckState.Unchecked)
        basic_info_layout.addWidget(self.platform_field)

        self.genre_field = QTreeWidget()
        self.genre_field.setHeaderHidden(True)
        genre_tree = QTreeWidgetItem(self.genre_field)
        genre_tree.setText(0, "Genres")
        genre_tree.setExpanded(False)
        for genre in self.genre_list:
            genre_item = QTreeWidgetItem(genre_tree)
            genre_item.setFlags(genre_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            genre_item.setText(0, genre)
            genre_item.setCheckState(0, Qt.CheckState.Unchecked)
        basic_info_layout.addWidget(self.genre_field)

        self.developer_field = QTreeWidget()
        self.developer_field.setHeaderHidden(True)
        developer_tree = QTreeWidgetItem(self.developer_field)
        developer_tree.setText(0, "Developers")
        developer_tree.setExpanded(False)
        for developer in self.developer_list:
            developer_item = QTreeWidgetItem(developer_tree)
            developer_item.setFlags(developer_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            developer_item.setText(0, developer)
            developer_item.setCheckState(0, Qt.CheckState.Unchecked)
        advanced_info_layout.addWidget(self.developer_field)

        self.publisher_field = QTreeWidget()
        self.publisher_field.setHeaderHidden(True)
        publisher_tree = QTreeWidgetItem(self.publisher_field)
        publisher_tree.setText(0, "Publishers")
        publisher_tree.setExpanded(False)
        for publisher in self.publisher_list:
            publisher_item = QTreeWidgetItem(publisher_tree)
            publisher_item.setFlags(publisher_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            publisher_item.setText(0, publisher)
            publisher_item.setCheckState(0, Qt.CheckState.Unchecked)
        advanced_info_layout.addWidget(self.publisher_field)

        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        submit_layout.addWidget(submit_button)

        layout_encapsulation.addLayout(basic_info_layout)
        layout_encapsulation.addLayout(advanced_info_layout)
        layout.addLayout(layout_encapsulation)
        layout.addLayout(submit_layout)
        self.setLayout(layout)

    def get_checked_items(self, tree):
        checked_items = []
        root = tree.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            parent = root.child(i)
            for j in range(parent.childCount()):
                child = parent.child(j)
                if child.checkState(0) == Qt.CheckState.Checked:
                    checked_items.append(child.text(0))
        return checked_items


    def submit(self):
        title = self.title_edit.text()
        date = self.date_edit.date().toString()

        # Get checked items from each tree
        selected_platforms = self.get_checked_items(self.platform_field)
        selected_genres = self.get_checked_items(self.genre_field)
        selected_developers = self.get_checked_items(self.developer_field)
        selected_publishers = self.get_checked_items(self.publisher_field)

        # Create the data dictionary
        data = {
            'title': title,
            'date': date,
            'platforms': selected_platforms,
            'genres': selected_genres,
            'developers': selected_developers,
            'publishers': selected_publishers
        }

        json_data = GameData()
        json_data.append_to_data_json(data)

        self.close()
