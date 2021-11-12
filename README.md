rd /s /q build
rd /s /q dist
pyinstaller --hidden-import=sip -w DiabloCloneStarHunter.py
copy README.txt dist\DiabloCloneStarHunter\
