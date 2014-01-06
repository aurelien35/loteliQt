# -*- coding: utf-8 -*-

import sqlite3
from PyQt4					import QtCore
from Tools.StringConvert	import *

class DataBase(object) :

	def __init__(self) :
		self.m_db		= sqlite3.connect('D:/Dev/loteliQt/data/loteli.sqlite3')
		self.m_cursor	= self.m_db.cursor()
		
	def insertClient(self, client) :
		self.m_cursor.execute('''INSERT INTO clients(name, firstName, birthDate, phones, emails, address, comment) VALUES(?,?,?,?,?,?,?)''', (
								client.name(),
								client.firstName(),
								date2str(client.birthDate()),
								u"¤".join(client.phones()),
								u"¤".join(client.emails()),
								client.address(),
								client.comment()))
		self.m_db.commit()
		print "insertClient !"
