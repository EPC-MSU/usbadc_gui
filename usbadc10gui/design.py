"""
This module is only responsible for the type of GUI.
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usbadc10gui/design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qwt import QwtPlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_1_blue = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_1_blue.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        self.b_1_blue.setFont(font)
        self.b_1_blue.setChecked(True)
        self.b_1_blue.setObjectName("b_1_blue")
        self.verticalLayout.addWidget(self.b_1_blue)
        self.b_2_green = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_2_green.setPalette(palette)
        self.b_2_green.setChecked(True)
        self.b_2_green.setObjectName("b_2_green")
        self.verticalLayout.addWidget(self.b_2_green)
        self.b_3_red = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_3_red.setPalette(palette)
        self.b_3_red.setChecked(True)
        self.b_3_red.setObjectName("b_3_red")
        self.verticalLayout.addWidget(self.b_3_red)
        self.b_4_black = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_4_black.setPalette(palette)
        self.b_4_black.setChecked(True)
        self.b_4_black.setObjectName("b_4_black")
        self.verticalLayout.addWidget(self.b_4_black)
        self.b_5_orange = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_5_orange.setPalette(palette)
        self.b_5_orange.setChecked(True)
        self.b_5_orange.setTristate(False)
        self.b_5_orange.setObjectName("b_5_orange")
        self.verticalLayout.addWidget(self.b_5_orange)
        self.b_6_blue_light = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_6_blue_light.setPalette(palette)
        self.b_6_blue_light.setChecked(True)
        self.b_6_blue_light.setObjectName("b_6_blue_light")
        self.verticalLayout.addWidget(self.b_6_blue_light)
        self.b_7_green_light = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_7_green_light.sizePolicy().hasHeightForWidth())
        self.b_7_green_light.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_7_green_light.setPalette(palette)
        self.b_7_green_light.setChecked(True)
        self.b_7_green_light.setObjectName("b_7_green_light")
        self.verticalLayout.addWidget(self.b_7_green_light)
        self.b_8_pig = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_8_pig.setPalette(palette)
        self.b_8_pig.setChecked(True)
        self.b_8_pig.setObjectName("b_8_pig")
        self.verticalLayout.addWidget(self.b_8_pig)
        self.b_9_gray = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_9_gray.setPalette(palette)
        self.b_9_gray.setChecked(True)
        self.b_9_gray.setObjectName("b_9_gray")
        self.verticalLayout.addWidget(self.b_9_gray)
        self.b_10_brown = QtWidgets.QCheckBox(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.b_10_brown.setPalette(palette)
        self.b_10_brown.setChecked(True)
        self.b_10_brown.setObjectName("b_10_brown")
        self.verticalLayout.addWidget(self.b_10_brown)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.graphWidget = QwtPlot(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayout_4.addWidget(self.graphWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start_stop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_stop.sizePolicy().hasHeightForWidth())
        self.start_stop.setSizePolicy(sizePolicy)
        self.start_stop.setObjectName("start_stop")
        self.verticalLayout_2.addWidget(self.start_stop)
        self.start_stop_recording = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop_recording.setObjectName("start_stop_recording")
        self.verticalLayout_2.addWidget(self.start_stop_recording)
        self.size_of_data_txt = QtWidgets.QLabel(self.centralwidget)
        self.size_of_data_txt.setObjectName("size_of_data_txt")
        self.verticalLayout_2.addWidget(self.size_of_data_txt)
        self.size_of_data_out = QtWidgets.QLabel(self.centralwidget)
        self.size_of_data_out.setText("")
        self.size_of_data_out.setObjectName("size_of_data_out")
        self.verticalLayout_2.addWidget(self.size_of_data_out)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_2.addWidget(self.save_button)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.device_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_label.sizePolicy().hasHeightForWidth())
        self.device_label.setSizePolicy(sizePolicy)
        self.device_label.setObjectName("device_label")
        self.verticalLayout_2.addWidget(self.device_label)
        self.comboBox_ports = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ports.setEditable(True)
        self.comboBox_ports.setObjectName("comboBox_ports")
        self.verticalLayout_2.addWidget(self.comboBox_ports)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout_3.addWidget(self.connect_button)
        self.disconnect_button = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_button.setObjectName("disconnect_button")
        self.horizontalLayout_3.addWidget(self.disconnect_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.rescan_botton = QtWidgets.QPushButton(self.centralwidget)
        self.rescan_botton.setObjectName("rescan_botton")
        self.verticalLayout_2.addWidget(self.rescan_botton)
        self.period = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.period.sizePolicy().hasHeightForWidth())
        self.period.setSizePolicy(sizePolicy)
        self.period.setObjectName("period")
        self.verticalLayout_2.addWidget(self.period)
        self.comboBox_period_val = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_period_val.sizePolicy().hasHeightForWidth())
        self.comboBox_period_val.setSizePolicy(sizePolicy)
        self.comboBox_period_val.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.comboBox_period_val.setEditable(False)
        self.comboBox_period_val.setMaxVisibleItems(10)
        self.comboBox_period_val.setObjectName("comboBox_period_val")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.comboBox_period_val.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_period_val)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1224, 29))
        self.menuBar.setObjectName("menuBar")
        self.menuFILE = QtWidgets.QMenu(self.menuBar)
        self.menuFILE.setObjectName("menuFILE")
        self.menuTOOLS = QtWidgets.QMenu(self.menuBar)
        self.menuTOOLS.setObjectName("menuTOOLS")
        self.menuABOUT = QtWidgets.QMenu(self.menuBar)
        self.menuABOUT.setObjectName("menuABOUT")
        self.menuVIEW = QtWidgets.QMenu(self.menuBar)
        self.menuVIEW.setObjectName("menuVIEW")
        self.menuChannels_2 = QtWidgets.QMenu(self.menuVIEW)
        self.menuChannels_2.setObjectName("menuChannels_2")
        MainWindow.setMenuBar(self.menuBar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionStart_Stop_getting_data = QtWidgets.QAction(MainWindow)
        self.actionStart_Stop_getting_data.setObjectName("actionStart_Stop_getting_data")
        self.actionStart_stop_recording = QtWidgets.QAction(MainWindow)
        self.actionStart_stop_recording.setObjectName("actionStart_stop_recording")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOut = QtWidgets.QAction(MainWindow)
        self.actionOut.setObjectName("actionOut")
        self.actionThis_Application = QtWidgets.QAction(MainWindow)
        self.actionThis_Application.setObjectName("actionThis_Application")
        self.action1_Blue = QtWidgets.QAction(MainWindow)
        self.action1_Blue.setCheckable(True)
        self.action1_Blue.setChecked(True)
        self.action1_Blue.setObjectName("action1_Blue")
        self.action2_Green = QtWidgets.QAction(MainWindow)
        self.action2_Green.setCheckable(True)
        self.action2_Green.setChecked(True)
        self.action2_Green.setObjectName("action2_Green")
        self.action3_Red = QtWidgets.QAction(MainWindow)
        self.action3_Red.setCheckable(True)
        self.action3_Red.setChecked(True)
        self.action3_Red.setObjectName("action3_Red")
        self.action4_Black = QtWidgets.QAction(MainWindow)
        self.action4_Black.setCheckable(True)
        self.action4_Black.setChecked(True)
        self.action4_Black.setObjectName("action4_Black")
        self.action5_Orange = QtWidgets.QAction(MainWindow)
        self.action5_Orange.setCheckable(True)
        self.action5_Orange.setChecked(True)
        self.action5_Orange.setObjectName("action5_Orange")
        self.action6_Blue_Light = QtWidgets.QAction(MainWindow)
        self.action6_Blue_Light.setCheckable(True)
        self.action6_Blue_Light.setChecked(True)
        self.action6_Blue_Light.setObjectName("action6_Blue_Light")
        self.action7_Green_Light = QtWidgets.QAction(MainWindow)
        self.action7_Green_Light.setCheckable(True)
        self.action7_Green_Light.setChecked(True)
        self.action7_Green_Light.setObjectName("action7_Green_Light")
        self.action8_Pig = QtWidgets.QAction(MainWindow)
        self.action8_Pig.setCheckable(True)
        self.action8_Pig.setChecked(True)
        self.action8_Pig.setObjectName("action8_Pig")
        self.action9_Gray = QtWidgets.QAction(MainWindow)
        self.action9_Gray.setCheckable(True)
        self.action9_Gray.setChecked(True)
        self.action9_Gray.setObjectName("action9_Gray")
        self.action10_Brown = QtWidgets.QAction(MainWindow)
        self.action10_Brown.setCheckable(True)
        self.action10_Brown.setChecked(True)
        self.action10_Brown.setObjectName("action10_Brown")
        self.actionRescan = QtWidgets.QAction(MainWindow)
        self.actionRescan.setObjectName("actionRescan")
        self.menuFILE.addAction(self.actionSave)
        self.menuFILE.addSeparator()
        self.menuFILE.addAction(self.actionOut)
        self.menuTOOLS.addAction(self.actionConnect)
        self.menuTOOLS.addAction(self.actionDisconnect)
        self.menuTOOLS.addAction(self.actionStart_Stop_getting_data)
        self.menuTOOLS.addAction(self.actionStart_stop_recording)
        self.menuTOOLS.addAction(self.actionRescan)
        self.menuABOUT.addAction(self.actionThis_Application)
        self.menuChannels_2.addAction(self.action1_Blue)
        self.menuChannels_2.addAction(self.action2_Green)
        self.menuChannels_2.addAction(self.action3_Red)
        self.menuChannels_2.addAction(self.action4_Black)
        self.menuChannels_2.addAction(self.action5_Orange)
        self.menuChannels_2.addAction(self.action6_Blue_Light)
        self.menuChannels_2.addAction(self.action7_Green_Light)
        self.menuChannels_2.addAction(self.action8_Pig)
        self.menuChannels_2.addAction(self.action9_Gray)
        self.menuChannels_2.addAction(self.action10_Brown)
        self.menuVIEW.addAction(self.menuChannels_2.menuAction())
        self.menuBar.addAction(self.menuFILE.menuAction())
        self.menuBar.addAction(self.menuVIEW.menuAction())
        self.menuBar.addAction(self.menuTOOLS.menuAction())
        self.menuBar.addAction(self.menuABOUT.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_period_val.setCurrentIndex(5)
        self.actionOut.triggered.connect(MainWindow.close)
        self.action1_Blue.triggered.connect(self.b_1_blue.toggle)
        self.action2_Green.triggered.connect(self.b_2_green.toggle)
        self.action3_Red.triggered.connect(self.b_3_red.toggle)
        self.action4_Black.triggered.connect(self.b_4_black.toggle)
        self.action10_Brown.triggered.connect(self.b_10_brown.toggle)
        self.action9_Gray.triggered.connect(self.b_9_gray.toggle)
        self.action8_Pig.triggered.connect(self.b_8_pig.toggle)
        self.action7_Green_Light.triggered.connect(self.b_7_green_light.toggle)
        self.action6_Blue_Light.triggered.connect(self.b_6_blue_light.toggle)
        self.action5_Orange.triggered.connect(self.b_5_orange.toggle)
        self.actionSave.triggered.connect(self.save_button.click)
        self.actionStart_Stop_getting_data.triggered.connect(self.start_stop.click)
        self.actionStart_stop_recording.triggered.connect(self.start_stop_recording.click)
        self.actionConnect.triggered.connect(self.connect_button.click)
        self.actionDisconnect.triggered.connect(self.disconnect_button.click)
        self.b_1_blue.clicked.connect(self.action1_Blue.toggle)
        self.b_2_green.clicked.connect(self.action2_Green.toggle)
        self.b_3_red.clicked.connect(self.action3_Red.toggle)
        self.b_4_black.clicked.connect(self.action4_Black.toggle)
        self.b_5_orange.clicked.connect(self.action5_Orange.toggle)
        self.b_6_blue_light.clicked.connect(self.action6_Blue_Light.toggle)
        self.b_7_green_light.clicked.connect(self.action7_Green_Light.toggle)
        self.b_9_gray.clicked.connect(self.action9_Gray.toggle)
        self.b_10_brown.clicked.connect(self.action10_Brown.toggle)
        self.b_8_pig.clicked.connect(self.action8_Pig.toggle)
        self.actionRescan.triggered.connect(self.rescan_botton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UALab"))
        self.b_1_blue.setText(_translate("MainWindow", "ADC1"))
        self.b_2_green.setText(_translate("MainWindow", "ADC2"))
        self.b_3_red.setText(_translate("MainWindow", "ADC3"))
        self.b_4_black.setText(_translate("MainWindow", "ADC4"))
        self.b_5_orange.setText(_translate("MainWindow", "ADC5"))
        self.b_6_blue_light.setText(_translate("MainWindow", "ADC6"))
        self.b_7_green_light.setText(_translate("MainWindow", "ADC7"))
        self.b_8_pig.setText(_translate("MainWindow", "ADC8"))
        self.b_9_gray.setText(_translate("MainWindow", "ADC9"))
        self.b_10_brown.setText(_translate("MainWindow", "ADC10"))
        self.start_stop.setText(_translate("MainWindow", "Start/Stop getting data"))
        self.start_stop_recording.setText(_translate("MainWindow", "Start/stop recording"))
        self.size_of_data_txt.setText(_translate("MainWindow", "Size of data in RAM"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.device_label.setText(_translate("MainWindow", "Enter device address"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.disconnect_button.setText(_translate("MainWindow", "Disconnect"))
        self.rescan_botton.setText(_translate("MainWindow", "Rescan"))
        self.period.setText(_translate("MainWindow", "Period"))
        self.comboBox_period_val.setCurrentText(_translate("MainWindow", "200 ms"))
        self.comboBox_period_val.setItemText(0, _translate("MainWindow", "<1 ms"))
        self.comboBox_period_val.setItemText(1, _translate("MainWindow", "10 ms"))
        self.comboBox_period_val.setItemText(2, _translate("MainWindow", "20 ms"))
        self.comboBox_period_val.setItemText(3, _translate("MainWindow", "50 ms"))
        self.comboBox_period_val.setItemText(4, _translate("MainWindow", "100 ms"))
        self.comboBox_period_val.setItemText(5, _translate("MainWindow", "200 ms"))
        self.comboBox_period_val.setItemText(6, _translate("MainWindow", "500 ms"))
        self.comboBox_period_val.setItemText(7, _translate("MainWindow", "1 s"))
        self.comboBox_period_val.setItemText(8, _translate("MainWindow", "5 s"))
        self.comboBox_period_val.setItemText(9, _translate("MainWindow", "10 s"))
        self.comboBox_period_val.setItemText(10, _translate("MainWindow", "1 m"))
        self.comboBox_period_val.setItemText(11, _translate("MainWindow", "5 m"))
        self.comboBox_period_val.setItemText(12, _translate("MainWindow", "10 m"))
        self.comboBox_period_val.setItemText(13, _translate("MainWindow", "30 m"))
        self.menuFILE.setTitle(_translate("MainWindow", "File"))
        self.menuTOOLS.setTitle(_translate("MainWindow", "Tools"))
        self.menuABOUT.setTitle(_translate("MainWindow", "About"))
        self.menuVIEW.setTitle(_translate("MainWindow", "View"))
        self.menuChannels_2.setTitle(_translate("MainWindow", "Channels"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionConnect.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionDisconnect.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionStart_Stop_getting_data.setText(_translate("MainWindow", "Start/Stop getting data"))
        self.actionStart_stop_recording.setText(_translate("MainWindow", "Start/stop recording"))
        self.actionStart_stop_recording.setShortcut(_translate("MainWindow", "Space"))
        self.actionSave.setText(_translate("MainWindow", "Save ..."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOut.setText(_translate("MainWindow", "Exit"))
        self.actionOut.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionThis_Application.setText(_translate("MainWindow", "This Application"))
        self.action1_Blue.setText(_translate("MainWindow", "ADC1"))
        self.action1_Blue.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.action2_Green.setText(_translate("MainWindow", "ADC2"))
        self.action2_Green.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.action3_Red.setText(_translate("MainWindow", "ADC3"))
        self.action3_Red.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action4_Black.setText(_translate("MainWindow", "ADC4"))
        self.action4_Black.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.action5_Orange.setText(_translate("MainWindow", "ADC5"))
        self.action5_Orange.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.action6_Blue_Light.setText(_translate("MainWindow", "ADC6"))
        self.action6_Blue_Light.setShortcut(_translate("MainWindow", "Ctrl+6"))
        self.action7_Green_Light.setText(_translate("MainWindow", "ADC7"))
        self.action7_Green_Light.setShortcut(_translate("MainWindow", "Ctrl+7"))
        self.action8_Pig.setText(_translate("MainWindow", "ADC8"))
        self.action8_Pig.setShortcut(_translate("MainWindow", "Ctrl+8"))
        self.action9_Gray.setText(_translate("MainWindow", "ADC9"))
        self.action9_Gray.setShortcut(_translate("MainWindow", "Ctrl+9"))
        self.action10_Brown.setText(_translate("MainWindow", "ADC10"))
        self.action10_Brown.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.actionRescan.setText(_translate("MainWindow", "Rescan"))
        self.actionRescan.setShortcut(_translate("MainWindow", "Ctrl+R"))
