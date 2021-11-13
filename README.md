cd C:\App\Project\DiabloUtil
rd /s /q build
rd /s /q dist
pyinstaller --hidden-import=sip --icon=star.ico -w DiabloCloneStarHunter.py
copy DiabloCloneStarHunterConfig-Source.yaml dist\DiabloCloneStarHunter\DiabloCloneStarHunterConfig.yaml
copy README.txt dist\DiabloCloneStarHunter\
copy star.png dist\DiabloCloneStarHunter\
copy star.ico dist\DiabloCloneStarHunter\
cd dist
rd /s /q DiabloCloneStarHunter-v14
ren DiabloCloneStarHunter DiabloCloneStarHunter-v14
zip -9vr DiabloCloneStarHunter-v14.zip ./DiabloCloneStarHunter-v14
cd ..
