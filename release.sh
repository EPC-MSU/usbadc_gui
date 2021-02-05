if [ -d venv ]; then rm -rf venv; fi;
if [ -d dist ]; then rm -rf dist; fi;
if [ -d build ]; then rm -rf build; fi;
if [ -d release ]; then rm -rf release; fi;
if [ -f release ]; then rm -f release; fi;
python3 -m venv venv
venv/bin/python -m pip install --upgrade pip
venv/bin/python -m pip install -r requirements.txt

venv/bin/python -m pip install pyinstaller
venv/bin/pyinstaller --clean -F --add-binary "urpcadcgui/urpcadc-debian/liburpcadc.so:." urpcadcgui/urgui.py 

mv dist release
cd release
if [ -d build ]; then rm -rf build; fi;
if [ -d dist ]; then rm -rf dist; fi;
count='ls -1 *.spec 2>/dev/null | wc -l'
if [[ $count != 0 ]]; then rm -rf *.spec; fi;