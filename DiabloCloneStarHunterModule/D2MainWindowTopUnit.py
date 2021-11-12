from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QCheckBox

__WIDGET__: QWidget = None


def targetIpTitle(widget, config):
    form = QLabel('목표 IP', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('targetIpTitle', form)


def targetIpForm(widget, config):
    form = QLineEdit(config.getConfig('targetIp'), widget)
    form.setMinimumHeight(25)
    config.set('targetIpForm', form)


def targetIpHelp(widget, config):
    form = QLabel('※ 우버디아 IP는 컴마(,)를 구분자로 여러개 입력 가능합니다.', widget)
    form.setMinimumHeight(25)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('targetIpHelp', form)


def topMostForm(widget, config):
    global __WIDGET__

    if __WIDGET__ is None:
        __WIDGET__ = widget

    form = QCheckBox('맨위 고정', widget)
    form.setMinimumHeight(25)
    form.stateChanged.connect(_topMostChangedActionCallback)
    config.set('topMostForm', form)


def _topMostChangedActionCallback(state):
    if state == Qt.Checked:
        __WIDGET__.setWindowFlags(__WIDGET__.windowFlags() | Qt.WindowStaysOnTopHint)
    else:
        __WIDGET__.setWindowFlags(__WIDGET__.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
    __WIDGET__.show()
