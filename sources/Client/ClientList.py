# -*- coding: utf-8 -*-

from PyQt4					import QtCore, QtGui
from Client					import Client
from ClientDialogs			import *
from ClientForm				import ClientForm
from ClientList_ui			import Ui_ClientList
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *

class ClientList(QtGui.QFrame) :

	def __init__(self) :
		super(ClientList, self).__init__()
		
		# Membres
		self.m_ui					= Ui_ClientList()
		self.m_db					= DataBase()
		self.m_clientsTableFilter	= None
		self.m_selectedClientIndex	= -1
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.clientsTable.setColumns([	(u"Id  ",			u"rowid"),
											(u"Nom    ",		u"name"),
											(u"Prénom    ",		u"firstName"),
											(u"Téléphone     ",	u"phones"),
											(u"e-mail     ",	u"emails")])
		self.m_ui.clientForm.setReadOnly(True)
		self.m_ui.labelClientsTableRowsCount.setText("")

		# Connexions
		self.m_ui.lineEditClientsTableFilter.textChanged.connect(self.setClientsTableFilter)
		self.m_ui.buttonClearClientsTableFilter.clicked.connect(self.clearClientsTableFilter)
		self.m_ui.buttonNewClient.clicked.connect(self.newClient)
		self.m_ui.buttonEditSelectedClient.clicked.connect(self.editSelectedClient)
		self.m_ui.clientsTable.rowSelected.connect(self.clientsTableSelectionChanged)
		self.m_ui.clientsTable.rowDoubleClicked.connect(self.clientsTableDoubleClicked)

		# Etat initial
		self.clientsTableSelectionChanged(-1)
		self.updateData()
		
	def setClientsTableFilter(self, clientFilter) :
		self.m_clientsTableFilter = None
		if (clientFilter != None) :
			self.m_clientsTableFilter = QString2str(clientFilter)
			if (len(self.m_clientsTableFilter) == 0) :
				self.m_clientsTableFilter = None
		self.updateData()
		
	def clearClientsTableFilter(self) :
		self.setClientsTableFilter(None)
		self.m_ui.lineEditClientsTableFilter.setText(QtCore.QString())
		
	def updateData(self) :
		# Mise à jour des données affichées dans la table des clients
		query = u'''SELECT rowid, name, firstName, phones, emails FROM clients'''
		if (self.m_clientsTableFilter != None) :
			query = u'''{0} WHERE name LIKE :filter OR firstName LIKE :filter OR phones LIKE :filter OR emails LIKE :filter OR address LIKE :filter OR comment LIKE :filter'''.format(query)
		query = u'''{0} ORDER BY name'''.format(query)
		self.m_ui.clientsTable.setQuery(query, {'filter':u"%{0}%".format(self.m_clientsTableFilter)}, "rowid")
		self.m_ui.labelClientsTableRowsCount.setText(u"{0} résultats".format(self.m_ui.clientsTable.rowsCount()))
		self.m_ui.buttonEditSelectedClient.setVisible(self.m_ui.clientForm.client() != None)
		
		# Mise à jour des données affichées dans le formulaire des clients
		self.m_ui.clientForm.reloadClient()
		
		# Mise à jour des données affichées dans la liste des reservations du client
		# TODO : reloadBookings
		
	def clientsTableSelectionChanged(self, clientIndex) :
		self.m_selectedClientIndex = clientIndex
		self.m_ui.clientForm.setClient(None)
		self.m_ui.bookingsTable.setBookings(None)
		self.m_ui.bookingsTable.hide()
		if (self.m_selectedClientIndex >= 0) :
			clientId = self.m_ui.clientsTable.row(self.m_selectedClientIndex)["rowid"]
			self.m_ui.clientForm.setClient(self.m_db.loadClient(clientId))
			bookings = self.m_db.loadBookingsByClientId(clientId)
			if (len(bookings) > 0) :
				self.m_ui.bookingsTable.setBookings(bookings)
				self.m_ui.bookingsTable.show()
		self.m_ui.buttonEditSelectedClient.setVisible(self.m_ui.clientForm.client() != None)

	def clientsTableDoubleClicked(self, clientIndex) :
		self.editSelectedClient()
			
	def newClient(self) :
		if (ClientCreateDialog().showDialog() == ModalDialog.Result.Ok) :
			self.updateData()
			
	def editSelectedClient(self) :
		if (ClientEditDialog(self.m_ui.clientForm.client()).showDialog() == ModalDialog.Result.Ok) :
			self.updateData()

	def showEvent(self, event) :
		super(ClientList, self).showEvent(event)
		self.updateData()
