# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Booking/BookingPlanning.ui'
#
# Created: Sun Jan 12 16:05:04 2014
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

class Ui_BookingPlanning(object):
    def setupUi(self, BookingPlanning):
        BookingPlanning.setObjectName(_fromUtf8("BookingPlanning"))
        BookingPlanning.resize(557, 370)
        BookingPlanning.setFrameShape(QtGui.QFrame.Box)
        BookingPlanning.setLineWidth(2)
        self.gridLayout = QtGui.QGridLayout(BookingPlanning)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.calendar = BookingCalendar(BookingPlanning)
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendar.setHorizontalHeaderFormat(QtGui.QCalendarWidget.NoHorizontalHeader)
        self.calendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendar.setDateEditEnabled(False)
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.gridLayout.addWidget(self.calendar, 0, 0, 1, 1)

        self.retranslateUi(BookingPlanning)
        QtCore.QMetaObject.connectSlotsByName(BookingPlanning)

    def retranslateUi(self, BookingPlanning):
        pass

from BookingCalendar import BookingCalendar
import loteliQt_rc
