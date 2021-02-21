from PyQt5 import QtWidgets
import PyQt5.QtCore as qtc
# from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
# from random import randint
import time
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.x = np.arange(100)  # 100 time points
        self.y = np.random.random((100, 10))
        self.graphWidget.setBackground('w')
        self.gcolors = [(0, 0, 255), (0, 170, 0), (255, 0, 0), (0, 0, 0), (255, 85, 0),
                        (0, 170, 255), (0, 255, 0), (255, 170, 255), (111, 111, 111), (170, 85, 0)]
        # 'blue', 'green', 'red', 'black', 'orange', 'lightblue', 'lightgreen', 'pink',  'grey', 'brown'
        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Volage, V', **styles)
        self.graphWidget.setLabel('bottom', 'Time', **styles)
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setYRange(0, 100, padding=0)
        self.linias = []
        for i in range(10):
            self.linias.append(self.graphWidget.plot(self.x,
                                                     self.y[:, i],
                                                     pen=pg.mkPen(color=self.gcolors[i],
                                                                  width=2)))

        self.timer_monitor = qtc.QTimer(self)
        self.timer_monitor.setSingleShot(False)
        self.timer_monitor.timeout.connect(self.plotgraph)
        self.timer_monitor.start(100)
        self.systimer = time.time()
        self.time_now = 0

    def plotgraph(self):
        # print("start")
        fordelta = self.time_now
        self.time_now = time.time() - self.systimer
        # self.x = np.append(self.x[1:], self.time_now)
        # self.y = np.vstack((self.y[1:], [randint(0, 100) for i in range(10)]))
        for i in range(10):
            self.linias[i].setData(self.x, self.y[:, i])
        # self.linias1.appendData
        # self.graphWidget.se
        print(self.time_now - fordelta)
        # self.timer_monitor.stop()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
