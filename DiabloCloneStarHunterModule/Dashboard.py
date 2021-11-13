from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QVBoxLayout, QWidget, QHBoxLayout)

from DiabloCloneStarHunterModule import DashboardUnit, DashboardConfigTab
from DiabloCloneStarHunterModule.D2Config import D2Config

__TITLE__ = 'Diablo Clone Star Hunter DASHBOARD'
__WIDTH__ = 1000
__HEIGHT__ = 25
__CONFIG__: D2Config = None


class DashboardApp(QWidget):
    def __init__(self, app, config):
        global __CONFIG__

        super().__init__()
        __CONFIG__ = config
        self.initUI(app, config)

    def getAppPosition(self, app, config: D2Config):
        qr = app.desktop().screenGeometry()
        width, height = qr.width(), qr.height()
        defaultX = width / 2 - __WIDTH__ / 2

        x = config.getConfig('dashboardPosX') or defaultX
        y = config.getConfig('dashboardPosY') or 40

        if width < x - 40 or height < y - 40:
            x = defaultX
            y = 40

        return x, y

    def initUI(self, app, config):

        self.setWindowTitle(__TITLE__)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(__WIDTH__, __HEIGHT__)
        x, y = self.getAppPosition(app, config)
        self.move(x, y)

        font = DashboardConfigTab.getDashboardFont(config)
        color = DashboardConfigTab.getDashboardFontColor(config)

        DashboardUnit.dashboardGameIp(self, config, font, color)
        DashboardUnit.dashboardTimer(self, config, font, color)

        sub = QHBoxLayout()
        sub.setContentsMargins(0, 0, 0, 0)
        sub.addWidget(config.get('dashboardGameIp'))
        sub.addWidget(config.get('dashboardTimer'))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(sub)
        self.setLayout(layout)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        config = __CONFIG__
        config.setConfig('dashboardPosX', self.pos().x())
        config.setConfig('dashboardPosY', self.pos().y())

    def open(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
