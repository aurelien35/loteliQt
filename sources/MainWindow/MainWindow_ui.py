# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\MainWindow/MainWindow.ui'
#
# Created: Sun Jan 12 15:41:50 2014
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(804, 632)
        MainWindow.setStyleSheet(_fromUtf8("/* Fenetre principale */\n"
"QFrame#MainWindow\n"
"{\n"
"    background-color:    #C4D1EC;\n"
"    border-style:            solid;\n"
"    border-color:            #000000;\n"
"    border-width:            2px;\n"
"}\n"
"\n"
"/* Barre de boutons */\n"
"QFrame#frameButtons\n"
"{\n"
"    background-color:    #535353;\n"
"    border-style:            solid;\n"
"    border-color:            #000000;\n"
"    border-width:            0px 2px 0px 0px;\n"
"}\n"
"\n"
"/* Barre de titre */\n"
"QFrame#frameTitle\n"
"{\n"
"    background-color:    #535353;\n"
"    border-style:            solid;\n"
"    border-width:            0px 0px 2px 0px;\n"
"    border-color:            #000000;\n"
"}\n"
"\n"
"QFrame#frameTitle > QLabel\n"
"{\n"
"    color:                    #FFFFFF;\n"
"    font-weight:        bold;\n"
"    font-style:            italic;\n"
"    font-size:                14pt;\n"
"    font-family:            \"Verdana\";\n"
"}\n"
""))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frameButtons = QtGui.QFrame(MainWindow)
        self.frameButtons.setObjectName(_fromUtf8("frameButtons"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frameButtons)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonBooking = QtGui.QPushButton(self.frameButtons)
        self.buttonBooking.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonBooking.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonBooking.setObjectName(_fromUtf8("buttonBooking"))
        self.verticalLayout.addWidget(self.buttonBooking)
        self.buttonClients = QtGui.QPushButton(self.frameButtons)
        self.buttonClients.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonClients.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonClients.setObjectName(_fromUtf8("buttonClients"))
        self.verticalLayout.addWidget(self.buttonClients)
        self.buttonBills = QtGui.QPushButton(self.frameButtons)
        self.buttonBills.setMinimumSize(QtCore.QSize(128, 128))
        self.buttonBills.setMaximumSize(QtCore.QSize(128, 128))
        self.buttonBills.setObjectName(_fromUtf8("buttonBills"))
        self.verticalLayout.addWidget(self.buttonBills)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frameButtons)
        self.frameContent = QtGui.QFrame(MainWindow)
        self.frameContent.setObjectName(_fromUtf8("frameContent"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frameTitle = QtGui.QFrame(self.frameContent)
        self.frameTitle.setObjectName(_fromUtf8("frameTitle"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frameTitle)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelTitle = QtGui.QLabel(self.frameTitle)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.horizontalLayout.addWidget(self.labelTitle)
        self.verticalLayout_2.addWidget(self.frameTitle)
        self.stackedWidget = QtGui.QStackedWidget(self.frameContent)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.clientList = ClientList()
        self.clientList.setObjectName(_fromUtf8("clientList"))
        self.stackedWidget.addWidget(self.clientList)
        self.bookingList = BookingList()
        self.bookingList.setObjectName(_fromUtf8("bookingList"))
        self.stackedWidget.addWidget(self.bookingList)
        self.billList = QtGui.QFrame()
        self.billList.setObjectName(_fromUtf8("billList"))
        self.stackedWidget.addWidget(self.billList)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frameContent)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.buttonBooking.setText(_translate("MainWindow", "Planning", None))
        self.buttonClients.setText(_translate("MainWindow", "Clients", None))
        self.buttonBills.setText(_translate("MainWindow", "Factures", None))
        self.labelTitle.setText(_translate("MainWindow", "TextLabel", None))

from Booking.BookingList import BookingList
from Client.ClientList import ClientList
import loteliQt_rc
