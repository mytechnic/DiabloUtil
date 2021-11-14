import math
import os
import time
import winsound

import pygame
from PyQt5 import QtCore, QtGui, QtTest
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule import D2ServerIp, D2Timer
from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None
__APP__: QApplication = None


def targetIpHunterTabWidget(widget, config, app):
    global __WIDGET__, __CONFIG__, __APP__
    __WIDGET__ = widget
    __CONFIG__ = config
    __APP__ = app

    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findIpModeTitle'))
    sub.addWidget(config.get('manualFindIpMode'))
    sub.addWidget(config.get('autoFindIpMode'))
    sub.addWidget(config.get('stayGameIpMode'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('targetIpViewTitle'))
    sub.addWidget(config.get('targetIpViewValue'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findIpRegionTitle'))
    sub.addWidget(config.get('findIpRegionResult'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findIpResultTitle'))
    sub.addWidget(config.get('findIpResultValue'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('stayIpTitle'))
    sub.addWidget(config.get('stayIpValue'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('findAllIpResultTitle'))
    sub.addWidget(config.get('findAllIpResultValue'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('autoFindTimerTitle'))
    sub.addWidget(config.get('autoFindTimerValue'))
    sub.addWidget(config.get('autoFindTimerUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.addWidget(config.get('gameIpSearchButton'))
    sub.addWidget(config.get('dashboardOpenButton'))
    sub.addWidget(config.get('gameIpResetButton'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.addWidget(config.get('gameIpHistory'))
    layout.addLayout(sub)

    group = QButtonGroup(widget)
    group.addButton(config.get('manualFindIpMode'))
    group.addButton(config.get('autoFindIpMode'))
    group.addButton(config.get('stayGameIpMode'))

    config.get('manualFindIpMode').setChecked(True)
    findIpSearchModeManualMode()

    widget = QWidget()
    widget.setLayout(layout)
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
    # findIpSearchModeAutoStart()


def stayModeClickedEvent():
    widget = __WIDGET__
    config = __CONFIG__

    if config.get('findIpMode') == 'STAY':
        return

    gameIpList = gameIpSearchAction()
    if len(gameIpList) == 0:
        QMessageBox.about(widget, '오류 메시지', '게임방 IP를 찾을 수 없습니다. 지킴이 모드는 게임방 안에서만 가능합니다.')
        config.get('manualFindIpMode').setChecked(True)
        findIpSearchModeManualMode()
        return

    findIpSearchModeStayMode()
    findIpSearchModeStayStart(','.join(gameIpList))


def gameIpSearchButtonClickedEvent():
    targetIpHunterConfigSave()
    gameIpSearchAction(True)


def gameIpResetClickedEvent():
    config = __CONFIG__
    config.get('findIpRegionResult').setText('N/A')
    config.get('findIpResultValue').setText('N/A')
    config.get('findAllIpResultValue').setText('N/A')
    config.get('gameIpHistory').setText('')
    config.get('autoFindIpTimer').stop()
    config.set('autoFindTimerStart', time.time())
    config.get('autoFindTimerValue').setText('0')
    if config.get('dashboard').isVisible():
        config.get('dashboardTimer').setText('0 초')
        config.get('dashboardTimer2').setText('')


def dashboardOpenButtonClickedEvent():
    config = __CONFIG__
    mainApp = config.get('dashboard')
    mainApp.open()


def autoFindIpTimerTimeoutEvent():
    config = __CONFIG__

    timer = str(math.floor(time.time() - config.get('autoFindTimerStart')))
    config.get('autoFindTimerValue').setText(timer)
    if config.get('dashboard').isVisible():
        config.get('dashboardTimer').setText(timer + ' 초')


def autoFindIpFinderTimeoutEvent():
    config = __CONFIG__

    if config.get('gameIpExist') is None:
        config.set('gameIpExist', True)
        config.set('gameIpLogWrite', True)

    gameIpList = gameIpSearchAction(config.get('gameIpLogWrite'))
    if len(gameIpList) > 0:
        config.set('gameIpExist', True)
        config.set('gameIpLogWrite', False)
    else:
        config.set('gameIpExist', False)
        config.set('gameIpLogWrite', True)


def targetIpHunterConfigSave():
    config = __CONFIG__
    config.setConfig('targetIp', config.get('targetIpForm').text().strip())
    config.saveConfig()


def findIpSearchModeManualMode():
    config = __CONFIG__

    config.set('findIpMode', 'MANUAL')
    config.get('targetIpForm').setReadOnly(False)
    config.get('gameIpSearchButton').setDisabled(False)
    config.get('stayIpValue').setText('N/A')
    targetIpHunterConfigSave()

    startGameIpFinder(False)


def findIpSearchModeAutoMode():
    config = __CONFIG__

    config.set('findIpMode', 'AUTO')
    config.get('targetIpForm').setReadOnly(True)
    config.get('gameIpSearchButton').setDisabled(True)
    config.get('stayIpValue').setText('N/A')
    targetIpHunterConfigSave()

    startGameIpTimer()
    startGameIpFinder(True)


def findIpSearchModeAutoStart():
    config = __CONFIG__

    isFirst = True
    while config.get('autoFindIpMode').isChecked():
        if config.get('KILL_SIGNAL'):
            break

        gameIpList = gameIpSearchAction(isFirst)
        if len(gameIpList) > 0 and isFirst:
            isFirst = False
        elif len(gameIpList) == 0:
            isFirst = True

        sleep(1000)


def findIpSearchModeStayMode():
    config = __CONFIG__

    config.set('findIpMode', 'STAY')
    config.get('targetIpForm').setReadOnly(True)
    config.get('gameIpSearchButton').setDisabled(True)
    config.get('stayIpValue').setText('N/A')
    targetIpHunterConfigSave()

    startGameIpFinder(False)


def gameIpSearchAction(isFirstFindReaction=False):
    config = __CONFIG__

    targetIp = config.getConfig('targetIp')
    serverIpList = D2ServerIp.getServerIpList()
    gameIpList = D2ServerIp.getGameIpList(serverIpList)
    gameRegion = D2ServerIp.getGameRegion(serverIpList)
    gameFindResult = D2ServerIp.getGameFindResult(targetIp, serverIpList, gameIpList,
                                                  config.get('stayGameIpMode').isChecked())

    if targetIp:
        config.get('targetIpViewValue').setText(targetIp)
    else:
        config.get('targetIpViewValue').setText('N/A')
    config.get('findIpRegionResult').setText(gameRegion)
    config.get('findIpResultValue').setText(gameFindResult)
    if config.get('dashboard').isVisible():
        config.get('dashboardGameIp').setText(gameFindResult)
    if len(serverIpList) > 0:
        config.get('findAllIpResultValue').setText(', '.join(serverIpList))
    else:
        config.get('findAllIpResultValue').setText('N/A')

    isFind = D2ServerIp.isFindGameIp(targetIp, gameIpList)
    if isFirstFindReaction:
        if len(gameIpList) > 0:
            startGameIpTimer()
            addGameIpHistory(gameIpList)

        if isFind:
            findGameIpReactionSound()

    return gameIpList


def findGameIpReactionSound():
    file = 'ok.mp3'
    if os.path.isfile(file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sleep(200)
    else:
        winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)
        sleep(2000)


def findIpSearchModeStayStart(stayIp):
    config = __CONFIG__

    config.get('stayIpValue').setText(stayIp)
    while config.get('stayGameIpMode').isChecked():
        if config.get('KILL_SIGNAL'):
            break

        gameIpList = gameIpSearchAction()
        if len(gameIpList) == 0:
            stayIpOutReaction(stayIp)
            break

        isStay = D2ServerIp.isFindGameIp(stayIp, gameIpList)
        if not isStay:
            stayIpOutReaction(stayIp)
            break

        sleep(1000)


def stayIpOutReaction(stayIp):
    config = __CONFIG__

    while config.get('stayGameIpMode').isChecked():
        if config.get('KILL_SIGNAL'):
            break

        msg = stayIp + '(지킴이 모드 실패)'
        config.get('findIpResultValue').setText(msg)
        if config.get('dashboard').isVisible():
            config.get('dashboardGameIp').setText(msg)

        stayIpOutReactionSound()


def stayIpOutReactionSound():
    file = 'stay_out.mp3'
    if os.path.isfile(file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sleep(200)
    else:
        for i in range(3):
            winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)
            sleep(1000)
        sleep(3000)


def now():
    return D2Timer.now()


def addGameIpHistory(gameIpList):
    config = __CONFIG__

    msg = now() + ' - ' + ', '.join(gameIpList)
    config.get('gameIpHistory').setText(config.get('gameIpHistory').toPlainText() + msg + "\n")
    config.get('gameIpHistory').moveCursor(QtGui.QTextCursor.End)


def startGameIpTimer():
    config = __CONFIG__

    if not config.get('autoFindTimerStart') and not config.get('autoFindIpTimer').isActive():
        config.get('autoFindIpTimer').start()
    config.set('autoFindTimerStart', time.time())


def startGameIpFinder(isStart=True):
    config = __CONFIG__

    if isStart:
        config.get('autoFindIpFinder').start()
    elif not isStart:
        config.get('autoFindIpFinder').stop()


def sleep(millisecond, func=None):
    per = 200
    s = time.time() * 1000
    count = math.ceil(millisecond / per)
    for i in range(count):
        e = time.time() * 1000 - s
        if e > millisecond:
            if func:
                func(0)
            return

        remainMillisecond = millisecond - e
        if func:
            if remainMillisecond >= 0:
                func(remainMillisecond)
            else:
                func(0)

        if remainMillisecond >= 0:
            QtTest.QTest.qWait(per)
