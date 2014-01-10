# -*- coding: utf-8 -*-
# SELECT
	# bookings.rowid,
	# bookings.date,
	# bookings.days,
	# clients.name,
	# clients.firstName,
	# rooms.name
# FROM
	# bookings
# LEFT JOIN 
	# clients
# ON
	# bookings.clients LIKE "%;" || clients.rowId || ";%"
# LEFT JOIN 
	# rooms
# ON
	# bookings.rooms LIKE "%;" || rooms.rowId || ";%"
# WHERE
	# bookings.date >= "2014-01-15"
# AND
	# date(bookings.date, "+" || bookings.days || " days") < "2014-03-15"


import os
import sqlite3
import datetime
from datetime				import *
from PyQt4					import QtCore
from Booking.Booking		import Booking
from Client.Client			import Client
from Room.Room				import Room
from Tools.StringConvert	import *

#TODO : logger les requetes

# Variable globale contenant le catalogue des chambres
RoomsCatalog = {}

def DataBaseRowFactory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

class DataBase(object) :

	def __init__(self) :
		self.m_db				= sqlite3.connect('./data/loteli.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
		self.m_db.row_factory	= DataBaseRowFactory
		
	def loadRoomsCatalog(self) :
		# TODO : gestion des erreurs : lever une exception
		global RoomsCatalog
		if (len(RoomsCatalog) == 0) :
			cursor = self.m_db.cursor()
			cursor.execute(u'''SELECT rowid, * FROM rooms ORDER BY rowid''')
			roomsData		= cursor.fetchall()
			RoomsCatalog	= {}
			for roomData in roomsData :
				room			= Room()
				room.m_id		= roomData["rowid"]
				room.m_number	= roomData["number"]
				room.m_name		= roomData["name"]
				RoomsCatalog[room.m_id] = room
				
		return RoomsCatalog	
		
	def loadClient(self, clientId) :
		# TODO : gestion des erreurs : lever une exception
		client = None
		cursor = self.m_db.cursor()
		cursor.execute(u'''SELECT rowid, * FROM clients WHERE rowid=:clientId''', {'clientId':clientId})
		result = cursor.fetchall()
		
		if (result != None) :
			if (len(result) == 1) :
				clientData = result[0]
				client				= Client()
				client.m_id 		= clientData["rowid"]
				client.setName		(clientData["name"])
				client.setFirstName	(clientData["firstName"])
				client.setBirthDate	(clientData["birthDate"])
				client.setPhones	(filter(None, clientData["phones"].split(u"¤")))
				client.setEmails	(filter(None, clientData["emails"].split(u"¤")))
				client.setAddress	(clientData["address"])
				client.setComment	(clientData["comment"])

		return client
		
	def loadBooking(self, bookingId) :
		# TODO : gestion des erreurs : lever une exception
		booking = None
		cursor = self.m_db.cursor()
		cursor.execute(u'''SELECT rowid, * FROM bookings WHERE rowid=:bookingId''', {'bookingId':bookingId})
		result = cursor.fetchall()
		
		if (result != None) :
			if (len(result) == 1) :
				roomsCatalog		= self.loadRoomsCatalog()
				bookingData			= result[0]
				booking				= Booking()
				booking.m_id 		= bookingData["rowid"]
				booking.setDate		(bookingData["date"])
				booking.setDays		(int(bookingData["days"]))
				booking.setComment	(bookingData["comment"])
				
				clientsId	= filter(None, bookingData["clients"].split(u"¤"))
				clients		= []
				for clientId in clientsId :
					clients.append(self.loadClient(clientId))
				booking.setClients(clients)
					
				roomsId	= filter(None, bookingData["rooms"].split(u"¤"))
				rooms	= []
				for roomId in roomsId :
					rooms.append(roomsCatalog[int(roomId)])
				booking.setRooms(rooms)

		return booking
		
	def loadBookingsByClientId(self, clientId) :
		# TODO : gestion des erreurs : lever une exception
		bookings = []
		cursor = self.m_db.cursor()
		cursor.execute(u'''SELECT rowid FROM bookings WHERE clients LIKE :clientId''', {'clientId':u"%¤" + str(clientId) + u"¤%"})
		data = cursor.fetchall()
		
		if (data != None) :
			for element in data :
				booking = self.loadBooking(element["rowid"])
				if (booking != None) :
					bookings.append(booking)

		return bookings
		
	def updateClient(self, client) :
		# TODO : gestion des erreurs : lever une exception
		cursor = self.m_db.cursor()
		cursor.execute(u'''UPDATE clients SET name=:name, firstName=:firstName, birthDate=:birthDate, phones=:phones, emails=:emails, address=:address, comment=:comment WHERE rowid=:rowid''',
						{	'name':			client.name(),
							'firstName':	client.firstName(),
							'birthDate':	client.birthDate(),
							'phones':		u"¤" + u"¤".join(client.phones()) + u"¤",
							'emails':		u"¤" + u"¤".join(client.emails()) + u"¤",
							'address':		client.address(),
							'comment':		client.comment(),
							'rowid':		client.id()			})
		self.m_db.commit()
		
	def insertClient(self, client) :
		# TODO : gestion des erreurs : lever une exception
		cursor = self.m_db.cursor()
		cursor.execute(u'''INSERT INTO clients(name, firstName, birthDate, phones, emails, address, comment) VALUES(:name, :firstName, :birthDate, :phones, :emails, :address, :comment)''',
						{	'name':			client.name(),
							'firstName':	client.firstName(),
							'birthDate':	client.birthDate(),
							'phones':		u"¤" + u"¤".join(client.phones()) + u"¤",
							'emails':		u"¤" + u"¤".join(client.emails()) + u"¤",
							'address':		client.address(),
							'comment':		client.comment()	})
		self.m_db.commit()
		
	def selectData(self, query, tokens) :
		# TODO : gestion des erreurs : lever une exception
		cursor = self.m_db.cursor()
		if (tokens == None) :
			cursor.execute(query)
		else :
			cursor.execute(query, tokens)
		data = cursor.fetchall()
		return data

	def selectBookings(self, month, year) :
		# TODO : gestion des erreurs : lever une exception
		startDate	= date(year, month, 1) - timedelta(10)			# Debut de la requete : 10 jours avant le 1er du mois
		endDate		= date(year, month, 1) + timedelta(40)			# Fin de la requete : 40 jours après le 1er du mois
		cursor		= self.m_db.cursor()
		cursor.execute(u'''SELECT rowid, * FROM bookings WHERE (date >= :startDate) AND date(date, "+" || days || " days") < :endDate ORDER BY date''', {'startDate':startDate, 'endDate':endDate})
		data		= cursor.fetchall()
		
		for element in data :
			element["clients"]	= filter(None, element["clients"].split(u"¤"))
			element["rooms"]	= filter(None, element["rooms"].split(u"¤"))

		return data
		