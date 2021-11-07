import os
import subprocess
import sys
import winsound

import pygetwindow as gw
import yaml
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MainApp(QWidget):
    findIpResult = None
    targetIpValue = None
    programPathValue = None
    config = {'program': 'C:\Program Files (x86)\Diablo II Resurrected\D2R.exe'}

    def __init__(self):
        super().__init__()
        if os.path.isfile('config.yaml'):
            self.loadConfig()
        else:
            self.saveConfig()
        self.initUI()

    def loadConfig(self):
        with open('config.yaml') as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)

    def saveConfig(self):
        with open('config.yaml', 'w') as f:
            print(self.config)
            yaml.dump(self.config, f)

    def initUI(self):
        layout = QVBoxLayout()
        self.openFindIpForm(layout)
        self.openMainForm(layout)

    def openFindIpForm(self, layout):

        # 우버디아 IP 설정
        targetIpTitle = QLabel('우버디아 IP   ')
        self.targetIpValue = QLineEdit()
        self.targetIpValue.setMinimumHeight(25)

        targetIpLayout = QHBoxLayout()
        targetIpLayout.addWidget(targetIpTitle)
        targetIpLayout.addWidget(self.targetIpValue)
        layout.addLayout(targetIpLayout)

        # 공백
        fireLayout = QVBoxLayout()
        fireLayout.setContentsMargins(-1, -1, -1, 10)
        layout.addLayout(fireLayout)

        # 방화벽 설정 - 실행영역
        programTitle = QLabel('디아블로 위치')
        self.programPathValue = QLineEdit(self.config.get('program'))
        self.programPathValue.setMinimumHeight(25)
        findGameButton = QPushButton('경로 찾기', self)
        findGameButton.setMinimumHeight(25)
        findGameButton.clicked.connect(self.findGameButtonClicked)
        firewallIpButton = QPushButton('방화벽 설정', self)
        firewallIpButton.setMinimumHeight(25)
        firewallIpButton.clicked.connect(self.firewallIpClicked)
        helpTitle = QLabel('우버디아 IP를 입력하지 않을 경우 방화벽 삭제만 진행 됩니다.')

        firewallIpLayout = QGridLayout()
        firewallIpLayout.addWidget(programTitle, 0, 0)
        firewallIpLayout.addWidget(self.programPathValue, 0, 1)
        firewallIpLayout.addWidget(findGameButton, 0, 2)
        firewallIpLayout.addWidget(firewallIpButton, 0, 3)
        firewallIpLayout.addWidget(helpTitle, 1, 0, 1, 3)
        layout.addLayout(firewallIpLayout)

        # 공백
        fireLayout = QVBoxLayout()
        fireLayout.setContentsMargins(-1, -1, -1, 10)
        layout.addLayout(fireLayout)

        # IP 조회 - 버튼 영역
        findIpButton = QPushButton('디아블로 방의 IP 검색', self)
        findIpButton.move(20, 20)
        findIpButton.setMinimumHeight(40)
        findIpButton.clicked.connect(self.findIpClicked)

        findIpButtonLayout = QHBoxLayout()
        findIpButtonLayout.addWidget(findIpButton)
        layout.addLayout(findIpButtonLayout)

        # IP 조회 - 결과 영역
        self.findIpResult = QLabel('방 생성 후 IP 조회 버튼을 클릭 해 주세요.')
        self.findIpResult.setAlignment(Qt.AlignLeft)
        self.findIpResult.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.findIpResult.move(40, 40)
        self.findIpResult.setFont(QtGui.QFont("", 14))

        findIpResultLayout = QGridLayout()
        findIpResultLayout.addWidget(self.findIpResult, 0, 0)

        layout.addLayout(findIpResultLayout)

    def findGameButtonClicked(self):
        fileOpen = QFileDialog.getOpenFileName(self, 'Open file', self.config.get('program'), 'Files (D2R.exe)')
        if fileOpen != ('', ''):
            program = fileOpen[0].replace('/', '\\')
            self.programPathValue.setText(program)
            self.config.update({'program': program})
            self.saveConfig()

    def firewallIpClicked(self):
        try:
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
        except Exception as e:
            print(e)

    def findIpClicked(self):
        self.findIpResult.setText('IP search ...')
        self.findIpResult.repaint()

        ipList = self.getFindIpList()

        if len(ipList) > 0:
            targetIp = self.targetIpValue.text().strip()
            isFind = self.isFindTargetIp(ipList, targetIp)

            ip = ', '.join(ipList)

            if targetIp and isFind:
                self.findIpResult.setText(ip + ' - OK! ★☆★☆★☆★')
                winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)
            elif targetIp:
                self.findIpResult.setText(ip + ' - FAIL.')
            else:
                self.findIpResult.setText(ip)
        else:
            self.findIpResult.setText('방 생성 후 IP 조회 버튼을 클릭 해 주세요.')

    def isFindTargetIp(self, ipList, targetIp):
        if not targetIp:
            return False

        # IP 확인
        isFind = False
        for d2Ip in ipList:
            if d2Ip == targetIp:
                isFind = True
                break

        return isFind

    def getFindIpList(self):
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
                    if (text.find(':443') != -1
                            and text.find('ESTABLISHED') != -1
                            and text.find('24.105.29.76') == -1):
                        z = text.split()
                        z = z[2].split(':')
                        ip = z[0]
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
            print(resMsg, '-', name)

    def setFirewall(self, program, targetIp):
        z = targetIp.split('.')
        o1 = int(z[0])
        o2 = int(z[1])

        # 34, 35, 104, 158, 37
        ipRangeList = []
        ipRangeList.append('34.1.1.1-34.255.255.255')
        ipRangeList.append('35.1.1.1-35.255.255.255')
        ipRangeList.append('104.1.1.1-104.255.255.255')
        ipRangeList.append('158.1.1.1-158.255.255.255')

        ipBlockList = []
        for ipRange in ipRangeList:
            if ipRange.startswith(str(o1) + '.'):
                continue
            ipBlockList.append(ipRange)

        # 입력한 IP의 앞쪽 대역 추가
        if (o1 != 37 and o2 != 1):
            ipBlockList.append(str(o1) + '.1.1.1-' + str(o1) + '.' + str(o2 - 1) + '.255.255')

        # 입력한 IP의 뒤쪽 대역 추가
        if (o1 != 37 and o2 != 255):
            ipBlockList.append(str(o1) + '.' + str(o2 + 1) + '.1.1-' + str(o1) + '.255.255.255')

        remoteip = ','.join(ipBlockList)
        name = '스타 우버디아 (' + str(o1) + '.' + str(o2) + '.x.x)'
        cmd = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=' + name, 'dir=out', 'program=' + program,
               'remoteip=' + remoteip, 'action=block', 'enable=yes']
        res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        if res.returncode == 0:
            resMsg = 'SET ... OK - ' + name
            print(resMsg)
            return True
        else:
            resMsg = 'SET ... FAIL - ' + name
            print(resMsg)
            return False

    def openMainForm(self, layout):
        self.setLayout(layout)
        self.setWindowTitle('디아블로2 레저렉션 아이피 설정 1.0')
        self.setFixedSize(600, 250)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    if len(gw.getWindowsWithTitle('디아블로2 레저렉션 아이피 설정 1.0')) > 0:
        sys.exit(0)

    app = QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())
