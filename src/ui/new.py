from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QDateEdit, QLabel, QHBoxLayout, \
    QTreeWidget, QTreeWidgetItem, QWidget

from src.core.data.developer_data import DeveloperData
from src.core.data.engine_data import EngineData
from src.core.data.game_data import GameData
from src.core.data.genre_data import GenreData
from src.core.data.platform_data import PlatformData
from src.core.data.publisher_data import PublisherData
from src.core.log import log


def helper_qtreewidget(item_list, title: str):
    widget = QTreeWidget()
    widget.setHeaderHidden(True)
    widget_tree = QTreeWidgetItem(widget)
    widget_tree.setText(0, title)
    widget_tree.setExpanded(False)
    for item in item_list:
        widget_item = QTreeWidgetItem(widget_tree)
        widget_item.setFlags(widget_item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        widget_item.setText(0, item)
        widget_item.setCheckState(0, Qt.CheckState.Unchecked)

    return widget


def get_checked_items(tree):
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


class New(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('New Title')
        self.layout = QVBoxLayout()


class NewManual(New):
    def __init__(self):
        super().__init__()
        self.platform_field = None
        self.date_edit = None
        self.developer_field = None
        self.genre_field = None
        self.title_edit = None
        self.publisher_field = None

    def init_submit(self, submit_layout):
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        submit_layout.addWidget(submit_button)

    def init_manual(self):
        parent_layout = QHBoxLayout()
        layout_top = QHBoxLayout()
        layout_13 = QVBoxLayout()
        layout_23 = QVBoxLayout()
        layout_33 = QVBoxLayout()
        layout_btm = QHBoxLayout()

        self.init_title(layout_top)
        self.init_date(layout_top)

        self.init_platform(layout_13)

        self.init_genre(layout_23)
        self.init_developer(layout_23)

        self.init_publisher(layout_33)
        self.init_engine(layout_33)

        self.init_submit(layout_btm)

        parent_layout.addLayout(layout_13)
        parent_layout.addLayout(layout_23)
        parent_layout.addLayout(layout_33)
        self.layout.addLayout(layout_top)
        self.layout.addLayout(parent_layout)
        self.layout.addLayout(layout_btm)

    def init_date(self, basic_info_layout):
        self.date_edit = QDateEdit(self)
        self.date_edit.setDisplayFormat('yyyy-MMM-dd')
        self.date_edit.setCalendarPopup(True)
        basic_info_layout.addWidget(QLabel("Date"))
        basic_info_layout.addWidget(self.date_edit)

    def init_title(self, basic_info_layout):
        self.title_edit = QLineEdit(self)
        basic_info_layout.addWidget(QLabel("Title"))
        basic_info_layout.addWidget(self.title_edit)

    def init_publisher(self, advanced_info_layout):
        log('info', 'initializing new publisher')
        publisher_data_obj = PublisherData()
        publisher_list = publisher_data_obj.get_publishers()
        self.publisher_field = helper_qtreewidget(publisher_list, 'Publishers')
        advanced_info_layout.addWidget(self.publisher_field)

    def init_genre(self, basic_info_layout):
        log('info', 'initializing new genre')
        genre_data_obj = GenreData()
        genre_list = genre_data_obj.get_genres()
        self.genre_field = helper_qtreewidget(genre_list, 'Genres')
        basic_info_layout.addWidget(self.genre_field)

    def init_developer(self, advanced_info_layout):
        log('info', 'initializing new developer')
        developer_data_obj = DeveloperData()
        developer_list = developer_data_obj.get_developers()
        self.developer_field = helper_qtreewidget(developer_list, 'Developers')
        advanced_info_layout.addWidget(self.developer_field)

    def init_platform(self, basic_info_layout):
        log('info', 'initializing new platform')
        platform_data_obj = PlatformData()
        platform_list = platform_data_obj.get_platforms()
        self.platform_field = helper_qtreewidget(platform_list, 'Platforms')
        basic_info_layout.addWidget(self.platform_field)

    def submit(self):
        title = self.title_edit.text()
        date = self.date_edit.date().toString()

        # Get checked items from each tree
        selected_platforms = get_checked_items(self.platform_field)
        selected_genres = get_checked_items(self.genre_field)
        selected_developers = get_checked_items(self.developer_field)
        selected_publishers = get_checked_items(self.publisher_field)

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
        json_data.append_to_json(data)

        self.close()

    def init_engine(self, layout_33):
        log('info', 'initializing new engine')
        engine_data_obj = EngineData()
        engine_list = engine_data_obj.get_engines()
        self.engine_field = helper_qtreewidget(engine_list, 'Engine')
        layout_33.addWidget(self.engine_field)


class NewSteam(New):
    def __init__(self):
        super().__init__()
        self.steam_id = None

    def init_steam(self):
        self.steam_id = QLineEdit()
        self.layout.addWidget(QLabel("Steam ID"))
        self.layout.addWidget(self.steam_id)
        self.init_submit_steam(self.layout)

    def init_submit_steam(self):
        submit_button = QPushButton("Submit")
        try:
            submit_button.clicked.connect(self.submit_steam)
        except Exception as e:
            print(e)
        self.layout.addWidget(submit_button)

    def submit_steam(self):
        steam_id = self.steam_id.text().strip()
        print(steam_id)
        self.close()


class NewWikipedia(New):
    def __init__(self):
        super().__init__()

    def init_wikipedia(self):
        parent_layout = QHBoxLayout()
        layout_top = QHBoxLayout()
        layout_13 = QVBoxLayout()
        layout_23 = QVBoxLayout()
        layout_btm = QHBoxLayout()

        self.wikipedia_url = QLineEdit()
        layout_top.addWidget(QLabel("Wikipedia page:"))
        layout_top.addWidget(self.wikipedia_url)

        self.init_submit_wkp(layout_top)

        parent_layout.addLayout(layout_top)
        parent_layout.addLayout(layout_13)
        parent_layout.addLayout(layout_23)
        parent_layout.addLayout(layout_btm)
        self.layout.addLayout(parent_layout)

    def init_submit_wkp(self, submit_layout):
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(lambda: self.submit_wikipedia(self.wikipedia_url))
        submit_layout.addWidget(submit_button)

    def submit_wikipedia(self, url_obj):
        url = url_obj.text()



class NewWizard(NewManual, NewSteam, NewWikipedia):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.init_wizard()
        self.setLayout(self.layout)

    def init_wizard(self):
        self.manual_button = QPushButton('Manual')
        self.layout.addWidget(self.manual_button)
        self.manual_button.clicked.connect(self.clicked_manual_btn)

        self.steam_button = QPushButton('From Steam')
        self.layout.addWidget(self.steam_button)
        self.steam_button.clicked.connect(self.clicked_steam_btn)

        self.wikipedia_button = QPushButton('From Wikipedia')
        self.layout.addWidget(self.wikipedia_button)
        self.wikipedia_button.clicked.connect(self.clicked_wikipedia_btn)

    def hide_wizard_btns(self):
        self.manual_button.hide()
        self.steam_button.hide()
        self.wikipedia_button.hide()

    def clicked_manual_btn(self):
        self.hide_wizard_btns()
        self.init_manual()

    def clicked_steam_btn(self):
        self.hide_wizard_btns()
        self.init_steam()

    def clicked_wikipedia_btn(self):
        self.hide_wizard_btns()
        self.init_wikipedia()
