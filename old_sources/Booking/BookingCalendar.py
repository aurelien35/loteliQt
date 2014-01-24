﻿# -*- coding: utf-8 -*-

import copy
from datetime				import *
from PyQt4					import QtCore, QtGui
from Tools.DataBase			import DataBase
from Room					import RoomCatalog

class BookingCalendar(QtGui.QCalendarWidget) :
	def __init__(self, parent=None) :
		super(BookingCalendar, self).__init__(parent)
		
		# Membres
		self.m_db					= DataBase()
		self.m_bookingsDataByDate	= {}
		self.m_cellPen				= QtGui.QPen(QtGui.QColor(187, 187, 187), 1.0)
		self.m_cellBrush			= QtGui.QBrush(QtGui.QColor(255, 255, 255))
		self.m_cellDisabledBrush	= QtGui.QBrush(QtGui.QColor(242, 242, 242))
		self.m_cellSelectedBrush	= QtGui.QBrush(QtGui.QColor("#006064"))
		self.m_headerPen			= QtGui.QPen(QtGui.QColor(187, 187, 187), 1.0)
		self.m_headerBrush			= QtGui.QBrush(QtGui.QColor(242, 242, 242))
		self.m_titlePen				= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_titleFont			= QtGui.QFont("Verdana", 8, 250, False)
		self.m_roomsPen				= QtGui.QPen(QtGui.QColor(0, 0, 0), 0)
		self.m_roomsBrush			= QtGui.QBrush(QtGui.QColor(255, 171, 0, 128))
		self.m_roomsErrorBrush		= QtGui.QBrush(QtGui.QColor(255, 0, 0, 200))
		self.m_roomsFont			= QtGui.QFont("Arial", 8, 0, False)

		# Connexions
		self.currentPageChanged.connect(self.updateData)
		
		# Etat initial
		self.updateData()

	def bookingsDataByDate(self) :
		return self.m_bookingsDataByDate
	
	def paintCell(self, painter, rect, date) :
		
		# widgets = self.findChildren(QtGui.QWidget)
		# for widget in widgets :
			# print str(widget.objectName())  + u"  " + str(type(widget))
	
		painter.setRenderHints(QtGui.QPainter.TextAntialiasing, True)
		pyDate				= date.toPyDate()
		titleRectHeight		= 18
	
		# Cellule
		painter.setPen(self.m_cellPen)
		if (date.month() != self.monthShown()) :
			painter.setBrush(self.m_cellDisabledBrush)
		else :
			if (date == self.selectedDate()) :
				painter.setBrush(self.m_cellSelectedBrush)
			else :
				painter.setBrush(self.m_cellBrush)

		painter.drawRect(rect)

		# Titre
		titleRect = QtCore.QRect(rect.x(), rect.y(), rect.width(), titleRectHeight)
		painter.setPen(self.m_headerPen)
		painter.setBrush(self.m_headerBrush)
		painter.drawRect(titleRect)
		painter.setPen(self.m_titlePen)
		painter.setFont(self.m_titleFont)
		painter.drawText(titleRect.adjusted(1, 0, -2, 0), QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter, QtCore.QString("%1").arg(date.day()))

		# Reservations
		if (self.m_bookingsDataByDate.has_key(pyDate) == True) :
			roomsCount		= len(RoomCatalog.Instance)
			bookingsData	= self.m_bookingsDataByDate[pyDate]
			bookingsCount	= len(bookingsData);
			if (bookingsCount > 0) :
				roomsRectHeight	= (rect.height() - titleRectHeight) / roomsCount
				roomRects		= []
				roomRects.append(QtCore.QRect(rect.x(), rect.y() + titleRectHeight + 1, rect.width(), roomsRectHeight));
				for index in range(1, roomsCount) :
					roomRects.append(QtCore.QRect(rect.x(), roomRects[index-1].bottom()+1, rect.width(), roomsRectHeight));
				roomRects[-1].setBottom(rect.bottom()-1);
				
				painter.save()
				painter.setPen(self.m_roomsPen)
				painter.setBrush(self.m_roomsBrush)
				painter.setFont(self.m_roomsFont)
				painter.setClipRect(rect)
				
				for bookingData in bookingsData :
					start	= bookingData[0]
					stop	= bookingData[1]
					for roomId in bookingData[2]["rooms"] :
						roomId		= int(roomId)
						roomRect	= QtCore.QRect(roomRects[roomId-1])

						# Draw rect
						if (start == False) :
							roomRect.adjust(-1, 0, 0, 0)
						else :
							roomRect.adjust(1, 0, 0, 0)
						if (stop == True) :
							roomRect.adjust(0, 0, -1, 0)
							
							
						painter.drawRect(roomRect)
						
						# Draw label
						if (start == True) :
							painter.drawText(roomRect.adjusted(4, 0.5, 0, 2), QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, RoomCatalog.Instance[roomId].name())
							
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
		