# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
import Tools.DataBase
import Client
	
class ClientList(object) :

	def __init__(self) :
		self.m_clients = []
	
	def clients(self) :
		return self.m_clients
		
	def load(self, filter) :
		# Clear
		self.m_clients = []
		# Load
		# TODO : gestion des erreurs : lever une exception
		query = u'''SELECT rowid, * FROM clients'''
		if (filter != None) :
			query = query + u''' WHERE name LIKE :filter OR firstName LIKE :filter OR phones LIKE :filter OR emails LIKE :filter OR address LIKE :filter OR comment LIKE :filter'''
		query = query + u''' ORDER BY name'''
		result = Tools.DataBase.select(query, {'filter':u"%{0}%".format(filter)})
		for data in result :
			client = Client.Client()
			client.loadData(data)
			self.m_clients.append(client)
