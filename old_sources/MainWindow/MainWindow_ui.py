# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\MainWindow/MainWindow.ui'
#
# Created: Mon Jan 20 21:34:00 2014
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
        MainWindow.resize(478, 398)
        MainWindow.setStyleSheet(_fromUtf8("QLineEdit, QSpinBox, QDoubleSpinBox\n"
"{\n"
"    color:                        #000000;\n"
"    padding:                    4px;\n"
"    border-style:            inset;\n"
"    border-width:             1px;\n"
"    border-radius:            5px;\n"
"    border-color:            #555555;\n"
"    background-color:    qlineargradient(    spread:pad,\n"
"                                                                x1:0, y1:0,\n"
"                                                                x2:0, y2:1,\n"
"                                                                stop:0        #FFFFFF,\n"
"                                                                stop:1        #DDDDDD);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color:                        #000000;\n"
"    padding:                    4px;\n"
"    border-style:            inset;\n"
"    border-width:             1px;\n"
"    border-radius:            7px;\n"
"    border-color:            #555555;\n"
"    background-color:    qlineargradient(    spread:pad,\n"
"                                                                x1:0, y1:0,\n"
"                                                                x2:0, y2:1,\n"
"                                                                stop:0        #FFFFFF,\n"
"                                                                stop:1        #D4D4D4);\n"
"}\n"
"\n"
"QPushButton:pressed, :checked \n"
"{\n"
"    font-weight:            bold;\n"
"    border-style:            outset;\n"
"    background-color:    qlineargradient(    spread:pad,\n"
"                                                                x1:0, y1:0,\n"
"                                                                x2:0, y2:1,\n"
"                                                                stop:0        #EEEEEE,\n"
"                                                                stop:1        #CCCCCC);\n"
" }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-color:            #000000;\n"
"}\n"
"\n"
".ButtonGreen\n"
"{\n"
"    background-color:    qlineargradient(    spread:pad,\n"
"                                                                x1:0, y1:0,\n"
"                                                                x2:0, y2:1,\n"
"                                                                stop:0        #3FC556,\n"
"                                                                stop:1        #038717);\n"
"}\n"
"\n"
".ButtonGreen::image\n"
"{\n"
"subcontrol-position: right bottom;\n"
"}\n"
"\n"
".NoBorder\n"
"{\n"
"    border-style:            None;\n"
"}\n"
"\n"
".Header\n"
"{\n"
"    background-color:    #D4D4D4;\n"
"    border-style:            inset;\n"
"    border-width:            1px;\n"
"    border-color:            #777777;\n"
"}\n"
"\n"
".Title\n"
"{\n"
"    color:                    #000000;\n"
"    font-weight:        normal;\n"
"    font-style:            italic;\n"
"    font-size:                14pt;\n"
"    font-family:            \"Verdana\";\n"
"}\n"
"\n"
".Panel\n"
"{\n"
"    background-color:    qlineargradient(spread:pad,\n"
"                                                             x1:0, y1:0,\n"
"                                                             x2:0, y2:1,\n"
"                                                             stop:0        #E3E3E3,\n"
"                                                             stop:0.2    #E3E3E3,\n"
"                                                             stop:1        #D2D2D2);\n"
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
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout = QtGui.QGridLayout(self.page)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.page)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/addIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.page)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.content.addWidget(self.page)
        self.verticalLayout_2.addWidget(self.content)
        self.horizontalLayout_2.addWidget(self.frameContent)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setProperty("class", _translate("MainWindow", "NoBorder", None))
        self.frameButtons.setProperty("class", _translate("MainWindow", "Header", None))
        self.buttonBooking.setText(_translate("MainWindow", "Planning", None))
        self.buttonClients.setText(_translate("MainWindow", "Clients", None))
        self.buttonBills.setText(_translate("MainWindow", "Factures", None))
        self.content.setProperty("class", _translate("MainWindow", "Panel", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton.setProperty("class", _translate("MainWindow", "Button", None))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_2.setProperty("class", _translate("MainWindow", "Button ButtonGreen", None))

from Booking.BookingList import BookingList
from Client.ClientList import ClientList
import loteliQt_rc
