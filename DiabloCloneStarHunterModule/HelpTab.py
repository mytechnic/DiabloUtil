import os

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel, QWidget

from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def helpTabWidget(widget, config):
    global __WIDGET__, __CONFIG__
    __WIDGET__ = widget
    __CONFIG__ = config

    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    helpFile = 'README.txt'
    if os.path.isfile(helpFile):
        with open(helpFile, encoding='UTF8') as f:
            content = f.read()

    form = QTextEdit('', widget)
    form.setTextInteractionFlags(Qt.TextSelectableByMouse)
    form.setPlainText(content)
    layout.addWidget(form)

    widget = QWidget()
    widget.setLayout(layout)
    return widget
