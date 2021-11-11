from D2IpScan import D2GameUnitAction, D2Config


def gameCreateFlow(position, title, password):
    D2GameUnitAction.gameTabMenuAction(position)
    D2GameUnitAction.gameTitleWriteAction(position, title)
    D2GameUnitAction.gamePasswordWriteAction(position, password)
    D2GameUnitAction.gameCreateButtonMove(position)
    D2GameUnitAction.gameCreateButtonAction(position)
