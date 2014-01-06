# -*- coding: utf-8 -*-

from PyQt4				import QtCore, QtGui
from Tools.ModalDialog	import ShowModalDialog
from Tools.ModalDialog	import ModalDialog
from DatePicker_ui		import Ui_DatePicker

def SelectDate(button, date) :
	position	= button.mapToGlobal(QtCore.QPoint(0, button.height()))
	datePicker	= DatePicker(date)
	result		= ShowModalDialog(datePicker, "Choisir une date", None, "Annuler", "Effacer", datePicker.m_ui.calendar.clicked, position)
	if (result == ModalDialog.Result.Ok) :
		return datePicker.m_ui.calendar.selectedDate()
	elif (result == ModalDialog.Result.Cancel) :
		return date
	return QtCore.QDate()

class DatePicker(QtGui.QDialog) :

	def __init__(self, date) :
		super(DatePicker, self).__init__()
		
		self.m_ui = Ui_DatePicker()
		self.m_ui.setupUi(self)
		self.m_ui.calendar.setSelectedDate(date)
		self.resize(375, 300)
