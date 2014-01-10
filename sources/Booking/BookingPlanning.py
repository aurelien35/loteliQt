# -*- coding: utf-8 -*-

import copy
from datetime				import date
from PyQt4					import QtCore, QtGui
from Booking				import Booking
from BookingPlanning_ui		import Ui_BookingPlanning
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *
from Tools.ModalDialog		import *

class BookingPlanning(QtGui.QFrame) :

	# Signaux
	dateClicked			= QtCore.pyqtSignal(date)
	dateDoubleClicked	= QtCore.pyqtSignal(date)
	selectedDateChanged	= QtCore.pyqtSignal(date)
	
	def __init__(self, parent=None) :
		super(BookingPlanning, self).__init__(parent)
		
		# Membres
		self.m_ui			= Ui_BookingPlanning()
		self.m_db			= DataBase()
		self.m_selectedDate	= None
		
		# Initialisation
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.calendar.activated.connect(self.calendarDateDoubleClicked)
		self.m_ui.calendar.clicked.connect(self.calendarDateClicked)
		self.m_ui.calendar.currentPageChanged.connect(self.calendarPageChanged)
		self.m_ui.calendar.selectionChanged.connect(self.calendarSelectionChanged)
		
		# Etat initial
		self.calendarPageChanged(self.m_ui.calendar.yearShown(), self.m_ui.calendar.monthShown())
		self.calendarSelectionChanged()
		
	def bookingsDataByDate(self) :
		return self.m_ui.calendar.bookingsDataByDate()
	
	def selectedDate(self) :
		return self.m_selectedDate
		
	def calendarDateDoubleClicked(self, qDate) :
		date = qDate.toPyDate()
		self.dateClicked.emit(date)
		ShowWarning("Erreur", "Erreur de test")
		
	def calendarDateClicked(self, qDate) :
		date = qDate.toPyDate()
		self.dateDoubleClicked.emit(date)
	
	def calendarPageChanged(self, year, month) :
		foo = None
		
	def calendarSelectionChanged(self) :
		self.m_selectedDate = self.m_ui.calendar.selectedDate().toPyDate()
		self.selectedDateChanged.emit(self.m_selectedDate)
