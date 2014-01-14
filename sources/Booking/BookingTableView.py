# -*- coding: utf-8 -*-
		  
import math
from PyQt4					import QtCore, QtGui
from Tools.StringConvert	import *

class BookingTableView(QtGui.QTableView) :

	# Signaux
	bookingSelected			= QtCore.pyqtSignal(object)
	bookingClicked			= QtCore.pyqtSignal(object)
	bookingDoubleClicked	= QtCore.pyqtSignal(object)
	
	def __init__(self, parent=None) :
		super(BookingTableView, self).__init__(parent)
		
		# Membres
		self.m_bookings			= None
		self.m_model			= QtGui.QStandardItemModel()
		self.m_selectionModel	= None
		
		# Initialisation
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
		tableViewPalette = self.palette()
		tableViewPalette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight,		tableViewPalette.brush(QtGui.QPalette.Active, QtGui.QPalette.Highlight))
		tableViewPalette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText,	tableViewPalette.brush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText))
		self.setPalette(tableViewPalette)
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
		self.bookingClicked.emit(self.m_bookings[modelIndex.row()])
		
	def itemDoubleClicked(self, modelIndex) :
		self.bookingDoubleClicked.emit(self.m_bookings[modelIndex.row()])
		
	def itemSelectionChanged(self) :
		selectedBooking = None
		selectedRows = self.m_selectionModel.selectedRows()
		if (selectedRows != None) :
			if (len(selectedRows) > 0) :
				selectedBooking = self.m_bookings[selectedRows[0].row()]
		self.bookingSelected.emit(selectedBooking)
