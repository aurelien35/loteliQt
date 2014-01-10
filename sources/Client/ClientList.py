# -*- coding: utf-8 -*-

import copy
from PyQt4					import QtCore, QtGui
from Client					import Client
from ClientForm				import ClientForm
from ClientList_ui			import Ui_ClientList
from Tools.DataBase			import DataBase
from Tools.ModalDialog		import ShowModalDialog
from Tools.ModalDialog		import ModalDialog
from Tools.StringConvert	import *

class ClientList(QtGui.QFrame) :

	def __init__(self) :
		super(ClientList, self).__init__()
		
		# Membres
		self.m_ui			= Ui_ClientList()
		self.m_db			= DataBase()
		self.m_clientFilter	= None
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.clients.setColumns([	(u"Id  ",			u"rowid"),
										(u"Nom    ",		u"name"),
										(u"Prénom    ",		u"firstName"),
										(u"Téléphone     ",	u"phones"),
										(u"e-mail     ",	u"emails")])
		self.m_ui.clientForm.setReadOnly(True)
		self.m_ui.labelClientsCount.setText("")
		self.m_ui.bookings.setColumns([	(u"Id  ",		u"rowid"),
										(u"Date    ",	u"date"),
										(u"Days    ",	u"days"),
										(u"Rooms    ",	u"rooms")])
		
		# Connexions
		self.m_ui.lineEditClientFilter.textChanged.connect(self.setClientFilter)
		self.m_ui.buttonClearClientFilter.clicked.connect(self.clearClientFilter)
		self.m_ui.buttonNewClient.clicked.connect(self.newClient)
		self.m_ui.buttonEditClient.clicked.connect(self.editClient)
		self.m_ui.clients.rowSelected.connect(self.clientSelected)
		self.m_ui.clients.rowClicked.connect(self.clientClicked)
		self.m_ui.clients.rowDoubleClicked.connect(self.clientDoubleClicked)
		
		# Bookings

		# Etat initial
		self.clientSelected(-1)
		self.updateQuery()
		
	def setClientFilter(self, clientFilter) :
		self.m_clientFilter = None
		if (clientFilter != None) :
			self.m_clientFilter = QString2str(clientFilter)
			if (len(self.m_clientFilter) == 0) :
				self.m_clientFilter = None
		self.updateQuery()
		
	def clearClientFilter(self) :
		self.setClientFilter(None)
		self.m_ui.lineEditClientFilter.setText(QtCore.QString())
		
	def updateQuery(self) :
		query = u'''SELECT rowid, name, firstName, phones, emails FROM clients'''
		if (self.m_clientFilter != None) :
			query = u'''{0} WHERE name LIKE :filter OR firstName LIKE :filter OR phones LIKE :filter OR emails LIKE :filter OR address LIKE :filter OR comment LIKE :filter'''.format(query)
		query = u'''{0} ORDER BY name'''.format(query)
		self.m_ui.clients.setQuery(query, {'filter':u"%{0}%".format(self.m_clientFilter)})
		self.m_ui.labelClientsCount.setText(u"{0} résultats".format(self.m_ui.clients.rowsCount()))
		self.m_ui.buttonEditClient.setVisible(self.m_ui.clientForm.client() != None)
		
	def clientSelected(self, clientIndex) :
		self.m_ui.clientForm.setClient(None)
		self.m_ui.bookings.hide()
		if (clientIndex >= 0) :
			clientId = self.m_ui.clients.row(clientIndex)["rowid"]
			self.m_ui.clientForm.setClient(self.m_db.loadClient(clientId))
			self.m_ui.bookings.setQuery(u'''SELECT rowid, date, days, rooms FROM bookings WHERE clients LIKE :clientId ORDER BY date''', {'clientId':u"%¤{0}¤%".format(clientId)})
			if (self.m_ui.bookings.rowsCount() > 0) :
				self.m_ui.bookings.show()
		self.m_ui.buttonEditClient.setVisible(self.m_ui.clientForm.client() != None)

	def clientClicked(self, clientIndex) :
		self.clientSelected(clientIndex)
	
	def clientDoubleClicked(self, clientIndex) :
		self.clientSelected(clientIndex)
		self.editClient()
			
	def newClient(self) :
		newClient		= Client()
		newClientForm	= ClientForm()
		newClientForm.setClient(newClient)
		if (ShowModalDialog(newClientForm, "Ajouter un client", "Ok", "Annuler") == ModalDialog.Result.Ok) :
			self.m_db.insertClient(newClient)
			self.updateQuery()
			
	def editClient(self) :
		if (self.m_ui.clientForm.client() != None) :
			editClient		= copy.deepcopy(self.m_ui.clientForm.client())
			editClientForm	= ClientForm()
			editClientForm.setClient(editClient)
			if (ShowModalDialog(editClientForm, "Modifier un client", "Ok", "Annuler") == ModalDialog.Result.Ok) :
				self.m_db.updateClient(editClient)
				self.updateQuery()
