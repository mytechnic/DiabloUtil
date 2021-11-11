from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from D2IpScan.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None


def firewallTabWidget(widget, config):
    global __WIDGET__, __CONFIG__
    __WIDGET__ = widget
    __CONFIG__ = config

    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

    widget = QWidget()
    widget.setLayout(layout)

    return widget
