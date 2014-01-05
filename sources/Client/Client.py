from PyQt4 import QtCore

class Client(object) :

	def __init__(self) :
		# Membres
		self.m_id			= -1
		self.m_name			= QtCore.QString()
		self.m_firstName	= QtCore.QString()
		self.m_birthDate	= QtCore.QDate()
		self.m_phones		= QtCore.QStringList()
		self.m_emails		= QtCore.QStringList()
		self.m_address		= QtCore.QString()
		self.m_comment		= QtCore.QString()

	def id(self) :
		return self.m_id
		
	def setId(self, id) :
		self.m_id = id	# TODO : checker le type

	def name(self) :
		return self.m_name
		
	def setName(self, name) :
		self.m_name = name	# TODO : checker le type

	def firstName(self) :
		return self.m_firstName
		
	def setFirstName(self, firstName) :
		self.m_firstName = firstName	# TODO : checker le type

	def birthDate(self) :
		return self.m_birthDate
		
	def birthDateString(self) :
		return self.m_birthDate.toString("dd/MM/yyyy (d MMMM yyyy)")
		
	def setBirthDate(self, birthDate) :
		self.m_birthDate = birthDate	# TODO : checker le type

	def phones(self) :
		return self.m_phones
		
	def setPhones(self, phones) :
		self.m_phones = phones	# TODO : checker le type

	def emails(self) :
		return self.m_emails
		
	def setEmails(self, emails) :
		self.m_emails = emails	# TODO : checker le type

	def address(self) :
		return self.m_address
		
	def setAddress(self, address) :
		self.m_address = address	# TODO : checker le type

	def comment(self) :
		return self.m_comment
		
	def setComment(self, comment) :
		self.m_comment = comment	# TODO : checker le type
