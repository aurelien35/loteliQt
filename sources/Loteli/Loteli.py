# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import MainWindow

application	= QtGui.QApplication(sys.argv)
mainWindow	= MainWindow.MainWindow()

mainWindow.showMaximized()
