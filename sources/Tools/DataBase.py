# -*- coding: utf-8 -*-

import sqlite3
from PyQt4					import QtCore
from Tools.StringConvert	import *

class DataBase(object) :

	def __init__(self) :
		self.m_db = sqlite3.connect('D:/Dev/loteliQt/data/loteli.sqlite3')
		
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
		print "selectData :"
		print str(len(data))
		return data
