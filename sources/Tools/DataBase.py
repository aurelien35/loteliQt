import sqlite3
from PyQt4	import QtCore

class DataBase(object) :

	def __init__(self) :
		self.m_db		= sqlite3.connect('D:/Dev/loteliQt/data/loteli.sqlite3')
		self.m_cursor	= self.m_db.cursor()
		
	def insertClient(self, client) :
		self.m_cursor.execute('''INSERT INTO clients(name, firstName, birthDate, phones, emails, address, comment) VALUES(?,?,?,?,?,?,?)''', (
								str(client.name().toUtf8()),
								str(client.firstName().toUtf8()),
								str(client.birthDate().toString("yyyy-MM-dd").toUtf8()),
								str(client.phones().join("¤").toUtf8()),
								str(client.emails().join("¤").toUtf8()),
								str(client.address().toUtf8()),
								str(client.comment().toUtf8())))
		self.m_db.commit()
		print "insertClient !"
