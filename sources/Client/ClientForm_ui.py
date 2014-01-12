# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Client/ClientForm.ui'
#
# Created: Sun Jan 12 16:05:05 2014
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

class Ui_ClientForm(object):
    def setupUi(self, ClientForm):
        ClientForm.setObjectName(_fromUtf8("ClientForm"))
        ClientForm.resize(427, 433)
        self.formLayout = QtGui.QFormLayout(ClientForm)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(ClientForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditName = QtGui.QLineEdit(ClientForm)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditName)
        self.label_2 = QtGui.QLabel(ClientForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditFirstName = QtGui.QLineEdit(ClientForm)
        self.lineEditFirstName.setObjectName(_fromUtf8("lineEditFirstName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditFirstName)
        self.label_3 = QtGui.QLabel(ClientForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditBirthDate = QtGui.QLineEdit(ClientForm)
        self.lineEditBirthDate.setReadOnly(True)
        self.lineEditBirthDate.setObjectName(_fromUtf8("lineEditBirthDate"))
        self.horizontalLayout_3.addWidget(self.lineEditBirthDate)
        self.pushButtonSelectBirthDate = QtGui.QPushButton(ClientForm)
        self.pushButtonSelectBirthDate.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonSelectBirthDate.setMaximumSize(QtCore.QSize(20, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/calendar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelectBirthDate.setIcon(icon)
        self.pushButtonSelectBirthDate.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonSelectBirthDate.setFlat(True)
        self.pushButtonSelectBirthDate.setObjectName(_fromUtf8("pushButtonSelectBirthDate"))
        self.horizontalLayout_3.addWidget(self.pushButtonSelectBirthDate)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_6 = QtGui.QLabel(ClientForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(ClientForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_4 = QtGui.QLabel(ClientForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.textEditAddress = QtGui.QTextEdit(ClientForm)
        self.textEditAddress.setObjectName(_fromUtf8("textEditAddress"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.textEditAddress)
        self.label_5 = QtGui.QLabel(ClientForm)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.textEditComment = QtGui.QTextEdit(ClientForm)
        self.textEditComment.setObjectName(_fromUtf8("textEditComment"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.textEditComment)
        self.emailsContainer = QtGui.QFrame(ClientForm)
        self.emailsContainer.setObjectName(_fromUtf8("emailsContainer"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.emailsContainer)
        self.phonesContainer = QtGui.QFrame(ClientForm)
        self.phonesContainer.setObjectName(_fromUtf8("phonesContainer"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.phonesContainer)

        self.retranslateUi(ClientForm)
        QtCore.QMetaObject.connectSlotsByName(ClientForm)

    def retranslateUi(self, ClientForm):
        self.label.setText(_translate("ClientForm", "Nom :", None))
        self.label_2.setText(_translate("ClientForm", "Prénom :", None))
        self.label_3.setText(_translate("ClientForm", "Date de naissance :", None))
        self.label_6.setText(_translate("ClientForm", "Téléphone :", None))
        self.label_7.setText(_translate("ClientForm", "e-mail :", None))
        self.label_4.setText(_translate("ClientForm", "Adresse :", None))
        self.label_5.setText(_translate("ClientForm", "Commentaire :", None))

import loteliQt_rc
