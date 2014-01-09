﻿# -*- coding: utf-8 -*-
		  
import math
from PyQt4					import QtCore, QtGui
from Tools.StringConvert	import *

class BookingTableView(QtGui.QTableView) :

	def __init__(self, parent=None) :
		super(BookingTableView, self).__init__(parent)
		
		# Membres
		self.m_bookings			= None
		self.m_model			= QtGui.QStandardItemModel()
		self.m_selectionModel	= None
		
		# Initialisation
		self.setFrameShape(QtGui.QFrame.Box)
		self.setFrameShadow(QtGui.QFrame.Plain)
		self.setLineWidth(2)
		self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.setTabKeyNavigation(False)
		self.setDropIndicatorShown(False)
		self.setDragDropOverwriteMode(False)
		self.setAlternatingRowColors(True)
		self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
		self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
		self.setCornerButtonEnabled(False)
		self.verticalHeader().setVisible(False)
		self.setModel(self.m_model)
		labelsQStringList = QtCore.QStringList()
		labelsQStringList.append(u"  Début  ")
		labelsQStringList.append(u"   Fin   ")
		labelsQStringList.append(u"  Nuits  ")
		labelsQStringList.append(u"  Chambres  ")
		labelsQStringList.append(u"  Clients  ")
		self.m_model.setHorizontalHeaderLabels(labelsQStringList)
		self.m_model.setColumnCount(labelsQStringList.count())
		self.m_selectionModel = self.selectionModel()
		
		# Connexions
		self.clicked.connect(self.itemClicked)
		self.doubleClicked.connect(self.itemDoubleClicked)
		self.m_selectionModel.selectionChanged.connect(self.itemSelectionChanged)

	def bookings(self) :
		return self.m_bookings
		
	def setBookings(self, bookings) :
		self.m_bookings	= bookings

		self.m_model.setRowCount(0)
		if (self.m_bookings != None) :
			for booking in self.m_bookings :
				items = []
				items.append(QtGui.QStandardItem(date2QString(booking.date())))
				items.append(QtGui.QStandardItem(date2QString(booking.endDate())))
				items.append(QtGui.QStandardItem(str2QString(unicode(booking.days()))))
				
				roomsLabels = []
				for room in booking.rooms() :
					roomsLabels.append(u"N°" + room.number() + u" - " + room.name())
				items.append(QtGui.QStandardItem(u"\n".join(roomsLabels)))
				
				clientsLabels = []
				for client in booking.clients() :
					clientsLabels.append(client.name() + u" " + client.firstName())
				items.append(QtGui.QStandardItem(u"\n".join(clientsLabels)))
				
				self.m_model.appendRow(items)
				
		self.resizeColumnsToContents()
		self.resizeRowsToContents()
		self.horizontalHeader().setStretchLastSection(True)
		self.itemSelectionChanged()

	def itemClicked(self, modelIndex) :
		print "itemClicked"
		# self.rowClicked.emit(modelIndex.data(QtCore.Qt.UserRole).toPyObject())
		
	def itemDoubleClicked(self, modelIndex) :
		print "itemDoubleClicked"
		# self.rowDoubleClicked.emit(modelIndex.data(QtCore.Qt.UserRole).toPyObject())
		
	def itemSelectionChanged(self) :
		print "itemSelectionChanged"
		# selectedRow = -1
		# selectedRows = self.m_selectionModel.selectedRows()
		# if (selectedRows != None) :
			# if (len(selectedRows) > 0) :
				# selectedRow = selectedRows[0].data(QtCore.Qt.UserRole).toPyObject()
		# self.rowSelected.emit(selectedRow)
