cd C:\App\Project\DiabloUtil
rd /s /q build
rd /s /q dist
pyinstaller --hidden-import=sip --icon=star.ico -w DiabloCloneStarHunter.py
copy DiabloCloneStarHunterConfig-Source.yaml dist\DiabloCloneStarHunter\DiabloCloneStarHunterConfig.yaml
copy README.txt dist\DiabloCloneStarHunter\
copy star.png dist\DiabloCloneStarHunter\
copy star.ico dist\DiabloCloneStarHunter\
cd dist
ren DiabloCloneStarHunter DiabloCloneStarHunter-v12
zip -9vr DiabloCloneStarHunter-v12.zip ./DiabloCloneStarHunter-v12
cd ..
