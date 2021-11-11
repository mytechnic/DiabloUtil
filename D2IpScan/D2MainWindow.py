from PyQt5 import QtGui
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QWidget, QHBoxLayout

from D2IpScan import TargetIpHunterTabUnit, TargetIpHunterTab, D2MainWindowTopUnit, FirewallTab
from D2IpScan.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def paintMainWindow(widget, config, app):
    loadWindowUnit(widget, config, app)

    layout = QVBoxLayout()
    layout.addLayout(getHeaderLayout(config))
    layout.addLayout(getTabLayout(widget, config, app))
    widget.setLayout(layout)


def loadWindowUnit(widget, config, app):
    D2MainWindowTopUnit.targetIpTitle(widget, config)
    D2MainWindowTopUnit.targetIpForm(widget, config)
    D2MainWindowTopUnit.targetIpHelp(widget, config)
    D2MainWindowTopUnit.topMostForm(widget, config)

    TargetIpHunterTabUnit.findIpModeTitle(widget, config)
    TargetIpHunterTabUnit.manualFindIpMode(widget, config, TargetIpHunterTab.manualFindIpModeClickedEvent)
    TargetIpHunterTabUnit.autoFindIpMode(widget, config, TargetIpHunterTab.autoFindIpModeClickedEvent)
    TargetIpHunterTabUnit.stayGameIpMode(widget, config, TargetIpHunterTab.stayModeClickedEvent)
    TargetIpHunterTabUnit.findIpRegionTitle(widget, config)
    TargetIpHunterTabUnit.findIpRegionResult(widget, config)
    TargetIpHunterTabUnit.findIpResultTitle(widget, config)
    TargetIpHunterTabUnit.findIpResultValue(widget, config)
    TargetIpHunterTabUnit.stayIpTitle(widget, config)
    TargetIpHunterTabUnit.stayIpValue(widget, config)
    TargetIpHunterTabUnit.findAllIpResultTitle(widget, config)
    TargetIpHunterTabUnit.findAllIpResultValue(widget, config)
    TargetIpHunterTabUnit.autoFindIpTimerTitle(widget, config)
    TargetIpHunterTabUnit.autoFindIpTimerValue(widget, config)
    TargetIpHunterTabUnit.autoFindIpTimerUnit(widget, config)
    TargetIpHunterTabUnit.autoFindIpTimer(widget, config, TargetIpHunterTab.autoFindIpTimerTimeoutEvent)
    TargetIpHunterTabUnit.gameIpSearchButton(widget, config, TargetIpHunterTab.gameIpSearchButtonClickedEvent)
    TargetIpHunterTabUnit.dashboardOpenButton(widget, config, TargetIpHunterTab.dashboardOpenButtonClickedEvent)

    TargetIpHunterTabUnit.gameIpHistoryClearButton(widget, config, TargetIpHunterTab.GameIpClearClickedEvent)
    TargetIpHunterTabUnit.gameIpHistory(widget, config)
    TargetIpHunterTabUnit.dashboard(app, config)


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


def getTabLayout(widget, config, app):
    tabs = QTabWidget()
    font = QtGui.QFont()
    tabs.setFont(font)

    tabs.addTab(TargetIpHunterTab.targetIpHunterTabWidget(widget, config, app), "게임IP 조회")
    tabs.addTab(FirewallTab.firewallTabWidget(widget, config), "방화벽 설정")
    tabs.addTab(gameHunterTabWidget(widget, config), "게임 헌터")
    tabs.setTabToolTip(0, "게임의 서버 IP를 조회 할 수 있습니다.")
    tabs.setTabToolTip(1, "방화벽을 설정 또는 삭제 할 수 있습니다.")
    tabs.setTabToolTip(2, "게임을 자동으로 생성 할 수 있습니다.")

    layout = QVBoxLayout()
    layout.addWidget(tabs)

    return layout


def firewallTabWidget(widget, config):
    layout = QVBoxLayout()

    widget = QWidget()
    widget.setLayout(layout)

    return widget


def gameHunterTabWidget(widget, config):
    layout = QVBoxLayout()

    widget = QWidget()
    widget.setLayout(layout)

    return widget
