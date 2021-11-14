import pygetwindow

from DiabloCloneStarHunterModule import D2GameUnitAction


def gameCreateFlow(position, title, password):
    gameFocus()
    D2GameUnitAction.gameTabMenuAction(position)
    D2GameUnitAction.gameTitleWriteAction(position, title)
    D2GameUnitAction.gamePasswordWriteAction(position, password)
    D2GameUnitAction.gameCreateButtonMove(position)


def gameFocus():
    try:
        windows = pygetwindow.getWindowsWithTitle('Diablo II: Resurrected')
        if windows is None or len(windows) == 0:
            return

        window = windows[0]
        window.activate()
    except Exception as e:
        print(e)
