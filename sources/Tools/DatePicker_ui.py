# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Tools/DatePicker.ui'
#
# Created: Thu Jan 09 20:33:50 2014
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

class Ui_DatePicker(object):
    def setupUi(self, DatePicker):
        DatePicker.setObjectName(_fromUtf8("DatePicker"))
        DatePicker.resize(375, 250)
        DatePicker.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(DatePicker)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(DatePicker)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.calendar = QtGui.QCalendarWidget(self.frame)
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendar.setGridVisible(True)
        self.calendar.setHorizontalHeaderFormat(QtGui.QCalendarWidget.LongDayNames)
        self.calendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendar.setDateEditEnabled(False)
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.gridLayout.addWidget(self.calendar, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(DatePicker)
        QtCore.QMetaObject.connectSlotsByName(DatePicker)

    def retranslateUi(self, DatePicker):
        pass

import loteliQt_rc
