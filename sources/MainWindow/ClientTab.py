# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
from PyQt4 import QtGui
import ClientTab_ui

class ClientTab(QtGui.QFrame) :

	def __init__(self) :
		super(QtGui.QFrame, self).__init__()
		
		# Membres
		self.m_ui = ClientTab_ui.Ui_ClientTab()
		
		# Etat initial
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.clientTableView.dataLoaded.connect(self.clientTableDataLoaded)
		self.m_ui.lineEditClientTableFilter.textChanged.connect(self.clientTableFilterChanged)
		self.m_ui.buttonClearClientTableFilter.clicked.connect(self.clearClientTableFilter)
		
		self.clientTableFilterChanged()
				
	def clientTableDataLoaded(self, clientsCount) :
		self.m_ui.labelClientTableRowCount.setText(u"{0} résultat(s)".format(clientsCount))
		
	def clientTableFilterChanged(self) :
		self.m_ui.clientTableView.setFilter(self.m_ui.lineEditClientTableFilter.text())

	def clearClientTableFilter(self) :
		self.m_ui.lineEditClientTableFilter.setText(QtCore.QString())
