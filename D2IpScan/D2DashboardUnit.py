from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget

__WIDGET__: QWidget = None


def dashboardGameIp(widget, config):
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)

    form = QLabel('IP를 검색 해 주세요.', widget)
    form.setFont(font)
    form.setStyleSheet('color: red')
    form.setAlignment(QtCore.Qt.AlignLeft)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardGameIp', form)


def dashboardTimer(widget, config):
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)

    form = QLabel('0 초', widget)
    form.setFont(font)
    form.setStyleSheet('color: red')
    form.setAlignment(QtCore.Qt.AlignRight)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardTimer', form)
