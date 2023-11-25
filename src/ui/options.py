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
        get_default_emulator_paths()

        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.emulator_path_layout = QGridLayout()

        # Multi Platform
        self.emulator_folder_path_helper('RetroArch', 0, 0, self.stub)

        # GameCube + Wii + WiiWare
        self.emulator_folder_path_helper('Dolphin', 2, 0, self.select_dolphin_dir)

        # 3DS
        self.emulator_folder_path_helper('Citra', 4, 0, self.select_citra_dir, 'citra_directory')
        self.emulator_folder_path_helper('Panda3DS', 4, 2, self.stub)

        # Switch
        self.emulator_folder_path_helper('Yuzu', 6, 0, self.stub)
        self.emulator_folder_path_helper('Ryujinx', 6, 2, self.stub)

        # DS
        self.emulator_folder_path_helper('melonDS', 8, 0, self.stub)
        self.emulator_folder_path_helper('DeSmuME', 8, 2, self.stub)

        # PS1
        self.emulator_folder_path_helper('DuckStation', 10, 0, self.stub)

        # PS2
        self.emulator_folder_path_helper('PCSX2', 10, 2, self.stub)
        self.emulator_folder_path_helper('Play!', 12, 0, self.stub)

        # PS3
        self.emulator_folder_path_helper('RPCS3', 12, 2, self.stub)

        # Xbox
        self.emulator_folder_path_helper('xemu', 14, 0, self.stub)

        # Xbox 360
        self.emulator_folder_path_helper('Xenia', 14, 2, self.stub)

        # Wii U
        self.emulator_folder_path_helper('Cemu', 16, 0, self.stub)

        layout.addLayout(self.emulator_path_layout)

        return widget

    def emulator_folder_path_helper(self, emulator_name: str, grid_x_loc: int, grid_y_loc: int, emulator_trigger_func, setting: str = None):
        """
        Helper func to set up emulator folder path Qt widgets

        @param emulator_name: Name of the emulator
        @param grid_x_loc: Grid row position (x) for QGridLayout
        @param grid_y_loc: Grid row position (y) for QGridLayout
        @param emulator_trigger_func: The function to be triggered when pressing browse
        @param setting: (optional) The setting to add to QLineEdit
        """
        self.emulator_path_layout.addWidget(QLabel(f"{emulator_name} Folder Path"), grid_x_loc, grid_y_loc)
        self.opt_emulator_dir = QLineEdit()
        self.opt_emulator_dir.setReadOnly(True)
        if setting:
            self.opt_emulator_dir.setText(check_option(setting))
        self.emulator_path_layout.addWidget(self.opt_emulator_dir, grid_x_loc + 1, grid_y_loc)
        self.opt_emulator_btn = QPushButton('Browse')
        self.opt_emulator_btn.clicked.connect(emulator_trigger_func)
        self.emulator_path_layout.addWidget(self.opt_emulator_btn, grid_x_loc + 1, grid_y_loc + 1)

    def select_dolphin_dir(self):
        self.dolphin_directory = QFileDialog.getExistingDirectory(self, 'Select Dolphin Directory', 'C:\\')
        self.opt_dolphin_dir.setText(self.dolphin_directory)
        add_to_config()

    def select_citra_dir(self):
        self.citra_directory = QFileDialog.getExistingDirectory(self, 'Select Citra Directory', 'C:\\')
        self.opt_citra_dir.setText(self.citra_directory)

    def stub(self):
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
