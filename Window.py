# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui_Window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_7 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_7.setObjectName("formLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab)
        self.formLayout_3.setObjectName("formLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 61))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_11.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_7.addWidget(self.lineEdit_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_7.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = PlotWidget(self.groupBox)
        self.graphicsView.setMinimumSize(QtCore.QSize(620, 439))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 2, 1)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout_6 = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout_6.setObjectName("formLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setMinimumSize(QtCore.QSize(91, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_14.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.horizontalLayout_8.addLayout(self.formLayout_4)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_15.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_16.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
        self.horizontalLayout_8.addLayout(self.formLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 2)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem9)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.groupBox1 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox1)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_8.addWidget(self.lineEdit_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox1)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_8.addWidget(self.lineEdit_6)
        self.label_10 = QtWidgets.QLabel(self.groupBox1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView_2 = PlotWidget(self.groupBox1)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(620, 439))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_3.addWidget(self.graphicsView_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox1)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.label_11 = QtWidgets.QLabel(self.groupBox1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.label_12 = QtWidgets.QLabel(self.groupBox1)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox1)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(91, 16777215))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9.addWidget(self.groupBox1)
        self.formLayout_6.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Open/open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Save/save_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionStop = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Stop/stop_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon2)
        self.actionStop.setObjectName("actionStop")
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionStop)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start \n"
" Continous Update"))
        self.pushButton_2.setText(_translate("MainWindow", "step left"))
        self.pushButton_3.setText(_translate("MainWindow", "step right"))
        self.label.setText(_translate("MainWindow", "step size (um)"))
        self.label_2.setText(_translate("MainWindow", "step size (fs)"))
        self.pushButton_4.setText(_translate("MainWindow", "home the stage"))
        self.pushButton_5.setText(_translate("MainWindow", "move to position"))
        self.label_3.setText(_translate("MainWindow", "position (um)"))
        self.label_4.setText(_translate("MainWindow", "position (fs)"))
        self.label_5.setText(_translate("MainWindow", "y max"))
        self.label_6.setText(_translate("MainWindow", "y min"))
        self.label_8.setText(_translate("MainWindow", "x min"))
        self.label_7.setText(_translate("MainWindow", "x max"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Spectrum Continuous Update"))
        self.pushButton_6.setText(_translate("MainWindow", "Collect \n"
" Spectrogram"))
        self.label_13.setText(_translate("MainWindow", "start (um)"))
        self.label_14.setText(_translate("MainWindow", "start (fs)"))
        self.label_15.setText(_translate("MainWindow", "end(um)"))
        self.label_16.setText(_translate("MainWindow", "end(fs)"))
        self.label_9.setText(_translate("MainWindow", "y max"))
        self.label_10.setText(_translate("MainWindow", "y min"))
        self.label_11.setText(_translate("MainWindow", "x min"))
        self.label_12.setText(_translate("MainWindow", "x max"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Spectrogram"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Integration Time"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Settings"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Upper Limit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lower Limit"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Units"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "ms"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Spectrometer and Stage Settings"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
from PlottingFunctions import PlotWidget
import QRC_file_rc
