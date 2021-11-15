cd C:\App\Project\DiabloUtil
rd /s /q build
rd /s /q dist
pyinstaller --noconfirm --onedir --windowed --icon "C:/App/Project/DiabloUtil/star.ico" --win-private-assemblies --win-no-prefer-redirects --add-data "C:/App/Project/DiabloUtil/README.txt;." --add-data "C:/App/Project/DiabloUtil/star.png;."  "C:/App/Project/DiabloUtil/DiabloCloneStarHunter.py"
mkdir dist\DiabloCloneStarHunter-v1.15
move dist\DiabloCloneStarHunter dist\DiabloCloneStarHunter-v1.15
copy DiabloCloneStarHunterConfig-Source.yaml dist\DiabloCloneStarHunter-v1.15\DiabloCloneStarHunterConfig.yaml
cd dist\
zip -9vr DiabloCloneStarHunter-v1.15.zip ./DiabloCloneStarHunter-v1.15
cd ..
