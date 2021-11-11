from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QWidget, QHBoxLayout, QButtonGroup

from D2IpScan import D2WindowUnit
from D2IpScan.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def paintMainWindow(widget, config):
    loadWindowUnit(widget, config)

    layout = QVBoxLayout()
    layout.addLayout(getHeaderLayout(config))
    layout.addLayout(getTabLayout(config))
    widget.setLayout(layout)


def loadWindowUnit(widget, config):
    global __WIDGET__, __CONFIG__
    __WIDGET__ = widget
    __CONFIG__ = config

    D2WindowUnit.targetIpTitle(config)
    D2WindowUnit.targetIpForm(config)
    D2WindowUnit.targetIpHelp(config)
    D2WindowUnit.topMostForm(widget, config)
    D2WindowUnit.findIpModeTitle(config)
    D2WindowUnit.manualFindIpMode(config, manualFindIpModeClickedAction)
    D2WindowUnit.autoFindIpMode(config, autoFindIpModeClickedAction)
    D2WindowUnit.autoFindIpModeConfigTitle(config)
    D2WindowUnit.autoFindIpModeScanSecondForm(config)
    D2WindowUnit.autoFindIpModeScanSecondUnit(config)
    D2WindowUnit.findIpRegionTitle(config)
    D2WindowUnit.findIpRegionResult(config)
    D2WindowUnit.findIpResultTitle(config)
    D2WindowUnit.findIpResultValue(config)
    D2WindowUnit.protectedGameIpTitle(config)
    D2WindowUnit.protectedGameIpOn(config, protectedGameIpOnClickedAction)
    D2WindowUnit.protectedGameIpOff(config, protectedGameIpOffClickedAction)


def getHeaderLayout(config):
    layout = QVBoxLayout()

    sub = QHBoxLayout()
    sub.addWidget(config.get('targetIpTitle'))
    sub.addWidget(config.get('targetIpForm'))
    sub.addWidget(config.get('topMostForm'))
    layout.addLayout(sub)

    sub = QVBoxLayout()
    sub.addWidget(config.get('targetIpHelp'))
    layout.addLayout(sub)

    return layout


def getTabLayout(config):
    tabs = QTabWidget()
    font = QtGui.QFont()
    tabs.setFont(font)

    tabs.addTab(targetIpHunterTabWidget(config), "게임IP 조회")
    tabs.addTab(firewallTabWidget(config), "방화벽 설정")
    tabs.addTab(gameHunterTabWidget(config), "게임 헌터")
    tabs.setTabToolTip(0, "게임의 서버 IP를 조회 할 수 있습니다.")
    tabs.setTabToolTip(1, "방화벽을 설정 또는 삭제 할 수 있습니다.")
    tabs.setTabToolTip(2, "게임을 자동으로 생성 할 수 있습니다.")

    layout = QVBoxLayout()
    layout.addWidget(tabs)

    return layout


def targetIpHunterTabWidget(config):
    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    group1 = QButtonGroup()
    group1.addButton(config.get('manualFindIpMode'))
    group1.addButton(config.get('autoFindIpMode'))
    sub.addWidget(config.get('findIpModeTitle'))
    sub.addWidget(config.get('manualFindIpMode'))
    sub.addWidget(config.get('autoFindIpMode'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('autoFindIpModeConfigTitle'))
    sub.addWidget(config.get('autoFindIpModeScanSecondForm'))
    sub.addWidget(config.get('autoFindIpModeScanSecondUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findIpRegionTitle'))
    sub.addWidget(config.get('findIpRegionResult'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findIpResultTitle'))
    sub.addWidget(config.get('findIpResultValue'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('protectedGameIpTitle'))
    group2 = QButtonGroup()
    group2.addButton(config.get('protectedGameIpOn'))
    group2.addButton(config.get('protectedGameIpOff'))
    sub.addWidget(config.get('protectedGameIpOn'))
    sub.addWidget(config.get('protectedGameIpOff'))
    layout.addLayout(sub)

    widget = QWidget()
    widget.setLayout(layout)

    return widget


def findIpModeClickedAction():
    __CONFIG__.setConfig('findIpSearchMode', 'MANUAL')


def manualFindIpModeClickedAction():
    __CONFIG__.setConfig('findIpSearchMode', 'MANUAL')


def autoFindIpModeClickedAction():
    __CONFIG__.setConfig('findIpSearchMode', 'AUTO')


def protectedGameIpOnClickedAction():
    __CONFIG__.setConfig('protectedGameIpMode', 'ON')


def protectedGameIpOffClickedAction():
    __CONFIG__.setConfig('protectedGameIpMode', 'OFF')


def firewallTabWidget(config):
    layout = QVBoxLayout()

    widget = QWidget()
    widget.setLayout(layout)

    return widget


def gameHunterTabWidget(config):
    layout = QVBoxLayout()

    widget = QWidget()
    widget.setLayout(layout)

    return widget
