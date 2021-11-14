from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QWidget

__WIDGET__: QWidget = None


def dashboardGameIp(widget, config, font, color: QColor):
    form = QLabel('IP를 검색 해 주세요.', widget)
    form.setFont(font)
    form.setStyleSheet('color: ' + color.name())
    form.setAlignment(QtCore.Qt.AlignLeft)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardGameIp', form)


def dashboardTimer(widget, config, font, color: QColor):
    form = QLabel('0 초', widget)
    form.setFont(font)
    form.setStyleSheet('color: ' + color.name())
    form.setAlignment(QtCore.Qt.AlignRight)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardTimer', form)


def dashboardTimer2(widget, config, font, color: QColor):
    form = QLabel('', widget)
    form.setFont(font)
    form.setStyleSheet('color: ' + color.name())
    form.setAlignment(QtCore.Qt.AlignRight)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardTimer2', form)
