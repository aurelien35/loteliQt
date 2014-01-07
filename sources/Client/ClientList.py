# -*- coding: utf-8 -*-

from PyQt4			import QtCore, QtGui
from Client			import Client
from ClientList_ui	import Ui_ClientList
from Tools.DataBase	import DataBase

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
		self.m_ui.dataTable.rowSelected.connect(self.rowSelected)
		self.m_ui.dataTable.rowClicked.connect(self.rowClicked)
		self.m_ui.dataTable.rowDoubleClicked.connect(self.rowDoubleClicked)

		# Etat initial
		self.m_ui.clientForm.setClient(Client())
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
