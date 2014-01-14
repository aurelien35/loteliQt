# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Client/ClientList.ui'
#
# Created: Tue Jan 14 22:48:46 2014
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

class Ui_ClientList(object):
    def setupUi(self, ClientList):
        ClientList.setObjectName(_fromUtf8("ClientList"))
        ClientList.resize(841, 483)
        self.gridLayout = QtGui.QGridLayout(ClientList)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.clientsTable = DataTableView(ClientList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientsTable.sizePolicy().hasHeightForWidth())
        self.clientsTable.setSizePolicy(sizePolicy)
        self.clientsTable.setObjectName(_fromUtf8("clientsTable"))
        self.gridLayout.addWidget(self.clientsTable, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonNewClient = QtGui.QPushButton(ClientList)
        self.buttonNewClient.setObjectName(_fromUtf8("buttonNewClient"))
        self.horizontalLayout_2.addWidget(self.buttonNewClient)
        self.buttonEditSelectedClient = QtGui.QPushButton(ClientList)
        self.buttonEditSelectedClient.setObjectName(_fromUtf8("buttonEditSelectedClient"))
        self.horizontalLayout_2.addWidget(self.buttonEditSelectedClient)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.clientForm = ClientForm(ClientList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientForm.sizePolicy().hasHeightForWidth())
        self.clientForm.setSizePolicy(sizePolicy)
        self.clientForm.setObjectName(_fromUtf8("clientForm"))
        self.verticalLayout.addWidget(self.clientForm)
        self.bookingsTable = BookingTableView(ClientList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookingsTable.sizePolicy().hasHeightForWidth())
        self.bookingsTable.setSizePolicy(sizePolicy)
        self.bookingsTable.setObjectName(_fromUtf8("bookingsTable"))
        self.verticalLayout.addWidget(self.bookingsTable)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelClientsTableRowsCount = QtGui.QLabel(ClientList)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelClientsTableRowsCount.setFont(font)
        self.labelClientsTableRowsCount.setObjectName(_fromUtf8("labelClientsTableRowsCount"))
        self.horizontalLayout.addWidget(self.labelClientsTableRowsCount)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(ClientList)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditClientsTableFilter = QtGui.QLineEdit(ClientList)
        self.lineEditClientsTableFilter.setObjectName(_fromUtf8("lineEditClientsTableFilter"))
        self.horizontalLayout.addWidget(self.lineEditClientsTableFilter)
        self.buttonClearClientsTableFilter = QtGui.QPushButton(ClientList)
        self.buttonClearClientsTableFilter.setMinimumSize(QtCore.QSize(24, 24))
        self.buttonClearClientsTableFilter.setMaximumSize(QtCore.QSize(24, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonClearClientsTableFilter.setIcon(icon)
        self.buttonClearClientsTableFilter.setFlat(True)
        self.buttonClearClientsTableFilter.setObjectName(_fromUtf8("buttonClearClientsTableFilter"))
        self.horizontalLayout.addWidget(self.buttonClearClientsTableFilter)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(ClientList)
        QtCore.QMetaObject.connectSlotsByName(ClientList)

    def retranslateUi(self, ClientList):
        self.buttonNewClient.setText(_translate("ClientList", "Ajouter un client", None))
        self.buttonEditSelectedClient.setText(_translate("ClientList", "Modifier...", None))
        self.labelClientsTableRowsCount.setText(_translate("ClientList", "TextLabel", None))
        self.label.setText(_translate("ClientList", "Filtre :", None))

from Booking.BookingTableView import BookingTableView
from ClientForm import ClientForm
from Tools.DataTableView import DataTableView
import loteliQt_rc
