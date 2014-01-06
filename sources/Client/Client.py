from datetime	import date
from PyQt4		import QtCore

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
		if (type(name) is str) :
			self.m_name = name
		else :
			raise Exception("Client::setName : name is " + type(name) + ", not a string.")

	def firstName(self) :
		return self.m_firstName
		
	def setFirstName(self, firstName) :
		if (type(firstName) is str) :
			self.m_firstName = firstName
		else :
			raise Exception("Client::setFirstName : firstName is " + type(firstName) + ", not a string.")

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
		if (type(phones) is not str) and (type(phones) is list) :
			self.m_phones = phones
		else :
			raise Exception("Client::setPhones : phones is " + type(phones) + ", not a string list.")

	def emails(self) :
		return self.m_emails
		
	def setEmails(self, emails) :
		if (type(emails) is not str) and (type(emails) is list) :
			self.m_emails = emails
		else :
			raise Exception("Client::setPhones : emails is " + type(emails) + ", not a string list.")

	def address(self) :
		return self.m_address
		
	def setAddress(self, address) :
		if (type(address) is str) :
			self.m_address = address
		else :
			raise Exception("Client::setAddress : address is " + type(address) + ", not a string.")

	def comment(self) :
		return self.m_comment
		
	def setComment(self, comment) :
		if (type(comment) is str) :
			self.m_comment = comment
		else :
			raise Exception("Client::setComment : comment is " + type(comment) + ", not a string.")
