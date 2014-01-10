# -*- coding: utf-8 -*-
		  
from copy					import deepcopy
from datetime				import date
from Client					import Client
from ClientForm				import ClientForm
from Tools.DataBase			import DataBase
from Tools.ModalDialog		import *

class ClientCreateDialog(ModalDialog) :

	def __init__(self) :
		super(ClientCreateDialog, self).__init__(u"Nouveau client", u"Ok", u"Annuler")
		
		self.m_client		= Client()
		self.m_clientForm	= ClientForm()
		self.m_clientForm.setClient(self.m_client)
		self.setContent(self.m_clientForm, 9)
		
	def buttonOkClicked(self) :
		error = self.m_client.validate()
		if (error != None) :
			ShowError(u"Erreur de saisie", error)
		else :
			# TODO : gerer les erreurs d'insertion
			DataBase().insertClient(self.m_client)
			super(ClientCreateDialog, self).buttonOkClicked()

class ClientEditDialog(ModalDialog) :

	def __init__(self, client) :
		super(ClientEditDialog, self).__init__(u"Editer un client", u"Ok", u"Annuler")
		
		self.m_client		= deepcopy(client)
		self.m_clientForm	= ClientForm()
		
		if (self.m_client == None) :
			self.m_client = Client()
			
		self.m_clientForm.setClient(self.m_client)
		self.setContent(self.m_clientForm, 9)
		
	def buttonOkClicked(self) :
		error = self.m_client.validate()
		if (error != None) :
			ShowError(u"Erreur de saisie", error)
		else :
			# TODO : gerer les erreurs d'update
			DataBase().updateClient(self.m_client)
			super(ClientEditDialog, self).buttonOkClicked()
