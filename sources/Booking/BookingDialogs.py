# -*- coding: utf-8 -*-
		  
from copy					import deepcopy
from datetime				import date
from Booking				import Booking
from BookingForm			import BookingForm
from Tools.DataBase			import DataBase
from Tools.ModalDialog		import *

class BookingCreateDialog(ModalDialog) :

	def __init__(self, date=None) :
		super(BookingCreateDialog, self).__init__(u"Nouvelle réservation", u"Ok", u"Annuler")
		
		self.m_booking		= Booking(date)
		self.m_bookingForm	= BookingForm()
		self.m_bookingForm.setBooking(self.m_booking)
		self.setContent(self.m_bookingForm, 9)
		
	def buttonOkClicked(self) :
		error = self.m_booking.validate()
		if (error != None) :
			ShowError(u"Erreur de saisie", error)
		else :
			# TODO : gerer les erreurs d'insertion
			DataBase().insertBooking(self.m_booking)
			super(BookingCreateDialog, self).buttonOkClicked()

class BookingEditDialog(ModalDialog) :

	def __init__(self, booking) :
		super(BookingEditDialog, self).__init__(u"Editer une réservation", u"Ok", u"Annuler")
		
		self.m_booking		= deepcopy(booking)
		self.m_bookingForm	= BookingForm()
		
		if (self.m_booking == None) :
			self.m_booking = Booking()
			
		self.m_bookingForm.setBooking(self.m_booking)
		self.setContent(self.m_bookingForm, 9)
		
	def buttonOkClicked(self) :
		error = self.m_booking.validate()
		if (error != None) :
			ShowError(u"Erreur de saisie", error)
		else :
			# TODO : gerer les erreurs d'update
			DataBase().updateBooking(self.m_booking)
			super(BookingEditDialog, self).buttonOkClicked()
