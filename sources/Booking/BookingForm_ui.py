# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Booking/BookingForm.ui'
#
# Created: Sun Jan 12 15:41:48 2014
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

class Ui_BookingForm(object):
    def setupUi(self, BookingForm):
        BookingForm.setObjectName(_fromUtf8("BookingForm"))
        BookingForm.resize(423, 434)
        self.formLayout = QtGui.QFormLayout(BookingForm)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditDate = QtGui.QLineEdit(BookingForm)
        self.lineEditDate.setReadOnly(True)
        self.lineEditDate.setObjectName(_fromUtf8("lineEditDate"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditDate)
        self.label_2 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDays = QtGui.QLineEdit(BookingForm)
        self.lineEditDays.setReadOnly(True)
        self.lineEditDays.setObjectName(_fromUtf8("lineEditDays"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDays)
        self.label_3 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_6 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.phonesContainer = QtGui.QFrame(BookingForm)
        self.phonesContainer.setObjectName(_fromUtf8("phonesContainer"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.phonesContainer)
        self.label_5 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.textEditComment = QtGui.QTextEdit(BookingForm)
        self.textEditComment.setObjectName(_fromUtf8("textEditComment"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.textEditComment)
        self.frame = QtGui.QFrame(BookingForm)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.frame)

        self.retranslateUi(BookingForm)
        QtCore.QMetaObject.connectSlotsByName(BookingForm)

    def retranslateUi(self, BookingForm):
        self.label.setText(_translate("BookingForm", "Date :", None))
        self.label_2.setText(_translate("BookingForm", "Nombre de nuits :", None))
        self.label_3.setText(_translate("BookingForm", "Clients :", None))
        self.label_6.setText(_translate("BookingForm", "Chambres :", None))
        self.label_5.setText(_translate("BookingForm", "Commentaire :", None))

import loteliQt_rc
