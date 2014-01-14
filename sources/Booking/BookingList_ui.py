# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Booking/BookingList.ui'
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

class Ui_BookingList(object):
    def setupUi(self, BookingList):
        BookingList.setObjectName(_fromUtf8("BookingList"))
        BookingList.resize(729, 435)
        self.horizontalLayout = QtGui.QHBoxLayout(BookingList)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.planning = BookingPlanning(BookingList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planning.sizePolicy().hasHeightForWidth())
        self.planning.setSizePolicy(sizePolicy)
        self.planning.setObjectName(_fromUtf8("planning"))
        self.horizontalLayout.addWidget(self.planning)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonNewBooking = QtGui.QPushButton(BookingList)
        self.buttonNewBooking.setObjectName(_fromUtf8("buttonNewBooking"))
        self.horizontalLayout_2.addWidget(self.buttonNewBooking)
        self.buttonEditSelectedBooking = QtGui.QPushButton(BookingList)
        self.buttonEditSelectedBooking.setObjectName(_fromUtf8("buttonEditSelectedBooking"))
        self.horizontalLayout_2.addWidget(self.buttonEditSelectedBooking)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.bookingForm = BookingForm(BookingList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookingForm.sizePolicy().hasHeightForWidth())
        self.bookingForm.setSizePolicy(sizePolicy)
        self.bookingForm.setObjectName(_fromUtf8("bookingForm"))
        self.verticalLayout.addWidget(self.bookingForm)
        self.bookingsTable = BookingTableView(BookingList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookingsTable.sizePolicy().hasHeightForWidth())
        self.bookingsTable.setSizePolicy(sizePolicy)
        self.bookingsTable.setObjectName(_fromUtf8("bookingsTable"))
        self.verticalLayout.addWidget(self.bookingsTable)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(BookingList)
        QtCore.QMetaObject.connectSlotsByName(BookingList)

    def retranslateUi(self, BookingList):
        self.buttonNewBooking.setText(_translate("BookingList", "Ajouter une réservation", None))
        self.buttonEditSelectedBooking.setText(_translate("BookingList", "Modifier...", None))

from BookingForm import BookingForm
from BookingPlanning import BookingPlanning
from BookingTableView import BookingTableView
import loteliQt_rc
