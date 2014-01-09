# -*- coding: utf-8 -*-

import copy
from PyQt4					import QtCore, QtGui
from Booking				import Booking
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
		
		# Connexions
		self.m_ui.planning.selectedDateChanged.connect(self.selectedDateChanged)
		self.selectedDateChanged(self.m_ui.planning.selectedDate())

		# Etat initial
		
	def selectedDateChanged(self, date) :
		# self.m_ui.bookingForm
		
		# Date debut		Date fin		Nombre de nuits			Clients			Chambres
		bookings = []
		if (self.m_ui.planning.bookingsDataByDate().has_key(date) == True) :
			bookingsData = self.m_ui.planning.bookingsDataByDate()[date]
			if (bookingsData != None) :
				for bookingData in bookingsData :
					bookings.append(self.m_db.loadBooking(bookingData[2]["rowid"]))					
		
		self.m_ui.tableView.setBookings(bookings)
		print "selectedDateChanged({0})".format(date2str(date))
		