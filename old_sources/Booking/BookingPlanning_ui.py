# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Booking/BookingPlanning.ui'
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

class Ui_BookingPlanning(object):
    def setupUi(self, BookingPlanning):
        BookingPlanning.setObjectName(_fromUtf8("BookingPlanning"))
        BookingPlanning.resize(557, 370)
        BookingPlanning.setStyleSheet(_fromUtf8("QFrame#BookingPlanning\n"
"{\n"
"    border-style:            none;\n"
"}\n"
"\n"
"QWidget#qt_calendar_calendarview\n"
"{\n"
"    background-color:    transparent;\n"
"    border-style:            solid;\n"
"    border-color:            #BBBBBB;\n"
"    border-width:            0px 1px 1x 0px;\n"
"}\n"
"\n"
"QWidget#qt_calendar_navigationbar\n"
"{\n"
"    background-color:    #01939A;\n"
"    border-style:            solid;\n"
"    border-color:            #BBBBBB;\n"
"    border-width:            1px 1px 0px 1px;\n"
"    color:                        #000000;\n"
"    font-weight:            normal;\n"
"    font-style:                italic;\n"
"    font-size:                    14pt;    \n"
"    font-family:                \"Verdana\";\n"
"}\n"
"\n"
"QWidget#qt_calendar_prevmonth\n"
"{\n"
"}\n"
"\n"
"QWidget#qt_calendar_nextmonth\n"
"{\n"
"}\n"
"\n"
"QWidget#qt_calendar_monthbutton,\n"
"QWidget#qt_calendar_yearbutton\n"
"{\n"
"    color:                        #FFFFFF;\n"
"    font-weight:            normal;\n"
"    font-style:                normal;\n"
"    font-size:                    14pt;    \n"
"    font-family:                \"Verdana\";\n"
"}\n"
""))
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
