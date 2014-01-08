# -*- coding: utf-8 -*-

import copy
from PyQt4					import QtCore, QtGui
from Booking				import Booking
from Tools.StringConvert	import *
from BookingList_ui			import Ui_BookingList

class BookingList(QtGui.QFrame) :

	def __init__(self) :
		super(BookingList, self).__init__()
		
		# Membres
		self.m_ui		= Ui_BookingList()
		
		# Initialisation
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.planning.selectedDateChanged.connect(self.selectedDateChanged)

		# Etat initial
		
	def selectedDateChanged(self, date) :
		print "selectedDateChanged({0})".format(date2str(date))
		