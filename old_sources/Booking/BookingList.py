# -*- coding: utf-8 -*-

import copy
from PyQt4					import QtCore, QtGui
from Booking				import Booking
from BookingDialogs			import *
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *
from BookingList_ui			import Ui_BookingList

class BookingList(QtGui.QFrame) :

	def __init__(self) :
		super(BookingList, self).__init__()
		
		# Membres
		self.m_db	= DataBase()
		self.m_ui	= Ui_BookingList()
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.planning.setMinimumWidth(800)
		
		# Connexions
		self.m_ui.planning.selectedDateChanged.connect(self.selectedDateChanged)
		self.m_ui.bookingsTable.bookingSelected.connect(self.selectedBookingChanged)
		self.m_ui.bookingsTable.bookingDoubleClicked.connect(self.selectedBookingDoubleClicked)
		self.m_ui.buttonNewBooking.clicked.connect(self.newBooking)
		self.m_ui.buttonEditSelectedBooking.clicked.connect(self.editSelectedBooking)

		# Etat initial
		self.m_ui.bookingForm.setReadOnly(True)
		
	def updateData(self) :
		self.m_ui.planning.updateData()
		self.selectedDateChanged(self.m_ui.planning.selectedDate())
			
	def selectedDateChanged(self, date) :
		print "selectedDateChanged"
		bookings = []
		if (self.m_ui.planning.bookingsDataByDate().has_key(date) == True) :
			bookingsData = self.m_ui.planning.bookingsDataByDate()[date]
			if (bookingsData != None) :
				for bookingData in bookingsData :
					bookings.append(self.m_db.loadBooking(bookingData[2]["rowid"]))					
		
		self.m_ui.bookingsTable.setBookings(bookings)

	def selectedBookingChanged(self, booking) :
		self.m_ui.bookingForm.setBooking(booking)
		self.m_ui.buttonEditSelectedBooking.setVisible(self.m_ui.bookingForm.booking() != None)

	def selectedBookingDoubleClicked(self, clientIndex) :
		self.editSelectedBooking()
			
	def newBooking(self) :
		if (BookingCreateDialog().showDialog() == ModalDialog.Result.Ok) :
			self.updateData()
			
	def editSelectedBooking(self) :
		if (BookingEditDialog(self.m_ui.bookingForm.booking()).showDialog() == ModalDialog.Result.Ok) :
			self.updateData()

	def showEvent(self, event) :
		super(BookingList, self).showEvent(event)
		self.updateData()
