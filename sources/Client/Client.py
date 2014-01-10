# -*- coding: utf-8 -*-
		  
from datetime	import date
from PyQt4		import QtCore

# TODO : controle du formulaire :
	# Au moins le nom de rempli
	
class Client(object) :

	def __init__(self) :
		# Membres
		self.m_id			= -1
		self.m_name			= ""
		self.m_firstName	= ""
		self.m_birthDate	= None
		self.m_phones		= []
		self.m_emails		= []
		self.m_address		= ""
		self.m_comment		= ""

	def id(self) :
		return self.m_id

	def name(self) :
		return self.m_name
		
	def setName(self, name) :
		if (type(name) is unicode) :
			self.m_name = name
		else :
			raise Exception("Client::setName : name is " + str(type(name)) + ", not a string.")

	def firstName(self) :
		return self.m_firstName
		
	def setFirstName(self, firstName) :
		if (type(firstName) is unicode) :
			self.m_firstName = firstName
		else :
			raise Exception("Client::setFirstName : firstName is " + str(type(firstName)) + ", not a string.")

	def birthDate(self) :
		return self.m_birthDate
		
	def setBirthDate(self, birthDate) :
		if (birthDate is None) :
			self.m_birthDate = None
		else :
			if (type(birthDate) is date) :
				self.m_birthDate = birthDate
			else :
				raise Exception("Client::setBirthDate : birthDate is " + str(type(birthDate)) + ", not a date.")

	def phones(self) :
		return self.m_phones
		
	def setPhones(self, phones) :
		if (type(phones) is list) :
			self.m_phones = phones
			while (len(self.m_phones) > 5) :
				del(self.m_phones[len(self.m_phones)-1])
		else :
			raise Exception("Client::setPhones : phones is " + str(type(phones)) + ", not a string list.")

	def emails(self) :
		return self.m_emails
		
	def setEmails(self, emails) :
		if (type(emails) is list) :
			self.m_emails = emails
			while (len(self.m_emails) > 5) :
				del(self.m_emails[len(self.m_emails)-1])
		else :
			raise Exception("Client::setEmails : emails is " + str(type(emails)) + ", not a string list.")

	def address(self) :
		return self.m_address
		
	def setAddress(self, address) :
		if (type(address) is unicode) :
			self.m_address = address
		else :
			raise Exception("Client::setAddress : address is " + str(type(address)) + ", not a string.")

	def comment(self) :
		return self.m_comment
		
	def setComment(self, comment) :
		if (type(comment) is unicode) :
			self.m_comment = comment
		else :
			raise Exception("Client::setComment : comment is " + str(type(comment)) + ", not a string.")
			
	def validate(self) :
		if (len(self.m_name) < 3) :
			return u"Le nom du client doit être rempli !";
		return None
