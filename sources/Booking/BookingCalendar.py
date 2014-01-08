# -*- coding: utf-8 -*-

import copy
from datetime				import *
from PyQt4					import QtCore, QtGui
from Tools.DataBase			import DataBase

# TODO : le calendrier ne doit pas réagir à la touche "entrée" ?

class BookingCalendar(QtGui.QCalendarWidget) :
	def __init__(self, parent=None) :
		super(BookingCalendar, self).__init__(parent)
		
		# Membres
		self.m_db					= DataBase()
		self.m_bookingsByDate		= {}
		self.m_roomsByDate			= {}
		self.m_cellPen				= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_cellBrush			= QtGui.QBrush(QtGui.QColor(255, 255, 255))
		self.m_cellDisabledBrush	= QtGui.QBrush(QtGui.QColor(160, 160, 160))
		self.m_cellSelectedBrush	= QtGui.QBrush(QtGui.QColor(135, 139, 255))
		self.m_headerPen			= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_headerBrush			= QtGui.QBrush(QtGui.QColor(83, 83, 83))
		self.m_titlePen				= QtGui.QPen(QtGui.QColor(255, 255, 255), 1.0)
		self.m_titleFont			= QtGui.QFont("Verdana", 10, 150, False)
		self.m_bookingPen			= QtGui.QPen(QtGui.QColor(0, 0, 0), 2.0)
		self.m_bookingHalfFullBrush	= QtGui.QBrush(QtGui.QColor(255, 178, 0, 128))
		self.m_bookingFullBrush		= QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
		self.m_roomsPen				= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_roomsFont			= QtGui.QFont("Verdana", 8, 50, False)
		
		# Initialisation
		# Connexions
		self.currentPageChanged.connect(self.updateData)
		
		# Etat initial
		self.updateData()
		
	def paintCell(self, painter, rect, date) :
		painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing, True)
		pyDate				= date.toPyDate()
		titleRectHeight		= 18
		bookingRectMargin	= 6
		roomsRectMargin		= 4
	
		# Cellule
		if (date == self.selectedDate()) :
			painter.setBrush(self.m_cellSelectedBrush)
		else :
			if (date.month() != self.monthShown()) :
				painter.setBrush(self.m_cellDisabledBrush)
			else :
				painter.setBrush(self.m_cellBrush)
		painter.setPen(self.m_cellPen)
		painter.drawRect(rect)
		
		# Titre
		titleRect = QtCore.QRect(rect.x(), rect.y(), rect.width(), titleRectHeight)
		painter.setPen(self.m_headerPen)
		painter.setBrush(self.m_headerBrush)
		painter.drawRect(titleRect)
		painter.setPen(self.m_titlePen)
		painter.setFont(self.m_titleFont)
		painter.drawText(titleRect, QtCore.Qt.AlignCenter, QtCore.QString("%1").arg(date.day()))

		# Booking
		bookingRect	= QtCore.QRect(rect.x() + bookingRectMargin, rect.y() + bookingRectMargin + titleRectHeight, rect.width() - bookingRectMargin - bookingRectMargin, rect.height() - bookingRectMargin - bookingRectMargin - titleRectHeight)
		if (self.m_bookingsByDate.has_key(pyDate) == True) :
			bookings = self.m_bookingsByDate[pyDate]
			if (len(bookings) > 0) :
				painter.setPen(self.m_bookingPen)
				painter.setBrush(self.m_bookingFullBrush)
				painter.drawRoundedRect(bookingRect, 7.0, 7.0)
		
		# Chambres
		roomsRect = QtCore.QRect(bookingRect.x() + roomsRectMargin, bookingRect.y() + roomsRectMargin, bookingRect.width() - roomsRectMargin - roomsRectMargin, bookingRect.height() - roomsRectMargin - roomsRectMargin)
		if (self.m_roomsByDate.has_key(pyDate) == True) :
			rooms = self.m_roomsByDate[pyDate]
			if (len(rooms) > 0) :
				roomsLabel = ""
				for room in rooms :
					roomsLabel = roomsLabel + room["name"] + "\n"
				painter.setPen(self.m_roomsPen)
				painter.setFont(self.m_roomsFont)
				painter.drawText(roomsRect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop, roomsLabel)
				
		
	def updateData(self) :
		self.m_rooms			= self.m_db.loadRooms()
		self.m_bookingsByDate	= {}
		self.m_roomsByDate		= {}
		
		# Recherche des reservations
		bookings = self.m_db.selectBookings(self.monthShown(), self.yearShown())
		
		if (len(bookings) > 0) :
			# Creation d'un index des reservations par date et d'un index des chambres par date
			for booking in bookings :
				bookingDate = booking["date"]
				for day in range(booking["days"]) :
					# Creation de la liste des reservations
					if (self.m_bookingsByDate.has_key(bookingDate) == False) :
						self.m_bookingsByDate[bookingDate] = []
					# Creation de la liste des chambres
					if (self.m_roomsByDate.has_key(bookingDate) == False) :
						self.m_roomsByDate[bookingDate] = []
					# Ajout dans la liste des reservations
					self.m_bookingsByDate[bookingDate].append(booking)
					# Ajout dans la liste des chambres					# TODO : methodes split et join dans DataBase
					roomsId = filter(None, booking["rooms"].split(";"))
					for roomId in roomsId :
						self.m_roomsByDate[bookingDate].append(self.m_rooms[roomId])
					# Incrementation de la date
					bookingDate	= bookingDate + timedelta(1)
				
		self.updateCells()
		
