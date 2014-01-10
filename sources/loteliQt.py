# -*- coding: utf-8 -*-

import sys
from PyQt4					import QtCore
from PyQt4					import QtGui
from MainMenu.MainMenu		import MainMenu
from MainWindow.MainWindow	import MainWindow

#############################
# Creation de l'application #
#############################
app = QtGui.QApplication(sys.argv)

##################################
# Configuration de l'application #
##################################
QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

###############################
# Ouverture du menu principal #
###############################
mainWindow = MainWindow()
mainWindow.showMaximized()
# mainWindow.showFullScreen()

# mainMenu = MainMenu()
# mainMenu.showFullScreen()

##############################
# Lancement de l'application #
##############################
app.exec_()
