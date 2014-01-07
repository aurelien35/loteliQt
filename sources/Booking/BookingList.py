# -*- coding: utf-8 -*-

import copy
from PyQt4				import QtCore, QtGui
from Booking				import Booking
from BookingForm			import BookingForm
from BookingList_ui		import Ui_BookingList
from Tools.DataBase		import DataBase
from Tools.ModalDialog	import ShowModalDialog
from Tools.ModalDialog	import ModalDialog

class BookingList(QtGui.QFrame) :

	def __init__(self) :
		super(BookingList, self).__init__()
		
		# Membres
		self.m_ui		= Ui_BookingList()
		self.m_db		= DataBase()
		self.m_filter	= None
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.dataTable.setLabels([u"Id  ", u"Nom    ", u"Prénom    ", u"Téléphone     ", u"e-mail     "])
		self.m_ui.bookingForm.setReadOnly(True)
		self.m_ui.labelRowsCount.setText("")
		
		# Connexions
		self.m_ui.lineEditFilter.textChanged.connect(self.setFilter)
		self.m_ui.pushButtonClearFilter.clicked.connect(self.clearFilter)
		self.m_ui.pushButtonNewBooking.clicked.connect(self.newBooking)
		self.m_ui.pushButtonEditBooking.clicked.connect(self.editBooking)
		self.m_ui.dataTable.rowSelected.connect(self.rowSelected)
		self.m_ui.dataTable.rowClicked.connect(self.rowClicked)
		self.m_ui.dataTable.rowDoubleClicked.connect(self.rowDoubleClicked)

		# Etat initial
		self.m_ui.bookingForm.setBooking(None)
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
		query = u'''SELECT rowId, name, firstName, phones, emails FROM clients'''
		if (self.m_filter != None) :
			query = u'''{0} WHERE name LIKE :filter OR firstName LIKE :filter OR phones LIKE :filter OR emails LIKE :filter OR address LIKE :filter OR comment LIKE :filter'''.format(query)
		self.m_ui.dataTable.setQuery(query, {'filter':m_filter})
		self.m_ui.labelRowsCount.setText(u"{0} résultats".format(self.m_ui.dataTable.rowsCount()))
		
	def rowSelected(self, rowIndex) :
		print "rowSelected : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.bookingForm.setBooking(self.m_db.loadBooking(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.bookingForm.setBooking(None)
	
	def rowClicked(self, rowIndex) :
		print "rowClicked : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.bookingForm.setBooking(self.m_db.loadBooking(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.bookingForm.setBooking(None)
	
	def rowDoubleClicked(self, rowIndex) :
		print "rowDoubleClicked : {0}".format(str(rowIndex))
		if (rowIndex >= 0) :
			self.m_ui.bookingForm.setBooking(self.m_db.loadBooking(self.m_ui.dataTable.row(rowIndex)["rowid"]))
		else :
			self.m_ui.bookingForm.setBooking(None)
		self.editBooking()
			
	def newBooking(self) :
		booking		= Booking()
		bookingForm	= BookingForm()
		bookingForm.setBooking(booking)
		if (ShowModalDialog(bookingForm, "Ajouter un booking", "Ok", "Annuler") == ModalDialog.Result.Ok) :
			self.m_db.insertBooking(booking)
			self.updateQuery()
			
	def editBooking(self) :
		if (self.m_ui.bookingForm.booking() != None) :
			booking		= copy.deepcopy(self.m_ui.bookingForm.booking())
			bookingForm	= BookingForm()
			bookingForm.setBooking(booking)
			if (ShowModalDialog(bookingForm, "Modifier un booking", "Ok", "Annuler") == ModalDialog.Result.Ok) :
				self.m_db.updateBooking(booking)
				self.updateQuery()
