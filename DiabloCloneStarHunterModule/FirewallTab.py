import os
import threading

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule import D2Firewall
from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def firewallTabWidget(widget, config):
    global __WIDGET__, __CONFIG__
    __WIDGET__ = widget
    __CONFIG__ = config

    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('programPathTitle'))
    sub.addWidget(config.get('programPathForm'))
    sub.addWidget(config.get('programSearchButton'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('firewallPolicyTitle'))
    sub.addWidget(config.get('firewallPolicyAClass'))
    sub.addWidget(config.get('firewallPolicyBClass'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('firewallPolicySetResultTitle'))
    sub.addWidget(config.get('firewallPolicySetResult'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignCenter)
    sub.addWidget(config.get('createFirewallButton'))
    sub.addWidget(config.get('deleteFirewallButton'))
    sub.addWidget(config.get('openFirewallButton'))
    layout.addLayout(sub)

    group = QButtonGroup(widget)
    group.addButton(config.get('firewallPolicyAClass'))
    group.addButton(config.get('firewallPolicyBClass'))

    widget = QWidget()
    widget.setLayout(layout)
    return widget


def programSearchButtonClickedEvent():
    widget = __WIDGET__
    config = __CONFIG__

    fileOpen = QFileDialog.getOpenFileName(widget, 'Open file', config.getConfig('programPath'), 'Files (D2R.exe)')
    if fileOpen != ('', ''):
        program = fileOpen[0].replace('/', '\\')
        config.get('programPathForm').setText(program)
        config.get('programPathForm').setCursorPosition(0)


def createFirewallButtonClickedEvent():
    widget = __WIDGET__
    config = __CONFIG__

    firewallConfigSave()

    targetIp = config.getConfig('targetIp')
    programPath = config.getConfig('programPath')
    firewallPolicy = config.getConfig('firewallPolicy')

    if not targetIp:
        QMessageBox.about(widget, '오류!!', '목표 IP를 입력 해 주세요.')
        return

    if len(targetIp.split(',')) > 1:
        QMessageBox.about(widget, '오류!!', '방화벽 설정을 위한 목표 IP는 1개만 지원 합니다.')
        return

    if not programPath:
        QMessageBox.about(widget, '오류!!', 'D2R 경로를 찾아 주세요.')
        return

    if not os.path.isfile(programPath):
        QMessageBox.about(widget, '오류!!', 'D2R 경로가 잘못 설정되었습니다.')
        return

    firewallIpList = D2Firewall.getFirewallIpList(targetIp, firewallPolicy)
    D2Firewall.clearFirewall()
    ret = D2Firewall.setFirewall(targetIp, programPath, firewallIpList)
    if ret:
        QMessageBox.about(widget, '성공!!', '방화벽이 설정 되었습니다.')
    else:
        QMessageBox.about(widget, '오류!!', '방화벽 설정에 실패 하였습니다.(관리자 실행 권한 필요)')

    config.get('firewallPolicySetResult').setText('\n'.join(firewallIpList))


def deleteFirewallButtonClickedEvent():
    widget = __WIDGET__

    ret = D2Firewall.clearFirewall()
    if ret:
        QMessageBox.about(widget, '성공!!', '방화벽이 삭제 되었습니다.')
    else:
        QMessageBox.about(widget, '오류!!', '방화벽 삭제에 실패 하였습니다.(관리자 실행 권한 필요)')


def openFirewallButtonClickedEvent():
    th = threading.Thread(target=openFirewall, args=())
    th.start()


def openFirewall():
    os.system('WF.msc')


def firewallConfigSave():
    config = __CONFIG__

    config.setConfig('targetIp', config.get('targetIpForm').text().strip())
    config.setConfig('programPath', config.get('programPathForm').text().strip())
    if config.get('firewallPolicyAClass').isChecked():
        config.setConfig('firewallPolicy', 'A')
    else:
        config.setConfig('firewallPolicy', 'B')
    config.saveConfig()
