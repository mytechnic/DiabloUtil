from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *

from D2IpScan.D2Dashboard import DashboardApp


def findIpModeTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('모드 설정', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('findIpModeTitle', form)


def manualFindIpMode(widget, config, ClickedEvent):
    form = QRadioButton('수동검색 모드', widget)
    form.setChecked(True)
    form.clicked.connect(ClickedEvent)
    form.setMinimumHeight(25)
    config.set('manualFindIpMode', form)


def autoFindIpMode(widget, config, ClickedEvent):
    form = QRadioButton('자동검색 모드', widget)
    form.setChecked(False)
    form.clicked.connect(ClickedEvent)
    form.setMinimumHeight(25)
    config.set('autoFindIpMode', form)


def stayGameIpMode(widget, config, ClickedEvent):
    form = QRadioButton('지킴이 모드', widget)
    form.setChecked(False)
    form.clicked.connect(ClickedEvent)
    form.setMinimumHeight(25)
    config.set('stayGameIpMode', form)


def findIpRegionTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('지역', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('findIpRegionTitle', form)


def findIpRegionResult(widget, config):
    form = QLabel('N/A', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('findIpRegionResult', form)


def findIpResultTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('게임방 IP', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('findIpResultTitle', form)


def findIpResultValue(widget, config):
    form = QLabel('N/A', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('findIpResultValue', form)


def stayIpTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('지킴이 IP', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('stayIpTitle', form)


def stayIpValue(widget, config):
    form = QLabel('N/A', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('stayIpValue', form)


def findAllIpResultTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('연결된 IP', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('findAllIpResultTitle', form)


def findAllIpResultValue(widget, config):
    form = QLabel('N/A', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('findAllIpResultValue', form)


def autoFindIpTimerTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('타이머', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('autoFindTimerTitle', form)


def autoFindIpTimerValue(widget, config):
    form = QLabel('0', widget)
    form.setMinimumHeight(25)
    form.setMinimumWidth(20)
    form.setMaximumWidth(60)
    form.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('autoFindTimerValue', form)


def autoFindIpTimerUnit(widget, config):
    form = QLabel('초 (자동검색 모드에서 동작)', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('autoFindTimerUnit', form)


def autoFindIpTimer(widget, config, timeoutAction):
    form = QTimer(widget)
    form.setInterval(200)
    form.timeout.connect(timeoutAction)
    config.set('autoFindIpTimer', form)


def gameIpSearchButton(widget, config, ClickedEvent):
    form = QPushButton('아이피 검색', widget)
    form.clicked.connect(ClickedEvent)
    form.setMinimumHeight(40)
    config.set('gameIpSearchButton', form)


def gameIpHistoryClearButton(widget, config, ClickedEvent):
    form = QPushButton('로그 초기화', widget)
    form.clicked.connect(ClickedEvent)
    form.setMinimumHeight(40)
    config.set('gameIpHistoryClearButton', form)


def dashboardOpenButton(widget, config, ClickedEvent):
    form = QPushButton('전광판', widget)
    form.clicked.connect(ClickedEvent)
    form.setMinimumHeight(40)
    config.set('dashboardOpenButton', form)


def gameIpHistory(widget, config):
    form = QTextEdit('', widget)
    form.setReadOnly(True)
    config.set('gameIpHistory', form)


def dashboard(app, config):
    app = DashboardApp(app, config)
    config.set('dashboard', app)
