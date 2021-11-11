import sys

import pygetwindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

__TITLE__ = 'Diablo Clone Star Hunter 1.0'
__PROGRAM_ID__ = 'DiabloCloneStarHunter'

from D2IpScan import D2Window
from D2IpScan.D2Config import D2Config


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        config = D2Config(__PROGRAM_ID__)
        D2Window.paintMainWindow(self, config)
        self.showMainForm()

    def showMainForm(self):
        self.setWindowTitle(__TITLE__)
        self.setWindowIcon(QIcon('star.png'))
        self.setFixedSize(500, 600)
        self.show()


if __name__ == '__main__':
    if len(pygetwindow.getWindowsWithTitle(__TITLE__)) > 0:
        sys.exit(0)

    app = QApplication(sys.argv)
    try:
        mainApp = MainApp()
        print('sys.exec_()')
        app.exec_()
        print('sys.exit()')
        sys.exit()
    except Exception as e:
        print(e)
