# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\MainWindow/MainWindow.ui'
#
# Created: Tue Jan 14 22:48:47 2014
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
"    border-style:            None;\n"
"}\n"
"\n"
"/* Barre de boutons */\n"
"QFrame#frameButtons\n"
"{\n"
"    background-color:    #D4D4D4;\n"
"    border-style:            inset;\n"
"    border-width:            1px;\n"
"    border-color:            #777777;\n"
"}\n"
"\n"
"/* Barre de titre */\n"
"QFrame#frameTitle\n"
"{\n"
"    background-color:    #D4D4D4;\n"
"    border-style:            inset;\n"
"    border-width:            1px;\n"
"    border-color:            #777777;\n"
"}\n"
"\n"
"QFrame#frameTitle > QLabel\n"
"{\n"
"    color:                    #000000;\n"
"    font-weight:        normal;\n"
"    font-style:            italic;\n"
"    font-size:                14pt;\n"
"    font-family:            \"Verdana\";\n"
"}\n"
"\n"
"/* Contenut */\n"
"QFrame#content\n"
"{\n"
"    background-color: qlineargradient(spread:pad,\n"
"                                                            x1:0, y1:0,\n"
"                                                            x3:0, y3:1,\n"
"                                                            stop:0 rgb(227, 227, 227),\n"
"                                                            stop:0.7 rgb(227, 227, 227),\n"
"                                                            stop:1 rgb(210, 210, 210));\n"
"    border-style:            outset;\n"
"    border-width:            1px 0px 0px 1px;\n"
"    border-color:            #FFFFFF;\n"
"}\n"
""))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frameButtons = QtGui.QFrame(MainWindow)
        self.frameButtons.setObjectName(_fromUtf8("frameButtons"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frameButtons)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonBooking = QtGui.QPushButton(self.frameButtons)
        self.buttonBooking.setMinimumSize(QtCore.QSize(96, 96))
        self.buttonBooking.setMaximumSize(QtCore.QSize(96, 96))
        self.buttonBooking.setObjectName(_fromUtf8("buttonBooking"))
        self.verticalLayout.addWidget(self.buttonBooking)
        self.buttonClients = QtGui.QPushButton(self.frameButtons)
        self.buttonClients.setMinimumSize(QtCore.QSize(96, 96))
        self.buttonClients.setMaximumSize(QtCore.QSize(96, 96))
        self.buttonClients.setObjectName(_fromUtf8("buttonClients"))
        self.verticalLayout.addWidget(self.buttonClients)
        self.buttonBills = QtGui.QPushButton(self.frameButtons)
        self.buttonBills.setMinimumSize(QtCore.QSize(96, 96))
        self.buttonBills.setMaximumSize(QtCore.QSize(96, 96))
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
        self.content = QtGui.QStackedWidget(self.frameContent)
        self.content.setObjectName(_fromUtf8("content"))
        self.clientList = ClientList()
        self.clientList.setObjectName(_fromUtf8("clientList"))
        self.content.addWidget(self.clientList)
        self.bookingList = BookingList()
        self.bookingList.setObjectName(_fromUtf8("bookingList"))
        self.content.addWidget(self.bookingList)
        self.billList = QtGui.QFrame()
        self.billList.setObjectName(_fromUtf8("billList"))
        self.content.addWidget(self.billList)
        self.verticalLayout_2.addWidget(self.content)
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
