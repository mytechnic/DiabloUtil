from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule import DashboardConfigTab


def dashboardConfigValue(widget: QWidget, config):
    font = DashboardConfigTab.getDashboardFont(config)
    color = DashboardConfigTab.getDashboardFontColor(config)

    form = QLabel('34.93.77.77', widget)
    form.setFont(font)
    form.setStyleSheet('color: ' + color.name())
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
