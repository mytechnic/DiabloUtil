from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def programPathTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('D2R 경로', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
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
    form.setFixedWidth(80)
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


def firewallPolicySetResultTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('적용 결과', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('firewallPolicySetResultTitle', form)


def firewallPolicySetResult(widget, config):
    form = QLabel('N/A', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('firewallPolicySetResult', form)


def createFirewallButton(widget, config, clickedEvent):
    button = QPushButton('방화벽 적용', widget)
    button.setMinimumHeight(40)
    button.clicked.connect(clickedEvent)
    config.set('createFirewallButton', button)


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
