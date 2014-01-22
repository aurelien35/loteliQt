# -*- coding: utf-8 -*-
		  
from PyQt4					import QtCore, QtGui
from Client.ClientList		import ClientList
from Booking.BookingForm	import BookingForm
from MainMenu_ui			import Ui_MainMenu

class MainMenu(QtGui.QFrame) :

	def __init__(self) :
		super(MainMenu, self).__init__()
		
		self.m_ui = Ui_MainMenu()
		self.m_ui.setupUi(self)
		self.m_ui.buttonWeb.clicked.connect(self.webClicked)
		self.m_ui.buttonHome.clicked.connect(self.homeClicked)
		
		self.m_clientList = ClientList()
		self.m_clientList.hide()
		
		self.m_bookingForm = BookingForm()
		self.m_bookingForm.hide()

	def webClicked(self) :
		self.m_clientList.show()

	def homeClicked(self) :
		self.m_bookingForm.show()
