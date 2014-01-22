# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\MainMenu/MainMenu.ui'
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

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName(_fromUtf8("MainMenu"))
        MainMenu.resize(873, 632)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(16, 115, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainMenu.setPalette(palette)
        self.gridlayout = QtGui.QGridLayout(MainMenu)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonHome = QtGui.QPushButton(MainMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonHome.setIcon(icon)
        self.buttonHome.setIconSize(QtCore.QSize(256, 256))
        self.buttonHome.setFlat(True)
        self.buttonHome.setObjectName(_fromUtf8("buttonHome"))
        self.gridlayout.addWidget(self.buttonHome, 1, 1, 1, 1)
        self.buttonUSB = QtGui.QPushButton(MainMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/USB-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUSB.setIcon(icon1)
        self.buttonUSB.setIconSize(QtCore.QSize(256, 256))
        self.buttonUSB.setFlat(True)
        self.buttonUSB.setObjectName(_fromUtf8("buttonUSB"))
        self.gridlayout.addWidget(self.buttonUSB, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 166, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 166, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.buttonWeb = QtGui.QPushButton(MainMenu)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/Globe1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonWeb.setIcon(icon2)
        self.buttonWeb.setIconSize(QtCore.QSize(256, 256))
        self.buttonWeb.setFlat(True)
        self.buttonWeb.setObjectName(_fromUtf8("buttonWeb"))
        self.gridlayout.addWidget(self.buttonWeb, 1, 0, 1, 1)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        pass

import loteliQt_rc
