# -*- coding: utf-8 -*-

from PyQt4					import QtCore
from PyQt4					import QtGui
from MainMenu.MainMenu		import MainMenu
from MainWindow.MainWindow	import MainWindow
from Client.ClientForm		import ClientForm
from Client.ClientList		import ClientList
from Tools.DataTableView	import DataTableView
import sys

# Creation de l'application
app = QtGui.QApplication(sys.argv)

# Configuration de l'application
QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

# Ouverture du menu principal
# mainMenu = MainMenu()
# mainMenu.setGeometry(50, 50, 800, 600)
# mainMenu.show()
# mainMenu.showFullScreen()

mainWindow = MainWindow()
mainWindow.showMaximized()
# mainWindow.showFullScreen()

# clientForm = ClientForm()
# clientForm.show()

# dataTableView = DataTableView()
# dataTableView.setLabels([u"Id", u"Nom", u"Prénom", u"Téléphone", u"e-mail"])
# dataTableView.setQuery(u"SELECT rowId as [INTEGER], name, firstName, phones, emails FROM clients", None)
# dataTableView.show()

# clientList = ClientList()
# clientList.show()


# Lancement de l'application
app.exec_()
