rd /s /q build
rd /s /q dist
pyinstaller --hidden-import=sip --icon=star.ico -w DiabloCloneStarHunter.py
copy README.txt dist\DiabloCloneStarHunter\
copy star.png dist\DiabloCloneStarHunter\
copy star.ico dist\DiabloCloneStarHunter\
