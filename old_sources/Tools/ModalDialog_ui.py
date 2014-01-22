# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Tools/ModalDialog.ui'
#
# Created: Mon Jan 20 21:34:01 2014
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

class Ui_ModalDialog(object):
    def setupUi(self, ModalDialog):
        ModalDialog.setObjectName(_fromUtf8("ModalDialog"))
        ModalDialog.resize(395, 268)
        ModalDialog.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(ModalDialog)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frameDialog = QtGui.QFrame(ModalDialog)
        self.frameDialog.setObjectName(_fromUtf8("frameDialog"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frameDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frameTitle = QtGui.QFrame(self.frameDialog)
        self.frameTitle.setObjectName(_fromUtf8("frameTitle"))
        self.gridlayout = QtGui.QGridLayout(self.frameTitle)
        self.gridlayout.setContentsMargins(-1, 4, 4, 4)
        self.gridlayout.setHorizontalSpacing(4)
        self.gridlayout.setVerticalSpacing(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.labelTitle = QtGui.QLabel(self.frameTitle)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.gridlayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frameTitle)
        self.frameContent = QtGui.QFrame(self.frameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameContent.sizePolicy().hasHeightForWidth())
        self.frameContent.setSizePolicy(sizePolicy)
        self.frameContent.setObjectName(_fromUtf8("frameContent"))
        self.containerLayout = QtGui.QVBoxLayout(self.frameContent)
        self.containerLayout.setMargin(0)
        self.containerLayout.setObjectName(_fromUtf8("containerLayout"))
        self.verticalLayout.addWidget(self.frameContent)
        self.frameButtons = QtGui.QFrame(self.frameDialog)
        self.frameButtons.setObjectName(_fromUtf8("frameButtons"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frameButtons)
        self.horizontalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonOk = QtGui.QPushButton(self.frameButtons)
        self.buttonOk.setObjectName(_fromUtf8("buttonOk"))
        self.horizontalLayout_2.addWidget(self.buttonOk)
        self.buttonCancel = QtGui.QPushButton(self.frameButtons)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout_2.addWidget(self.buttonCancel)
        self.buttonOther = QtGui.QPushButton(self.frameButtons)
        self.buttonOther.setObjectName(_fromUtf8("buttonOther"))
        self.horizontalLayout_2.addWidget(self.buttonOther)
        self.verticalLayout.addWidget(self.frameButtons)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout_2.addWidget(self.frameDialog, 0, 0, 1, 1)

        self.retranslateUi(ModalDialog)
        QtCore.QMetaObject.connectSlotsByName(ModalDialog)

    def retranslateUi(self, ModalDialog):
        ModalDialog.setProperty("class", _translate("ModalDialog", "NoBorder", None))
        self.frameTitle.setProperty("class", _translate("ModalDialog", "Header", None))
        self.labelTitle.setText(_translate("ModalDialog", "Titre", None))
        self.labelTitle.setProperty("class", _translate("ModalDialog", "Title", None))
        self.frameContent.setProperty("class", _translate("ModalDialog", "Panel", None))
        self.frameButtons.setProperty("class", _translate("ModalDialog", "Header", None))
        self.buttonOk.setText(_translate("ModalDialog", "Ok", None))
        self.buttonCancel.setText(_translate("ModalDialog", "Annuler", None))
        self.buttonOther.setText(_translate("ModalDialog", "Other", None))

import loteliQt_rc
