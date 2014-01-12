# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Booking/BookingList.ui'
#
# Created: Sun Jan 12 15:41:49 2014
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
        BookingList.resize(752, 609)
        self.gridLayout_2 = QtGui.QGridLayout(BookingList)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.planning = BookingPlanning(BookingList)
        self.planning.setObjectName(_fromUtf8("planning"))
        self.gridLayout_2.addWidget(self.planning, 0, 0, 1, 1)
        self.tableView = BookingTableView(BookingList)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 0, 1, 1, 1)

        self.retranslateUi(BookingList)
        QtCore.QMetaObject.connectSlotsByName(BookingList)

    def retranslateUi(self, BookingList):
        pass

from BookingTableView import BookingTableView
from BookingPlanning import BookingPlanning
import loteliQt_rc
