import sys
import PyQt5.QtWidgets as qt
from PyQt5 import QtGui
import numpy as np
import PyQt5.QtCore as qtc
import urpcadcgui.gui as gui
import urpcadcgui.urpcadc as urpcadc
import csv
import serial.tools.list_ports
from platform import system
import pyqtgraph as pg


class uRPCApp(qt.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = qtc.QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.timer_handler)

        self.timer_monitor = qtc.QTimer(self)
        self.timer_monitor.setSingleShot(False)
        self.timer_monitor.timeout.connect(self.timer_monitoring)
        self.timer_monitor.start(5000)

        self.os_kind = system().lower()
        self.rescan_com_ports()

        self.start_stop_status = False
        self.start_stop_recording_status = False
        period_vals = np.array([0.05, 0.1, 0.2, 0.5, 1, 5, 10, 60, 300, 600])
        for i in range(10):
            self.comboBox_period_val.setItemData(i, period_vals[i])
        self.data_to_scv = np.empty((0, 10))
        self.gstates = [True for gstates in range(10)]
        self.gcolors = [(0, 0, 255), (0, 170, 0), (255, 0, 0), (0, 0, 0), (255, 85, 0),
                        (0, 170, 255), (0, 255, 0), (255, 170, 255), (111, 111, 111), (170, 85, 0)]
        # 'blue', 'green', 'red', 'black', 'orange', 'lightblue', 'lightgreen', 'pink',  'grey', 'brown'

        self.x = np.linspace(-0.2*1000, 0, 1000)
        self.y = np.zeros((1000, 10))

        self.graphWidget.setBackground('w')
        self.graphWidget.enableAutoRange()
        self.graphWidget.setLimits(yMin=0, yMax=3.3)
        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Voltage, V', **styles)
        self.graphWidget.setLabel('bottom', 'Time, s', **styles)
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setYRange(-0, 3.3, padding=0)
        self.linias = []
        for i in range(10):
            self.linias.append(self.graphWidget.plot(self.x,
                                                     self.y[:, i],
                                                     pen=pg.mkPen(color=self.gcolors[i],
                                                                  width=2)))

        self.disconnect_button.setEnabled(False)
        self.start_stop_recording.setEnabled(False)
        self.start_stop.setEnabled(False)
        self.actionDisconnect.setEnabled(False)
        self.actionStart_stop_recording.setEnabled(False)
        self.actionStart_Stop_getting_data.setEnabled(False)
        self.setWindowIcon(QtGui.QIcon('usbadc10.ico'))

        self.actionThis_Application.triggered.connect(self.this_app)
        self.connect_button.clicked.connect(self.connection)
        self.disconnect_button.clicked.connect(self.disconnection)
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
        """
        Connect devise unlock some options.
        """
        device_name = self.comboBox_ports.currentText()
        try:
            self.device = urpcadc.UrpcadcDeviceHandle(device_name)
            self.disconnect_button.setEnabled(True)
            self.connect_button.setEnabled(False)
            self.start_stop.setEnabled(True)
            self.actionDisconnect.setEnabled(True)
            # self.actionStart_stop_recording.setEnabled(True)
            self.actionStart_Stop_getting_data.setEnabled(True)
            self.actionConnect.setEnabled(False)
        except urpcadc.UrpcDeviceUndefinedError:
            msgbox = qt.QMessageBox()
            msgbox.setText("No connection")
            msgbox.exec_()

    def disconnection(self):
        """
        Disconnect devise and rollback of GUI to its original state.
        """
        self.start_stop_recording.setStyleSheet('background: rgb(238,238,238);')
        self.save_button.setEnabled(True)
        self.actionSave.setEnabled(True)
        self.timer.stop()
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
        self.start_stop_status = False
        self.device.close_device()

    def this_app(self):
        """
        Simple about))) no more.
        """
        msgbox = qt.QMessageBox()
        msgbox.setText("This is a simple cross-platform application for the usbadc10 device.\nVersion 1.0.0\n" +
                       "Copyright © 2020 Nikita Presnov\npresnovnikita@yandex.ru")
        msgbox.exec_()

    def period_chanded(self):
        """
        If you chaged period.
        """
        self.timer_period = 1000*(self.comboBox_period_val.currentData())
        if self.start_stop_status:
            self.timer.start(self.timer_period)
            self.y = np.zeros((1000, 10))
            self.data_to_scv = np.empty((0, 10))
            self.x = np.linspace(-self.timer_period, 0, 1000)
        else:
            self.timer.stop()

    def timer_handler(self):
        """
        Reading data.
        """
        try:
            data = self.device.get_conversion()
            self.x = self.x + self.timer_period/1000
            for i in range(10):
                self.y[:, i] = np.roll(self.y[:, i], -1, axis=0)
                self.y[-1, i] = data.data[i] / 10000
                if self.gstates[i]:
                    self.linias[i].setData(self.x, self.y[:, i])
            if self.start_stop_recording_status:
                self.data_to_scv = np.vstack((self.data_to_scv, self.y[-1, :]))
        except urpcadc.UrpcDeviceUndefinedError:
            self.timer.stop()
            self.start_stop_recording.setEnabled(False)
            self.start_stop_recording_status = False
            self.start_stop_status = False
            self.start_stop_recording.setStyleSheet('background: rgb(238,238,238);')
            self.save_button.setEnabled(True)
            self.actionSave.setEnabled(True)
            msgbox = qt.QMessageBox()
            msgbox.setText("Connection lost")
            msgbox.exec_()

    def start_stop_handler(self):
        """
        Start or stop getting data.
        """
        self.start_stop_status = not (self.start_stop_status)
        if self.start_stop_status:
            self.start_stop_recording.setEnabled(True)
            self.actionStart_stop_recording.setEnabled(True)
        else:
            self.start_stop_recording.setEnabled(False)
            self.actionStart_stop_recording.setEnabled(False)
            self.start_stop_recording_status = False
            self.start_stop_recording.setStyleSheet('background: rgb(238,238,238);')
            self.save_button.setEnabled(True)
            self.actionSave.setEnabled(True)
        self.period_chanded()

    def start_stop_recording_handler(self):
        """
        Start or stop recording data.
        In fact, it only cange flag value.
        """
        self.start_stop_recording_status = not (self.start_stop_recording_status)
        if self.start_stop_recording_status:
            self.start_stop_recording.setStyleSheet('background: rgb(0,170,0);')
            self.save_button.setEnabled(False)
            self.actionSave.setEnabled(False)
        else:
            self.start_stop_recording.setStyleSheet('background: rgb(238,238,238);')
            self.save_button.setEnabled(True)
            self.actionSave.setEnabled(True)

    def save_handler(self):
        """
        Save data from data_to_scv.
        Of course, I can do it from graph, but here you can get more than 1000 values.
        """
        FILENAME = qt.QFileDialog.getSaveFileName(None,
                                                  'Save File',
                                                  "output.csv",
                                                  filter="CSV Files (*.csv)",
                                                  options=qt.QFileDialog.DontUseNativeDialog)
        try:
            with open(FILENAME[0], "w", newline="") as file:
                writer = csv.writer(file, delimiter='\t')
                adcs = []
                for i in range(10):
                    adcs.append("ADC"+str(i+1))
                writer.writerow(adcs)
                writer.writerows(self.data_to_scv)
            self.data_to_scv = np.empty((0, 10))
        except FileNotFoundError:
            msgbox = qt.QMessageBox()
            msgbox.setText("Did not saved")
            msgbox.exec_()

    def replot(self):
        """
        It only clear unselected lines.
        """
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
        """
        Read name)
        """
        self.comboBox_ports.clear()
        ports = serial.tools.list_ports.comports()
        valid_ports = []
        if self.os_kind == "windows":
            for port in sorted(ports):
                try:
                    s = serial.Serial(port.device)
                    s.close()
                    valid_ports.append("com:\\\\.\\" + port.device)
                except (OSError, serial.SerialException):
                    pass
        elif self.os_kind == "darwin":
            print("Unsupported system")
        elif self.os_kind == "freebsd" or "linux" in self.os_kind:
            for port in sorted(ports):
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
        """
        Also read name)
        """
        self.graphWidget.enableAutoRange()

    def timer_monitoring(self):
        """
        Ask the size of data_to_csv to print it.
        """
        self.size_of_data_out.setText(str(sys.getsizeof(self.data_to_scv)/1000)+" Kb")


def fortest():
    hello = "Hello, i am working app)))"
    print(hello)
    return hello


def main():
    app = qt.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = uRPCApp()
    window.show()
    sys.exit(app.exec_())
    window.disconnecton()


if __name__ == '__main__':
    main()
