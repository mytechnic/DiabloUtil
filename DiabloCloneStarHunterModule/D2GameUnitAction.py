import random
import time

import pyautogui
import pygetwindow
from PyQt5 import QtTest

from DiabloCloneStarHunterModule import D2GameFlow


def moveRelAndClick(x1, y1, x2, y2):
    moveRelOnly(x1, y1, x2, y2)
    sleep(random.randrange(100, 400))
    pyautogui.click()


def moveToAndClick(x1, y1, x2, y2):
    moveToOnly(x1, y1, x2, y2)
    sleep(random.randrange(100, 400))
    pyautogui.click()


def moveRelOnly(x1, y1, x2, y2):
    x = random.randrange(x1, x2)
    y = random.randrange(y1, y2)
    pyautogui.moveRel(x, y)


def moveToOnly(x1, y1, x2, y2):
    x = random.randrange(x1, x2)
    y = random.randrange(y1, y2)
    pyautogui.moveTo(x, y, random.randrange(15, 40) / 100)


def gameStartAction():
    windows = pygetwindow.getWindowsWithTitle('Diablo II: Resurrected')
    if windows is None or len(windows) == 0:
        return False

    window = windows[0]
    window.activate()
    window.top = 0
    window.left = 0

    return True


def gameTabMenuAction(position):
    (x1, y1, x2, y2) = position['tabMenu']
    moveToAndClick(x1, y1, x2, y2)


def gameTitleWriteAction(position, title):
    (x1, y1, x2, y2) = position['title']
    moveToAndClick(x1, y1, x2, y2)
    pyautogui.typewrite(title, interval=random.randrange(15, 30) / 100)


def gamePasswordWriteAction(position, password):
    if not password:
        return

    (x1, y1, x2, y2) = position['password']
    moveToAndClick(x1, y1, x2, y2)
    pyautogui.typewrite(password, interval=random.randrange(15, 30) / 100)


def gameCreateButtonMove(position):
    (x1, y1, x2, y2) = position['createButton']
    moveToOnly(x1, y1, x2, y2)


def gameCreateButtonAction(position):
    (x1, y1, x2, y2) = position['createButton']
    moveToAndClick(x1, y1, x2, y2)


def gameExitAction(position):
    D2GameFlow.gameFocus()
    pyautogui.hotkey('esc')

    sleep(random.randrange(1000, 1500))
    (x1, y1, x2, y2) = position['exitButton']
    moveToAndClick(x1, y1, x2, y2)


def sleep(millisecond):
    QtTest.QTest.qWait(millisecond)


def now():
    return time.strftime('%H시 %M분 %S초', time.localtime(time.time()))
