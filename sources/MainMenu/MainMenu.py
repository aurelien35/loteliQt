# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore, QtGui
from MainMenu_ui import Ui_MainMenu

class MainMenu(QtGui.QFrame) :

	def __init__(self) :
		super(MainMenu, self).__init__()
		
		self.ui = Ui_MainMenu()
		self.ui.setupUi(self)
		self.ui.buttonWeb.clicked.connect(self.launchBrowser)

	def launchBrowser(self) :
		os.system("chromium")
