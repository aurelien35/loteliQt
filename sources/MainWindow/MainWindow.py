﻿# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
from PyQt4 import QtGui
import MainWindow_ui

class MainWindow(QtGui.QFrame) :

	def __init__(self) :
		super(QtGui.QFrame, self).__init__()
		
		# Membres
		self.m_ui = MainWindow_ui.Ui_MainWindow()

		# Etat initial
		self.m_ui.setupUi(self)
		
		# Connexions
		
	# def bookingClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.bookingList)
	
	# def clientsClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.clientList)
	
	# def billsClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.billList)
		
