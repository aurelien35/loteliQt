# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
from PyQt4 import QtGui
import Tools.DataBase
import ClientList

class ClientTableView(QtGui.QTableView) :

	def __init__(self, parent) :
		super(QtGui.QTableView, self).__init__(parent)
		
		# Membres
		self.m_columns				= [u"Id  ", u"Nom    ", u"Prénom    ", u"Téléphone     ", u"e-mail     "]
		self.m_model				= QtGui.QStandardItemModel()
		self.m_selectionModel		= None
		self.m_clientList			= ClientList.ClientList()
		self.m_filter				= None
		
		# Etat initial
		initialPalette = self.palette()
		initialPalette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight,			initialPalette.brush(QtGui.QPalette.Active, QtGui.QPalette.Highlight))
		initialPalette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText,	initialPalette.brush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText))
		self.setPalette(initialPalette)
		self.setAlternatingRowColors(True)
		self.setAutoScroll(True)
		self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
		self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		
		self.setModel(self.m_model)
		self.m_selectionModel = self.selectionModel()
		labels = QtCore.QStringList()
		for column in self.m_columns :
			labels.append(column)
		self.m_model.setHorizontalHeaderLabels(labels)
		self.m_model.setColumnCount(labels.count())
		self.horizontalHeader().setMinimumSectionSize(100)
		self.verticalHeader().setVisible(False)
		self.resizeColumnsToContents()
		self.horizontalHeader().setStretchLastSection(True)
		
		# Connexions
				
		self.reload()
		
	def setFilter(self, filter) :
		self.m_filter = filter
		self.reload()
	
	def reload(self) :
		self.m_clientList.load(self.m_filter)
		self.m_model.setRowCount(0)
		for client in self.m_clientList.clients() :
			items = self.createItems(client)
			self.m_model.appendRow(items)
		self.resizeRowsToContents()
		
	def createItems(self, client) :
		result = []
		result.append(QtGui.QStandardItem(str(client.id())))
		result.append(QtGui.QStandardItem(client.name()))
		result.append(QtGui.QStandardItem(client.firstName()))
		result.append(QtGui.QStandardItem(u"\n".join(client.emails())))
		result.append(QtGui.QStandardItem(u"\\n".join(client.phones())))
		return result
