import random

import pyautogui
import pygetwindow

from D2IpScan import D2Timer


def moveRelAndClick(x1, y1, x2, y2):
    moveRelOnly(x1, y1, x2, y2)
    D2Timer.sleep(random.randrange(100, 400))
    pyautogui.click()


def moveToAndClick(x1, y1, x2, y2):
    moveToOnly(x1, y1, x2, y2)
    D2Timer.sleep(random.randrange(100, 400))
    pyautogui.click()


def moveRelOnly(x1, y1, x2, y2):
    x = random.randrange(x1, x2)
    y = random.randrange(y1, y2)
    pyautogui.moveRel(x, y)


def moveToOnly(x1, y1, x2, y2):
    x = random.randrange(x1, x2)
    y = random.randrange(y1, y2)
    pyautogui.moveTo(x, y, random.randrange(15, 40) / 100)


def gameWindowFocusAction():
    window = pygetwindow.getWindowsWithTitle('Diablo II: Resurrected')[0]
    window.activate()
    window.resizeTo(1280, 768)
    window.top = 0
    window.left = 0


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
    pyautogui.hotkey('esc')
    D2Timer.sleep(random.randrange(1000, 1500))
    (x1, y1, x2, y2) = position['exitButton']
    moveToAndClick(x1, y1, x2, y2)
