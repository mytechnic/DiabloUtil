import math
import os
import random
import socket
import struct
import subprocess
import sys
import threading
import time
import winsound

import pyautogui as gui
import pygetwindow as gw
import yaml
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtTest
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from pynput.keyboard import Controller


class MainApp(QWidget):
    findIpResult = None
    targetIpValue = None
    programPathValue = None
    createRoomValue = None
    createPasswordValue = None
    createRoomGameNumber = None
    createGameNumberValue = None
    createCycleSecValue = None
    createRoomButton = None
    createDelayValue = None
    sleepModeButton = None
    roomNameTitle = None
    remainSecTitle = None
    debugText = None
    serverTitle = None
    keyboard = Controller()
    isMacroMode = False
    isSleepMode = False

    createTime = 0
    ipLogFile = 'ip-' + time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time())) + '.txt'
    debugLogFile = 'debug-' + time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time())) + '.txt'

    config = {
        'targetIp': '',
        'program': 'C:\Program Files (x86)\Diablo II Resurrected\D2R.exe',
        'room': 'AAA',
        'password': '1',
        'delay': 10,
        'gameNumber': 1,
        'cycleSec': 85
    }

    def __init__(self):
        super().__init__()
        if os.path.isfile('config.yaml'):
            self.loadConfig()
        else:
            self.saveConfig()

        self.initUI()

    def sleep(self, n):
        if n < 3000:
            QtTest.QTest.qWait(n)
            return

        s = time.time() * 1000
        count = math.ceil(n / 500)
        for sec in range(count):
            e = time.time() * 1000 - s
            if e > n:
                return

            remainTime = math.floor((n - e) / 1000.0)
            if remainTime >= 0:
                self.remainSecTitle.setText(str(remainTime))
                self.remainSecTitle.repaint()
                QtTest.QTest.qWait(500)
            else:
                self.remainSecTitle.setText('0')
                self.remainSecTitle.repaint()

    def debugPrint(self, debugMessage):
        msg = self.now() + ' ' + debugMessage
        print(msg)
        self.debugText.setText(self.debugText.toPlainText() + msg + "\n")
        self.debugText.moveCursor(QtGui.QTextCursor.End)
        self.writeDebugLogFile(msg)

    def loadConfig(self):
        with open('config.yaml') as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

    def saveConfig(self):
        with open('config.yaml', 'w') as f:
            yaml.dump(self.config, f)

    def currentSaveConfig(self):
        programPath = self.programPathValue.text().strip()
        roomName = self.createRoomValue.text().strip()
        roomPassword = self.createPasswordValue.text().strip()
        targetIp = self.targetIpValue.text().strip()
        monitoringDelaySec = int(self.createDelayValue.text().strip())
        number = int(self.createGameNumberValue.text().strip())
        cycleSec = int(self.createCycleSecValue.text().strip())

        config = {
            'targetIp': targetIp,
            'program': programPath,
            'room': roomName,
            'password': roomPassword,
            'delay': monitoringDelaySec,
            'gameNumber': number,
            'cycleSec': cycleSec
        }
        self.config.update(config)

        self.saveConfig()

    def initUI(self):
        layout = QVBoxLayout()
        self.openFindIpForm(layout)
        self.openMainForm(layout)

    def now(self):
        return time.strftime('[%H:%M:%S]', time.localtime(time.time()))

    def moveRelAndClick(self, x1, y1, x2, y2):
        self.moveRelOnly(x1, y1, x2, y2)
        delay = random.randrange(100, 400)
        self.sleep(delay)
        gui.click()

    def moveToAndClick(self, x1, y1, x2, y2):
        self.moveToOnly(x1, y1, x2, y2)
        delay = random.randrange(100, 400)
        self.sleep(delay)
        gui.click()

    def moveRelOnly(self, x1, y1, x2, y2):
        x = random.randrange(x1, x2)
        y = random.randrange(y1, y2)
        gui.moveRel(x, y)

    def moveToOnly(self, x1, y1, x2, y2):
        x = random.randrange(x1, x2)
        y = random.randrange(y1, y2)
        delay = (random.randrange(15, 40) / 100)
        gui.moveTo(x, y, delay)

    def gameCreate(self, name, password, number, roomCreateDelay):
        try:
            if not self.isMacroMode:
                return False

            # 게임생성 탭메뉴
            self.moveToAndClick(810, 75, 940, 98)

            if not self.isMacroMode:
                return False

            # 게임이름 입력
            self.moveToAndClick(885, 150, 1135, 160)
            room = name + str(number)
            gui.typewrite(room, interval=0.15)

            if not self.isMacroMode:
                return False

            # 비밀번호 입력
            self.moveToAndClick(885, 198, 1135, 208)
            gui.typewrite(password, interval=0.2)

            if not self.isMacroMode:
                return False

            # 게임생성 대기시간 보기위해 이동
            self.moveToOnly(945, 480, 1080, 505)

            if not self.isMacroMode:
                return False

            # 1분 대기
            if (self.createTime > 0):
                plus = random.randrange(5, 10)
                remainTime = math.ceil(roomCreateDelay + plus - (time.time() - self.createTime))
                self.debugPrint(str(remainTime) + '초 기다립니다.')
                if remainTime > 0:
                    self.sleep(remainTime * 1000)

            if not self.isMacroMode:
                return False

            # 게임생성 버튼
            self.moveToAndClick(945, 480, 1080, 505)
            self.debugPrint('게임을 생성합니다. - ' + room)

            # 생성된 게임이름 업데이트
            self.createGameNumberValue.setText(str(number + 1))
            self.roomNameTitle.setText(room)
            self.roomNameTitle.repaint()
            self.currentSaveConfig()

            # 게임생성시간 기록
            self.createTime = time.time()

            if not self.isMacroMode:
                return False

            return True

        except Exception as err:
            print(err)
            return False

    def gameExit(self):
        if not self.isMacroMode:
            return

            # 메뉴 오픈
        self.sleep(1000)
        gui.hotkey('esc')

        if not self.isMacroMode:
            return

        # 저장 및 종료 버튼
        self.sleep(1000)
        self.moveToAndClick(555, 355, 745, 380)

    def sleepModeAction(self, isSleepMode):
        self.setSleepMode(isSleepMode)
        while True:
            if not self.isSleepMode:
                break

            # 잠에서 깨기
            self.debugPrint('깨어나~~!')
            for i in range(4):
                if i % 2 == 0:
                    gui.moveTo(600, 405, 0.1)
                else:
                    gui.moveTo(680, 405, 0.1)
                gui.click()
                self.sleep(200)

            if not self.isSleepMode:
                break

            # 잠자기
            sleep = random.randrange(120, 300)
            self.debugPrint(str(sleep) + '초 동안 잠을 잡니다.')
            self.sleep(random.randrange(30000, 120000))

            if not self.isSleepMode:
                break

    def writeIpLogFile(self, str):
        f = open(self.ipLogFile, 'a', encoding="UTF-8")
        f.write(str + "\n")
        f.close()

    def writeDebugLogFile(self, str):
        f = open(self.debugLogFile, 'a', encoding="UTF-8")
        f.write(str + "\n")
        f.close()

    def runMacroMode(self):
        try:
            if not self.isMacroMode:
                return

            roomName = self.createRoomValue.text().strip()
            roomPassword = self.createPasswordValue.text().strip()
            targetIp = self.targetIpValue.text().strip()
            monitoringDelaySec = int(self.createDelayValue.text().strip())
            number = int(self.createGameNumberValue.text().strip())
            roomCreateDelay = int(self.createCycleSecValue.text().strip())

            if not roomName:
                QMessageBox.about(self, '자동 게임생성 오류', '게임이름을 입력 해 주세요.')
                return

            if not roomPassword:
                QMessageBox.about(self, '자동 게임생성 오류', '비밀번호를 입력 해 주세요.')
                return

            if not targetIp:
                QMessageBox.about(self, '자동 게임생성 오류', '우버디아 IP를 입력 해 주세요.')
                return

            if not monitoringDelaySec:
                QMessageBox.about(self, '자동 게임생성 오류', '입장 후 대기시간을 초 단위로 입력 해 주세요.')
                return

            if not number:
                QMessageBox.about(self, '자동 게임생성 오류', '게임생성 시작번호를 입력 해 주세요.')
                return

            if not roomCreateDelay:
                QMessageBox.about(self, '자동 게임생성 오류', '게임생성 주기를 초 단위로 입력 해 주세요.')
                return

            self.runMacroAction(roomName, roomPassword, targetIp, monitoringDelaySec, number, roomCreateDelay)
        except Exception as err:
            print(err)

    def clearAutoMode(self):
        self.isMacroMode = False
        self.isSleepMode = False

    def setMacroMode(self, isMacroMode):
        self.isMacroMode = isMacroMode
        self.isSleepMode = False
        if isMacroMode:
            self.createRoomButton.setText('게임생성 정지')
            self.sleepModeButton.setText('잠수모드 실행')
        else:
            self.createRoomButton.setText('게임생성 실행')

    def setSleepMode(self, isSleepMode):
        self.isMacroMode = False
        self.isSleepMode = isSleepMode
        if isSleepMode:
            self.sleepModeButton.setText('잠수모드 정지')
            self.createRoomButton.setText('게임생성 실행')
        else:
            self.sleepModeButton.setText('잠수모드 실행')

    def runMacroAction(self, roomName, roomPassword, targetIp, monitoringDelaySec, number, roomCreateDelay):
        window = gw.getWindowsWithTitle('Diablo II: Resurrected')[0]
        window.top = 0
        window.left = 0

        while True:
            # 게임 생성
            isActive = self.gameCreate(roomName, roomPassword, number, roomCreateDelay)
            if not isActive:
                break

            # 게임 IP 검색
            self.sleep(5000)
            self.findIpResult.setText('아이피 검색 중 ...')
            self.findIpResult.repaint()

            if not self.isMacroMode:
                break

            serverIpList = self.getD2ServerIpAllList()
            gameIpList = self.getD2GameIpList(serverIpList)
            self.debugPrint(', '.join(gameIpList))

            isFind = self.isFindTargetIp(gameIpList, targetIp)
            self.paintFindIpResult(serverIpList, gameIpList, targetIp, isFind)

            # IP 로그 기록
            if len(gameIpList) > 0:
                self.writeIpLogFile(', '.join(gameIpList))

            if not self.isMacroMode:
                break

            # 원하는 IP를 찾았을 경우 대기 모드로 전환
            if isFind:
                self.sleepModeAction(True)
                break

            if not self.isMacroMode:
                break

            # 게임 생성 후 기다림
            self.debugPrint(str(monitoringDelaySec) + '초 동안 게임 안에서 대기합니다.')
            self.sleep(monitoringDelaySec * 1000)

            if not self.isMacroMode:
                break

            # 게임 종료
            self.gameExit()

            if not self.isMacroMode:
                break

            # 게임 생성 전 대기 5초
            self.debugPrint('대기실에서 5초 후 게임을 새로 생성합니다.')
            self.sleep(5000)

            number += 1

    def openFindIpForm(self, layout):

        # 영역1
        subLayout = QHBoxLayout()
        subLayout.addWidget(QLabel('우버디아 IP   '))
        self.targetIpValue = QLineEdit(self.config.get('targetIp'))
        self.targetIpValue.setMinimumHeight(25)
        subLayout.addWidget(self.targetIpValue)
        topMost = QCheckBox('맨위 고정', self)
        topMost.stateChanged.connect(self.topMostChanged)
        subLayout.addWidget(topMost)
        layout.addLayout(subLayout)

        subLayout = QVBoxLayout()
        subLayout.setContentsMargins(-1, 0, -1, 10)
        helpTitle = QLabel('※ 우버디아 IP를 입력하지 않을 경우 자동 게임생성이 진행되지 않습니다.')
        subLayout.addWidget(helpTitle)
        layout.addLayout(subLayout)

        # 영역2
        subLayout = QHBoxLayout()
        programTitle = QLabel('디아블로 위치')
        programTitle.setMinimumHeight(25)
        self.programPathValue = QLineEdit(self.config.get('program'))
        self.programPathValue.setReadOnly(True)
        self.programPathValue.setMinimumHeight(25)
        findGameButton = QPushButton('찾기..', self)
        findGameButton.setMinimumHeight(25)
        findGameButton.setMaximumWidth(50)
        findGameButton.clicked.connect(self.findGameButtonClicked)
        firewallIpButton = QPushButton('설정', self)
        firewallIpButton.setMinimumHeight(25)
        firewallIpButton.clicked.connect(self.firewallIpClicked)
        firewallIpButton.setMaximumWidth(50)
        firewallViewButton = QPushButton('조회', self)
        firewallViewButton.setMinimumHeight(25)
        firewallViewButton.setMaximumWidth(50)
        firewallViewButton.clicked.connect(self.firewallViewClicked)

        subLayout.addWidget(programTitle)
        subLayout.addWidget(self.programPathValue)
        subLayout.addWidget(findGameButton)
        subLayout.addWidget(firewallIpButton)
        subLayout.addWidget(firewallViewButton)
        layout.addLayout(subLayout)

        subLayout = QVBoxLayout()
        subLayout.setContentsMargins(-1, -1, -1, 10)
        helpTitle = QLabel('※ 디아블로2 리저렉션의 아웃바운드 방화벽을 설정 할 수 있습니다.')
        helpTitle.setMinimumHeight(25)
        subLayout.addWidget(helpTitle)
        layout.addLayout(subLayout)

        # 영역 3
        subLayout = QVBoxLayout()
        subLayout.setContentsMargins(-1, -1, -1, 10)

        myFont = QtGui.QFont()
        myFont.setBold(True)

        helpTitle = QLabel('자동 게임생성 (창모드, 1280x768)')
        helpTitle.setFont(myFont)
        subLayout.addWidget(helpTitle)
        layout.addLayout(subLayout)

        subLayout = QGridLayout()

        createRoomTitle = QLabel('게임이름')
        createRoomTitle.setMinimumHeight(25)
        subLayout.addWidget(createRoomTitle, 0, 0)
        self.createRoomValue = QLineEdit(self.config.get('room'))
        self.createRoomValue.setMinimumHeight(25)
        self.createRoomValue.setMaximumWidth(100)
        subLayout.addWidget(self.createRoomValue, 0, 1, 1, 2)

        createPasswordTitle = QLabel('비밀번호')
        createPasswordTitle.setMinimumHeight(25)
        subLayout.addWidget(createPasswordTitle, 0, 3)
        self.createPasswordValue = QLineEdit(self.config.get('password'))
        self.createPasswordValue.setMinimumHeight(25)
        self.createPasswordValue.setMaximumWidth(50)
        subLayout.addWidget(self.createPasswordValue, 0, 4)

        createCycleSecTitle = QLabel('게임생성 주기')
        createCycleSecTitle.setMinimumHeight(25)
        subLayout.addWidget(createCycleSecTitle, 1, 0)
        self.createCycleSecValue = QLineEdit(str(self.config.get('cycleSec')))
        self.createCycleSecValue.setMinimumHeight(25)
        self.createCycleSecValue.setMaximumWidth(50)
        subLayout.addWidget(self.createCycleSecValue, 1, 1)
        createCycleSecUnitTitle = QLabel('초')
        createCycleSecUnitTitle.setMinimumHeight(25)
        subLayout.addWidget(createCycleSecUnitTitle, 1, 2)

        createGameNumberTitle = QLabel('게임생성 예약번호')
        createGameNumberTitle.setMinimumHeight(25)
        subLayout.addWidget(createGameNumberTitle, 1, 3)
        self.createGameNumberValue = QLineEdit(str(self.config.get('gameNumber')))
        self.createGameNumberValue.setMinimumHeight(25)
        self.createGameNumberValue.setMaximumWidth(50)
        subLayout.addWidget(self.createGameNumberValue, 1, 4)

        createDelayTitle = QLabel('생성 후 대기시간')
        createDelayTitle.setMinimumHeight(25)
        subLayout.addWidget(createDelayTitle, 2, 0)
        self.createDelayValue = QLineEdit(str(self.config.get('delay')))
        self.createDelayValue.setMinimumHeight(25)
        self.createDelayValue.setMaximumWidth(50)
        subLayout.addWidget(self.createDelayValue, 2, 1)
        createPasswordUnitTitle = QLabel('초')
        createPasswordUnitTitle.setMinimumHeight(25)
        subLayout.addWidget(createPasswordUnitTitle, 2, 2)

        createRoomNameTitle = QLabel('생성된 게임이름')
        createRoomNameTitle.setMinimumHeight(25)
        subLayout.addWidget(createRoomNameTitle, 2, 3)
        self.roomNameTitle = QLabel('N/A')
        self.roomNameTitle.setMinimumHeight(25)
        self.roomNameTitle.setTextInteractionFlags(Qt.TextSelectableByMouse)
        subLayout.addWidget(self.roomNameTitle, 2, 4)

        label = QLabel('TICK')
        label.setMinimumHeight(25)
        subLayout.addWidget(label, 3, 0)
        self.remainSecTitle = QLabel('0초')
        self.remainSecTitle.setMinimumHeight(25)
        subLayout.addWidget(self.remainSecTitle, 3, 1)

        label = QLabel('서버')
        label.setMinimumHeight(25)
        subLayout.addWidget(label, 3, 3)
        self.serverTitle = QLabel('N/A')
        self.serverTitle.setMinimumHeight(25)
        self.serverTitle.setMinimumWidth(100)
        subLayout.addWidget(self.serverTitle, 3, 4)

        layout.addLayout(subLayout)

        subLayout = QHBoxLayout()
        subLayout.setContentsMargins(-1, -1, -1, -1)
        findIpButton = QPushButton('게임 IP 검색', self)
        findIpButton.setMinimumHeight(30)
        findIpButton.clicked.connect(self.findIpClicked)
        subLayout.addWidget(findIpButton)

        button = QPushButton('설정 저장', self)
        button.setMinimumHeight(30)
        button.clicked.connect(self.saveConfigClicked)
        subLayout.addWidget(button)

        self.createRoomButton = QPushButton('게임생성 실행', self)
        self.createRoomButton.setMinimumHeight(30)
        self.createRoomButton.clicked.connect(self.createRoomClicked)
        subLayout.addWidget(self.createRoomButton)

        self.sleepModeButton = QPushButton('잠수모드 실행', self)
        self.sleepModeButton.setMinimumHeight(30)
        self.sleepModeButton.clicked.connect(self.sleepModeClicked)
        subLayout.addWidget(self.sleepModeButton)

        button = QPushButton('데이터 리셋', self)
        button.setMinimumHeight(30)
        button.clicked.connect(self.resetClicked)
        subLayout.addWidget(button)

        layout.addLayout(subLayout)

        # IP 조회 - 결과 영역
        self.findIpResult = QLabel('게임 생성 후 IP 조회 버튼을 클릭 해 주세요.')
        self.findIpResult.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.findIpResult.setFont(QtGui.QFont("", 14))

        subLayout = QHBoxLayout()
        subLayout.addWidget(self.findIpResult)
        layout.addLayout(subLayout)

        # 디버그 콘솔
        self.debugText = QTextEdit('')
        self.debugText.setReadOnly(True)
        debugTextLayout = QHBoxLayout()
        debugTextLayout.addWidget(self.debugText)
        layout.addLayout(debugTextLayout)

    def saveConfigClicked(self):
        self.currentSaveConfig()

    def resetClicked(self):
        self.createTime = 0
        self.ipLogFile = 'ip-' + time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time())) + '.txt'
        self.debugLogFile = 'debug-' + time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time())) + '.txt'
        self.debugText.setText("")

    def sleepModeClicked(self):
        if self.isSleepMode:
            self.sleepModeAction(False)
        else:
            self.sleepModeAction(True)

    def topMostChanged(self, state):
        if state == Qt.Checked:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    def createRoomClicked(self):
        self.currentSaveConfig()
        if self.isMacroMode:
            self.setMacroMode(False)
        else:
            self.setMacroMode(True)
        self.runMacroMode()

    def findGameButtonClicked(self):
        fileOpen = QFileDialog.getOpenFileName(self, 'Open file', self.config.get('program'), 'Files (D2R.exe)')
        if fileOpen != ('', ''):
            self.programPathValue.setText(fileOpen[0].replace('/', '\\'))
        self.currentSaveConfig()

    def firewallIpClicked(self):
        self.currentSaveConfig()
        targetIp = self.targetIpValue.text().strip()
        program = self.programPathValue.text().strip()

        self.clearFirewall()
        if targetIp and program:
            ret = self.setFirewall(program, targetIp)
            if ret:
                QMessageBox.about(self, '방화벽 설정', '방화벽 대역이 설정 되었습니다.')
            else:
                QMessageBox.about(self, '방화벽 설정', '방화벽 대역 설정에 실패 하였습니다.')
        else:
            QMessageBox.about(self, '방화벽 설정', '설정 된 방화벽이 제거 되었습니다.')

    def firewallViewClicked(self):
        self.openFirewall()

    def findIpClicked(self):
        self.currentSaveConfig()

        targetIp = self.targetIpValue.text().strip()

        self.findIpResult.setText('IP search ...')
        self.findIpResult.repaint()

        serverIpList = self.getD2ServerIpAllList()
        gameIpList = self.getD2GameIpList(serverIpList)
        isFind = self.isFindTargetIp(gameIpList, targetIp)

        self.paintFindIpResult(serverIpList, gameIpList, targetIp, isFind)

    def paintFindIpResult(self, serverIpList, gameIpList, findIp, isFind):
        serverTitle = self.getServerTitle(serverIpList)
        self.serverTitle.setText(serverTitle)
        self.debugPrint('서버 IP - ' + ', '.join(serverIpList))

        if len(gameIpList) > 0:
            ip = ', '.join(gameIpList)
            if findIp and isFind:
                self.findIpResult.setText(ip + ' - OK! ★☆★☆★☆★')
                winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)
            elif findIp:
                self.findIpResult.setText(ip + ' - FAIL.')
            else:
                self.findIpResult.setText(ip)
        else:
            self.findIpResult.setText('게임 생성 후 IP 조회 버튼을 클릭 해 주세요.')

    def getServerTitle(self, serverIpList):
        if len(serverIpList) < 1:
            return 'N/A'

        # IP 확인
        if '117.52.35.79' in serverIpList:
            return '아시아(79)'
        elif '117.52.35.179' in serverIpList:
            return '아시아(179)'
        elif '137.221.106.88' in serverIpList:
            return '아메리카'
        elif '37.244.28.80' in serverIpList:
            return '유럽'
        else:
            return 'None'

    def isFindTargetIp(self, ipList, targetIp):
        if not targetIp:
            return False

        if len(ipList) < 1:
            return False

        # 멀티 IP
        ips = targetIp.split(',')

        # IP 확인
        isFind = False
        for d2Ip in ipList:
            for ip in ips:
                ip = ip.strip()
                if d2Ip == ip:
                    isFind = True
                    break
            if isFind:
                break

        return isFind

    def getD2ServerIpAllList(self):
        data = subprocess.run(['netstat', '-anob'], stdout=subprocess.PIPE, text=True)
        arr = data.stdout.split("\n")

        isD2Ip = False
        d2IpList = []
        for text in reversed(arr):
            text = text.strip()
            if text.startswith('['):
                if text == "[D2R.exe]":
                    isD2Ip = True
                else:
                    isD2Ip = False
            else:
                if isD2Ip:
                    if (text.find(':443') != -1 and text.find('ESTABLISHED') != -1):
                        z = text.split()
                        z = z[2].split(':')
                        ip = z[0]
                        if ip not in d2IpList:
                            d2IpList.append(ip)

        return d2IpList

    def getD2GameIpList(self, serverIpList):
        d2IpList = []
        for ip in serverIpList:
            if (ip == '24.105.29.76'
                    # 유럽
                    or ip == '37.244.28.80'
                    or ip == '104.76.67.204'
                    # 아메리카
                    or ip == '34.117.122.6'
                    or ip == '137.221.106.88'):
                continue

            if (ip.startswith('34.')
                    or ip.startswith('35.')
                    or ip.startswith('104.')
                    or ip.startswith('158.')
                    or ip.startswith('37.')):
                if ip not in d2IpList:
                    d2IpList.append(ip)

        return d2IpList

    def clearFirewall(self):
        data = subprocess.run(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all', 'dir=out'],
                              stdout=subprocess.PIPE, text=True)
        arr = data.stdout.split("\n")

        for text in arr:
            if (text.find('스타 우버디아 (') == -1):
                continue
            z = text.split('규칙 이름:')
            name = z[1].strip()
            res = subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', 'name=', name],
                                 stdout=subprocess.PIPE, text=True)
            if res.returncode == 0:
                resMsg = 'DEL ... OK'
            else:
                resMsg = 'DEL ... FAIL'
            self.debugPrint(resMsg + ' - ' + name)

    def ip2int(self, ip):
        return struct.unpack("!I", socket.inet_aton(ip))[0]

    def int2ip(self, ipValue):
        return socket.inet_ntoa(struct.pack("!I", ipValue))

    def setFirewall(self, program, targetIp):
        z = targetIp.split('.')
        o1 = int(z[0])
        o2 = int(z[1])
        o3 = int(z[2])
        o4 = int(z[3])

        # 34, 35, 104, 158, 37, exclude: 34.117.122.6
        ipRangeList = []
        ipRangeList.append('34.1.1.1-34.117.122.5')
        ipRangeList.append('34.117.122.7-34.255.255.255')
        ipRangeList.append('35.1.1.1-35.255.255.255')
        ipRangeList.append('104.1.1.1-104.255.255.255')
        ipRangeList.append('158.1.1.1-158.255.255.255')

        ipBlockList = []
        for ipRange in ipRangeList:
            if ipRange.startswith(str(o1) + '.'):
                continue
            ipBlockList.append(ipRange)

        # 입력한 IP의 앞쪽 대역 추가
        if o1 != 37:
            ignoreIpValue = self.ip2int('34.117.122.6')
            targetIpValue = self.ip2int(targetIp)
            if o1 == 34:
                if targetIpValue < ignoreIpValue:
                    ipBlockList.append(str(o1) + '.1.1.1-' + self.int2ip(targetIpValue - 1))
                    if targetIpValue != ignoreIpValue - 1:
                        ipBlockList.append(self.int2ip(targetIpValue + 1) + '-34.117.122.5')
                    ipBlockList.append('34.117.122.7-34.255.255.255')
                elif targetIpValue > ignoreIpValue:
                    ipBlockList.append('34.117.1.1-34.117.122.5')
                    if targetIpValue != ignoreIpValue + 1:
                        ipBlockList.append('34.117.122.7-' + self.int2ip(targetIpValue - 1))
                    ipBlockList.append(self.int2ip(targetIpValue + 1) + '-34.255.255.255')
                else:
                    ipBlockList.append('34.117.1.1-34.117.122.5')
                    ipBlockList.append('34.117.122.7-34.255.255.255')
            else:
                ipBlockList.append(str(o1) + '.1.1.1-' + str(o1) + '.' + str(o2 - 1) + '.255.255')
                ipBlockList.append(str(o1) + '.' + str(o2 + 1) + '.1.1-' + str(o1) + '.255.255.255')

        remoteip = ','.join(ipBlockList)
        name = '스타 우버디아 (' + str(o1) + '.' + str(o2) + '.x.x)'
        cmd = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=' + name, 'dir=out', 'program=' + program,
               'remoteip=' + remoteip, 'action=block', 'enable=yes']
        res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        if res.returncode == 0:
            resMsg = 'SET ... OK - ' + name
            self.debugPrint(resMsg)
            return True
        else:
            resMsg = 'SET ... FAIL - ' + name
            self.debugPrint(resMsg)
            return False

    def openFirewallAsync(self):
        x = threading.Thread(target=self.openFirewall, args=())
        x.start()

    def openFirewall(self):
        try:
            os.system('start C:\Windows\System32\WF.msc')
        except Exception as err:
            print(err)

    def openMainForm(self, layout):
        self.setLayout(layout)
        self.setWindowTitle('디아블로2 레저렉션 관리자 버전 1.0')
        self.setWindowIcon(QIcon('star.png'))
        self.setFixedSize(500, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    try:
        if len(gw.getWindowsWithTitle('디아블로2 레저렉션 관리자 버전 1.0')) > 0:
            sys.exit(0)

        app = QApplication(sys.argv)
        mainApp = MainApp()
        sys.exit(app.exec_())
    except Exception as err:
        print(err)
