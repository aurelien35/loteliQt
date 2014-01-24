# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
import datetime
import Tools.DataBase
import Client.Client
import Room.RoomCatalog

# TODO : controle du formulaire :
	# unicité des clients
	# unicité des chambres

class Booking(object) :

	def __init__(self, id=-1) :
		self.load(id)

	def id(self) :
		return self.m_id

	def date(self) :
		return self.m_date
		
	def setDate(self, date_) :
		if (type(date_) is datetime.date) :
			self.m_date = date_
		else :
			raise Exception("Booking::setDate : date is " + str(type(date_)) + ", not a date.")

	def days(self) :
		return self.m_days
		
	def setDays(self, days) :
		if (type(days) is int) :
			self.m_days = days
		else :
			raise Exception("Booking::setDays : days is " + str(type(days)) + ", not a integer.")

	def endDate(self) :
		if (self.m_date != None) :
			return self.m_date + datetime.timedelta(self.m_days)
		return None

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
			while (len(self.m_rooms) > 10) :
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
			
	def validate(self) :
		if (len(self.m_clients) == 0) :
			return u"Il n'y a aucun client pour cette réservation !";
		if (len(self.m_rooms) == 0) :
			return u"Il n'y a aucune chambre pour cette réservation !";
		if (self.m_days < 1) :
			return u"Aucune nuit dans cette réservation !";
		return None

	def load(self, id) :
		# Clear
		self.m_id		= -1
		self.m_date		= datetime.datetime.now().date()
		self.m_days		= 1
		self.m_clients	= []
		self.m_rooms	= []
		self.m_comment	= ""
		# Load
		if (id != -1) :
			# TODO : gestion des erreurs : lever une exception
			data = Tools.DataBase.selectOne(u'''SELECT rowid, * FROM bookings WHERE rowid=:bookingId''', {'bookingId':id})
			return self.loadData(data)
		return True
	
	def loadData(self, data) :
		if (data != None) :
			self.m_id 		= data["rowid"]
			self.setDate	(data["date"])
			self.setDays	(int(data["days"]))
			self.setComment	(data["comment"])
			
			clientsId	= filter(None, data["clients"].split(u"¤"))
			clients		= []
			for clientId in clientsId :
				clients.append(Client.Client(clientId))
			self.setClients(clients)
				
			roomsId	= filter(None, data["rooms"].split(u"¤"))
			rooms	= []
			for roomId in roomsId :
				rooms.append(Room.RoomCatalog[int(roomId)])
			self.setRooms(rooms)
			return True
		return False

	def save(self) :
		clientsIds	= []
		roomsIds	= []
		
		for client in booking.clients() :
			if (client != None) :
				clientsIds.append(str(client.id()))
				
		for room in booking.rooms() :
			if (room != None) :
				roomsIds.append(str(room.id()))
				
		values = {	'rowid':		self.m_id,
					'date':			self.m_date,
					'days':			self.m_days,
					'clients':		u"¤" + u"¤".join(clientsIds) + u"¤",
					'rooms':		u"¤" + u"¤".join(roomsIds) + u"¤",
					'comment':		self.m_comment		}

		# TODO : gestion des erreurs : lever une exception
		if (self.m_id == -1) :
			self.m_id = Tools.DataBase.insert(u'''INSERT INTO bookings (date, days, clients, rooms, comment)
												  VALUES (:date, :days, :clients, :rooms, :comment)''', values)
		else :
			 Tools.DataBase.update(u'''UPDATE bookings SET date=:date, days=:days, clients=:clients, rooms=:rooms, comment=:comment
									   WHERE rowid=:rowid''', values)
