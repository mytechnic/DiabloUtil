import math
import random
import time

import pyautogui
from PyQt5 import QtCore, QtTest
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule import D2GameUnitAction, D2GamePosition, D2Process, D2GameFlow, D2Timer
from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None
__APP__: QApplication = None


def gameHunterTabWidget(widget, config, app):
    global __WIDGET__, __CONFIG__, __APP__
    __WIDGET__ = widget
    __CONFIG__ = config
    __APP__ = app

    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameNameTitle'))
    sub.addWidget(config.get('gameNameForm'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gamePasswordTitle'))
    sub.addWidget(config.get('gamePasswordForm'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameCreateNumberTitle'))
    sub.addWidget(config.get('gameCreateNumberForm'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameCreateCycleSecTitle'))
    sub.addWidget(config.get('gameCreateCycleSecForm'))
    sub.addWidget(config.get('gameCreateCycleSecUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameJoinAfterSecTitle'))
    sub.addWidget(config.get('gameJoinAfterSecForm'))
    sub.addWidget(config.get('gameJoinAfterSecUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('createdGameNameTitle'))
    sub.addWidget(config.get('createdGameName'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameHunterTickTitle'))
    sub.addWidget(config.get('gameHunterTick'))
    sub.addWidget(config.get('gameHunterTickUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameHunterStatusTitle'))
    sub.addWidget(config.get('gameHunterStatus'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.addWidget(config.get('gameHunterStartButton'))
    sub.addWidget(config.get('gameHunterConfigApplyButton'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.addWidget(config.get('gameHunterHistory'))
    layout.addLayout(sub)

    widget = QWidget()
    widget.setLayout(layout)
    return widget


def gameHunterStartButtonClickedEvent():
    widget = __WIDGET__
    config = __CONFIG__

    saveGameHunterParameter()

    if not D2GameUnitAction.gameStartAction():
        QMessageBox.about(widget, '실행 오류', '디아블로 게임이 실행되지 않았습니다.')
        return

    targetIp = config.getConfig('targetIp')
    gameNamePrefix = config.getConfig('gameNamePrefix')
    gamePassword = config.getConfig('gamePassword')
    gameCreateNumber = config.getConfig('gameCreateNumber')
    gameCreateCycleSec = config.getConfig('gameCreateCycleSec')
    gameJoinAfterSec = config.getConfig('gameJoinAfterSec')

    if not targetIp:
        QMessageBox.about(widget, '입력 오류', '목표 IP를 입력 해 주세요.')
        return

    if not gameNamePrefix:
        QMessageBox.about(widget, '입력 오류', '게임이름을 입력 해 주세요.')
        return

    if not gamePassword:
        QMessageBox.about(widget, '입력 오류', '비밀번호를 입력 해 주세요.')
        return

    if not gameCreateNumber:
        QMessageBox.about(widget, '입력 오류', '생성번호를 입력 해 주세요.')
        return

    if not gameCreateCycleSec:
        QMessageBox.about(widget, '입력 오류', '생성주기를 입력 해 주세요.')
        return

    if not gameJoinAfterSec:
        QMessageBox.about(widget, '입력 오류', '게임내 대기시간을 입력 해 주세요.')
        return

    config.set('gameHunterCreateTime', 0)
    if config.get('isGameHunterActiveMode'):
        setGameHunterActiveMode(False)
    else:
        setGameHunterActiveMode(True)

    runMacroAction(targetIp, gameNamePrefix, gamePassword, gameCreateNumber, gameJoinAfterSec, gameCreateCycleSec)


def gameHunterConfigApplyButtonClickedEvent():
    pass


def saveGameHunterParameter():
    config = __CONFIG__

    targetIp = config.get('targetIpForm').text().strip()
    gameNamePrefix = config.get('gameNameForm').text().strip()
    gamePassword = config.get('gamePasswordForm').text().strip()
    gameCreateNumber = int(config.get('gameCreateNumberForm').text().strip())
    gameCreateCycleSec = int(config.get('gameCreateCycleSecForm').text().strip())
    gameJoinAfterSec = int(config.get('gameJoinAfterSecForm').text().strip())

    config.setConfig('targetIp', targetIp)
    config.setConfig('gameNamePrefix', gameNamePrefix)
    config.setConfig('gamePassword', gamePassword)
    config.setConfig('gameCreateNumber', gameCreateNumber)
    config.setConfig('gameCreateCycleSec', gameCreateCycleSec)
    config.setConfig('gameJoinAfterSec', gameJoinAfterSec)
    config.saveConfig()


def clearAutoMode():
    config = __CONFIG__
    config.set('isGameHunterActiveMode', False)


def setGameHunterActiveMode(isGameHunterActiveMode):
    config = __CONFIG__
    config.set('isGameHunterActiveMode', isGameHunterActiveMode)
    if isGameHunterActiveMode:
        config.get('gameHunterStatus').setText('실행 중 ...')
        config.get('gameHunterStartButton').setText('실행 중지')
    else:
        config.get('gameHunterStatus').setText('준비')
        config.get('gameHunterStartButton').setText('생성 시작')


def runMacroAction(targetIp, gameNamePrefix, gamePassword, gameCreateNumber, gameJoinAfterSec, gameCreateCycleSec):
    config = __CONFIG__

    position = D2GamePosition.getDisplayPosition('1280x768')

    while config.get('isGameHunterActiveMode'):

        # 게임 생성
        gameIpList = getGameCreateRequestAndGameIpList(position, gameNamePrefix, gamePassword, gameCreateNumber,
                                                       gameCreateCycleSec)

        if gameIpList is None:
            break

        if not config.get('isGameHunterActiveMode'):
            break

        sleep(2000)

        if not config.get('isGameHunterActiveMode'):
            break

        # 원하는 IP를 찾았을 경우 대기 모드로 전환
        isFind, findIp = D2Process.isFindGameIp(targetIp, gameIpList)
        if isFind:
            setGameHunterSleepMode()
            break

        if not config.get('isGameHunterActiveMode'):
            break

        # 게임 생성 후 기다림
        debugPrint(str(gameJoinAfterSec) + '초 동안 게임 안에서 대기합니다.')
        sleepAndDisplay(gameJoinAfterSec * 1000)

        if not config.get('isGameHunterActiveMode'):
            break

        # 게임 종료
        gameExit(position)

        if not config.get('isGameHunterActiveMode'):
            break

        # 게임 생성 전 대기 5초
        debugPrint('2초 후 게임 생성을 진행합니다.')
        sleepAndDisplay(2000)

        gameCreateNumber += 1


def getGameCreateRequestAndGameIpList(position, gameNamePrefix, gamePassword, gameCreateNumber, gameCreateCycleSec):
    config = __CONFIG__

    if not config.get('isGameHunterActiveMode'):
        return None

    serverIpList = D2Process.getServerIpList(config.get('programPath'))
    if len(serverIpList) == 0:
        config.get('gameHunterStatus').setText('진행 불가')
        debugPrint('디아블로 서버를 찾을 수 없습니다.')
        return None

    gameIpList = D2Process.getGameIpList(serverIpList)
    if len(gameIpList) > 0:
        config.get('gameHunterStatus').setText('진행 불가')
        debugPrint('게임방 안에 있어 실행 할 수 없습니다.')
        return None

    gameName = gameNamePrefix + str(gameCreateNumber)
    D2GameFlow.gameCreateFlow(position, gameName, gamePassword)
    config.get('gameCreateNumberForm').setText(str(gameCreateNumber + 1))

    if not config.get('isGameHunterActiveMode'):
        return None

    sleepWaitRoom(config, gameCreateCycleSec)

    if not config.get('isGameHunterActiveMode'):
        return None

    # 게임생성 버튼 클릭
    gameIpList = createGameAndIpList(position)
    if gameIpList is None:
        return None

    # 생성된 게임이름 업데이트
    config.get('createdGameName').setText(gameName)
    config.get('createdGameName').repaint()
    config.set('gameHunterCreateTime', time.time())
    config.saveConfig()

    debugPrint('게임을 생성합니다. - ' + gameName)

    return gameIpList


def createGameAndIpList(position):
    config = __CONFIG__

    while config.get('isGameHunterActiveMode'):

        D2GameUnitAction.gameCreateButtonAction(position)
        serverIpList = D2Process.getServerIpList(config.get('programPath'))
        if len(serverIpList) == 0:
            config.get('gameHunterStatus').setText('진행 불가')
            debugPrint('디아블로 서버를 찾을 수 없습니다.')
            break

        gameIpList = D2Process.getGameIpList(serverIpList)
        if len(gameIpList) > 0:
            return gameIpList

        sleep(random.randrange(1000, 3000))

    return None


def sleepWaitRoom(config, gameCreateCycleSec):
    if config.get('gameHunterCreateTime') > 0:
        plus = random.randrange(100, 2000) / 1000
        remainTime = math.ceil(gameCreateCycleSec + plus - (time.time() - config.get('gameHunterCreateTime')))
        debugPrint(str(remainTime) + '초 기다립니다.')
        if remainTime > 0:
            sleepAndDisplay(remainTime * 1000)


def gameExit(position):
    config = __CONFIG__

    if not config.get('isGameHunterActiveMode'):
        return

    serverIpList = D2Process.getServerIpList(config.get('programPath'))
    if len(serverIpList) == 0:
        config.get('gameHunterStatus').setText('진행 불가')
        debugPrint('디아블로 서버를 찾을 수 없습니다.')
        return

    gameIpList = D2Process.getGameIpList(serverIpList)
    if len(gameIpList) == 0:
        config.get('gameHunterStatus').setText('진행 불가')
        debugPrint('게임방 IP를 찾을 수 없습니다.')
        return

    D2GameUnitAction.gameExitAction(position)


def setGameHunterSleepMode():
    config = __CONFIG__

    while config.get('isGameHunterActiveMode'):

        # 잠에서 깨기
        debugPrint('깨어나~~!')
        for i in range(4):
            if i % 2 == 0:
                pyautogui.moveTo(600, 405, 0.1)
            else:
                pyautogui.moveTo(680, 405, 0.1)
            pyautogui.click()
            debugPrint('click')
            sleep(200)

        if not config.get('isGameHunterActiveMode'):
            break

        # 잠자기
        s = random.randrange(60, 120)
        debugPrint(str(s) + '초 동안 잠을 잡니다.')
        sleepAndDisplay(sleep * 1000)

        if not config.get('isGameHunterActiveMode'):
            break


def sleepAndDisplay(n):
    sleep(n, sleepAndDisplayAction)


def sleepAndDisplayAction(remainTime):
    config = __CONFIG__

    timer = str(math.ceil(remainTime / 1000))
    config.get('gameHunterTick').setText(timer),
    config.get('gameHunterTick').repaint()

    if config.get('dashboard').isVisible():
        config.get('dashboardTimer2').setText(timer + ' 초')


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


def debugPrint(message):
    print(now(), ':', message)


def now():
    return D2Timer.now()
