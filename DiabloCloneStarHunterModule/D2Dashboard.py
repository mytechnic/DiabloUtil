from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule import D2DashboardUnit

__TITLE__ = 'Diablo Clone Star Hunter 1.0 DASHBOARD'
__WIDTH__ = 800
__HEIGHT__ = 25


class DashboardApp(QWidget):
    def __init__(self, app, config):
        super().__init__()
        self.initUI(app, config)

    def initUI(self, app, config):
        self.setWindowFlags(self.windowFlags()
                            | QtCore.Qt.WindowStaysOnTopHint
                            | QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WA_ShowWithoutActivating)
        self.setWindowTitle(__TITLE__)
        self.center(app)
        self.setFixedSize(__WIDTH__, __HEIGHT__)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        D2DashboardUnit.dashboardGameIp(self, config)
        D2DashboardUnit.dashboardTimer(self, config)

        sub = QHBoxLayout()
        sub.setContentsMargins(0, 0, 0, 0)
        sub.addWidget(config.get('dashboardGameIp'))
        sub.addWidget(config.get('dashboardTimer'))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(sub)

        self.setLayout(layout)

    def center(self, app):
        qr = app.desktop().screenGeometry()
        width, height = qr.width(), qr.height()
        self.move(width / 2 - __WIDTH__ / 2, 40)

    def open(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
