from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit, QCheckBox, QLabel, QPushButton, QWidget, QRadioButton, QGroupBox

__WIDGET__: QWidget = None


# 헤더 영역

def targetIpTitle(config):
    form = QLabel('목표 IP')
    form.setMinimumHeight(25)
    config.put('targetIpTitle', form)


def targetIpForm(config):
    form = QLineEdit(config.getConfig('targetIp'))
    form.setMinimumHeight(25)
    config.put('targetIpForm', form)


def targetIpHelp(config):
    form = QLabel('※ 우버디아 IP를 입력하지 않을 경우 자동 게임생성이 진행되지 않습니다.')
    form.setMinimumHeight(25)
    config.put('targetIpHelp', form)


def topMostForm(widget, config):
    global __WIDGET__

    if __WIDGET__ is None:
        __WIDGET__ = widget

    form = QCheckBox('맨위 고정')
    form.setMinimumHeight(25)
    form.stateChanged.connect(_topMostChangedActionCallback)
    config.put('topMostForm', form)


def _topMostChangedActionCallback(state):
    if state == Qt.Checked:
        __WIDGET__.setWindowFlags(__WIDGET__.windowFlags() | Qt.WindowStaysOnTopHint)
    else:
        __WIDGET__.setWindowFlags(__WIDGET__.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
    __WIDGET__.show()


# 게임IP 조회 영역


def findIpModeTitle(config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('검색방법')
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    config.put('findIpModeTitle', form)


def manualFindIpMode(config, clickedAction):
    form = QRadioButton('수동검색')
    form.setChecked(config.getConfig('findIpSearchMode') != 'AUTO')
    form.clicked.connect(clickedAction)
    form.setMinimumHeight(25)
    config.put('manualFindIpMode', form)


def autoFindIpMode(config, clickedAction):
    form = QRadioButton('자동검색')
    form.setChecked(config.getConfig('findIpSearchMode') == 'AUTO')
    form.clicked.connect(clickedAction)
    form.setMinimumHeight(25)
    config.put('autoFindIpMode', form)


def autoFindIpModeConfigTitle(config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('검색설정')
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    config.put('autoFindIpModeConfigTitle', form)


def autoFindIpModeScanSecondForm(config):
    form = QLineEdit(config.getConfig('autoFindIpModeScanSecond') or '1')
    form.setMinimumHeight(25)
    form.setFixedWidth(50)
    form.setMaxLength(3)
    form.setValidator(QIntValidator(1, 100))
    config.put('autoFindIpModeScanSecondForm', form)


def autoFindIpModeScanSecondUnit(config):
    form = QLabel('초마다 갱신(1부터 100까지 입력 가능)')
    form.setMinimumHeight(25)
    config.put('autoFindIpModeScanSecondUnit', form)


def findIpRegionTitle(config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('지역')
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    config.put('findIpRegionTitle', form)


def findIpRegionResult(config):
    form = QLabel('N/A')
    form.setMinimumHeight(25)
    config.put('findIpRegionResult', form)


def findIpResultTitle(config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('아이피')
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    config.put('findIpResultTitle', form)


def findIpResultValue(config):
    form = QLabel('N/A')
    form.setMinimumHeight(25)
    config.put('findIpResultValue', form)


def protectedGameIpTitle(config):
    font = QtGui.QFont()
    font.setBold(True)

    form = QLabel('게임IP 보호')
    form.setFont(font)
    form.setMinimumHeight(25)
    form.setFixedWidth(80)
    config.put('protectedGameIpTitle', form)


def protectedGameIpOn(config, clickedAction):
    form = QRadioButton('사용')
    form.setChecked(config.getConfig('protectedGameIpMode') == 'ON')
    form.clicked.connect(clickedAction)
    form.setMinimumHeight(25)
    config.put('protectedGameIpOn', form)


def protectedGameIpOff(config, clickedAction):
    form = QRadioButton('사용안함')
    form.setChecked(config.getConfig('protectedGameIpMode') != 'OFF')
    form.clicked.connect(clickedAction)
    form.setMinimumHeight(25)
    config.put('protectedGameIpOff', form)


# 방화벽 설정 영역


def programPathTitle(config):
    form = QLineEdit('D2R 위치')
    form.setMinimumHeight(25)
    config.put('programPathTitle', form)


def programPathForm(config):
    form = QLineEdit(config.getConfig('program'))
    form.setReadOnly(True)
    form.setMinimumHeight(25)
    config.put('programPathForm', form)


def firewallButton(config, clickedActionCallback):
    button = QPushButton('방화벽 설정')
    button.setMinimumHeight(25)
    button.setMaximumWidth(50)
    button.clicked.connect(clickedActionCallback)
    config.put('firewallButton', button)


def firewallWindowOpen(config, clickedActionCallback):
    button = QPushButton('방화벽 조회')
    button.setMinimumHeight(25)
    button.setMaximumWidth(50)
    button.clicked.connect(clickedActionCallback)
    config.put('firewallWindowOpen', button)


def firewallHelp(config):
    form = QLabel('※ 디아블로2 리저렉션의 아웃바운드 방화벽을 설정 할 수 있습니다.')
    form.setMinimumHeight(25)
    config.put('firewallHelp', form)


def hunterControllerTitle(config):
    myFont = QtGui.QFont()
    myFont.setBold(True)

    form = QLabel('자동 게임생성 (창모드, 1280x768)')
    form.setMinimumHeight(25)
    form.setFont(myFont)
    config.put('hunterControllerTitle', form)
