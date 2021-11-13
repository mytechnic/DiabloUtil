from PyQt5 import QtGui
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QWidget

from DiabloCloneStarHunterMasterModule import GameHunterTabUnit, GameHunterTab
from DiabloCloneStarHunterModule import TargetIpHunterTab, FirewallTab, \
    HelpTab, D2MainWindow
from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def paintMainWindow(widget, config, app):
    global __WIDGET__, __CONFIG__
    __WIDGET__ = widget
    __CONFIG__ = config

    D2MainWindow.loadWindowUnit(widget, config, app)
    loadWindowUnit(widget, config, app)

    layout = QVBoxLayout()
    layout.addLayout(D2MainWindow.getHeaderLayout(config))
    layout.addLayout(getTabLayout(widget, config, app))
    widget.setLayout(layout)


def loadWindowUnit(widget, config, app):
    GameHunterTabUnit.gameNameTitle(widget, config)
    GameHunterTabUnit.gameNameForm(widget, config)
    GameHunterTabUnit.gamePasswordTitle(widget, config)
    GameHunterTabUnit.gamePasswordForm(widget, config)
    GameHunterTabUnit.gameCreateNumberTitle(widget, config)
    GameHunterTabUnit.gameCreateNumberForm(widget, config)
    GameHunterTabUnit.gameCreateCycleSecTitle(widget, config)
    GameHunterTabUnit.gameCreateCycleSecForm(widget, config)
    GameHunterTabUnit.gameCreateCycleSecUnit(widget, config)
    GameHunterTabUnit.gameJoinAfterSecTitle(widget, config)
    GameHunterTabUnit.gameJoinAfterSecForm(widget, config)
    GameHunterTabUnit.gameJoinAfterSecUnit(widget, config)
    GameHunterTabUnit.createdGameNameTitle(widget, config)
    GameHunterTabUnit.createdGameName(widget, config)
    GameHunterTabUnit.gameHunterTickTitle(widget, config)
    GameHunterTabUnit.gameHunterTick(widget, config)
    GameHunterTabUnit.gameHunterTickUnit(widget, config)
    GameHunterTabUnit.gameHunterStatusTitle(widget, config)
    GameHunterTabUnit.gameHunterStatus(widget, config)
    GameHunterTabUnit.gameHunterStartButton(widget, config, GameHunterTab.gameHunterStartButtonClickedEvent)
    GameHunterTabUnit.gameHunterConfigApplyButton(widget, config, GameHunterTab.gameHunterConfigApplyButtonClickedEvent)


def getTabLayout(widget, config, app):
    font = QtGui.QFont()

    tabs = QTabWidget()
    tabs.setFont(font)
    tabs.currentChanged.connect(currentChangedEvent)

    tabs.addTab(TargetIpHunterTab.targetIpHunterTabWidget(widget, config, app), "게임IP 조회")
    tabs.addTab(FirewallTab.firewallTabWidget(widget, config), "방화벽 설정")
    tabs.addTab(GameHunterTab.gameHunterTabWidget(widget, config, app), "게임 헌터")
    tabs.addTab(HelpTab.helpTabWidget(widget, config), "도움말")

    tabs.setTabToolTip(0, "게임의 IP를 조회 할 수 있습니다.")
    tabs.setTabToolTip(1, "방화벽을 설정 또는 삭제 할 수 있습니다.")
    tabs.setTabToolTip(2, "게임을 자동으로 생성 할 수 있습니다.")
    tabs.setTabToolTip(3, "도움말")

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
