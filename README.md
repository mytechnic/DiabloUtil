컴파일 방법
    # pyinstaller --icon=star.ico -w -F StarDiablo2AdminUtils.py
    pyinstaller --hidden-import=sip --icon=star.ico -w DiabloCloneStarHunter.py
    copy star.png dist\StarDiablo2AdminUtils

    pyinstaller --icon=star.ico -w -F DiabloCloneStarHunter.py
    copy star.png dist\StarDiablo2AdminUtils
