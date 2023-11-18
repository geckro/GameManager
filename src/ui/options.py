from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QDialog, QCheckBox, QVBoxLayout, QToolBar, QWidget, QHBoxLayout, QFileDialog, QComboBox, \
    QLabel


class Options(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameManager - Options")
        self.init_ui()

    def general_opts(self, parent_layout):
        layout = QVBoxLayout()

        opt_hide_toolbar = QCheckBox('Hide Toolbar')
        layout.addWidget(opt_hide_toolbar)

        opt_theme = QComboBox()
        opt_theme.addItems(['System', 'Light', 'Dark'])
        layout.addWidget(QLabel('Application Theme'))
        layout.addWidget(opt_theme)

        layout.setDirection(QVBoxLayout.Direction.TopToBottom)

        layout.addStretch()
        parent_layout.addLayout(layout)


    def emulator_opts(self, parent_layout):
        layout = QVBoxLayout()
        opt_dolphin_dir = QFileDialog.getExistingDirectory(None, 'Select folder', 'C:\\')
        layout.addWidget(opt_dolphin_dir)
        parent_layout.addLayout(layout)

    def init_ui(self):
        self.parent_layout = QHBoxLayout(self)

        self.toolbar = QToolBar()
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolbar.setMovable(False)
        self.toolbar.setOrientation(Qt.Orientation.Vertical)
        self.toolbar.setStyleSheet(
            "background-color: rgb(255, 255, 255); border-radius: 1em; padding: 3px;"
        )

        general_opt = QAction(QIcon('src/img/icons/actions/configure.svg'), 'General', self)
        self.toolbar.addAction(general_opt)

        emulator_opt = QAction(QIcon('src/img/icons/actions/application-x-apple-diskimage.svg'), 'Emulators', self)
        self.toolbar.addAction(emulator_opt)

        general_opt.triggered.connect(self.general_opts)

        emulator_opt.triggered.connect(self.emulator_opts)

        self.parent_layout.addWidget(self.toolbar)

        self.general_opts(self.parent_layout)