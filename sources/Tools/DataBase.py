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
from datetime				import *
from PyQt4					import QtCore
from Client.Client			import Client
from Tools.StringConvert	import *

#TODO : logger les requetes

class DataBase(object) :

	def __init__(self) :
		self.m_db				= sqlite3.connect('./data/loteli.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
		self.m_db.row_factory	= sqlite3.Row
		
	def loadClient(self, clientId) :
		client = None
		cursor = self.m_db.cursor()
		cursor.execute(u'''SELECT rowid, * FROM clients WHERE rowid=:clientId''', {'clientId':clientId})
		result = cursor.fetchall()
		
		if (result != None) :
			if (len(result) == 1) :
				clientData = result[0]
				client = Client()
				client.m_id 		= clientData["rowid"]
				client.setName		(clientData["name"])
				client.setFirstName	(clientData["firstName"])
				client.setBirthDate	(clientData["birthDate"])
				client.setPhones	(filter(None, clientData["phones"].split(u"¤")))
				client.setEmails	(filter(None, clientData["emails"].split(u"¤")))
				client.setAddress	(clientData["address"])
				client.setComment	(clientData["comment"])

		return client
		
	def loadRoomsCatalog(self) :
		cursor = self.m_db.cursor()
		cursor.execute(u'''SELECT rowid, * FROM rooms''')
		data	= cursor.fetchall()
		rooms	= {}
		for room in data :
			rooms[room["rowid"]] = room
		return rooms		
		
	def updateClient(self, client) :
		# TODO : gestion des erreurs : code de retour
		cursor = self.m_db.cursor()
		cursor.execute(u'''UPDATE clients SET name=:name, firstName=:firstName, birthDate=:birthDate, phones=:phones, emails=:emails, address=:address, comment=:comment WHERE rowid=:rowid''',
						{	'name':			client.name(),
							'firstName':	client.firstName(),
							'birthDate':	client.birthDate(),
							'phones':		u"¤".join(client.phones()),
							'emails':		u"¤".join(client.emails()),
							'address':		client.address(),
							'comment':		client.comment(),
							'rowid':		client.id()			})
		self.m_db.commit()
		
	def insertClient(self, client) :
		# TODO : gestion des erreurs : code de retour
		cursor = self.m_db.cursor()
		cursor.execute(u'''INSERT INTO clients(name, firstName, birthDate, phones, emails, address, comment) VALUES(:name, :firstName, :birthDate, :phones, :emails, :address, :comment)''',
						{	'name':			client.name(),
							'firstName':	client.firstName(),
							'birthDate':	client.birthDate(),
							'phones':		u"¤".join(client.phones()),
							'emails':		u"¤".join(client.emails()),
							'address':		client.address(),
							'comment':		client.comment()	})
		self.m_db.commit()
		
	def selectData(self, query, tokens) :
		cursor = self.m_db.cursor()
		if (tokens == None) :
			cursor.execute(query)
		else :
			cursor.execute(query, tokens)
		data = cursor.fetchall()
		return data

	def selectBookings(self, month, year) :
		# Debut de la requete : 10 jours avant le 1er du mois
		startDate = date(year, month, 1) - timedelta(10)
		
		# Fin de la requete : 40 jours après le 1er du mois
		endDate = date(year, month, 1) + timedelta(40)

		# Execution
		cursor = self.m_db.cursor()
		cursor.execute(u'''SELECT rowid, * FROM bookings WHERE (date >= :startDate) AND date(date, "+" || days || " days") < :endDate''', {'startDate':startDate, 'endDate':endDate})
		data = cursor.fetchall()

		# Decodage
		# for booking in data :
			# booking["roomsId"]		= filter(None, booking["rooms"].split(";"))
			# booking["clientsId"]	= filter(None, booking["clients"].split(";"))
			
		print "selectBookings : from {0} to {1}".format(date2str(startDate), date2str(endDate))
		return data
		