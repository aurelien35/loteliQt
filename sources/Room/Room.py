# -*- coding: utf-8 -*-
		  
from PyQt4		import QtCore

class Room(object) :

	def __init__(self) :
		# Membres
		self.m_id		= -1
		self.m_number	= ""
		self.m_name		= ""

	def id(self) :
		return self.m_id

	def number(self) :
		return self.m_number

	def name(self) :
		return self.m_name
