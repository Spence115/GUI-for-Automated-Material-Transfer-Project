# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkOrder.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidget,QTableWidget
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *
from PyQt5.QtCore import *

# Global string used to determine the Work Order of a given delivery
workOrder = ""

CAPS = True
invEntry = False

class Ui_WorkOrder(object):
    def setupUi(self, WorkOrder):
        WorkOrder.setObjectName("WorkOrder")
        WorkOrder.resize(1167, 600)
        self.centralwidget = QtWidgets.QWidget(WorkOrder)
        self.centralwidget.setObjectName("centralwidget")
        self.confirmWOBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmWOBtn.setGeometry(QtCore.QRect(230, 490, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirmWOBtn.setFont(font)
        self.confirmWOBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.confirmWOBtn.setObjectName("confirmWOBtn")
        self.fourBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fourBtn.setGeometry(QtCore.QRect(880, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.fourBtn.setFont(font)
        self.fourBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fourBtn.setObjectName("fourBtn")
        self.fiveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fiveBtn.setGeometry(QtCore.QRect(970, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.fiveBtn.setFont(font)
        self.fiveBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fiveBtn.setObjectName("fiveBtn")
        self.nineBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nineBtn.setGeometry(QtCore.QRect(1060, 260, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nineBtn.setFont(font)
        self.nineBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nineBtn.setObjectName("nineBtn")
        self.workOrderLabel = QtWidgets.QLabel(self.centralwidget)
        self.workOrderLabel.setGeometry(QtCore.QRect(200, 430, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workOrderLabel.setFont(font)
        self.workOrderLabel.setStyleSheet("")
        self.workOrderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.workOrderLabel.setObjectName("workOrderLabel")
        self.eightBtn = QtWidgets.QPushButton(self.centralwidget)
        self.eightBtn.setGeometry(QtCore.QRect(970, 260, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.eightBtn.setFont(font)
        self.eightBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.eightBtn.setObjectName("eightBtn")
        self.threeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.threeBtn.setGeometry(QtCore.QRect(1060, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.threeBtn.setFont(font)
        self.threeBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.threeBtn.setObjectName("threeBtn")
        self.WOLabel = QtWidgets.QLabel(self.centralwidget)
        self.WOLabel.setGeometry(QtCore.QRect(220, 20, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.WOLabel.setFont(font)
        self.WOLabel.setStyleSheet("")
        self.WOLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WOLabel.setObjectName("WOLabel")
        self.sevenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sevenBtn.setGeometry(QtCore.QRect(880, 260, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.sevenBtn.setFont(font)
        self.sevenBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sevenBtn.setObjectName("sevenBtn")
        self.zeroBtn = QtWidgets.QPushButton(self.centralwidget)
        self.zeroBtn.setGeometry(QtCore.QRect(1060, 340, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.zeroBtn.setFont(font)
        self.zeroBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.zeroBtn.setObjectName("zeroBtn")
        self.clearWorkOrderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearWorkOrderBtn.setGeometry(QtCore.QRect(880, 340, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.clearWorkOrderBtn.setFont(font)
        self.clearWorkOrderBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.clearWorkOrderBtn.setObjectName("clearWorkOrderBtn")
        self.oneBtn = QtWidgets.QPushButton(self.centralwidget)
        self.oneBtn.setGeometry(QtCore.QRect(880, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.oneBtn.setFont(font)
        self.oneBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.oneBtn.setObjectName("oneBtn")
        self.twoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.twoBtn.setGeometry(QtCore.QRect(970, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.twoBtn.setFont(font)
        self.twoBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.twoBtn.setObjectName("twoBtn")
        self.sixBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sixBtn.setGeometry(QtCore.QRect(1060, 180, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.sixBtn.setFont(font)
        self.sixBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sixBtn.setObjectName("sixBtn")
        self.wBtn = QtWidgets.QPushButton(self.centralwidget)
        self.wBtn.setGeometry(QtCore.QRect(130, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.wBtn.setFont(font)
        self.wBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.wBtn.setObjectName("wBtn")
        self.pBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pBtn.setGeometry(QtCore.QRect(770, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pBtn.setFont(font)
        self.pBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pBtn.setObjectName("pBtn")
        self.qBtn = QtWidgets.QPushButton(self.centralwidget)
        self.qBtn.setGeometry(QtCore.QRect(50, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.qBtn.setFont(font)
        self.qBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.qBtn.setObjectName("qBtn")
        self.eBtn = QtWidgets.QPushButton(self.centralwidget)
        self.eBtn.setGeometry(QtCore.QRect(210, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.eBtn.setFont(font)
        self.eBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.eBtn.setObjectName("eBtn")
        self.tBtn = QtWidgets.QPushButton(self.centralwidget)
        self.tBtn.setGeometry(QtCore.QRect(370, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.tBtn.setFont(font)
        self.tBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tBtn.setObjectName("tBtn")
        self.yBtn = QtWidgets.QPushButton(self.centralwidget)
        self.yBtn.setGeometry(QtCore.QRect(450, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.yBtn.setFont(font)
        self.yBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.yBtn.setObjectName("yBtn")
        self.rBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rBtn.setGeometry(QtCore.QRect(290, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rBtn.setFont(font)
        self.rBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.rBtn.setObjectName("rBtn")
        self.iBtn = QtWidgets.QPushButton(self.centralwidget)
        self.iBtn.setGeometry(QtCore.QRect(610, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.iBtn.setFont(font)
        self.iBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.iBtn.setObjectName("iBtn")
        self.oBtn = QtWidgets.QPushButton(self.centralwidget)
        self.oBtn.setGeometry(QtCore.QRect(690, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.oBtn.setFont(font)
        self.oBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.oBtn.setObjectName("oBtn")
        self.uBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uBtn.setGeometry(QtCore.QRect(530, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.uBtn.setFont(font)
        self.uBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.uBtn.setObjectName("uBtn")
        self.aBtn = QtWidgets.QPushButton(self.centralwidget)
        self.aBtn.setGeometry(QtCore.QRect(100, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.aBtn.setFont(font)
        self.aBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.aBtn.setObjectName("aBtn")
        self.sBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sBtn.setGeometry(QtCore.QRect(180, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.sBtn.setFont(font)
        self.sBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sBtn.setObjectName("sBtn")
        self.lBtn = QtWidgets.QPushButton(self.centralwidget)
        self.lBtn.setGeometry(QtCore.QRect(740, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lBtn.setFont(font)
        self.lBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lBtn.setObjectName("lBtn")
        self.jBtn = QtWidgets.QPushButton(self.centralwidget)
        self.jBtn.setGeometry(QtCore.QRect(580, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.jBtn.setFont(font)
        self.jBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.jBtn.setObjectName("jBtn")
        self.hBtn = QtWidgets.QPushButton(self.centralwidget)
        self.hBtn.setGeometry(QtCore.QRect(500, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.hBtn.setFont(font)
        self.hBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.hBtn.setObjectName("hBtn")
        self.fBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fBtn.setGeometry(QtCore.QRect(340, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.fBtn.setFont(font)
        self.fBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fBtn.setObjectName("fBtn")
        self.dBtn = QtWidgets.QPushButton(self.centralwidget)
        self.dBtn.setGeometry(QtCore.QRect(260, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.dBtn.setFont(font)
        self.dBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dBtn.setObjectName("dBtn")
        self.kBtn = QtWidgets.QPushButton(self.centralwidget)
        self.kBtn.setGeometry(QtCore.QRect(660, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.kBtn.setFont(font)
        self.kBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.kBtn.setObjectName("kBtn")
        self.gBtn = QtWidgets.QPushButton(self.centralwidget)
        self.gBtn.setGeometry(QtCore.QRect(420, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.gBtn.setFont(font)
        self.gBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.gBtn.setObjectName("gBtn")
        self.vBtn = QtWidgets.QPushButton(self.centralwidget)
        self.vBtn.setGeometry(QtCore.QRect(470, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.vBtn.setFont(font)
        self.vBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.vBtn.setObjectName("vBtn")
        self.nBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nBtn.setGeometry(QtCore.QRect(630, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nBtn.setFont(font)
        self.nBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nBtn.setObjectName("nBtn")
        self.cBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cBtn.setGeometry(QtCore.QRect(390, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.cBtn.setFont(font)
        self.cBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cBtn.setObjectName("cBtn")
        self.mBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mBtn.setGeometry(QtCore.QRect(710, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.mBtn.setFont(font)
        self.mBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mBtn.setObjectName("mBtn")
        self.zBtn = QtWidgets.QPushButton(self.centralwidget)
        self.zBtn.setGeometry(QtCore.QRect(230, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.zBtn.setFont(font)
        self.zBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.zBtn.setObjectName("zBtn")
        self.bBtn = QtWidgets.QPushButton(self.centralwidget)
        self.bBtn.setGeometry(QtCore.QRect(550, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.bBtn.setFont(font)
        self.bBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bBtn.setObjectName("bBtn")
        self.xBtn = QtWidgets.QPushButton(self.centralwidget)
        self.xBtn.setGeometry(QtCore.QRect(310, 290, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.xBtn.setFont(font)
        self.xBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.xBtn.setObjectName("xBtn")
        self.capsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.capsBtn.setGeometry(QtCore.QRect(40, 290, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.capsBtn.setFont(font)
        self.capsBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.capsBtn.setObjectName("capsBtn")
        WorkOrder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WorkOrder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1167, 26))
        self.menubar.setObjectName("menubar")
        WorkOrder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WorkOrder)
        self.statusbar.setObjectName("statusbar")
        WorkOrder.setStatusBar(self.statusbar)

        self.retranslateUi(WorkOrder)
        QtCore.QMetaObject.connectSlotsByName(WorkOrder)

    # Button triggers here

        self.zeroBtn.clicked.connect(lambda: self.clicked("Zero"))
        self.oneBtn.clicked.connect(lambda: self.clicked("One"))
        self.twoBtn.clicked.connect(lambda: self.clicked("Two"))
        self.threeBtn.clicked.connect(lambda: self.clicked("Three"))
        self.fourBtn.clicked.connect(lambda: self.clicked("Four"))
        self.fiveBtn.clicked.connect(lambda: self.clicked("Five"))
        self.sixBtn.clicked.connect(lambda: self.clicked("Six"))
        self.sevenBtn.clicked.connect(lambda: self.clicked("Seven"))
        self.eightBtn.clicked.connect(lambda: self.clicked("Eight"))
        self.nineBtn.clicked.connect(lambda: self.clicked("Nine"))

        self.aBtn.clicked.connect(lambda: self.clicked("a"))
        self.bBtn.clicked.connect(lambda: self.clicked("b"))
        self.cBtn.clicked.connect(lambda: self.clicked("c"))
        self.dBtn.clicked.connect(lambda: self.clicked("d"))
        self.eBtn.clicked.connect(lambda: self.clicked("e"))
        self.fBtn.clicked.connect(lambda: self.clicked("f"))
        self.gBtn.clicked.connect(lambda: self.clicked("g"))
        self.hBtn.clicked.connect(lambda: self.clicked("h"))
        self.iBtn.clicked.connect(lambda: self.clicked("i"))
        self.jBtn.clicked.connect(lambda: self.clicked("j"))
        self.kBtn.clicked.connect(lambda: self.clicked("k"))
        self.lBtn.clicked.connect(lambda: self.clicked("l"))
        self.mBtn.clicked.connect(lambda: self.clicked("m"))
        self.nBtn.clicked.connect(lambda: self.clicked("n"))
        self.oBtn.clicked.connect(lambda: self.clicked("o"))
        self.pBtn.clicked.connect(lambda: self.clicked("p"))
        self.qBtn.clicked.connect(lambda: self.clicked("q"))
        self.rBtn.clicked.connect(lambda: self.clicked("r"))
        self.sBtn.clicked.connect(lambda: self.clicked("s"))
        self.tBtn.clicked.connect(lambda: self.clicked("t"))
        self.uBtn.clicked.connect(lambda: self.clicked("u"))
        self.vBtn.clicked.connect(lambda: self.clicked("v"))
        self.wBtn.clicked.connect(lambda: self.clicked("w"))
        self.xBtn.clicked.connect(lambda: self.clicked("x"))
        self.yBtn.clicked.connect(lambda: self.clicked("y"))
        self.zBtn.clicked.connect(lambda: self.clicked("z"))

        self.capsBtn.clicked.connect(lambda: self.clicked("Toggle CAPS"))

        self.clearWorkOrderBtn.clicked.connect(lambda: self.clicked("Clear"))

        self.confirmWOBtn.clicked.connect(lambda: self.clicked("Confirm"))

    # end button triggers

    def retranslateUi(self, WorkOrder):
        _translate = QtCore.QCoreApplication.translate
        WorkOrder.setWindowTitle(_translate("WorkOrder", "MainWindow"))
        self.confirmWOBtn.setText(_translate("WorkOrder", "Confirm Work Order"))
        self.fourBtn.setText(_translate("WorkOrder", "4"))
        self.fiveBtn.setText(_translate("WorkOrder", "5"))
        self.nineBtn.setText(_translate("WorkOrder", "9"))
        self.workOrderLabel.setText(_translate("WorkOrder", "Work Order:"))
        self.eightBtn.setText(_translate("WorkOrder", "8"))
        self.threeBtn.setText(_translate("WorkOrder", "3"))
        self.WOLabel.setText(_translate("WorkOrder", "Please enter the Work Order below"))
        self.sevenBtn.setText(_translate("WorkOrder", "7"))
        self.zeroBtn.setText(_translate("WorkOrder", "0"))
        self.clearWorkOrderBtn.setText(_translate("WorkOrder", "Clear"))
        self.oneBtn.setText(_translate("WorkOrder", "1"))
        self.twoBtn.setText(_translate("WorkOrder", "2"))
        self.sixBtn.setText(_translate("WorkOrder", "6"))
        self.wBtn.setText(_translate("WorkOrder", "W"))
        self.pBtn.setText(_translate("WorkOrder", "P"))
        self.qBtn.setText(_translate("WorkOrder", "Q"))
        self.eBtn.setText(_translate("WorkOrder", "E"))
        self.tBtn.setText(_translate("WorkOrder", "T"))
        self.yBtn.setText(_translate("WorkOrder", "Y"))
        self.rBtn.setText(_translate("WorkOrder", "R"))
        self.iBtn.setText(_translate("WorkOrder", "I"))
        self.oBtn.setText(_translate("WorkOrder", "O"))
        self.uBtn.setText(_translate("WorkOrder", "U"))
        self.aBtn.setText(_translate("WorkOrder", "A"))
        self.sBtn.setText(_translate("WorkOrder", "S"))
        self.lBtn.setText(_translate("WorkOrder", "L"))
        self.jBtn.setText(_translate("WorkOrder", "J"))
        self.hBtn.setText(_translate("WorkOrder", "H"))
        self.fBtn.setText(_translate("WorkOrder", "F"))
        self.dBtn.setText(_translate("WorkOrder", "D"))
        self.kBtn.setText(_translate("WorkOrder", "K"))
        self.gBtn.setText(_translate("WorkOrder", "G"))
        self.vBtn.setText(_translate("WorkOrder", "V"))
        self.nBtn.setText(_translate("WorkOrder", "N"))
        self.cBtn.setText(_translate("WorkOrder", "C"))
        self.mBtn.setText(_translate("WorkOrder", "M"))
        self.zBtn.setText(_translate("WorkOrder", "Z"))
        self.bBtn.setText(_translate("WorkOrder", "B"))
        self.xBtn.setText(_translate("WorkOrder", "X"))
        self.capsBtn.setText(_translate("WorkOrder", "CAPS: On"))

    def clicked(self, text):
        global workOrder
        global CAPS

        invEntry = False

        if text == "Zero":
            workOrder = workOrder + "0"
        if text == "One":
            workOrder = workOrder + "1"
        if text == "Two":
            workOrder = workOrder + "2"
        if text == "Three":
            workOrder = workOrder + "3"
        if text == "Four":
            workOrder = workOrder + "4"
        if text == "Five":
            workOrder = workOrder + "5"
        if text == "Six":
            workOrder = workOrder + "6"
        if text == "Seven":
            workOrder = workOrder + "7"
        if text == "Eight":
            workOrder = workOrder + "8"
        if text == "Nine":
            workOrder = workOrder + "9"
        
        if CAPS == True:
            if text == "a":
                workOrder = workOrder + "A"
            if text == "b":
                workOrder = workOrder + "B"
            if text == "c":
                workOrder = workOrder + "C"
            if text == "d":
                workOrder = workOrder + "D"
            if text == "e":
                workOrder = workOrder + "E"
            if text == "f":
                workOrder = workOrder + "F"
            if text == "g":
                workOrder = workOrder + "G"
            if text == "h":
                workOrder = workOrder + "H"
            if text == "i":
                workOrder = workOrder + "I"
            if text == "j":
                workOrder = workOrder + "J"
            if text == "k":
                workOrder = workOrder + "K"
            if text == "l":
                workOrder = workOrder + "L"
            if text == "m":
                workOrder = workOrder + "M"
            if text == "n":
                workOrder = workOrder + "N"
            if text == "o":
                workOrder = workOrder + "O"
            if text == "p":
                workOrder = workOrder + "P"
            if text == "q":
                workOrder = workOrder + "Q"
            if text == "r":
                workOrder = workOrder + "R"
            if text == "s":
                workOrder = workOrder + "S"
            if text == "t":
                workOrder = workOrder + "T"
            if text == "u":
                workOrder = workOrder + "U"
            if text == "v":
                workOrder = workOrder + "V"
            if text == "w":
                workOrder = workOrder + "W"
            if text == "x":
                workOrder = workOrder + "X"
            if text == "y":
                workOrder = workOrder + "Y"
            if text == "z":
                workOrder = workOrder + "Z"

        elif CAPS == False:
            if text == "a":
                workOrder = workOrder + "a"
            if text == "b":
                workOrder = workOrder + "b"
            if text == "c":
                workOrder = workOrder + "c"
            if text == "d":
                workOrder = workOrder + "d"
            if text == "e":
                workOrder = workOrder + "e"
            if text == "f":
                workOrder = workOrder + "f"
            if text == "g":
                workOrder = workOrder + "g"
            if text == "h":
                workOrder = workOrder + "h"
            if text == "i":
                workOrder = workOrder + "i"
            if text == "j":
                workOrder = workOrder + "j"
            if text == "k":
                workOrder = workOrder + "k"
            if text == "l":
                workOrder = workOrder + "l"
            if text == "m":
                workOrder = workOrder + "m"
            if text == "n":
                workOrder = workOrder + "n"
            if text == "o":
                workOrder = workOrder + "o"
            if text == "p":
                workOrder = workOrder + "p"
            if text == "q":
                workOrder = workOrder + "q"
            if text == "r":
                workOrder = workOrder + "r"
            if text == "s":
                workOrder = workOrder + "s"
            if text == "t":
                workOrder = workOrder + "t"
            if text == "u":
                workOrder = workOrder + "u"
            if text == "v":
                workOrder = workOrder + "v"
            if text == "w":
                workOrder = workOrder + "w"
            if text == "x":
                workOrder = workOrder + "x"
            if text == "y":
                workOrder = workOrder + "y"
            if text == "z":
                workOrder = workOrder + "z"

        if text == "Toggle CAPS":
            if CAPS == True:
                CAPS = False
                self.capsBtn.setText("CAPS: Off")
                self.aBtn.setText("a")
                self.bBtn.setText("b")
                self.cBtn.setText("c")
                self.dBtn.setText("d")
                self.eBtn.setText("e")
                self.fBtn.setText("f")
                self.gBtn.setText("g")
                self.hBtn.setText("h")
                self.iBtn.setText("i")
                self.jBtn.setText("j")
                self.kBtn.setText("k")
                self.lBtn.setText("l")
                self.mBtn.setText("m")
                self.nBtn.setText("n")
                self.oBtn.setText("o")
                self.pBtn.setText("p")
                self.qBtn.setText("q")
                self.rBtn.setText("r")
                self.sBtn.setText("s")
                self.tBtn.setText("t")
                self.uBtn.setText("u")
                self.vBtn.setText("v")
                self.wBtn.setText("w")
                self.xBtn.setText("x")
                self.yBtn.setText("y")
                self.zBtn.setText("z")

            elif CAPS == False:
                CAPS = True
                self.capsBtn.setText("CAPS: On")   
                self.aBtn.setText("A")
                self.bBtn.setText("B")
                self.cBtn.setText("C")
                self.dBtn.setText("D")
                self.eBtn.setText("E")
                self.fBtn.setText("F")
                self.gBtn.setText("G")
                self.hBtn.setText("H")
                self.iBtn.setText("I")
                self.jBtn.setText("J")
                self.kBtn.setText("K")
                self.lBtn.setText("L")
                self.mBtn.setText("M")
                self.nBtn.setText("N")
                self.oBtn.setText("O")
                self.pBtn.setText("P")
                self.qBtn.setText("Q")
                self.rBtn.setText("R")
                self.sBtn.setText("S")
                self.tBtn.setText("T")
                self.uBtn.setText("U")
                self.vBtn.setText("V")
                self.wBtn.setText("W")
                self.xBtn.setText("X")
                self.yBtn.setText("Y")
                self.zBtn.setText("Z")

        if text == "Clear":
            workOrder = ""

        if text == "Confirm":
            WOLength = len(workOrder)
            if WOLength > 9:
                print("Work order too long! Must be 9 characters.")
                self.workOrderLabel.setText("INVALID: Work order too long! Must be exactly 9 characters.")
                self.workOrderLabel.adjustSize()
                self.workOrderLabel.setAlignment(Qt.AlignCenter)
                invEntry = True
            elif WOLength < 9:
                print("Work order too short! Must be 9 characters.")
                self.workOrderLabel.setText("INVALID: Work order too short! Must be exactly 9 characters.")
                self.workOrderLabel.adjustSize()
                self.workOrderLabel.setAlignment(Qt.AlignCenter)
                invEntry = True
            elif WOLength == 9:
                print("confirming Qty")
                self.insertWO(workOrder)
                self.workOrderLabel.setText("Work Order " + workOrder + " has been submitted.")
                self.workOrderLabel.adjustSize()
                self.workOrderLabel.setAlignment(Qt.AlignCenter)
                invEntry = True

        print(workOrder)

        if invEntry == False:
            self.workOrderLabel.setText("Work Order: " + workOrder)
            self.workOrderLabel.adjustSize()
            self.workOrderLabel.setAlignment(Qt.AlignCenter)

    def insertWO(self,l):
        curRow = self.whichRow()
        
        WOcon = sqlite3.connect("Z:\BPT.db")

        print("connected for insert Qty\n")

        cursor = WOcon.cursor()
                    
        insWO = "UPDATE tasks SET Work_Order ='"+l+"' WHERE row_ID = "+curRow+";"

        cursor.execute(insWO)
        WOcon.commit()
        WOcon.close()

    def whichRow(self):
        con = sqlite3.connect("Z:\BPT.db")
        cellCon = con.cursor()

        cellCon.execute('SELECT Current_Row FROM states')
        data = cellCon.fetchone()
        rw = str(data[0])
        print("Current_Row is:" + str(rw))
        return rw

    def startUp():
        global WOWindow
        app = QtWidgets.QApplication(sys.argv)
        WOWindow = QtWidgets.QMainWindow()
        ui = Ui_WorkOrder()
        ui.setupUi(WOWindow)
        WOWindow.show()
        sys.exit(app.exec_())

class SQL_Table(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delivery Request Window")
        self.resize(1200, 200)
        # Set up the model
        self.model = QSqlTableModel(self)
        self.model.setTable("tasks")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "Work_Order")
        self.model.setHeaderData(1, Qt.Horizontal, "QTY")
        self.model.setHeaderData(2, Qt.Horizontal, "Pickup_Location")
        self.model.setHeaderData(3, Qt.Horizontal, "Delivery_Location")
        self.model.select()
        # Set up the view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)

    # Creates the GUI's connection to the SQLite database on the Raspberry Pi
    def createConnection():
        con = QSqlDatabase.addDatabase("QSQLITE")
        # Sets the file path of the SQL Database file
        # **Note**: Change this to the path of your SQL database located on your local network drive
        con.setDatabaseName("Z:\BPT.db")
        if not con.open():
            # Returns the following message if program fails to connect to database
            QMessageBox.critical(
                None,
                "QTableView Example - Error!",
                "Database Error: %s" % con.lastError().databaseText(),
            )
            return False
        return True

if __name__ == "__main__":
    import sys
    Ui_WorkOrder.startUp()

if not SQL_Table.createConnection():
    sys.exit(1)
DB_win = SQL_Table()
