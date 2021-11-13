from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule import DashboardConfigTab


def dashboardConfigValue(widget: QWidget, config):
    family = config.getConfig('dashboardFontFamily') or widget.font().family()
    pointSize = config.getConfig('dashboardFontPointSize') or 20
    weight = config.getConfig('dashboardFontWeight') or QFont.Bold
    italic = config.getConfig('dashboardFontItalic') or False
    strikeOut = config.getConfig('dashboardFontStrikeOut') or False
    underline = config.getConfig('dashboardFontUnderline') or False

    font = QtGui.QFont(family, pointSize, weight, italic)
    font.setStrikeOut(strikeOut)
    font.setUnderline(underline)

    form = QLabel('34.93.77.77', widget)
    form.setFont(DashboardConfigTab.getDashboardFont(config))
    config.set('dashboardConfigValue', form)


def dashboardFontConfigButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('폰트 설정', widget)
    form.setMinimumHeight(40)
    form.clicked.connect(clickedEvent)
    config.set('dashboardFontConfigButton', form)


def dashboardFontColorForm(widget: QWidget, config, clickedEvent):
    form = QPushButton('색상 설정', widget)
    form.setMinimumHeight(40)
    form.clicked.connect(clickedEvent)
    config.set('dashboardFontColorForm', form)


def dashboardPositionButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('위치 설정', widget)
    form.setMinimumHeight(40)
    form.clicked.connect(clickedEvent)
    config.set('dashboardPositionConfigButton', form)
