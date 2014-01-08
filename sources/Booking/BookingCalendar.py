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
		self.m_data					= None
		self.m_cellPen				= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_cellBrush			= QtGui.QBrush(QtGui.QColor(255, 255, 255))
		self.m_cellDisabledBrush	= QtGui.QBrush(QtGui.QColor(160, 160, 160))
		self.m_cellSelectedBrush	= QtGui.QBrush(QtGui.QColor(135, 139, 255))
		self.m_headerPen			= QtGui.QPen(QtGui.QColor(0, 0, 0), 1.0)
		self.m_headerBrush			= QtGui.QBrush(QtGui.QColor(83, 83, 83))
		self.m_titlePen				= QtGui.QPen(QtGui.QColor(255, 255, 255), 1.0)
		self.m_titleFont			= QtGui.QFont("Verdana", 10, 150, False)
		
		# Initialisation
		# Connexions
		self.currentPageChanged.connect(self.updateData)
		
		# Etat initial
		self.updateData()
		
	def paintCell(self, painter, rect, date) :
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
		titleRect = QtCore.QRect(rect.x(), rect.y(), rect.width(), 18)
		painter.setPen(self.m_headerPen)
		painter.setBrush(self.m_headerBrush)
		painter.drawRect(titleRect)
		painter.setPen(self.m_titlePen)
		painter.setFont(self.m_titleFont)
		painter.drawText(titleRect, QtCore.Qt.AlignCenter, QtCore.QString("%1").arg(date.day()))
		
		# painter.drawText(QtCore.QRectF(rect), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop, QtCore.QString("%1").arg(date.day()))
		
	def updateData(self) :
		self.m_data = None
		
		# Recherche des reservations et creation d'un index
		bookings = self.m_db.selectBookings(self.monthShown(), self.yearShown())
		if (len(bookings) > 0) :
			self.m_data = {}
			for booking in bookings :
				bookingDate = booking["date"]
				for day in range(booking["days"]) :
					if (self.m_data.has_key(bookingDate) == False) :
						self.m_data[bookingDate] = []
					self.m_data[bookingDate].append(booking)
					bookingDate	= bookingDate + timedelta(1)
				
		self.updateCells()
		
