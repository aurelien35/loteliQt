# -*- coding: utf-8 -*-

import copy
from PyQt4				import QtCore, QtGui
from Booking			import Booking
from BookingList_ui		import Ui_BookingList

class BookingList(QtGui.QFrame) :

	def __init__(self) :
		super(BookingList, self).__init__()
		
		# Membres
		self.m_ui		= Ui_BookingList()
		
		# Initialisation
		self.m_ui.setupUi(self)
		
		# Connexions

		# Etat initial
		
