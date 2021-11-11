import sys

import pygetwindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

__TITLE__ = 'Diablo Clone Star Hunter 1.0'
__PROGRAM_ID__ = 'DiabloCloneStarHunter'

from D2IpScan import D2MainWindow
from D2IpScan.D2Config import D2Config


class MainApp(QMainWindow):
    def __init__(self, app):
        super().__init__()

        widget = QWidget()
        config = D2Config(__PROGRAM_ID__)
        D2MainWindow.paintMainWindow(widget, config, app)
        self.showMainForm(widget)

    def showMainForm(self, win):
        win.setWindowTitle(__TITLE__)
        win.setWindowIcon(QIcon('star.png'))
        win.setFixedSize(500, 600)
        win.show()


if __name__ == '__main__':
    if len(pygetwindow.getWindowsWithTitle(__TITLE__)) > 0:
        sys.exit(0)

    app = QApplication(sys.argv)
    try:
        mainApp = MainApp(app)
        app.exec_()
        sys.exit()
    except Exception as e:
        print(e)
