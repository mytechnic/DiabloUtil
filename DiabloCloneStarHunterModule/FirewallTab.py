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
    sub.addWidget(config.get('firewallPolicyRuleIpTitle'), alignment=QtCore.Qt.AlignTop)
    sub.addWidget(config.get('firewallPolicyRuleIp'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
    sub.addWidget(config.get('createTargetIpFirewallButton'))
    sub.addWidget(config.get('createInputTextFirewallButton'))
    sub.addWidget(config.get('deleteFirewallButton'))
    sub.addWidget(config.get('openFirewallButton'))
    layout.addLayout(sub)

    group = QButtonGroup(widget)
    group.addButton(config.get('firewallPolicyAClass'))
    group.addButton(config.get('firewallPolicyBClass'))
    config.get('firewallPolicyAClass').setChecked(config.getConfig('firewallPolicy') == 'A')
    config.get('firewallPolicyBClass').setChecked(config.getConfig('firewallPolicy') != 'A')

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
        config.setConfig('programPath', program)
        config.saveConfig()


def firewallPolicyAClassClickedEvent():
    config = __CONFIG__
    config.setConfig('firewallPolicy', 'A')
    config.saveConfig()


def firewallPolicyBClassClickedEvent():
    config = __CONFIG__
    config.setConfig('firewallPolicy', 'B')
    config.saveConfig()


def createTargetIpFirewallButtonClickedEvent():
    widget = __WIDGET__
    config = __CONFIG__

    firewallConfigSave()

    targetIp = config.getConfig('targetIp')
    programPath = config.getConfig('programPath')
    firewallPolicy = config.getConfig('firewallPolicy')

    if not targetIp:
        QMessageBox.about(widget, '오류!!', '목표 IP를 입력 해 주세요.')
        return

    # if not isValidFirewallRuleIp():
    #     QMessageBox.about(widget, '오류!!', '목표 IP의 입력 형식이 잘 못 되었습니다.')
    #     return

    if len(targetIp.split(',')) > 1:
        QMessageBox.about(widget, '오류!!', '방화벽 설정을 위한 목표 IP는 1개만 지원 합니다.')
        return

    if not programPath:
        QMessageBox.about(widget, '오류!!', 'D2R 경로를 찾아 주세요.')
        return

    if not os.path.isfile(programPath):
        QMessageBox.about(widget, '오류!!', 'D2R 경로가 잘못 설정되었습니다.')
        return

    firewallIpList = D2Firewall.getTargetIpToFirewallIpList(targetIp, firewallPolicy)
    print(firewallIpList)
    D2Firewall.clearFirewall()
    ret = D2Firewall.setFirewall(targetIp, programPath, firewallIpList)
    if ret:
        QMessageBox.about(widget, '성공!!', '방화벽이 설정 되었습니다.')
    else:
        QMessageBox.about(widget, '오류!!', '방화벽 설정에 실패 하였습니다.')

    config.get('firewallPolicyRuleIp').setText('\n'.join(firewallIpList))


def isValidFirewallRuleIp(firewallRuleIp):
    firewallIpList = D2Firewall.getRuleIpToFirewallIpList(firewallRuleIp)
    for ip in firewallRuleIp:
        z = ip.strip().split('-')
        if len(z) != 2:
            return False

        ip1 = z[0].strip()
        ip2 = z[1].strip()


def createInputTextFirewallButtonClickedEvent():
    widget = __WIDGET__
    config = __CONFIG__

    firewallRuleIp = config.get('firewallPolicyRuleIp').toPlainText().strip()
    targetIp = config.getConfig('targetIp')
    programPath = config.getConfig('programPath')

    if not firewallRuleIp:
        QMessageBox.about(widget, '오류!!', '규칙을 입력 해 주세요.')
        return

    if not programPath:
        QMessageBox.about(widget, '오류!!', 'D2R 경로를 찾아 주세요.')
        return

    if not os.path.isfile(programPath):
        QMessageBox.about(widget, '오류!!', 'D2R 경로가 잘못 설정되었습니다.')
        return

    firewallIpList = D2Firewall.getRuleIpToFirewallIpList(firewallRuleIp)
    config.get('firewallPolicyRuleIp').setText('\n'.join(firewallIpList))
    firewallConfigSave()

    D2Firewall.clearFirewall()
    ret = D2Firewall.setFirewall(targetIp, programPath, firewallIpList)
    if ret:
        QMessageBox.about(widget, '성공!!', '방화벽이 설정 되었습니다.')
    else:
        QMessageBox.about(widget, '오류!!', '방화벽 설정에 실패 하였습니다.')


def deleteFirewallButtonClickedEvent():
    widget = __WIDGET__

    firewallConfigSave()
    ret = D2Firewall.clearFirewall()
    if ret:
        QMessageBox.about(widget, '성공!!', '방화벽이 삭제 되었습니다.')
    else:
        QMessageBox.about(widget, '오류!!', '방화벽 삭제에 실패 하였습니다.')


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
    config.setConfig('firewallRuleIp', config.get('firewallPolicyRuleIp').toPlainText().strip())
    config.saveConfig()
