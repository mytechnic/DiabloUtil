from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

__WIDGET__: QWidget = None


def dashboardGameIp(widget, config, font, color: QColor):
    form = QLabel('IP를 검색 해 주세요.', widget)
    form.setFont(font)
    form.setStyleSheet('color: ' + color.name())
    form.setAlignment(QtCore.Qt.AlignLeft)
    config.set('dashboardGameIp', form)


def dashboardTimer1(widget, config, font, color: QColor):
    form = QLabel('0 초', widget)
    form.setFont(font)
    form.setStyleSheet('color: ' + color.name())
    form.setAlignment(QtCore.Qt.AlignRight)
    config.set('dashboardTimer1', form)


def dashboardTimer2(widget, config, font, color: QColor):
    form = QLabel('', widget)
    form.setFont(font)
    form.setStyleSheet('color: ' + color.name())
    form.setAlignment(QtCore.Qt.AlignRight)
    config.set('dashboardTimer2', form)
