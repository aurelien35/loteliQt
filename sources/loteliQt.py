from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
from MainMenu.MainMenu import MainMenu
from Client.ClientForm import ClientForm

# Creation de l'application
app = QtGui.QApplication(sys.argv)

# Configuration de l'application
QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

# Ouverture du menu principal
# mainMenu = MainMenu()
# mainMenu.showFullScreen()
clientForm = ClientForm()
clientForm.show()

# Lancement de l'application
app.exec_()
