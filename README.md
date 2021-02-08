# usbadc10

## RU
Графический интерфейс для устройства usbadc10.
Помимо неё здесь также приложены тесты и тест скорости, по которому оценивалась скорость работы. 
Для работы у вас также должен стоять интерпретатор питон(32 бита для виндовс).

### Запустить из под корня под Linux
```bash
sudo -H pip3 install -r requirements.txt
python3 -m urpcadcgui.urgui
```
### Запустить из под корня под Windows
```bash
pip install -r requirements.txt
python -m urpcadcgui.urgui
```
### Сборка бинарного файла Linux
```bash
source release.sh
```
### Сборка бинарного файла Windows
```bash
.\release-win.bat
```
![Скриншот совта](screen.png)

## EN
Graphical interface for usbadc10 device.
In addition to it, tests and a speed test are also attached here, by which the speed of work was assessed.
To work, you must also have a python interpreter (32 bits for Windows). 

### Run from root under Linux
```bash
sudo -H pip3 install -r requirements.txt
python3 -m urpcadcgui.urgui
```
### Run from root under Windows
```bash
pip install -r requirements.txt
python -m urpcadcgui.urgui
```
### Build Linux Binary
```bash
source release.sh
```
### Build Windows Binary
```bash
.\release-win.bat
```
![Owt screenshot](screen.png)