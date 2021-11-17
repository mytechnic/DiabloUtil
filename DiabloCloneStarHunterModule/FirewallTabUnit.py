from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def programPathTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('D2R 경로', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(100)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('programPathTitle', form)


def programPathForm(widget, config):
    form = QLineEdit(config.getConfig('programPath'), widget)
    form.setReadOnly(True)
    form.setMinimumHeight(25)
    form.setCursorPosition(0)
    config.set('programPathForm', form)


def programSearchButton(widget, config, clickedEvent):
    form = QPushButton('찾아보기...', widget)
    form.clicked.connect(clickedEvent)
    form.setMinimumHeight(25)
    config.set('programSearchButton', form)


def firewallPolicyTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('차단 정책', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(100)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('firewallPolicyTitle', form)


def firewallPolicyAClass(widget, config, clickedEvent):
    form = QRadioButton('A 클래스(예 - 34.x.x.x)', widget)
    form.clicked.connect(clickedEvent)
    form.setChecked(config.getConfig('firewallPolicy') == 'A')
    form.setMinimumHeight(25)
    config.set('firewallPolicyAClass', form)


def firewallPolicyBClass(widget, config, clickedEvent):
    form = QRadioButton('B 클래스(예 - 34.93.x.x)', widget)
    form.clicked.connect(clickedEvent)
    form.setChecked(config.getConfig('firewallPolicy') != 'A')
    form.setMinimumHeight(25)
    config.set('firewallPolicyBClass', form)


def firewallPolicyRuleIpTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('방화벽 규칙', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(100)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('firewallPolicyRuleIpTitle', form)


def firewallPolicyRuleIp(widget, config):
    form = QTextEdit('', widget)
    form.setReadOnly(False)
    form.setPlainText(config.getConfig('firewallRuleIp'))
    form.setMaximumHeight(150)
    config.set('firewallPolicyRuleIp', form)


def createTargetIpFirewallButton(widget, config, clickedEvent):
    button = QPushButton('목표IP로 설정', widget)
    button.setMinimumHeight(40)
    button.clicked.connect(clickedEvent)
    config.set('createTargetIpFirewallButton', button)


def createInputTextFirewallButton(widget, config, clickedEvent):
    button = QPushButton('규칙으로 설정', widget)
    button.setMinimumHeight(40)
    button.clicked.connect(clickedEvent)
    config.set('createInputTextFirewallButton', button)


def deleteFirewallButton(widget, config, clickedEvent):
    button = QPushButton('방화벽 삭제', widget)
    button.setMinimumHeight(40)
    button.clicked.connect(clickedEvent)
    config.set('deleteFirewallButton', button)


def openFirewallButton(widget, config, clickedEvent):
    button = QPushButton('방화벽 조회', widget)
    button.setMinimumHeight(40)
    button.clicked.connect(clickedEvent)
    config.set('openFirewallButton', button)
