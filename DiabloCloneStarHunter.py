import ctypes
import os
import sys

import pygetwindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from DiabloCloneStarHunterModule import D2MainWindow, D2Process
from DiabloCloneStarHunterModule.D2Config import D2Config

os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'

__TITLE__ = 'Diablo Clone Star Hunter 1.17'
__PROGRAM_ID__ = 'DiabloCloneStarHunter'


def global_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    print(traceback.format_exc())
    sys._excepthook(exctype, value, traceback)


sys._excepthook = sys.excepthook
sys.excepthook = global_exception_hook


def getAppTitle(gamePath=None):
    if gamePath is None:
        return __TITLE__

    return __TITLE__ + ' ' + gamePath


class MainApp(QWidget):
    config: D2Config = None

    def __init__(self, app, title, gamePath):
        super().__init__()

        self.config = D2Config(__PROGRAM_ID__)
        self.config.set('programId', __PROGRAM_ID__)
        self.config.set('programPath', gamePath)
        self.config.set('KILL_SIGNAL', False)

        D2MainWindow.paintMainWindow(self, self.config, app)
        self.showMainForm(title)

    def showMainForm(self, title):
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('star.png'))
        self.setFixedSize(500, 600)
        self.show()

        if not ctypes.windll.shell32.IsUserAnAdmin():
            QMessageBox.about(self, '실행 오류', '관리자 권한으로 다시 실행 해 주세요.')
            self.exit()
            sys.exit(0)

    def closeEvent(self, event):
        self.config.set('KILL_SIGNAL', True)
        self.exit()
        event.accept()

    def exit(self):
        self.config.set('KILL_SIGNAL', True)
        if self.config.get('dashboard'):
            self.config.get('dashboard').close()


if __name__ == '__main__':
    pathList = D2Process.getAppPathList()

    appTitle = None
    appPath = None
    if len(pathList) == 0:
        appTitle = getAppTitle()
    else:
        for path in pathList:
            if len(pygetwindow.getWindowsWithTitle(getAppTitle(path))) == 0:
                appTitle = getAppTitle(path)
                appPath = path
                break

    if appTitle is not None:
        app = QApplication(sys.argv)
        mainApp = MainApp(app, appTitle, appPath)
        sys.exit(app.exec_())
    else:
        sys.exit(0)
