from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *


def dashboardPositionConfigTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('전광판 위치', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardPositionConfigTitle', form)


def dashboardPositionConfigXTitle(widget, config):
    form = QLabel('X:', widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(20)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardPositionConfigXTitle', form)


def dashboardPositionX(widget, config, event):
    form = QLineEdit(str(config.getConfig('dashboardPosX')), widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setValidator(QIntValidator(0, 9999))
    form.textChanged.connect(event)
    config.set('dashboardPositionX', form)


def dashboardPositionConfigYTitle(widget, config):
    form = QLabel('Y:', widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(20)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardPositionConfigYTitle', form)


def dashboardPositionY(widget, config, event):
    form = QLineEdit(str(config.getConfig('dashboardPosY')), widget)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setValidator(QIntValidator(0, 9999))
    form.textChanged.connect(event)
    config.set('dashboardPositionY', form)


def dashboardTargetIpNormalText(widget, config, event):
    form = QLineEdit(config.getConfig('dashboardNormalText') or '{{GAME_IP}}', widget)
    form.setMinimumHeight(25)
    form.textChanged.connect(event)
    config.set('dashboardTargetIpNormalText', form)


def dashboardTargetIpOkText(widget, config, event):
    form = QLineEdit(config.getConfig('dashboardSuccessText') or '{{GAME_IP}} - ★☆★☆ OK ☆★☆★', widget)
    form.setMinimumHeight(25)
    form.textChanged.connect(event)
    config.set('dashboardTargetIpOkText', form)


def dashboardTargetIpFailText(widget, config, event):
    form = QLineEdit(config.getConfig('dashboardFailText') or '{{GAME_IP}} - FAIL!', widget)
    form.setMinimumHeight(25)
    form.textChanged.connect(event)
    config.set('dashboardTargetIpFailText', form)


def dashboardTimerConfigTitle(widget, config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('타이머 설정', widget)
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    config.set('dashboardTimerConfigTitle', form)


def dashboardTimerShow(widget, config, clickedEvent):
    form = QRadioButton('보이기', widget)
    form.setChecked(True)
    form.clicked.connect(clickedEvent)
    form.setMinimumHeight(25)
    form.setFixedWidth(65)
    config.set('dashboardTimerShow', form)


def dashboardTimerHide(widget, config, clickedEvent):
    form = QRadioButton('감추기', widget)
    form.setChecked(False)
    form.clicked.connect(clickedEvent)
    form.setMinimumHeight(25)
    form.setFixedWidth(65)
    config.set('dashboardTimerHide', form)


def dashboardNormalFontButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('Font', widget)
    form.setMinimumHeight(20)
    form.clicked.connect(clickedEvent)
    config.set('dashboardNormalFontButton', form)


def dashboardNormalColorButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('Color', widget)
    form.setMinimumHeight(20)
    form.clicked.connect(clickedEvent)
    config.set('dashboardNormalColorButton', form)


def dashboardOkFontButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('Font', widget)
    form.setMinimumHeight(20)
    form.clicked.connect(clickedEvent)
    config.set('dashboardOkFontButton', form)


def dashboardOkColorButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('Color', widget)
    form.setMinimumHeight(20)
    form.clicked.connect(clickedEvent)
    config.set('dashboardOkColorButton', form)


def dashboardFailFontButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('Font', widget)
    form.setMinimumHeight(20)
    form.clicked.connect(clickedEvent)
    config.set('dashboardFailFontButton', form)


def dashboardFailColorButton(widget: QWidget, config, clickedEvent):
    form = QPushButton('Color', widget)
    form.setMinimumHeight(20)
    form.clicked.connect(clickedEvent)
    config.set('dashboardFailColorButton', form)
