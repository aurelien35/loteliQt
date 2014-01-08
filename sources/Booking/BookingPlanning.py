﻿# -*- coding: utf-8 -*-

import copy
from datetime				import date
from PyQt4					import QtCore, QtGui
from Booking				import Booking
from BookingPlanning_ui		import Ui_BookingPlanning
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *

class BookingPlanning(QtGui.QFrame) :

	# Signaux
	dateClicked			= QtCore.pyqtSignal(date)
	dateDoubleClicked	= QtCore.pyqtSignal(date)
	selectedDateChanged	= QtCore.pyqtSignal(date)
	
	def __init__(self, parent=None) :
		super(BookingPlanning, self).__init__(parent)
		
		# Membres
		self.m_ui	= Ui_BookingPlanning()
		self.m_db	= DataBase()
		
		# Initialisation
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.calendar.activated.connect(self.calendarDateDoubleClicked)
		self.m_ui.calendar.clicked.connect(self.calendarDateClicked)
		self.m_ui.calendar.currentPageChanged.connect(self.calendarPageChanged)
		self.m_ui.calendar.selectionChanged.connect(self.calendarSelectionChanged)
		
		# Etat initial
		self.calendarPageChanged(self.m_ui.calendar.yearShown(), self.m_ui.calendar.monthShown())
		
	def calendarDateDoubleClicked(self, qDate) :
		date = qDate.toPyDate()
		print "calendarDateDoubleClicked({0})".format(date2str(date))
		self.dateClicked.emit(date)
		
	def calendarDateClicked(self, qDate) :
		date = qDate.toPyDate()
		print "calendarDateClicked({0})".format(date2str(date))
		self.dateDoubleClicked.emit(date)
	
	def calendarPageChanged(self, year, month) :
		print "calendarPageChanged({0}, {1})".format(year, month)
		
	def calendarSelectionChanged(self) :
		print "calendarSelectionChanged"
		self.selectedDateChanged.emit(self.m_ui.calendar.selectedDate().toPyDate())
