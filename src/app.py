from PyQt6.QtWidgets import QMainWindow, QMenuBar, QMenu, QLabel, QLineEdit, QToolBar
from PyQt6.QtGui import QAction, QIcon
from ui.menubar.help import Help
from search import Search

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

        # Window Title and Icon
        self.setWindowTitle("GameManager")
        self.setWindowIcon(QIcon("src/img/gamemanager.svg"))

        
        
    def initUI(self):
        # Create toolbar
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        # Create search label and search box and add it to toolbar
        search_label = QLabel("Search: ")
        toolbar.addWidget(search_label)
        search_box = QLineEdit()
        toolbar.addWidget(search_box)

        # When the enter key is pressed, connect it to to search.py
        search_box.returnPressed.connect(lambda: Search.search(search_box))

        # Add menubar
        self.MenuActions()
        self.MenuBar()

        # Center the window
        self.center()

    def MenuBar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # File Menu
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)
        file_menu.addAction(self.file_new)
        file_menu.addAction(self.file_open)
        file_menu.addAction(self.file_save)
        file_menu.addAction(self.file_exit)

        # Edit Menu
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction(self.edit_copy)
        edit_menu.addAction(self.edit_cut)
        edit_menu.addAction(self.edit_paste)

        # Help Menu
        help_menu = menu_bar.addMenu("&Help")
        help_menu.addAction(self.help_update)
        help_menu.addAction(self.help_about)

    
    def MenuActions(self):
        self.file_new = QAction(QIcon.fromTheme('document-new'), "&New", self)
        self.file_open = QAction(QIcon.fromTheme('document-open'), "&Open", self)
        self.file_save = QAction(QIcon.fromTheme('document-save'), "&Save", self)
        self.file_exit = QAction(QIcon.fromTheme('application-exit'), "&Exit", self)

        self.edit_copy = QAction(QIcon.fromTheme('edit-copy'), "&Copy", self)
        self.edit_cut = QAction(QIcon.fromTheme('edit-cut'), "&Cut", self)
        self.edit_paste = QAction(QIcon.fromTheme('edit-paste'), "&Paste", self)

        self.help_update = QAction(QIcon.fromTheme('update-none'), "&Check for Updates", self)
        self.help_update.triggered.connect(lambda: Help().MenuUpdate(self))
        self.help_about = QAction(QIcon.fromTheme('help-about'), "&About GameManager", self)
        self.help_about.triggered.connect(lambda: Help().MenuAbout(self))
    
    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

