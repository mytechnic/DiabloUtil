cd C:\App\Project\DiabloUtil
rd /s /q build
rd /s /q dist
pyinstaller --onefile --noconsole DiabloCloneStarHunter.py
mkdir dist\DiabloCloneStarHunter-v1.15
move dist\DiabloCloneStarHunter.exe dist\DiabloCloneStarHunter-v1.15\
copy DiabloCloneStarHunterConfig-Source.yaml dist\DiabloCloneStarHunter-v1.15\DiabloCloneStarHunterConfig.yaml
copy star.png dist\DiabloCloneStarHunter-v1.15\
copy README.txt dist\DiabloCloneStarHunter-v1.15\
cd dist\
zip -9vr DiabloCloneStarHunter-v1.15.zip ./DiabloCloneStarHunter-v1.15
cd ..
