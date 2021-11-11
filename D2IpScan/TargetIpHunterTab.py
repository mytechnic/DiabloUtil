import math
import time
import winsound

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *

from D2IpScan import D2ServerIp, D2Timer
from D2IpScan.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None
__APP__: QApplication = None


def targetIpHunterTabWidget(widget, config, app):
    global __WIDGET__, __CONFIG__, __APP__
    __WIDGET__ = widget
    __CONFIG__ = config
    __APP__ = app

    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findIpModeTitle'))
    sub.addWidget(config.get('manualFindIpMode'))
    sub.addWidget(config.get('autoFindIpMode'))
    sub.addWidget(config.get('stayGameIpMode'))
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
    sub.addWidget(config.get('stayIpTitle'))
    sub.addWidget(config.get('stayIpValue'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findAllIpResultTitle'))
    sub.addWidget(config.get('findAllIpResultValue'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('autoFindTimerTitle'))
    sub.addWidget(config.get('autoFindTimerValue'))
    sub.addWidget(config.get('autoFindTimerUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.addWidget(config.get('gameIpSearchButton'))
    sub.addWidget(config.get('gameIpHistoryClearButton'))
    sub.addWidget(config.get('dashboardOpenButton'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.addWidget(config.get('gameIpHistory'))
    layout.addLayout(sub)

    widget = QWidget()
    widget.setLayout(layout)

    group = QButtonGroup(widget)
    group.addButton(config.get('manualFindIpMode'))
    group.addButton(config.get('autoFindIpMode'))
    group.addButton(config.get('stayGameIpMode'))

    findIpSearchModeManualMode()

    return widget


def manualFindIpModeClickedEvent():
    config = __CONFIG__

    if config.get('findIpMode') == 'MANUAL':
        return

    findIpSearchModeManualMode()


def autoFindIpModeClickedEvent():
    config = __CONFIG__

    if config.get('findIpMode') == 'AUTO':
        return

    findIpSearchModeAutoMode()
    findIpSearchModeAutoStart()


def stayModeClickedEvent():
    widget = __WIDGET__
    config = __CONFIG__

    if config.get('findIpMode') == 'STAY':
        return

    gameIpList = gameIpSearchAction()
    if len(gameIpList) == 0:
        QMessageBox.about(widget, '오류 메시지', '지킴이 모드는 게임 내에서만 가능합니다.')
        config.get('manualFindIpMode').setChecked(True)
        findIpSearchModeManualMode()
        return

    findIpSearchModeStayMode()
    findIpSearchModeStayStart(','.join(gameIpList))


def gameIpSearchButtonClickedEvent():
    gameIpSearchAction(True, True)


def GameIpClearClickedEvent():
    config = __CONFIG__
    config.get('gameIpHistory').setText('')


def dashboardOpenButtonClickedEvent():
    config = __CONFIG__
    try:
        mainApp = config.get('dashboard')
        mainApp.open()

    except Exception as e:
        print(e)


def autoFindIpTimerTimeoutEvent():
    config = __CONFIG__

    timer = str(math.floor(time.time() - config.get('autoFindTimerStart')))
    config.get('autoFindTimerValue').setText(timer)
    if config.get('dashboard').isVisible():
        config.get('dashboardTimer').setText(timer + ' 초')


def targetIpHunterConfigSave():
    config = __CONFIG__
    config.setConfig('targetIp', config.get('targetIpForm').text().strip())
    config.saveConfig()


def findIpSearchModeManualMode():
    config = __CONFIG__

    config.set('findIpMode', 'MANUAL')
    config.get('targetIpForm').setReadOnly(False)
    config.get('gameIpSearchButton').setDisabled(False)
    config.get('stayIpValue').setText('')
    targetIpHunterConfigSave()


def findIpSearchModeAutoMode():
    config = __CONFIG__

    config.set('findIpMode', 'AUTO')
    config.get('targetIpForm').setReadOnly(True)
    config.get('gameIpSearchButton').setDisabled(True)
    config.get('stayIpValue').setText('')

    startGameIpTimer()
    targetIpHunterConfigSave()


def findIpSearchModeAutoStart():
    config = __CONFIG__

    isGameIpHistory = True
    while config.get('autoFindIpMode').isChecked():
        gameIpList = gameIpSearchAction(isAddGameIpHistory=isGameIpHistory)
        if len(gameIpList) == 0:
            isFindGame = False
        else:
            isFindGame = True

        if isGameIpHistory:
            isGameIpHistory = False
        elif not isFindGame:
            isGameIpHistory = True

        D2Timer.sleep(1000)


def findIpSearchModeStayMode():
    config = __CONFIG__

    config.set('findIpMode', 'STAY')
    config.get('targetIpForm').setReadOnly(True)
    config.get('gameIpSearchButton').setDisabled(True)
    config.get('stayIpValue').setText('')
    targetIpHunterConfigSave()


def gameIpSearchAction(isReaction=False, isAddGameIpHistory=False):
    config = __CONFIG__
    targetIpHunterConfigSave()

    targetIp = config.getConfig('targetIp')
    serverIpList = D2ServerIp.getServerIpList()
    gameIpList = D2ServerIp.getGameIpList(serverIpList)
    gameRegion = D2ServerIp.getGameRegion(serverIpList)
    gameFindResult = D2ServerIp.getGameFindResult(targetIp, gameIpList, config.get('stayGameIpMode').isChecked())

    config.get('findIpRegionResult').setText(gameRegion)
    config.get('findIpResultValue').setText(gameFindResult)
    if config.get('dashboard').isVisible():
        config.get('dashboardGameIp').setText(gameFindResult)
    config.get('findAllIpResultValue').setText(', '.join(serverIpList))

    if isAddGameIpHistory and len(gameIpList) > 0:
        startGameIpTimer()
        addGameIpHistory(gameIpList)

    isFind = D2ServerIp.isFindGameIp(targetIp, gameIpList)
    if isFind and isReaction:
        findGameIpReaction()

    return gameIpList


def findGameIpReaction():
    winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)


def findIpSearchModeStayStart(stayIp):
    config = __CONFIG__

    config.get('stayIpValue').setText(stayIp)
    while config.get('stayGameIpMode').isChecked():
        gameIpList = gameIpSearchAction()
        if len(gameIpList) == 0:
            stayIpOutReaction(stayIp)
            break

        isStay = D2ServerIp.isFindGameIp(stayIp, gameIpList)
        if not isStay:
            stayIpOutReaction(stayIp)
            break

        D2Timer.sleep(1000)


def stayIpOutReaction(stayIp):
    config = __CONFIG__

    while config.get('stayGameIpMode').isChecked():
        msg = stayIp + '(지킴이 모드 실패)'
        config.get('findIpResultValue').setText(msg)
        if config.get('dashboard').isVisible():
            config.get('dashboardGameIp').setText(msg)
        winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)
        D2Timer.sleep(2000)


def addGameIpHistory(gameIpList):
    config = __CONFIG__

    msg = ', '.join(gameIpList)
    config.get('gameIpHistory').setText(config.get('gameIpHistory').toPlainText() + msg + "\n")
    config.get('gameIpHistory').moveCursor(QtGui.QTextCursor.End)


def startGameIpTimer():
    config = __CONFIG__

    try:
        if not config.get('autoFindTimerStart'):
            config.get('autoFindIpTimer').start()
        config.set('autoFindTimerStart', time.time())
    except Exception as e:
        print(e)
