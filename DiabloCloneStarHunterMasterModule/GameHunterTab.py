from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule.D2Config import D2Config

__WIDGET__: QWidget = None
__CONFIG__: D2Config = None
__APP__: QApplication = None


def gameHunterTabWidget(widget, config, app):
    global __WIDGET__, __CONFIG__, __APP__
    __WIDGET__ = widget
    __CONFIG__ = config
    __APP__ = app

    layout = QVBoxLayout()
    layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameNameTitle'))
    sub.addWidget(config.get('gameNameForm'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gamePasswordTitle'))
    sub.addWidget(config.get('gamePasswordForm'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameCreateNumberTitle'))
    sub.addWidget(config.get('gameCreateNumberForm'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameCreateCycleSecTitle'))
    sub.addWidget(config.get('gameCreateCycleSecForm'))
    sub.addWidget(config.get('gameCreateCycleSecUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameJoinAfterSecTitle'))
    sub.addWidget(config.get('gameJoinAfterSecForm'))
    sub.addWidget(config.get('gameJoinAfterSecUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('createdGameNameTitle'))
    sub.addWidget(config.get('createdGameName'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameHunterTickTitle'))
    sub.addWidget(config.get('gameHunterTick'))
    sub.addWidget(config.get('gameHunterTickUnit'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.setAlignment(QtCore.Qt.AlignLeft)
    sub.addWidget(config.get('gameHunterStatusTitle'))
    sub.addWidget(config.get('gameHunterStatus'))
    layout.addLayout(sub)

    sub = QHBoxLayout()
    sub.addWidget(config.get('gameHunterStartButton'))
    sub.addWidget(config.get('gameHunterConfigApplyButton'))
    layout.addLayout(sub)

    widget = QWidget()
    widget.setLayout(layout)
    return widget


def gameHunterStartButtonClickedEvent():
    pass


def gameHunterConfigApplyButtonClickedEvent():
    pass
