# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './sources\Tools/DataTableView.ui'
#
# Created: Sun Jan 12 15:41:50 2014
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

class Ui_DataTableView(object):
    def setupUi(self, DataTableView):
        DataTableView.setObjectName(_fromUtf8("DataTableView"))
        DataTableView.resize(672, 489)
        self.verticalLayout = QtGui.QVBoxLayout(DataTableView)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(DataTableView)
        self.tableView.setFrameShape(QtGui.QFrame.Box)
        self.tableView.setFrameShadow(QtGui.QFrame.Plain)
        self.tableView.setLineWidth(2)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableView.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableView.setCornerButtonEnabled(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.navigationBar = QtGui.QFrame(DataTableView)
        self.navigationBar.setObjectName(_fromUtf8("navigationBar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.navigationBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonPreviousPage = QtGui.QPushButton(self.navigationBar)
        self.buttonPreviousPage.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonPreviousPage.setMaximumSize(QtCore.QSize(36, 36))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPreviousPage.setIcon(icon)
        self.buttonPreviousPage.setIconSize(QtCore.QSize(32, 32))
        self.buttonPreviousPage.setFlat(True)
        self.buttonPreviousPage.setObjectName(_fromUtf8("buttonPreviousPage"))
        self.horizontalLayout.addWidget(self.buttonPreviousPage)
        spacerItem = QtGui.QSpacerItem(263, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBoxCurrentPage = QtGui.QComboBox(self.navigationBar)
        self.comboBoxCurrentPage.setObjectName(_fromUtf8("comboBoxCurrentPage"))
        self.horizontalLayout.addWidget(self.comboBoxCurrentPage)
        spacerItem1 = QtGui.QSpacerItem(262, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonNextPage = QtGui.QPushButton(self.navigationBar)
        self.buttonNextPage.setMinimumSize(QtCore.QSize(36, 36))
        self.buttonNextPage.setMaximumSize(QtCore.QSize(36, 36))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNextPage.setIcon(icon1)
        self.buttonNextPage.setIconSize(QtCore.QSize(32, 32))
        self.buttonNextPage.setFlat(True)
        self.buttonNextPage.setObjectName(_fromUtf8("buttonNextPage"))
        self.horizontalLayout.addWidget(self.buttonNextPage)
        self.verticalLayout.addWidget(self.navigationBar)

        self.retranslateUi(DataTableView)
        QtCore.QMetaObject.connectSlotsByName(DataTableView)

    def retranslateUi(self, DataTableView):
        pass

import loteliQt_rc
