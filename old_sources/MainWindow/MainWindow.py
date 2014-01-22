# -*- coding: utf-8 -*-
		  
from PyQt4					import QtCore, QtGui
from MainWindow_ui			import Ui_MainWindow
import MainWindowInstance

class MainWindow(QtGui.QFrame) :

	def __init__(self) :
		super(MainWindow, self).__init__()
		MainWindowInstance.Instance = self
		
		# Membres
		self.m_ui = Ui_MainWindow()
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.buttonBooking.clicked.connect(self.bookingClicked)
		self.m_ui.buttonClients.clicked.connect(self.clientsClicked)
		self.m_ui.buttonBills.clicked.connect(self.billsClicked)
		
		# Etat initial
		self.bookingClicked()
		# self.clientsClicked()
		# self.billsClicked()
		
	def bookingClicked(self) :
		self.m_ui.content.setCurrentWidget(self.m_ui.bookingList)
	
	def clientsClicked(self) :
		self.m_ui.content.setCurrentWidget(self.m_ui.clientList)
	
	def billsClicked(self) :
		self.m_ui.content.setCurrentWidget(self.m_ui.billList)
		
