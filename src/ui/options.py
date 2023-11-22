from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QDialog, QCheckBox, QVBoxLayout, QToolBar, QWidget, QHBoxLayout, QFileDialog, QComboBox, \
    QLabel, QStackedLayout, QPushButton, QLineEdit, QGridLayout

from core.config import add_to_config, check_option
from core.emulator_config import get_default_emulator_paths


class Options(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameManager - Options")
        self.init_ui()

    def general_opts(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        opt_hide_toolbar = QCheckBox('Hide Toolbar')
        layout.addWidget(opt_hide_toolbar)

        opt_theme = QComboBox()
        opt_theme.addItems(['System', 'Light', 'Dark'])
        layout.addWidget(QLabel('Application Theme'))
        layout.addWidget(opt_theme)

        return widget

    def emulator_opts(self):
        if check_option('has_not_checked_emulator_paths'):
            get_default_emulator_paths()

        widget = QWidget()
        layout = QVBoxLayout(widget)

        emulator_path_layout = QGridLayout()

        emulator_path_layout.addWidget(QLabel("Dolphin Folder Path"), 0, 0)
        self.opt_dolphin_dir = QLineEdit()
        self.opt_dolphin_dir.setReadOnly(True)
        emulator_path_layout.addWidget(self.opt_dolphin_dir, 1, 0)
        opt_dolphin_button = QPushButton('Browse...')
        opt_dolphin_button.clicked.connect(self.select_dolphin_dir)
        emulator_path_layout.addWidget(opt_dolphin_button, 1, 1)

        emulator_path_layout.addWidget(QLabel("RetroArch Folder Path"), 0, 2)
        self.opt_retroarch_dir = QLineEdit()
        self.opt_retroarch_dir.setReadOnly(True)
        emulator_path_layout.addWidget(self.opt_retroarch_dir, 1, 2)
        opt_retroarch_button = QPushButton('Browse...')
        opt_retroarch_button.clicked.connect(self.select_retroarch_dir)
        emulator_path_layout.addWidget(opt_retroarch_button, 1, 3)

        emulator_path_layout.addWidget(QLabel("Citra Folder Path"), 2, 0)
        self.opt_citra_dir = QLineEdit()
        self.opt_citra_dir.setReadOnly(True)
        emulator_path_layout.addWidget(self.opt_citra_dir, 3, 0)
        opt_citra_button = QPushButton('Browse...')
        opt_citra_button.clicked.connect(self.select_citra_dir)
        emulator_path_layout.addWidget(opt_citra_button, 3, 1)

        emulator_path_layout.addWidget(QLabel("Yuzu Folder Path"), 4, 0)
        self.opt_yuzu_dir = QLineEdit()
        self.opt_yuzu_dir.setReadOnly(True)
        emulator_path_layout.addWidget(self.opt_yuzu_dir, 5, 0)
        opt_yuzu_button = QPushButton('Browse...')
        opt_yuzu_button.clicked.connect(self.select_yuzu_dir)
        emulator_path_layout.addWidget(opt_yuzu_button, 5, 1)

        emulator_path_layout.addWidget(QLabel("Ryujinx Folder Path"), 4, 2)
        self.opt_ryujinx_dir = QLineEdit()
        self.opt_ryujinx_dir.setReadOnly(True)
        emulator_path_layout.addWidget(self.opt_ryujinx_dir, 5, 2)
        opt_ryujinx_button = QPushButton('Browse...')
        opt_ryujinx_button.clicked.connect(self.select_ryujinx_dir)
        emulator_path_layout.addWidget(opt_ryujinx_button, 5, 3)

        layout.addLayout(emulator_path_layout)

        return widget

    def select_dolphin_dir(self):
        self.dolphin_directory = QFileDialog.getExistingDirectory(self, 'Select Dolphin Directory', 'C:\\')
        self.opt_dolphin_dir.setText(self.dolphin_directory)
        add_to_config()

    def select_citra_dir(self):
        self.citra_directory = QFileDialog.getExistingDirectory(self, 'Select Citra Directory', 'C:\\')
        self.opt_citra_dir.setText(self.citra_directory)

    def select_yuzu_dir(self):
        pass

    def select_ryujinx_dir(self):
        pass


    def select_retroarch_dir(self):
        pass

    def init_ui(self):
        self.layout = QHBoxLayout(self)

        self.toolbar = QToolBar()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolbar.setMovable(False)
        self.toolbar.setOrientation(Qt.Orientation.Vertical)
        self.toolbar.setStyleSheet("border-right: 1px solid rgba(0, 0, 0, 100);")
        self.layout.addWidget(self.toolbar)

        general_opt = QAction(QIcon('src/img/icons/actions/configure.svg'), 'General', self)
        self.toolbar.addAction(general_opt)

        emulator_opt = QAction(QIcon('src/img/icons/actions/application-x-apple-diskimage.svg'), 'Emulators', self)
        self.toolbar.addAction(emulator_opt)

        self.stacked_layout = QStackedLayout()
        self.layout.addLayout(self.stacked_layout)

        self.stacked_layout.addWidget(self.general_opts())
        self.stacked_layout.addWidget(self.emulator_opts())

        general_opt.triggered.connect(lambda: self.stacked_layout.setCurrentIndex(0))
        emulator_opt.triggered.connect(lambda: self.stacked_layout.setCurrentIndex(1))
