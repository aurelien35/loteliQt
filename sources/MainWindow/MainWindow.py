# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
from PyQt4 import QtGui
import Room.RoomCatalog
import Client.Client
import Client.ClientList
import Booking.Booking

class MainWindow(QtGui.QMainWindow) :

	def __init__(self) :
		super(QtGui.QMainWindow, self).__init__()
		
		# Membres
		
		# print Room.RoomCatalog
	
		# print Client.Client()
		# client = Client.Client(409)
		# print client.name()
		# client.save()
		
		# client = Client.Client()
		# client.setName(u"Machin")
		# print client.name()
		# print client.id()
		# client.save()
		# print client.id()

		# clientList = Client.ClientList()
		# print "========================"
		# print clientList.clients()
		# clientList.load("to")
		# print "========================"
		# print clientList.clients()

		print Booking.Booking()
		booking = Booking.Booking(50)
		print booking.date()
		print booking.days()
		print booking.clients()
		print booking.rooms()
		
		# Connexions
		
		# Etat initial
		
	# def bookingClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.bookingList)
	
	# def clientsClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.clientList)
	
	# def billsClicked(self) :
		# self.m_ui.content.setCurrentWidget(self.m_ui.billList)
		
