# -*- coding: utf-8 -*-

import copy
from PyQt4				import QtCore, QtGui
from Client				import Client
from ClientForm			import ClientForm
from ClientList_ui		import Ui_ClientList
from Tools.DataBase		import DataBase
from Tools.ModalDialog	import ShowModalDialog
from Tools.ModalDialog	import ModalDialog

class ClientList(QtGui.QFrame) :

	def __init__(self) :
		super(ClientList, self).__init__()
		
		# Membres
		self.m_ui		= Ui_ClientList()
		self.m_db		= DataBase()
		self.m_filter	= None
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.dataTable.setLabels([u"Id  ", u"Nom    ", u"Prénom    ", u"Téléphone     ", u"e-mail     "])
		self.m_ui.clientForm.setReadOnly(True)
		self.m_ui.labelRowsCount.setText("")
		
		# Connexions
		self.m_ui.lineEditFilter.textChanged.connect(self.setFilter)
		self.m_ui.pushButtonClearFilter.clicked.connect(self.clearFilter)
		self.m_ui.pushButtonNewClient.clicked.connect(self.newClient)
		self.m_ui.pushButtonEditClient.clicked.connect(self.editClient)
		self.m_ui.dataTable.rowSelected.connect(self.rowSelected)
		self.m_ui.dataTable.rowClicked.connect(self.rowClicked)
		self.m_ui.dataTable.rowDoubleClicked.connect(self.rowDoubleClicked)

		# Etat initial
		self.m_ui.clientForm.setClient(None)
		self.updateQuery()
		
	def setFilter(self, filter) :
		self.m_filter = filter
		if (self.m_filter != None) :
			if (len(self.m_filter) == 0) :
				self.m_filter = None
		self.updateQuery()
		
	def clearFilter(self) :
		self.setFilter(None)
		
	def updateQuery(self) :
		query = u"SELECT rowId, name, firstName, phones, emails FROM clients" 
		if (self.m_filter != None) :
			query = u"{0} WHERE name LIKE '%{1}%' OR firstName LIKE '%{1}%' OR phones LIKE '%{1}%' OR emails LIKE '%{1}%' OR address LIKE '%{1}%' OR comment LIKE '%{1}%'".format(query, self.m_filter)
		self.m_ui.dataTable.setQuery(query)
		self.m_ui.labelRowsCount.setText(u"{0} résultats".format(self.m_ui.dataTable.rowsCount()))
		
	def rowSelected(self, rowIndex) :
		print "rowSelected : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.clientForm.setClient(self.m_db.loadClient(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.clientForm.setClient(None)
	
	def rowClicked(self, rowIndex) :
		print "rowClicked : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.clientForm.setClient(self.m_db.loadClient(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.clientForm.setClient(None)
	
	def rowDoubleClicked(self, rowIndex) :
		print "rowDoubleClicked : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.clientForm.setClient(self.m_db.loadClient(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.clientForm.setClient(None)
		self.editClient()
			
	def newClient(self) :
		client		= Client()
		clientForm	= ClientForm()
		clientForm.setClient(client)
		if (ShowModalDialog(clientForm, "Ajouter un client", "Ok", "Annuler") == ModalDialog.Result.Ok) :
			self.m_db.insertClient(client)
			self.updateQuery()
			
	def editClient(self) :
		if (self.m_ui.clientForm.client() != None) :
			client		= copy.deepcopy(self.m_ui.clientForm.client())
			clientForm	= ClientForm()
			clientForm.setClient(client)
			if (ShowModalDialog(clientForm, "Modifier un client", "Ok", "Annuler") == ModalDialog.Result.Ok) :
				self.m_db.updateClient(client)
				self.updateQuery()
