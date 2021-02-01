import sys
import PyQt5.QtWidgets as qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt 
import numpy as np
import PyQt5.QtCore as qtc
from matplotlib.animation import FuncAnimation as ani
import gui
import urpcadc
import csv
import serial.tools.list_ports
from platform import system
import pyqtgraph as pg

class uRPCApp(qt.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        # self.graphWidget = pg.PlotWidget()# self.plot_window)
        # # self.plot_window.add(self.graphWidget)
        # # self.graphWidget.
        # self.graphWidget.setParent(self.plot_window)
        # self.ur_graphicsView.
        self.graphWidget.setBackground('w')
        self.timer = qtc.QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.timer_handler)

        self.os_kind = system().lower()
        self.rescan_com_ports()

        # self.device = urpcadc.UrpcadcDeviceHandle("com:///dev/ttyACM0")
        self.start_stop_status = False
        self.start_stop_recording_status = False
        period_vals = np.array([0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1])
        self.comboBox_period_val.setCurrentIndex(7)
        for i in range(10):
            self.comboBox_period_val.setItemData(i, period_vals[i])
        self.data_to_scv = np.empty((1,10))
        self.gstates = [True for gstates in range(10)]
        self.gcolors = [(0, 0, 255), (0, 170, 0), (255, 0, 0), (0, 0, 0), (	255, 85, 0), (0, 170, 255), (0, 255, 0), (255, 170, 255),  (111, 111, 111), (170, 85, 0)] 
        #'blue', 'green', 'red', 'black', 'orange', 'lightblue', 'lightgreen', 'pink',  'grey', 'brown'

        
        self.x = np.linspace(0, 10, 1000)
        self.y = np.zeros((1000,10))#np.sin(2 * np.pi * ((x+phi) * f))
        self.graphWidget.setBackground('w')
        # plot data: x, y values
        # pen1 = pg.mkPen(color=(255, 0, 0),width=2)
        # pen2 = pg.mkPen(color=(0, 255, 0),width=2)
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Volage, V', **styles)
        self.graphWidget.setLabel('bottom', 'Time', **styles)
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setYRange(-10, 33000, padding=0)
        self.graphWidget.setXRange(0, 10, padding=0)
        self.linias = []
        for i in range(10):
            # linia, = 
            # ax.plot(x, y[:,i], color = gcolors[i])
            self.linias.append(self.graphWidget.plot(self.x, 
                                            self.y[:,i], 
                                            pen=pg.mkPen(color=self.gcolors[i], 
                                                            width=2)))


        self.disconnect_button.setEnabled(False)
        self.start_stop_recording.setEnabled(False)
        self.start_stop.setEnabled(False)
        self.actionDisconnect.setEnabled(False)
        self.actionStart_stop_recording.setEnabled(False)
        self.actionStart_Stop_getting_data.setEnabled(False)

        self.actionThis_Application.triggered.connect(self.this_app)
        # self.actionDisconnect.triggered(self.connection)
        self.connect_button.clicked.connect(self.connection)
        self.disconnect_button.clicked.connect(self.disconnection)
        # self.apply_button.clicked.connect(self.period_chanded)
        # self.actionApply.triggered.connect(self.period_chanded)
        self.comboBox_period_val.activated.connect(self.period_chanded)
        self.rescan_botton.clicked.connect(self.rescan_com_ports)
        self.b_1_blue.toggled.connect(self.replot)
        self.b_2_green.toggled.connect(self.replot)
        self.b_3_red.toggled.connect(self.replot)
        self.b_4_black.toggled.connect(self.replot)
        self.b_5_orange.toggled.connect(self.replot)
        self.b_6_blue_light.toggled.connect(self.replot)
        self.b_7_green_light.toggled.connect(self.replot)
        self.b_8_pig.toggled.connect(self.replot)
        self.b_9_gray.toggled.connect(self.replot)
        self.b_10_brown.toggled.connect(self.replot)
        self.save_button.clicked.connect(self.save_handler)
        self.start_stop.clicked.connect(self.start_stop_handler)
        self.start_stop_recording.clicked.connect(self.start_stop_recording_handler)
        self.autoscale_button.clicked.connect(self.autoscale)
    def connection(self):
        device_name = self.comboBox_ports.currentText()
        print (device_name)
        try:
            self.device = urpcadc.UrpcadcDeviceHandle(device_name)
            self.disconnect_button.setEnabled(True)
            self.connect_button.setEnabled(False)
            self.start_stop.setEnabled(True)
            self.actionDisconnect.setEnabled(True)
            # self.actionStart_stop_recording.setEnabled(True)
            self.actionStart_Stop_getting_data.setEnabled(True)
            self.actionConnect.setEnabled(False)
        except:
            msgbox = qt.QMessageBox()
            msgbox.setText("No connection")
            msgbox.exec_()
    def disconnection(self):
        self.device.close_device()
        self.rescan_com_ports()
        self.disconnect_button.setEnabled(False)
        self.connect_button.setEnabled(True)
        self.start_stop.setEnabled(False)
        self.actionDisconnect.setEnabled(False)
        self.actionStart_stop_recording.setEnabled(False)
        self.actionStart_Stop_getting_data.setEnabled(False)
        self.actionConnect.setEnabled(True)
        self.start_stop_recording.setEnabled(False)
        self.start_stop_recording_status = False
    def this_app(self):
        msgbox = qt.QMessageBox()
        msgbox.setText("This is a simple cross-platform application for the uRPCADC device.\nVersion 0.1\nCopyright © 2020 Nikita Presnov\npresnovnikita@yandex.ru")
        msgbox.exec_()
    def period_chanded(self):
        """
        """
        # Получаем данные из текстовых полей
        self.timer_period = 1000*(self.comboBox_period_val.currentData())
        if self.start_stop_status:
            self.timer.start(self.timer_period)
            self.y = np.zeros((1000,10))
        else:
            self.timer.stop()
        
        print(self.comboBox_period_val.currentData())
    def timer_handler(self):
        """
        Обработчик таймера.
        """
        self.data = self.device.get_conversion()
        for i in range(10):
            self.y[:,i] = np.roll(self.y[:,i],-1,axis=0)
            self.y[-1,i]=self.data.data[i]
            # self.linias[i].setData(self.x, self.y[:,i])
            if self.gstates[i]:
                self.linias[i].setData(self.x, self.y[:,i])
        
        if self.start_stop_recording_status:
            # print(self.y[-1,:])
            self.data_to_scv = np.vstack((self.data_to_scv, self.y[-1,:]))

    def start_stop_handler(self):
        self.start_stop_status = not (self.start_stop_status)
        if self.start_stop_status:
            self.start_stop_recording.setEnabled(True)
            self.actionStart_stop_recording(True)
        else:
            self.start_stop_recording.setEnabled(False)
            self.actionStart_stop_recording(False)
        self.period_chanded()
        
    def start_stop_recording_handler(self):
        self.start_stop_recording_status = not (self.start_stop_recording_status)
        if self.start_stop_recording_status:
            self.start_stop_recording.setStyleSheet('background: rgb(0,170,0);')
        else:
            self.start_stop_recording.setStyleSheet('background: rgb(238,238,238);')
            # setStyleSheet('background: rgb(254,254,254);')
        # print(self.start_stop_recording_status)
    def save_handler(self):
        FILENAME, FILTER = qt.QFileDialog.getSaveFileName(None, 
                                                    'Save File', 
                                                    "output.csv",
                                                    filter= "CSV Files (*.csv)", 
                                                    options=qt.QFileDialog.DontUseNativeDialog)
        print(FILENAME)       
        print(FILTER)

        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerows(self.data_to_scv)
        print(self.data_to_scv)
        self.data_to_scv = np.empty((1,10))
    def replot(self):
        self.gstates[0] = self.b_1_blue.isChecked()
        self.gstates[1] = self.b_2_green.isChecked()
        self.gstates[2] = self.b_3_red.isChecked()
        self.gstates[3] = self.b_4_black.isChecked()
        self.gstates[4] = self.b_5_orange.isChecked()
        self.gstates[5] = self.b_6_blue_light.isChecked()
        self.gstates[6] = self.b_7_green_light.isChecked()
        self.gstates[7] = self.b_8_pig.isChecked()
        self.gstates[8] = self.b_9_gray.isChecked()
        self.gstates[9] = self.b_10_brown.isChecked()
        for i in range(10):
            if not self.gstates[i]:
                self.linias[i].clear()

    def rescan_com_ports(self):
        self.comboBox_ports.clear()
        ports = serial.tools.list_ports.comports()
        valid_ports = []
        if self.os_kind == "windows":
            for port in sorted(ports):
                # print(port.device)
                try:
                    s = serial.Serial(port.device)
                    s.close()
                    valid_ports.append("com:\\\\.\\" + port.device)
                except (OSError, serial.SerialException):
                    pass
        elif self.os_kind == "darwin":
            print("Unsupported system")
            # msgbox = qt.QMessageBox()
            # msgbox.setText("Unsupported system")
            # msgbox.exec_()
        elif self.os_kind == "freebsd" or "linux" in self.os_kind:
            for port in sorted(ports):
                # print(port.device)
                try:
                    s = serial.Serial(port.device)
                    s.close()
                    valid_ports.append("com://" + port.device)
                except (OSError, serial.SerialException):
                    pass
        else:
            raise RuntimeError("unexpected OS")
        self.comboBox_ports.addItems(valid_ports)
    def autoscale(self):
        self.graphWidget.setYRange(-10, 33000, padding=0)
        self.graphWidget.setXRange(0, 10, padding=0)


def main():
    app = qt.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = uRPCApp()  # Создаём объект класса uRPCApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())
    window.disconnecton()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()