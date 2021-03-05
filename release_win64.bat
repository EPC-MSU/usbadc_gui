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
venv\Scripts\pyinstaller -i "usbadc10gui/usbadc10.ico" --add-data "usbadc10gui/usbadc10.ico;." --clean -F --noconsole --add-binary "usbadc10gui/usbadc10-win64/usbadc10.dll;." usbadc10gui/__main__.py -n Usbadc10

move dist release_win64
if exist build rd /s/q build
if exist dist rd /s/q dist
if exist urgui.spec del urgui.spec
copy urpcadcgui\usbadc10.ico release_win64