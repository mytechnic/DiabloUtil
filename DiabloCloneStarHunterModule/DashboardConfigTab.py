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
    sub.setAlignment(Qt.AlignLeft)
    sub.addWidget(config.get('dashboardPositionConfigTitle'))
    sub.addWidget(config.get('dashboardPositionConfigXTitle'))
    sub.addWidget(config.get('dashboardPositionX'))
    sub.addWidget(config.get('dashboardPositionConfigYTitle'))
    sub.addWidget(config.get('dashboardPositionY'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(Qt.AlignLeft)
    sub.addWidget(config.get('dashboardTimerConfigTitle'))
    sub.addWidget(config.get('dashboardTimerShow'))
    sub.addWidget(config.get('dashboardTimerHide'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    groupBox = QGroupBox()
    groupBox.setTitle('일반/오류 - 폰트/색상 설정')
    groupBoxLayout = QVBoxLayout()

    sub2 = QHBoxLayout()
    sub2.addWidget(config.get('dashboardTargetIpNormalText'))
    sub2.addWidget(config.get('dashboardNormalFontButton'))
    sub2.addWidget(config.get('dashboardNormalColorButton'))
    groupBoxLayout.addLayout(sub2)
    groupBox.setLayout(groupBoxLayout)
    sub.addWidget(groupBox)
    layout.addLayout(sub)

    sub = QHBoxLayout()
    groupBox = QGroupBox()
    groupBox.setTitle('성공시 - 폰트/색상 설정')
    groupBoxLayout = QVBoxLayout()

    sub2 = QHBoxLayout()
    sub2.addWidget(config.get('dashboardTargetIpOkText'))
    sub2.addWidget(config.get('dashboardOkFontButton'))
    sub2.addWidget(config.get('dashboardOkColorButton'))
    groupBoxLayout.addLayout(sub2)
    groupBox.setLayout(groupBoxLayout)
    sub.addWidget(groupBox)
    layout.addLayout(sub)

    sub = QHBoxLayout()
    groupBox = QGroupBox()
    groupBox.setTitle('실패시 - 폰트/색상 설정')
    groupBoxLayout = QVBoxLayout()

    sub2 = QHBoxLayout()
    sub2.addWidget(config.get('dashboardTargetIpFailText'))
    sub2.addWidget(config.get('dashboardFailFontButton'))
    sub2.addWidget(config.get('dashboardFailColorButton'))
    groupBoxLayout.addLayout(sub2)
    groupBox.setLayout(groupBoxLayout)
    sub.addWidget(groupBox)
    layout.addLayout(sub)

    group = QButtonGroup(widget)
    group.addButton(config.get('dashboardTimerShow'))
    group.addButton(config.get('dashboardTimerHide'))

    widget = QWidget()
    widget.setLayout(layout)
    return widget


def getDashboardFont(config, mode):
    if mode == 'ok':
        family = config.getConfig('dashboardSuccessFontFamily') or 'Arial'
        pointSize = config.getConfig('dashboardSuccessFontPointSize') or 20
        weight = config.getConfig('dashboardSuccessFontWeight') or QFont.Bold
        italic = config.getConfig('dashboardSuccessFontItalic') or False
        strikeOut = config.getConfig('dashboardSuccessFontStrikeOut') or False
        underline = config.getConfig('dashboardSuccessFontUnderline') or False
    elif mode == 'fail':
        family = config.getConfig('dashboardFailFontFamily') or 'Arial'
        pointSize = config.getConfig('dashboardFailFontPointSize') or 20
        weight = config.getConfig('dashboardFailFontWeight') or QFont.Bold
        italic = config.getConfig('dashboardFailFontItalic') or False
        strikeOut = config.getConfig('dashboardFailFontStrikeOut') or False
        underline = config.getConfig('dashboardFailFontUnderline') or False
    else:
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


def getDashboardFontColor(config, mode):
    color = QColor()
    if mode == 'ok':
        color.setNamedColor(config.getConfig('dashboardSuccessFontColor') or 'red')
    elif mode == 'fail':
        color.setNamedColor(config.getConfig('dashboardFailFontColor') or 'red')
    else:
        color.setNamedColor(config.getConfig('dashboardFontColor') or 'red')

    return color


def normalFontButtonClickedEvent():
    config = __CONFIG__

    font, ok = QFontDialog.getFont(getDashboardFont(config, 'normal'))
    if ok:
        config.setConfig('dashboardFontFamily', font.family())
        config.setConfig('dashboardFontPointSize', font.pointSize())
        config.setConfig('dashboardFontWeight', font.weight())
        config.setConfig('dashboardFontItalic', font.italic())
        config.setConfig('dashboardFontStrikeOut', font.strikeOut())
        config.setConfig('dashboardFontUnderline', font.underline())
        targetIpHunterConfigSave()

        config.get('dashboardGameIp').setFont(font)
        config.get('dashboardTimer1').setFont(font)
        config.get('dashboardTimer2').setFont(font)


def normalColorButtonClickedEvent():
    config = __CONFIG__

    color = QColorDialog.getColor(getDashboardFontColor(config, 'normal'))
    if color.isValid():
        config.setConfig('dashboardFontColor', color.name())
        targetIpHunterConfigSave()

        config.get('dashboardGameIp').setStyleSheet("color: %s" % color.name())
        config.get('dashboardTimer1').setStyleSheet("color: %s" % color.name())
        config.get('dashboardTimer2').setStyleSheet("color: %s" % color.name())


def okFontButtonClickedEvent():
    config = __CONFIG__

    font, ok = QFontDialog.getFont(getDashboardFont(config, 'ok'))
    if ok:
        config.setConfig('dashboardSuccessFontFamily', font.family())
        config.setConfig('dashboardSuccessFontPointSize', font.pointSize())
        config.setConfig('dashboardSuccessFontWeight', font.weight())
        config.setConfig('dashboardSuccessFontItalic', font.italic())
        config.setConfig('dashboardSuccessFontStrikeOut', font.strikeOut())
        config.setConfig('dashboardSuccessFontUnderline', font.underline())
        targetIpHunterConfigSave()

        config.get('dashboardGameIp').setFont(font)
        config.get('dashboardTimer1').setFont(font)
        config.get('dashboardTimer2').setFont(font)


def okColorButtonClickedEvent():
    config = __CONFIG__

    color = QColorDialog.getColor(getDashboardFontColor(config, 'ok'))
    if color.isValid():
        config.setConfig('dashboardSuccessFontColor', color.name())
        targetIpHunterConfigSave()

        config.get('dashboardGameIp').setStyleSheet("color: %s" % color.name())
        config.get('dashboardTimer1').setStyleSheet("color: %s" % color.name())
        config.get('dashboardTimer2').setStyleSheet("color: %s" % color.name())


def failFontButtonClickedEvent():
    config = __CONFIG__

    font, ok = QFontDialog.getFont(getDashboardFont(config, 'fail'))
    if ok:
        config.setConfig('dashboardFailFontFamily', font.family())
        config.setConfig('dashboardFailFontPointSize', font.pointSize())
        config.setConfig('dashboardFailFontWeight', font.weight())
        config.setConfig('dashboardFailFontItalic', font.italic())
        config.setConfig('dashboardFailFontStrikeOut', font.strikeOut())
        config.setConfig('dashboardFailFontUnderline', font.underline())
        targetIpHunterConfigSave()

        config.get('dashboardGameIp').setFont(font)
        config.get('dashboardTimer1').setFont(font)
        config.get('dashboardTimer2').setFont(font)


def failColorButtonClickedEvent():
    config = __CONFIG__

    color = QColorDialog.getColor(getDashboardFontColor(config, 'fail'))
    if color.isValid():
        config.setConfig('dashboardFailFontColor', color.name())
        targetIpHunterConfigSave()

        config.get('dashboardGameIp').setStyleSheet("color: %s" % color.name())
        config.get('dashboardTimer1').setStyleSheet("color: %s" % color.name())
        config.get('dashboardTimer2').setStyleSheet("color: %s" % color.name())


def dashboardTimerShowClickedEvent():
    config = __CONFIG__

    config.get('dashboardTimer1').setVisible(True)

    config.setConfig('dashboardTimer', 'SHOW')
    config.saveConfig()


def dashboardTimerHideClickedEvent():
    config = __CONFIG__

    config.get('dashboardTimer1').setVisible(False)

    config.setConfig('dashboardTimer', 'HIDE')
    config.saveConfig()


def dashboardConfigRealtimeEvent(text):
    config = __CONFIG__

    dashboard = config.get('dashboard')

    x = int(config.get('dashboardPositionX').text())
    y = int(config.get('dashboardPositionY').text())
    dashboard.move(x, y)

    config.setConfig('dashboardPosX', x)
    config.setConfig('dashboardPosY', y)
    config.setConfig('dashboardNormalText', config.get('dashboardTargetIpNormalText').text().strip())
    config.setConfig('dashboardSuccessText', config.get('dashboardTargetIpOkText').text().strip())
    config.setConfig('dashboardFailText', config.get('dashboardTargetIpFailText').text().strip())
    config.saveConfig()
