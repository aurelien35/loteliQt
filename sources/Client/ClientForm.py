# -*- coding: utf-8 -*-

import sip
from PyQt4					import QtCore, QtGui
from Tools.DatePicker		import SelectDate
from Tools.StringConvert	import *
from Client					import Client
from ClientForm_ui			import Ui_ClientForm

class ClientForm(QtGui.QFrame) :

	def __init__(self, parent=None) :
		super(ClientForm, self).__init__(parent)
		
		# Membres
		self.m_ui						= Ui_ClientForm()
		self.m_isReadOnly				= False
		self.m_client					= None
		self.m_phonesEditors			= []
		self.m_emailsEditors			= []
		
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
		self.setClient(Client())
		
	def isReadOnly(self) :
		return self.m_isReadOnly

	def setReadOnly(self, readOnly) :
		self.m_isReadOnly = readOnly
		self.m_ui.lineEditName.setReadOnly(self.m_isReadOnly)
		self.m_ui.lineEditFirstName.setReadOnly(self.m_isReadOnly)
		self.m_ui.textEditAddress.setReadOnly(self.m_isReadOnly)
		self.m_ui.textEditComment.setReadOnly(self.m_isReadOnly)
		self.m_ui.pushButtonSelectBirthDate.setVisible(not self.m_isReadOnly)
		for phoneEditor in self.m_phonesEditors :
			phoneEditor[0].setReadOnly(self.m_isReadOnly)
			phoneEditor[1].setVisible(not self.m_isReadOnly)
		for emailEditor in self.m_emailsEditors :
			emailEditor[0].setReadOnly(self.m_isReadOnly)
			emailEditor[1].setVisible(not self.m_isReadOnly)

	def client(self) :
		return self.m_client

	def setClient(self, client) :
		self.m_client = client
		self.updatePhonesEditors()
		self.updateEmailsEditors()
		self.updateFormsValues()

	def selectBirthDate(self) :
		self.m_client.setBirthDate(SelectDate(self.m_ui.pushButtonSelectBirthDate, self.m_client.birthDate()))
		self.updateFormsValues()

	def addPhone(self) :
		phones = self.m_client.phones()
		phones.append("")
		if (len(phones) == 1) :
			phones.append("")
		self.m_client.setPhones(phones)
		self.updatePhonesEditors()
		self.updateFormsValues();

	def removePhone(self) :
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
		emails = self.m_client.emails()
		emails.append("")
		if (len(emails) == 1) :
			emails.append("")
		self.m_client.setEmails(emails)
		self.updateEmailsEditors()
		self.updateFormsValues()

	def removeEmail(self) :
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
				
	def updatePhonesEditors(self) :
		self.createLineEditList(self.m_client.phones(), self.m_phonesEditors, self.m_ui.phonesContainer, self.clientPhoneChanged, self.addPhone, self.removePhone)
				
	def updateEmailsEditors(self) :
		self.createLineEditList(self.m_client.emails(), self.m_emailsEditors, self.m_ui.emailsContainer, self.clientEmailChanged, self.addEmail, self.removeEmail)
	
	def clientNameChanged(self) :
		self.m_client.setName(QString2str(self.m_ui.lineEditName.text()))

	def clientFirstNameChanged(self) :
		self.m_client.setFirstName(QString2str(self.m_ui.lineEditFirstName.text()))

	def clientPhoneChanged(self) :
		index = 0
		for phoneEditor in self.m_phonesEditors :
			if (self.sender() == phoneEditor[0]) :
				if (index == 0) :
					self.m_client.phones().append(QString2str(phoneEditor[0].text()))
				else :
					self.m_client.phones()[index] = QString2str(phoneEditor[0].text())
				break
			index += 1

	def clientEmailChanged(self) :
		index = 0
		for emailEditor in self.m_emailsEditors :
			if (self.sender() == emailEditor[0]) :
				if (index == 0) :
					self.m_client.emails().append(QString2str(emailEditor[0].text()))
				else :
					self.m_client.emails()[index] = QString2str(emailEditor[0].text())
				break
			index += 1
		
	def clientAddressChanged(self) :
		self.m_client.setAddress(QString2str(self.m_ui.textEditAddress.toPlainText()))
		
	def clientCommentChanged(self) :
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
			pushButton.setVisible(not self.m_isReadOnly)
			editorsList.append((lineEdit, pushButton))
			if (index == 0) :
				pushButton.clicked.connect(onAddButtonClicked)
				pushButton.setIcon(QtGui.QIcon(":/resources/add.png"))
			else :
				pushButton.clicked.connect(onRemoveButtonClicked)
				pushButton.setIcon(QtGui.QIcon(":/resources/remove.png"))
