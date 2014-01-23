# -*- coding: utf-8 -*-
		  
from PyQt4 import QtCore
import Tools.DataBase
	
class Client(object) :

	def __init__(self, id=-1) :
		self.load(id)

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

	def phones(self) :
		return self.m_phones
		
	def setPhones(self, phones) :
		if (type(phones) is list) :
			self.m_phones = phones
			print phones
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

	def load(self, id) :
		# Clear
		self.m_id			= -1
		self.m_name			= ""
		self.m_firstName	= ""
		self.m_phones		= []
		self.m_emails		= []
		self.m_address		= ""
		self.m_comment		= ""
		# Load
		if (id != -1) :
			# TODO : gestion des erreurs : lever une exception
			data = Tools.DataBase.selectOne(u'''SELECT rowid, * FROM clients WHERE rowid=:clientId''', {'clientId':id})
			return self.loadData(data)
		return True
	
	def loadData(self, data) :
		if (data != None) :
			self.m_id 			= data["rowid"]
			self.setName		(data["name"])
			self.setFirstName	(data["firstName"])
			self.setPhones		(filter(None, data["phones"].split(u"¤")))
			self.setEmails		(filter(None, data["emails"].split(u"¤")))
			self.setAddress		(data["address"])
			self.setComment		(data["comment"])
			return True
		return False

	def save(self) :
		values = {	'rowid':		self.m_id,
					'name':			self.m_name,
					'firstName':	self.m_firstName,
					'phones':		u"¤" + u"¤".join(self.m_phones) + u"¤",
					'emails':		u"¤" + u"¤".join(self.m_emails) + u"¤",
					'address':		self.m_address,
					'comment':		self.m_comment}

		# TODO : gestion des erreurs : lever une exception
		if (self.m_id == -1) :
			self.m_id = Tools.DataBase.insert(u'''INSERT INTO clients (name, firstName, phones, emails, address, comment)
												  VALUES (:name, :firstName, :phones, :emails, :address, :comment)''', values)
		else :
			 Tools.DataBase.update(u'''UPDATE clients SET name=:name, firstName=:firstName, phones=:phones, emails=:emails, address=:address, comment=:comment
									   WHERE rowid=:rowid''', values)
