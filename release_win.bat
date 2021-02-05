: Releases UALab
@echo off
if exist venv rd /s/q venv
if exist dist rd /s/q dist
if exist built rd /s/q built
if exist release rd /s/q release
echo Please wait. Unfortunately, sometimes it takes several minutes :(
python -m venv  venv

venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install -r requirements.txt

venv\Scripts\python -m pip install pyinstaller
venv\Scripts\pyinstaller -i "urpcadcgui/usbadc10.ico" --add-data "urpcadcgui/usbadc10.ico;." --clean -F --noconsole --add-binary "urpcadcgui/urpcadc-win64/urpcadc.dll;." urpcadcgui/urgui.py

move dist release
if exist build rd /s/q build
if exist dist rd /s/q dist
if exist urgui.spec del urgui.spec
copy urpcadcgui\usbadc10.ico release
cd release