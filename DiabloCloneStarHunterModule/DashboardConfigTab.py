from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule.D2Config import D2Config
from DiabloCloneStarHunterModule.TargetIpHunterTab import targetIpHunterConfigSave

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None
__APP__: QApplication = None


def dashboardConfigTabWidget(widget, config, app):
    global __WIDGET__, __CONFIG__, __APP__
    __WIDGET__ = widget
    __CONFIG__ = config
    __APP__ = app

    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    sub = QHBoxLayout()
    sub.addWidget(config.get('dashboardFontConfigButton'))
    sub.addWidget(config.get('dashboardFontColorForm'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(Qt.AlignLeft)
    sub.addWidget(config.get('dashboardConfigValue'))
    layout.addLayout(sub)

    widget = QWidget()
    widget.setLayout(layout)
    return widget


def getDashboardFont(config):
    family = config.getConfig('dashboardFontFamily') or 'Arial'
    pointSize = config.getConfig('dashboardFontPointSize') or 20
    weight = config.getConfig('dashboardFontWeight') or QFont.Bold
    italic = config.getConfig('dashboardFontItalic') or False
    strikeOut = config.getConfig('dashboardFontStrikeOut') or False
    underline = config.getConfig('dashboardFontUnderline') or False

    font = QtGui.QFont(family, pointSize, weight, italic)
    font.setStrikeOut(strikeOut)
    font.setUnderline(underline)

    return font


def fontConfigButtonClickedEvent():
    config = __CONFIG__

    font, ok = QFontDialog.getFont(getDashboardFont(config))
    if ok:
        config.setConfig('dashboardFontFamily', font.family())
        config.setConfig('dashboardFontPointSize', font.pointSize())
        config.setConfig('dashboardFontWeight', font.weight())
        config.setConfig('dashboardFontItalic', font.italic())
        config.setConfig('dashboardFontStrikeOut', font.strikeOut())
        config.setConfig('dashboardFontUnderline', font.underline())
        targetIpHunterConfigSave()

        config.get('dashboardConfigValue').setFont(font)
        config.get('dashboardGameIp').setFont(font)
        config.get('dashboardTimer').setFont(font)


def getDashboardFontColor(config):
    color = QColor()
    color.setNamedColor(config.getConfig('dashboardFontColor') or 'red')
    return color


def fontColorFormClickedEvent():
    config = __CONFIG__

    color = QColorDialog.getColor(getDashboardFontColor(config))
    if color.isValid():
        config.setConfig('dashboardFontColor', color.name())
        targetIpHunterConfigSave()

        config.get('dashboardConfigValue').setStyleSheet("color: %s" % color.name())
        config.get('dashboardGameIp').setStyleSheet("color: %s" % color.name())
        config.get('dashboardTimer').setStyleSheet("color: %s" % color.name())
