# -*- coding: utf-8 -*-
		  
from datetime	import date
from PyQt4		import QtCore

class Booking(object) :

	def __init__(self) :
		# Membres
		self.m_id		= -1
		self.m_date		= ""
		self.m_days		= 0
		self.m_clients	= []
		self.m_rooms	= []
		self.m_comment	= ""

	def id(self) :
		return self.m_id

	def date(self) :
		return self.m_date
		
	def setDate(self, date) :
		if (type(date) is date) :
			self.m_date = date
		else :
			raise Exception("Booking::setDate : date is " + str(type(date)) + ", not a date.")

	def days(self) :
		return self.m_days
		
	def setDays(self, days) :
		if (type(days) is integer) :
			self.m_days = firstName
		else :
			raise Exception("Booking::setDays : firstName is " + str(type(firstName)) + ", not a integer.")

	def clients(self) :
		return self.m_clients
		
	def setClients(self, clients) :
		if (type(clients) is list) :
			self.m_clients = clients
		else :
			raise Exception("Booking::setClients : clients is " + str(type(clients)) + ", not a client list.")

	def rooms(self) :
		return self.m_rooms
		
	def setRooms(self, rooms) :
		if (type(rooms) is list) :
			self.m_rooms = rooms
			while (len(self.m_rooms) > 5) :
				del(self.m_rooms[len(self.m_rooms)-1])
		else :
			raise Exception("Booking::setRooms : rooms is " + str(type(rooms)) + ", not a room list.")

	def comment(self) :
		return self.m_comment
		
	def setComment(self, comment) :
		if (type(comment) is unicode) :
			self.m_comment = comment
		else :
			raise Exception("Booking::setComment : comment is " + str(type(comment)) + ", not a string.")
