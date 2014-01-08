# -*- coding: utf-8 -*-

import copy
from PyQt4					import QtCore, QtGui

# TODO : le calendrier ne doit pas réagir à la touche "entrée" ?

class BookingCalendar(QtGui.QCalendarWidget) :
	def __init__(self, parent=None) :
		super(BookingCalendar, self).__init__(parent)
		
	def paintCell(self, painter, rect, date) :
		super(BookingCalendar, self).paintCell(painter, rect, date)
