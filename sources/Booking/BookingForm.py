# -*- coding: utf-8 -*-

import sip
from PyQt4					import QtCore, QtGui
from Tools.DatePicker		import SelectDate
from Tools.StringConvert	import *
from Booking				import Booking
from BookingForm_ui			import Ui_BookingForm

class BookingForm(QtGui.QFrame) :

	def __init__(self, parent=None) :
		super(BookingForm, self).__init__(parent)
		
		# Membres
		self.m_ui						= Ui_BookingForm()
		self.m_isReadOnly				= False
		self.m_booking					= None
		
		# Initialisation
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.textEditComment.textChanged.connect(self.bookingCommentChanged)

		# Etat initial
		self.setReadOnly(False)
		self.setBooking(None)
		
	def isReadOnly(self) :
		return self.m_isReadOnly

	def setReadOnly(self, readOnly) :
		self.m_isReadOnly = readOnly
		effectiveReadOnly = self.m_isReadOnly
		if (effectiveReadOnly == False) :
			if (self.m_booking == None) :
				effectiveReadOnly = True
		self.m_ui.textEditComment.setReadOnly(effectiveReadOnly)
		# TODO

	def booking(self) :
		return self.m_booking

	def setBooking(self, booking) :
		self.m_booking = booking
		# TODO
		self.updateFormsValues()
		self.setReadOnly(self.isReadOnly())

	def updateFormsValues(self) :
		if (self.m_booking != None) :
			self.m_ui.lineEditDate.setText(date2QString(self.m_booking.date()))
			self.m_ui.lineEditDays.setText(str2QString(self.m_booking.days()))
			self.m_ui.textEditComment.setText(str2QString(self.m_booking.comment()))
			# TODO
		else :
			self.m_ui.lineEditDate.setText(QtCore.QString())
			self.m_ui.lineEditDays.setText(QtCore.QString())
			self.m_ui.textEditComment.setText(QtCore.QString())
			# TODO
				
	def bookingCommentChanged(self) :
		if (self.m_booking != None) :
			self.m_booking.setComment(QString2str(self.m_ui.textEditComment.toPlainText()))
