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
		self.m_roomsCatalog			= self.m_db.loadRoomsCatalog()
		self.m_bookingsDataByDate	= {}
		self.m_cellPen				= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_cellBrush			= QtGui.QBrush(QtGui.QColor(255, 255, 255))
		self.m_cellDisabledBrush	= QtGui.QBrush(QtGui.QColor(160, 160, 160))
		self.m_cellSelectedBrush	= QtGui.QBrush(QtGui.QColor(135, 139, 255))
		self.m_headerPen			= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_headerBrush			= QtGui.QBrush(QtGui.QColor(83, 83, 83))
		self.m_titlePen				= QtGui.QPen(QtGui.QColor(255, 255, 255), 1.0)
		self.m_titleFont			= QtGui.QFont("Verdana", 8, 250, False)
		self.m_roomsPen				= QtGui.QPen(QtGui.QColor(0, 0, 0), 0)
		self.m_roomsBrush			= QtGui.QBrush(QtGui.QColor(255, 178, 0, 128))
		self.m_roomsFont			= QtGui.QFont("Arial", 8, 0, False)

		# Connexions
		self.currentPageChanged.connect(self.updateData)
		
		# Etat initial
		self.updateData()

	def bookingsDataByDate(self) :
		return self.m_bookingsDataByDate
	
	def paintCell(self, painter, rect, date) :
		painter.setRenderHints(QtGui.QPainter.TextAntialiasing, True)
		pyDate				= date.toPyDate()
		titleRectHeight		= 18
	
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

		# Reservations
		if (self.m_bookingsDataByDate.has_key(pyDate) == True) :
			roomsCount		= len(self.m_roomsCatalog)
			bookingsData	= self.m_bookingsDataByDate[pyDate]
			bookingsCount	= len(bookingsData);
			if (bookingsCount > 0) :
				roomsRectHMargin	= 3.0
				roomsRectVMargin	= 0.0
				roomsRectRadius		= 5.0
				roomsRectSpacing	= 0.0
				roomsRectHeight		= (rect.height()+1.0 - titleRectHeight - roomsRectVMargin - roomsRectVMargin - (roomsCount-1.0) * roomsRectSpacing) / roomsCount
				
				painter.save()
				painter.setPen(self.m_roomsPen)
				painter.setBrush(self.m_roomsBrush)
				painter.setFont(self.m_roomsFont)
				painter.setClipRect(rect)
				
				for bookingData in bookingsData :
					start	= bookingData[0]
					stop	= bookingData[1]
					for roomId in filter(None, bookingData[2]["rooms"].split(";")) :
						roomId = int(roomId)
						roomRect = QtCore.QRect(rect.x(),
												rect.y() + titleRectHeight + roomsRectVMargin + (roomsRectHeight + roomsRectSpacing) * (roomId-1.0),
												rect.width(),
												roomsRectHeight)

						# Draw rect
						if (start == True) :
							roomRect.adjust(roomsRectHMargin, 0, 0, 0)
						else :
							roomRect.adjust(-10, 0, 0, 0)
							
						if (stop == True) :
							roomRect.adjust(0, 0, -roomsRectHMargin, 0)
						else :
							roomRect.adjust(0, 0, 10, 0)
							
						painter.drawRoundedRect(roomRect, roomsRectRadius, roomsRectRadius)
						
						# Draw label
						if (start == True) :
							painter.drawText(roomRect.adjusted(2 + roomsRectRadius, 0.5, 0, 2), QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, self.m_roomsCatalog[roomId]["name"])
							
				painter.restore()
				
		
	def updateData(self) :
		self.m_bookingsDataByDate = {}
		
		# Recherche des reservations
		bookingsData = self.m_db.selectBookings(self.monthShown(), self.yearShown())
		
		if (len(bookingsData) > 0) :
			# Creation d'un index des reservations par date et d'un index des chambres par date
			for bookingData in bookingsData :
				bookingDate = bookingData["date"]
				bookingDays	= bookingData["days"]
				for day in range(bookingDays) :
				
					# Creation de la liste des reservation pour cette date
					if (self.m_bookingsDataByDate.has_key(bookingDate) == False) :
						self.m_bookingsDataByDate[bookingDate] = []
						
					# Ajout dans la liste des reservations pour cette date
					start	= (day == 0)
					stop	= (day == bookingDays-1)
					self.m_bookingsDataByDate[bookingDate].append((start, stop, bookingData))
						
					# Incrementation de la date
					bookingDate	= bookingDate + timedelta(1)
				
		self.updateCells()
		
