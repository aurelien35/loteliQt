# -*- coding: utf-8 -*-

import os
import sqlite3
from PyQt4					import QtCore
from Client.Client			import Client
from Tools.StringConvert	import *

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
				client.setPhones	(clientData["phones"].split(u"¤"))
				client.setEmails	(clientData["emails"].split(u"¤"))
				client.setAddress	(clientData["address"])
				client.setComment	(clientData["comment"])

		return client
		
		
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
		cursor.execute(u'''INSERT INTO clients(name, firstName, birthDate, phones, emails, address, comment) VALUES(?,?,?,?,?,?,?)''',
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
