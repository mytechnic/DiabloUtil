import sys

import pygetwindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

__TITLE__ = 'Diablo Clone Star Hunter 1.1'
__PROGRAM_ID__ = 'DiabloCloneStarHunter'

from DiabloCloneStarHunterModule import D2MainWindow
from DiabloCloneStarHunterModule.D2Config import D2Config


class MainApp(QWidget):
    config: D2Config = None

    def __init__(self, app):
        super().__init__()

        self.config = D2Config(__PROGRAM_ID__)
        self.config.set('programId', __PROGRAM_ID__)
        self.config.set('killSignal', False)

        D2MainWindow.paintMainWindow(self, self.config, app)
        self.showMainForm()

    def showMainForm(self):
        self.setWindowTitle(__TITLE__)
        self.setWindowIcon(QIcon('star.png'))
        self.setFixedSize(500, 600)
        self.show()

    def closeEvent(self, event):
        self.config.set('killSignal', True)
        self.exit()
        event.accept()

    def exit(self):
        if self.config.get('dashboard'):
            self.config.get('dashboard').close()


if __name__ == '__main__':
    if len(pygetwindow.getWindowsWithTitle(__TITLE__)) > 0:
        sys.exit(0)

    app = QApplication(sys.argv)
    try:
        mainApp = MainApp(app)
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
