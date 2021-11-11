from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

__WIDGET__: QWidget = None


def programPathTitle(widget, config):
    form = QLineEdit('D2R 위치', widget)
    form.setMinimumHeight(25)
    config.set('programPathTitle', form)


def programPathForm(widget, config):
    form = QLineEdit(config.getConfig('program'), widget)
    form.setReadOnly(True)
    form.setMinimumHeight(25)
    config.set('programPathForm', form)


def firewallButton(widget, config, ClickedEventCallback):
    button = QPushButton('방화벽 설정', widget)
    button.setMinimumHeight(25)
    button.setMaximumWidth(50)
    button.clicked.connect(ClickedEventCallback)
    config.set('firewallButton', button)


def firewallWindowOpen(widget, config, ClickedEventCallback):
    button = QPushButton('방화벽 조회', widget)
    button.setMinimumHeight(25)
    button.setMaximumWidth(50)
    button.clicked.connect(ClickedEventCallback)
    config.set('firewallWindowOpen', button)


def firewallHelp(widget, config):
    form = QLabel('※ 디아블로2 리저렉션의 아웃바운드 방화벽을 설정 할 수 있습니다.', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('firewallHelp', form)


def hunterControllerTitle(widget, config):
    myFont = QtGui.QFont()
    myFont.setBold(True)

    form = QLabel('자동 게임생성 (창모드, 1280x768)', widget)
    form.setMinimumHeight(25)
    form.setFont(myFont)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('hunterControllerTitle', form)
