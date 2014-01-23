# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
from PyQt4 import QtGui
import ClientTab_ui

class ClientTab(QtGui.QFrame) :

	def __init__(self) :
		super(QtGui.QFrame, self).__init__()
		
		# Membres
		self.m_ui = ClientTab_ui.Ui_ClientTab()
		
		# Etat initial
		self.m_ui.setupUi(self)
		
		# Connexions
				
	# def bookingClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.bookingList)
	
	# def clientsClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.clientList)
	
	# def billsClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.billList)
		
