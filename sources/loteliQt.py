# -*- coding: utf-8 -*-

from PyQt4				import QtCore
from PyQt4				import QtGui
from MainMenu.MainMenu	import MainMenu
from Client.ClientForm	import ClientForm
import sys

# Creation de l'application
app = QtGui.QApplication(sys.argv)

# Configuration de l'application
QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

# Ouverture du menu principal
mainMenu = MainMenu()
# mainMenu.setGeometry(50, 50, 800, 600)
# mainMenu.show()
mainMenu.showFullScreen()
# clientForm = ClientForm()
# clientForm.show()

# Lancement de l'application
app.exec_()
