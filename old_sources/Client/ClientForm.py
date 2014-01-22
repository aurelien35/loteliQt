# -*- coding: utf-8 -*-

import sip
from PyQt4					import QtCore, QtGui
from Tools.DatePicker		import SelectDate
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *
from Client					import Client
from ClientForm_ui			import Ui_ClientForm

class ClientForm(QtGui.QFrame) :

	def __init__(self, parent=None) :
		super(ClientForm, self).__init__(parent)
		
		# Membres
		self.m_ui				= Ui_ClientForm()
		self.m_isReadOnly		= False
		self.m_client			= None
		self.m_phonesEditors	= []
		self.m_emailsEditors	= []
		
		# Initialisation
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.lineEditName.editingFinished.connect(self.clientNameChanged)
		self.m_ui.lineEditFirstName.editingFinished.connect(self.clientFirstNameChanged)
		self.m_ui.textEditAddress.textChanged.connect(self.clientAddressChanged)
		self.m_ui.textEditComment.textChanged.connect(self.clientCommentChanged)
		self.m_ui.pushButtonSelectBirthDate.clicked.connect(self.selectBirthDate)

		# Etat initial
		self.setReadOnly(False)
		self.setClient(None)
		
	def isReadOnly(self) :
		return self.m_isReadOnly

	def setReadOnly(self, readOnly) :
		self.m_isReadOnly = readOnly
		effectiveReadOnly = self.m_isReadOnly
		if (effectiveReadOnly == False) :
			if (self.m_client == None) :
				effectiveReadOnly = True
		self.m_ui.lineEditName.setReadOnly(effectiveReadOnly)
		self.m_ui.lineEditFirstName.setReadOnly(effectiveReadOnly)
		self.m_ui.textEditAddress.setReadOnly(effectiveReadOnly)
		self.m_ui.textEditComment.setReadOnly(effectiveReadOnly)
		self.m_ui.pushButtonSelectBirthDate.setVisible(not effectiveReadOnly)
		for phoneEditor in self.m_phonesEditors :
			phoneEditor[0].setReadOnly(effectiveReadOnly)
			phoneEditor[1].setVisible(not effectiveReadOnly)
		for emailEditor in self.m_emailsEditors :
			emailEditor[0].setReadOnly(effectiveReadOnly)
			emailEditor[1].setVisible(not effectiveReadOnly)

	def client(self) :
		return self.m_client

	def setClient(self, client) :
		self.m_client = client
		self.updatePhonesEditors()
		self.updateEmailsEditors()
		self.updateFormsValues()
		self.setReadOnly(self.isReadOnly())

	def reloadClient(self) :
		if (self.m_client != None) :
			self.setClient(DataBase().loadClient(self.m_client.id()))
		
	def selectBirthDate(self) :
		if (self.m_client != None) :
			self.m_client.setBirthDate(SelectDate(self.m_ui.pushButtonSelectBirthDate, self.m_client.birthDate()))
			self.updateFormsValues()

	def addPhone(self) :
		if (self.m_client != None) :
			phones = self.m_client.phones()
			phones.append("")
			if (len(phones) == 1) :
				phones.append("")
			self.m_client.setPhones(phones)
			self.updatePhonesEditors()
			self.updateFormsValues();

	def removePhone(self) :
		if (self.m_client != None) :
			index = 0;
			phones = self.m_client.phones()
			for phoneEditor in self.m_phonesEditors :
				if (self.sender() == phoneEditor[1]) :
					del (phones[index])
					break
				index += 1
			self.m_client.setPhones(phones)
			self.updatePhonesEditors()
			self.updateFormsValues()
			
	def addEmail(self) :
		if (self.m_client != None) :
			emails = self.m_client.emails()
			emails.append("")
			if (len(emails) == 1) :
				emails.append("")
			self.m_client.setEmails(emails)
			self.updateEmailsEditors()
			self.updateFormsValues()

	def removeEmail(self) :
		if (self.m_client != None) :
			index = 0;
			emails = self.m_client.emails()
			for emailEditor in self.m_emailsEditors :
				if (self.sender() == emailEditor[1]) :
					del (emails[index])
					break
				index += 1
			self.m_client.setEmails(emails)
			self.updateEmailsEditors()
			self.updateFormsValues()
		
	def updateFormsValues(self) :
		if (self.m_client != None) :
			self.m_ui.lineEditName.setText(str2QString(self.m_client.name()))
			self.m_ui.lineEditFirstName.setText(str2QString(self.m_client.firstName()))
			self.m_ui.lineEditBirthDate.setText(date2QString(self.m_client.birthDate()))
			self.m_ui.textEditAddress.setText(str2QString(self.m_client.address()))
			self.m_ui.textEditComment.setText(str2QString(self.m_client.comment()))
		
			# Mise à jour des numéro de téléphone
			for index in range(len(self.m_client.phones())) :
				self.m_phonesEditors[index][0].setText(str2QString(self.m_client.phones()[index]))
					
			# Mise à jour des emails
			for index in range(len(self.m_client.emails())) :
				self.m_emailsEditors[index][0].setText(str2QString(self.m_client.emails()[index]))
		else :
			self.m_ui.lineEditName.setText(QtCore.QString())
			self.m_ui.lineEditFirstName.setText(QtCore.QString())
			self.m_ui.lineEditBirthDate.setText(QtCore.QString())
			self.m_ui.textEditAddress.setText(QtCore.QString())
			self.m_ui.textEditComment.setText(QtCore.QString())
		
			# Mise à jour des numéro de téléphone
			for editor in self.m_phonesEditors :
				editor[0].setText(QtCore.QString())
					
			# Mise à jour des emails
			for editor in self.m_emailsEditors :
				editor[0].setText(QtCore.QString())
				
	def updatePhonesEditors(self) :
		if (self.m_client != None) :
			self.createLineEditList(self.m_client.phones(), self.m_phonesEditors, self.m_ui.phonesContainer, self.clientPhoneChanged, self.addPhone, self.removePhone)
		else :
			self.createLineEditList([], self.m_phonesEditors, self.m_ui.phonesContainer, self.clientPhoneChanged, self.addPhone, self.removePhone)
				
	def updateEmailsEditors(self) :
		if (self.m_client != None) :
			self.createLineEditList(self.m_client.emails(), self.m_emailsEditors, self.m_ui.emailsContainer, self.clientEmailChanged, self.addEmail, self.removeEmail)
		else :
			self.createLineEditList([], self.m_emailsEditors, self.m_ui.emailsContainer, self.clientEmailChanged, self.addEmail, self.removeEmail)
	
	def clientNameChanged(self) :
		if (self.m_client != None) :
			self.m_client.setName(QString2str(self.m_ui.lineEditName.text()))

	def clientFirstNameChanged(self) :
		if (self.m_client != None) :
			self.m_client.setFirstName(QString2str(self.m_ui.lineEditFirstName.text()))

	def clientPhoneChanged(self) :
		if (self.m_client != None) :
			index = 0
			for phoneEditor in self.m_phonesEditors :
				if (self.sender() == phoneEditor[0]) :
					if (index == 0) and (len(self.m_client.phones()) == 0) :
						self.m_client.phones().append(QString2str(phoneEditor[0].text()))
					else :
						self.m_client.phones()[index] = QString2str(phoneEditor[0].text())
					break
				index += 1

	def clientEmailChanged(self) :
		if (self.m_client != None) :
			index = 0
			for emailEditor in self.m_emailsEditors :
				if (self.sender() == emailEditor[0]) :
					if (index == 0) and (len(self.m_client.emails()) == 0) :
						self.m_client.emails().append(QString2str(emailEditor[0].text()))
					else :
						self.m_client.emails()[index] = QString2str(emailEditor[0].text())
					break
				index += 1
		
	def clientAddressChanged(self) :
		if (self.m_client != None) :
			self.m_client.setAddress(QString2str(self.m_ui.textEditAddress.toPlainText()))
		
	def clientCommentChanged(self) :
		if (self.m_client != None) :
			self.m_client.setComment(QString2str(self.m_ui.textEditComment.toPlainText()))

	def createLineEditList(self, stringList, editorsList, container, onEditingFinished, onAddButtonClicked, onRemoveButtonClicked) :
		for editor in editorsList :
			sip.delete(editor[0])
			sip.delete(editor[1])
		if (container.layout() != None) :
			sip.delete(container.layout())
			
		editorsList[:]	= []
		editorsCount	= 0
		if (stringList != None) :
			editorsCount = len(stringList)
		if (editorsCount == 0) :
			editorsCount = 1
		
		container.setLayout(QtGui.QGridLayout(container))
		container.layout().setContentsMargins (0, 0, 0, 0)
			
		for index in range(editorsCount) :
			lineEdit = QtGui.QLineEdit()
			pushButton = QtGui.QPushButton()
			pushButton.setMinimumSize(QtCore.QSize(20, 20))
			pushButton.setMaximumSize(QtCore.QSize(20, 20))
			pushButton.setIconSize(QtCore.QSize(12, 12))
			pushButton.setFlat(True)
			container.layout().addWidget(lineEdit, index, 0)
			container.layout().addWidget(pushButton, index, 1)
			lineEdit.editingFinished.connect(onEditingFinished)
			pushButton.setVisible((not self.m_isReadOnly) and (self.m_client != None))
			editorsList.append((lineEdit, pushButton))
			if (index == 0) :
				pushButton.clicked.connect(onAddButtonClicked)
				pushButton.setIcon(QtGui.QIcon(":/resources/add.png"))
			else :
				pushButton.clicked.connect(onRemoveButtonClicked)
				pushButton.setIcon(QtGui.QIcon(":/resources/remove.png"))
