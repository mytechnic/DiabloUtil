from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def gameNameTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('게임이름', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('gameNameTitle', form)


def gameNameForm(widget, config):
    form = QLineEdit(config.getConfig('gameNamePrefix') or 'SBW', widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setMaxLength(15)
    form.setCursorPosition(0)
    config.set('gameNameForm', form)


def gamePasswordTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('비밀번호', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('gamePasswordTitle', form)


def gamePasswordForm(widget, config):
    form = QLineEdit(config.getConfig('gamePassword') or '1004', widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(100)
    form.setMaxLength(10)
    form.setCursorPosition(0)
    config.set('gamePasswordForm', form)


def gameCreateNumberTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('생성번호', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('gameCreateNumberTitle', form)


def gameCreateNumberForm(widget, config):
    form = QLineEdit(str(config.getConfig('gameCreateNumber')) or '1', widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(50)
    form.setMaxLength(10)
    form.setCursorPosition(0)
    config.set('gameCreateNumberForm', form)


def gameCreateCycleSecTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('생성주기', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('gameCreateCycleSecTitle', form)


def gameCreateCycleSecForm(widget, config):
    form = QLineEdit(str(config.getConfig('gameCreateCycleSec')) or '90', widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(50)
    form.setMaxLength(10)
    form.setCursorPosition(0)
    config.set('gameCreateCycleSecForm', form)


def gameCreateCycleSecUnit(widget, config):
    form = QLabel('초', widget)
    form.setMinimumHeight(25)
    config.set('gameCreateCycleSecUnit', form)


def gameJoinAfterSecTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('게임내 대기시간', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('gameJoinAfterSecTitle', form)


def gameJoinAfterSecForm(widget, config):
    form = QLineEdit(str(config.getConfig('gameJoinAfterSec')) or '30', widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(50)
    form.setMaxLength(10)
    form.setCursorPosition(0)
    config.set('gameJoinAfterSecForm', form)


def gameJoinAfterSecUnit(widget, config):
    form = QLabel('초', widget)
    form.setMinimumHeight(25)
    config.set('gameJoinAfterSecUnit', form)


def createdGameNameTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('생성된 게임이름', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('createdGameNameTitle', form)


def createdGameName(widget, config):
    form = QLabel('N/A', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('createdGameName', form)


def gameHunterTickTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('다음 액션까지', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('gameHunterTickTitle', form)


def gameHunterTick(widget, config):
    form = QLabel('N/A', widget)
    form.setMinimumHeight(25)
    config.set('gameHunterTick', form)


def gameHunterTickUnit(widget, config):
    form = QLabel('초 남았습니다.', widget)
    form.setMinimumHeight(25)
    config.set('gameHunterTickUnit', form)


def gameHunterStatusTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('동작상태', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(120)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('gameHunterStatusTitle', form)


def gameHunterStatus(widget, config):
    form = QLabel('준비', widget)
    form.setMinimumHeight(25)
    config.set('gameHunterStatus', form)


def gameHunterStartButton(widget, config, clickedEvent):
    form = QPushButton('생성 시작', widget)
    form.clicked.connect(clickedEvent)
    form.setMinimumHeight(40)
    config.set('gameHunterStartButton', form)


def gameHunterConfigApplyButton(widget, config, clickedEvent):
    form = QPushButton('설정값 적용', widget)
    form.clicked.connect(clickedEvent)
    form.setMinimumHeight(40)
    config.set('gameHunterConfigApplyButton', form)


def gameHunterHistory(widget, config):
    form = QTextEdit('', widget)
    form.setReadOnly(True)
    config.set('gameHunterHistory', form)
