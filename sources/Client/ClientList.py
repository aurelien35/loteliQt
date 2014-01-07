# -*- coding: utf-8 -*-

from PyQt4			import QtCore, QtGui
from Client			import Client
from ClientList_ui	import Ui_ClientList
from Tools.DataBase	import DataBase

class ClientList(QtGui.QFrame) :

	def __init__(self) :
		super(ClientList, self).__init__()
		
		# Membres
		self.m_ui	= Ui_ClientList()
		self.m_db	= DataBase()
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.dataTable.setLabels([u"Id  ", u"Nom    ", u"Prénom    ", u"Téléphone     ", u"e-mail     "])
		self.m_ui.dataTable.setQuery(u"SELECT rowId, name, firstName, phones, emails FROM clients")
		self.m_ui.clientForm.setReadOnly(True)
		
		# Connexions
		self.m_ui.dataTable.rowSelected.connect(self.rowSelected)
		self.m_ui.dataTable.rowClicked.connect(self.rowClicked)
		self.m_ui.dataTable.rowDoubleClicked.connect(self.rowDoubleClicked)

		# Etat initial
		self.m_ui.clientForm.setClient(Client())
		
	def rowSelected(self, rowIndex) :
		print "rowSelected : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.clientForm.setClient(self.m_db.loadClient(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.clientForm.setClient(Client())
	
	def rowClicked(self, rowIndex) :
		print "rowClicked : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.clientForm.setClient(self.m_db.loadClient(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.clientForm.setClient(Client())
	
	def rowDoubleClicked(self, rowIndex) :
		print "rowDoubleClicked : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.clientForm.setClient(self.m_db.loadClient(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.clientForm.setClient(Client())
