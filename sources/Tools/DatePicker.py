from PyQt4 import QtCore, QtGui
from DatePicker_ui import Ui_DatePicker

class DatePicker(QtGui.QDialog) :

	def __init__(self) :
		super(DatePicker, self).__init__()
		
		self.m_ui = Ui_DatePicker()
		self.m_ui.setupUi(self)
		self.m_ui.calendar.clicked.connect(self.dateClicked)
		self.setWindowFlags(QtCore.Qt.Popup)
		self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.hide()

	def selectDate(self, button) :
		position = button.mapToGlobal(QtCore.QPoint(0, button.height()))
		self.setGeometry(position.x(), position.y(), 375, 250)
		if (self.exec_() == QtGui.QDialog.Accepted) :
			return self.m_ui.calendar.selectedDate()
		else :
			return QtCore.QDate()
		
	def dateClicked(self) :
		self.accept()
		
	def mousePressEvent(self, event) :
		print event.globalPos()
