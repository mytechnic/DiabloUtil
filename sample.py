import math, sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        widget = QWidget(self)
        self.editor = QTextEdit()
        self.editor.setWordWrapMode(QTextOption.WrapAnywhere)
        self.editor.setPlainText("https://kwonkyo.tistory.com  " * 100)
        layout = QGridLayout(widget)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        button = QPushButton("Wait")
        layout.addWidget(button, 1, 1, 1, 1)

        self.setCentralWidget(widget)
        self.overlay = Overlay(self.centralWidget())
        self.overlay.hide()
        button.clicked.connect(self.overlay.show)

    def resizeEvent(self, event):
        self.overlay.resize(event.size())
        event.accept()


class Overlay(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)

        self.cntPreset = 150
        self.label = QLabel('000', self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 180)))

        self.label.move(self.width() / 2 - 10, self.height() / 2 - 5)

        painter.setPen(QPen(Qt.NoPen))
        for i in range(14):
            if (self.counter / 5) % 14 == i:
                painter.setBrush(QBrush(QColor(127 + (self.counter % 5) * 32, 0, 127)))
            else:
                painter.setBrush(QBrush(QColor(127, 127, 127)))
            painter.drawEllipse(
                self.width() / 2 + 50 * math.cos(2 * math.pi * i / 14.0) - 5,
                self.height() / 2 + 50 * math.sin(2 * math.pi * i / 14.0) - 10,
                10, 10)
        painter.end()

    # 30 millisecond 간격으로 이벤트가 발생하는 타이머 설정
    def showEvent(self, event):
        self.timer = self.startTimer(30)
        self.counter = 0

    # 타이머 콜백
    def timerEvent(self, event):
        self.counter += 1
        self.update()
        self.label.setText(str(self.cntPreset - self.counter))
        if self.counter == self.cntPreset:  # 300번 호출되면
            self.killTimer(self.timer)  # 타이머 종료하고
            self.hide()  # 오버레이 숨기기


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())