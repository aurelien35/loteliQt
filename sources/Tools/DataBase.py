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
		print "loadClient : {0}".format(str(clientId))
		cursor = self.m_db.cursor()
		cursor.execute('''SELECT rowid, * FROM clients WHERE rowid=?''', ((clientId),))
		result = cursor.fetchall()
		
		if (result == None) :
			print "	=> no result"
		elif (len(result) != 1) :
			print "	=> bad result count ({0})".format(str(len(result)))
		else :
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
		
	def insertClient(self, client) :
		cursor = self.m_db.cursor()
		cursor.execute('''INSERT INTO clients(name, firstName, birthDate, phones, emails, address, comment) VALUES(?,?,?,?,?,?,?)''', (
							client.name(),
							client.firstName(),
							date2str(client.birthDate()),
							u"¤".join(client.phones()),
							u"¤".join(client.emails()),
							client.address(),
							client.comment()))
		self.m_db.commit()
		print "insertClient !"
		
	def selectData(self, query) :
		cursor = self.m_db.cursor()
		cursor.execute(query)
		data = cursor.fetchall()
		print "selectData : {0} rows ".format(str(len(data)))
		return data
