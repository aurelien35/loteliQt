# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Booking/BookingsList.ui'
#
# Created: Tue Jan 07 22:05:21 2014
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
        self.gridLayout = QtGui.QGridLayout(BookingList)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelRowsCount = QtGui.QLabel(BookingList)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelRowsCount.setFont(font)
        self.labelRowsCount.setObjectName(_fromUtf8("labelRowsCount"))
        self.horizontalLayout.addWidget(self.labelRowsCount)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(BookingList)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditFilter = QtGui.QLineEdit(BookingList)
        self.lineEditFilter.setObjectName(_fromUtf8("lineEditFilter"))
        self.horizontalLayout.addWidget(self.lineEditFilter)
        self.pushButtonClearFilter = QtGui.QPushButton(BookingList)
        self.pushButtonClearFilter.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonClearFilter.setMaximumSize(QtCore.QSize(20, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClearFilter.setIcon(icon)
        self.pushButtonClearFilter.setFlat(True)
        self.pushButtonClearFilter.setObjectName(_fromUtf8("pushButtonClearFilter"))
        self.horizontalLayout.addWidget(self.pushButtonClearFilter)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.dataTable = DataTableView(BookingList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTable.sizePolicy().hasHeightForWidth())
        self.dataTable.setSizePolicy(sizePolicy)
        self.dataTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dataTable.setFrameShadow(QtGui.QFrame.Raised)
        self.dataTable.setObjectName(_fromUtf8("dataTable"))
        self.gridLayout.addWidget(self.dataTable, 1, 0, 1, 1)
        self.bookingForm = BookingForm(BookingList)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookingForm.sizePolicy().hasHeightForWidth())
        self.bookingForm.setSizePolicy(sizePolicy)
        self.bookingForm.setMinimumSize(QtCore.QSize(20, 0))
        self.bookingForm.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bookingForm.setFrameShadow(QtGui.QFrame.Raised)
        self.bookingForm.setObjectName(_fromUtf8("bookingForm"))
        self.gridLayout.addWidget(self.bookingForm, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonNewBooking = QtGui.QPushButton(BookingList)
        self.pushButtonNewBooking.setObjectName(_fromUtf8("pushButtonNewBooking"))
        self.horizontalLayout_2.addWidget(self.pushButtonNewBooking)
        self.pushButtonEditBooking = QtGui.QPushButton(BookingList)
        self.pushButtonEditBooking.setObjectName(_fromUtf8("pushButtonEditBooking"))
        self.horizontalLayout_2.addWidget(self.pushButtonEditBooking)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.retranslateUi(BookingList)
        QtCore.QMetaObject.connectSlotsByName(BookingList)

    def retranslateUi(self, BookingList):
        self.labelRowsCount.setText(_translate("BookingList", "TextLabel", None))
        self.label.setText(_translate("BookingList", "Filtre :", None))
        self.pushButtonNewBooking.setText(_translate("BookingList", "Ajouter un booking", None))
        self.pushButtonEditBooking.setText(_translate("BookingList", "Modifier...", None))

from BookingForm import BookingForm
from Tools.DataTableView import DataTableView
import loteliQt_rc
