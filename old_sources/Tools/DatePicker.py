# -*- coding: utf-8 -*-

from PyQt4				import QtCore, QtGui
from Tools.ModalDialog	import *

def SelectDate(button, date, clearEnabled=True) :
	datePicker	= DatePicker(date, clearEnabled)
	result		= datePicker.showDialog(button.mapToGlobal(QtCore.QPoint(0, button.height())))
	if (result == ModalDialog.Result.Ok) :
		return datePicker.m_calendar.selectedDate().toPyDate()
	elif (result == ModalDialog.Result.Cancel) :
		return date
	return None

class DatePicker(ModalDialog) :

	def __init__(self, date, clearEnabled) :
		if (clearEnabled == True) :
			super(DatePicker, self).__init__(u"Choisir une date", u"Ok", u"Annuler", u"Effacer")
		else :
			super(DatePicker, self).__init__(u"Choisir une date", u"Ok", u"Annuler")
		
		self.m_calendar	= QtGui.QCalendarWidget()
		self.m_calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
		self.m_calendar.setGridVisible(True)
		self.m_calendar.setHorizontalHeaderFormat(QtGui.QCalendarWidget.LongDayNames)
		self.m_calendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
		self.m_calendar.setDateEditEnabled(False)
		self.setContent(self.m_calendar, 0)
		
		if (date != None) :
			self.m_calendar.setSelectedDate(QtCore.QDate(date.year, date.month, date.day))
		self.resize(375, 300)
		
		self.m_calendar.clicked.connect(self.buttonOkClicked)
