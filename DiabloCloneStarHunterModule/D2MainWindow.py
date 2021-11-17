from PyQt5 import QtGui
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QWidget, QHBoxLayout

from DiabloCloneStarHunterModule import TargetIpHunterTabUnit, TargetIpHunterTab, D2MainWindowTopUnit, FirewallTab, \
    FirewallTabUnit, HelpTab, DashboardConfigTab, DashboardConfigTabUnit
from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def paintMainWindow(widget, config, app):
    global __WIDGET__, __CONFIG__
    __WIDGET__ = widget
    __CONFIG__ = config

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

    TargetIpHunterTabUnit.appExecuteModeTitle(widget, config)
    TargetIpHunterTabUnit.appExecuteModeValue(widget, config)
    TargetIpHunterTabUnit.findIpModeTitle(widget, config)
    TargetIpHunterTabUnit.manualFindIpMode(widget, config, TargetIpHunterTab.manualFindIpModeClickedEvent)
    TargetIpHunterTabUnit.autoFindIpMode(widget, config, TargetIpHunterTab.autoFindIpModeClickedEvent)
    TargetIpHunterTabUnit.stayGameIpMode(widget, config, TargetIpHunterTab.stayModeClickedEvent)
    TargetIpHunterTabUnit.targetIpViewTitle(widget, config)
    TargetIpHunterTabUnit.targetIpViewValue(widget, config)
    TargetIpHunterTabUnit.findIpRegionTitle(widget, config)
    TargetIpHunterTabUnit.findIpRegionResult(widget, config)
    TargetIpHunterTabUnit.findIpResultTitle(widget, config)
    TargetIpHunterTabUnit.findIpResultValue(widget, config)
    TargetIpHunterTabUnit.stayIpTitle(widget, config)
    TargetIpHunterTabUnit.stayIpValue(widget, config)
    TargetIpHunterTabUnit.findAllIpResultTitle(widget, config)
    TargetIpHunterTabUnit.findAllIpResultValue(widget, config)
    TargetIpHunterTabUnit.autoFindIpCounterTimerTitle(widget, config)
    TargetIpHunterTabUnit.autoFindIpCounterTimerValue(widget, config)
    TargetIpHunterTabUnit.autoFindIpCounterTimerUnit(widget, config)
    TargetIpHunterTabUnit.autoFindIpCounterTimer(widget, config, TargetIpHunterTab.autoFindIpCounterTimerTimeoutEvent)
    TargetIpHunterTabUnit.autoFindIpSearchTimer(widget, config, TargetIpHunterTab.autoFindIpSearchTimerTimeoutEvent)
    TargetIpHunterTabUnit.gameIpSearchButton(widget, config, TargetIpHunterTab.gameIpSearchButtonClickedEvent)
    TargetIpHunterTabUnit.dashboardOpenButton(widget, config, TargetIpHunterTab.dashboardOpenButtonClickedEvent)
    TargetIpHunterTabUnit.gameIpResetButton(widget, config, TargetIpHunterTab.gameIpResetClickedEvent)
    TargetIpHunterTabUnit.gameIpHistory(widget, config)
    TargetIpHunterTabUnit.dashboard(app, config)

    FirewallTabUnit.programPathTitle(widget, config)
    FirewallTabUnit.programPathForm(widget, config)
    FirewallTabUnit.programSearchButton(widget, config, FirewallTab.programSearchButtonClickedEvent)
    FirewallTabUnit.firewallPolicyTitle(widget, config)
    FirewallTabUnit.firewallPolicyAClass(widget, config, FirewallTab.firewallPolicyAClassClickedEvent)
    FirewallTabUnit.firewallPolicyBClass(widget, config, FirewallTab.firewallPolicyBClassClickedEvent)
    FirewallTabUnit.firewallPolicyRuleIpTitle(widget, config)
    FirewallTabUnit.firewallPolicyRuleIp(widget, config)
    FirewallTabUnit.createTargetIpFirewallButton(widget, config, FirewallTab.createTargetIpFirewallButtonClickedEvent)
    FirewallTabUnit.createInputTextFirewallButton(widget, config, FirewallTab.createInputTextFirewallButtonClickedEvent)
    FirewallTabUnit.deleteFirewallButton(widget, config, FirewallTab.deleteFirewallButtonClickedEvent)
    FirewallTabUnit.openFirewallButton(widget, config, FirewallTab.openFirewallButtonClickedEvent)

    DashboardConfigTabUnit.dashboardPositionConfigTitle(widget, config)
    DashboardConfigTabUnit.dashboardPositionConfigXTitle(widget, config)
    DashboardConfigTabUnit.dashboardPositionX(widget, config, DashboardConfigTab.dashboardConfigRealtimeEvent)
    DashboardConfigTabUnit.dashboardPositionConfigYTitle(widget, config)
    DashboardConfigTabUnit.dashboardPositionY(widget, config, DashboardConfigTab.dashboardConfigRealtimeEvent)

    DashboardConfigTabUnit.dashboardTargetIpNormalText(widget, config, DashboardConfigTab.dashboardConfigRealtimeEvent)
    DashboardConfigTabUnit.dashboardTargetIpOkText(widget, config, DashboardConfigTab.dashboardConfigRealtimeEvent)
    DashboardConfigTabUnit.dashboardTargetIpFailText(widget, config, DashboardConfigTab.dashboardConfigRealtimeEvent)

    DashboardConfigTabUnit.dashboardTimerConfigTitle(widget, config)
    DashboardConfigTabUnit.dashboardTimerShow(widget, config, DashboardConfigTab.dashboardTimerShowClickedEvent)
    DashboardConfigTabUnit.dashboardTimerHide(widget, config, DashboardConfigTab.dashboardTimerHideClickedEvent)

    DashboardConfigTabUnit.dashboardNormalFontButton(widget, config, DashboardConfigTab.normalFontButtonClickedEvent)
    DashboardConfigTabUnit.dashboardNormalColorButton(widget, config, DashboardConfigTab.normalColorButtonClickedEvent)
    DashboardConfigTabUnit.dashboardOkFontButton(widget, config, DashboardConfigTab.okFontButtonClickedEvent)
    DashboardConfigTabUnit.dashboardOkColorButton(widget, config, DashboardConfigTab.okColorButtonClickedEvent)
    DashboardConfigTabUnit.dashboardFailFontButton(widget, config, DashboardConfigTab.failFontButtonClickedEvent)
    DashboardConfigTabUnit.dashboardFailColorButton(widget, config, DashboardConfigTab.failColorButtonClickedEvent)


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
    font = QtGui.QFont()

    tabs = QTabWidget()
    tabs.setFont(font)
    tabs.currentChanged.connect(currentChangedEvent)

    tabs.addTab(TargetIpHunterTab.targetIpHunterTabWidget(widget, config, app), "게임IP 조회")
    tabs.addTab(FirewallTab.firewallTabWidget(widget, config), "방화벽 설정")
    tabs.addTab(DashboardConfigTab.dashboardConfigTabWidget(widget, config, app), "전광판 설정")
    tabs.addTab(HelpTab.helpTabWidget(widget, config), "도움말")

    layout = QVBoxLayout()
    layout.addWidget(tabs)

    return layout


def currentChangedEvent(i):
    config = __CONFIG__

    config.setConfig('targetIp', config.get('targetIpForm').text().strip())
    if i == 0:
        if config.get('manualFindIpMode').isChecked():
            config.get('targetIpForm').setReadOnly(False)
        else:
            config.get('targetIpForm').setReadOnly(True)
    elif i == 1:
        config.get('targetIpForm').setReadOnly(False)
