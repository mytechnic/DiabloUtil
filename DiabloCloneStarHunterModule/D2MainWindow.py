from PyQt5 import QtGui
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QWidget, QHBoxLayout

from DiabloCloneStarHunterModule import TargetIpHunterTabUnit, TargetIpHunterTab, D2MainWindowTopUnit, FirewallTab, \
    FirewallTabUnit, HelpTab
from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def paintMainWindow(widget, config, app):
    loadWindowUnit(widget, config, app)

    layout = QVBoxLayout()
    layout.addLayout(getHeaderLayout(widget, config))
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

    FirewallTabUnit.programPathTitle(widget, config)
    FirewallTabUnit.programPathForm(widget, config)
    FirewallTabUnit.programSearchButton(widget, config, FirewallTab.programSearchButtonClickedEvent)
    FirewallTabUnit.firewallPolicyTitle(widget, config)
    FirewallTabUnit.firewallPolicyAClass(widget, config)
    FirewallTabUnit.firewallPolicyBClass(widget, config)
    FirewallTabUnit.firewallPolicySetResultTitle(widget, config)
    FirewallTabUnit.firewallPolicySetResult(widget, config)
    FirewallTabUnit.createFirewallButton(widget, config, FirewallTab.createFirewallButtonClickedEvent)
    FirewallTabUnit.deleteFirewallButton(widget, config, FirewallTab.deleteFirewallButtonClickedEvent)
    FirewallTabUnit.openFirewallButton(widget, config, FirewallTab.openFirewallButtonClickedEvent)


def getHeaderLayout(widget, config):
    global __WIDGET__, __CONFIG__
    __WIDGET__ = widget
    __CONFIG__ = config

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
    font = QtGui.QFont()

    tabs = QTabWidget()
    tabs.setFont(font)
    tabs.currentChanged.connect(currentChangedEvent)

    tabs.addTab(TargetIpHunterTab.targetIpHunterTabWidget(widget, config, app), "게임IP 조회")
    tabs.addTab(FirewallTab.firewallTabWidget(widget, config), "방화벽 설정")
    tabs.addTab(HelpTab.helpTabWidget(widget, config), "도움말")

    tabs.setTabToolTip(0, "게임의 IP를 조회 할 수 있습니다.")
    tabs.setTabToolTip(1, "방화벽을 설정 또는 삭제 할 수 있습니다.")
    tabs.setTabToolTip(2, "도움말")

    layout = QVBoxLayout()
    layout.addWidget(tabs)

    return layout


def currentChangedEvent(i):
    config = __CONFIG__

    if i == 0:
        if config.get('manualFindIpMode').isChecked():
            config.get('targetIpForm').setReadOnly(False)
        else:
            config.get('targetIpForm').setReadOnly(True)
    elif i == 1:
        config.get('targetIpForm').setReadOnly(False)
