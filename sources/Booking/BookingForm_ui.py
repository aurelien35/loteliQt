# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Booking/BookingForm.ui'
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
        self.label_2 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDays = QtGui.QLineEdit(BookingForm)
        self.lineEditDays.setObjectName(_fromUtf8("lineEditDays"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDays)
        self.label_3 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_6 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.roomsContainer = QtGui.QFrame(BookingForm)
        self.roomsContainer.setObjectName(_fromUtf8("roomsContainer"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.roomsContainer)
        self.label_5 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.textEditComment = QtGui.QTextEdit(BookingForm)
        self.textEditComment.setObjectName(_fromUtf8("textEditComment"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.textEditComment)
        self.clientsContainer = QtGui.QFrame(BookingForm)
        self.clientsContainer.setObjectName(_fromUtf8("clientsContainer"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.clientsContainer)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditStartDate = QtGui.QLineEdit(BookingForm)
        self.lineEditStartDate.setReadOnly(True)
        self.lineEditStartDate.setObjectName(_fromUtf8("lineEditStartDate"))
        self.horizontalLayout_4.addWidget(self.lineEditStartDate)
        self.pushButtonSelectStartDate = QtGui.QPushButton(BookingForm)
        self.pushButtonSelectStartDate.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonSelectStartDate.setMaximumSize(QtCore.QSize(20, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/calendar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelectStartDate.setIcon(icon)
        self.pushButtonSelectStartDate.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonSelectStartDate.setFlat(True)
        self.pushButtonSelectStartDate.setObjectName(_fromUtf8("pushButtonSelectStartDate"))
        self.horizontalLayout_4.addWidget(self.pushButtonSelectStartDate)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_4 = QtGui.QLabel(BookingForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditEndDate = QtGui.QLineEdit(BookingForm)
        self.lineEditEndDate.setReadOnly(True)
        self.lineEditEndDate.setObjectName(_fromUtf8("lineEditEndDate"))
        self.horizontalLayout_3.addWidget(self.lineEditEndDate)
        self.pushButtonSelectEndDate = QtGui.QPushButton(BookingForm)
        self.pushButtonSelectEndDate.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonSelectEndDate.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButtonSelectEndDate.setIcon(icon)
        self.pushButtonSelectEndDate.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonSelectEndDate.setFlat(True)
        self.pushButtonSelectEndDate.setObjectName(_fromUtf8("pushButtonSelectEndDate"))
        self.horizontalLayout_3.addWidget(self.pushButtonSelectEndDate)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)

        self.retranslateUi(BookingForm)
        QtCore.QMetaObject.connectSlotsByName(BookingForm)

    def retranslateUi(self, BookingForm):
        self.label.setText(_translate("BookingForm", "Date d\'arrivée :", None))
        self.label_2.setText(_translate("BookingForm", "Nombre de nuits :", None))
        self.lineEditDays.setInputMask(_translate("BookingForm", "9000; ", None))
        self.label_3.setText(_translate("BookingForm", "Clients :", None))
        self.label_6.setText(_translate("BookingForm", "Chambres :", None))
        self.label_5.setText(_translate("BookingForm", "Commentaire :", None))
        self.label_4.setText(_translate("BookingForm", "Date de départ :", None))

import loteliQt_rc
