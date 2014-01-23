# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
import Tools.DataBase
import Booking
	
class BookingList(object) :

	def __init__(self) :
		self.m_bookings = []
	
	def bookings(self) :
		return self.m_bookings
		
	def loadByClient(self, client) :
		# Clear
		self.m_bookings = []
		# Load
		if (client != None) :
			# TODO : gestion des erreurs : lever une exception
			result = Tools.DataBase.select(u'''SELECT rowid FROM bookings WHERE clients LIKE :clientId ORDER BY date''', {'clientId':u"%¤{0}¤%".format(str(client.id()))})
			for data in result :
				booking = Booking.Booking()
				booking.loadData(data) # TODO : verifier la validité
				self.m_bookings.append(booking)
				
	def loadByMonth(self, month, year) :
		# Clear
		self.m_bookings = []
		# Load
		# TODO : gestion des erreurs : lever une exception
		startDate	= date(year, month, 1) - timedelta(10)			# Debut de la requete : 10 jours avant le 1er du mois
		endDate		= date(year, month, 1) + timedelta(40)			# Fin de la requete : 40 jours après le 1er du mois
		result		= Tools.DataBase.select(u'''SELECT rowid FROM bookings WHERE (date >= :startDate) AND date(date, "+" || days || " days") < :endDate ORDER BY date''', {'clientId':u"%¤{0}¤%".format(str(client.id()))})
		for data in result :
			booking = Booking.Booking()
			booking.loadData(data) # TODO : verifier la validité
			self.m_bookings.append(booking)
