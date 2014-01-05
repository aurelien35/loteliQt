import sip
from PyQt4				import QtCore, QtGui
from Tools.DatePicker	import DatePicker
from Client				import Client
from ClientForm_ui		import Ui_ClientForm

class ClientForm(QtGui.QFrame) :

	def __init__(self) :
		super(ClientForm, self).__init__()
		
		# Membres
		self.m_ui						= Ui_ClientForm()
		self.m_isReadOnly				= False
		self.m_client					= None
		self.m_phonesEditors			= []
		self.m_phoneEditorsContainer	= QtGui.QFrame()
		self.m_emailsEditors			= []
		self.m_emailEditorsContainer	= QtGui.QFrame()
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.formLayout.insertRow(4, None, self.m_phoneEditorsContainer)
		self.m_ui.formLayout.insertRow(6, None, self.m_emailEditorsContainer)
		
		# Connexions
		self.m_ui.lineEditName.editingFinished.connect(self.clientNameChanged)
		self.m_ui.lineEditFirstName.editingFinished.connect(self.clientFirstNameChanged)
		self.m_ui.lineEditPhone.editingFinished.connect(self.clientPhoneChanged)
		self.m_ui.lineEditEmail.editingFinished.connect(self.clientEmailChanged)
		self.m_ui.textEditAddress.textChanged.connect(self.clientAddressChanged)
		self.m_ui.textEditComment.textChanged.connect(self.clientCommentChanged)
		
		self.m_ui.pushButtonSelectBirthDate.clicked.connect(self.selectBirthDate)
		self.m_ui.pushButtonAddPhone.clicked.connect(self.addPhone)
		self.m_ui.pushButtonAddEmail.clicked.connect(self.addEmail)

		# Etat initial
		self.setReadOnly(False)
		self.setClient(Client())
		
	def isReadOnly(self) :
		return self.m_isReadOnly

	def setReadOnly(self, readOnly) :	# TODO
		self.m_isReadOnly = readOnly
		self.m_ui.lineEditName.setReadOnly(self.m_isReadOnly)
		self.m_ui.lineEditFirstName.setReadOnly(self.m_isReadOnly)
		self.m_ui.lineEditPhone.setReadOnly(self.m_isReadOnly)
		self.m_ui.lineEditEmail.setReadOnly(self.m_isReadOnly)
		self.m_ui.textEditAddress.setReadOnly(self.m_isReadOnly)
		self.m_ui.textEditComment.setReadOnly(self.m_isReadOnly)
		self.m_ui.pushButtonSelectBirthDate.setVisible(not self.m_isReadOnly)
		self.m_ui.pushButtonAddPhone.setVisible(not self.m_isReadOnly)
		self.m_ui.pushButtonAddEmail.setVisible(not self.m_isReadOnly)
		for phoneEditor in self.m_phonesEditors :
			phoneEditor[1].setVisible(not self.m_isReadOnly)
		for emailEditor in self.m_emailsEditors :
			emailEditor[1].setVisible(not self.m_isReadOnly)

	def client(self) :
		return self.m_client

	def setClient(self, client) :
		self.m_client = client
		self.updateFormsValues();

	def selectBirthDate(self) :
		datePicker = DatePicker()
		date = datePicker.selectDate(self.m_ui.pushButtonSelectBirthDate)
		if (date.isValid() == True) :
			self.m_client.setBirthDate(date)
			self.m_ui.lineEditBirthDate.setText(self.m_client.birthDateString())

	def addPhone(self) :
		phones = self.m_client.phones()
		phones.append(QtCore.QString())
		if (phones.count() == 1) :
			phones.append(QtCore.QString())
		self.m_client.setPhones(phones)
		self.updateFormsValues();

	def removePhone(self) :
		index = 0;
		phones = self.m_client.phones()
		for phoneEditor in self.m_phonesEditors :
			if (self.sender() == phoneEditor[1]) :
				phones.removeAt(index+1)
				break
			index += 1
		self.m_client.setPhones(phones)
		self.updateFormsValues()
			
	def addEmail(self) :
		emails = self.m_client.emails()
		emails.append(QtCore.QString())
		if (emails.count() == 1) :
			emails.append(QtCore.QString())
		self.m_client.setEmails(emails)
		self.updateFormsValues()

	def removeEmail(self) :
		index = 0;
		emails = self.m_client.emails()
		for emailEditor in self.m_emailsEditors :
			if (self.sender() == emailEditor[1]) :
				emails.removeAt(index+1)
				break
			index += 1
		self.m_client.setEmails(emails)
		self.updateFormsValues()
		
	def updateFormsValues(self) :
		self.m_ui.lineEditName.setText(self.m_client.name())
		self.m_ui.lineEditFirstName.setText(self.m_client.firstName())
		self.m_ui.lineEditBirthDate.setText(self.m_client.birthDateString())
		self.m_ui.textEditAddress.setText(self.m_client.address())
		self.m_ui.textEditComment.setText(self.m_client.comment())

		# Ajouter ou supprimer des editeurs de numéro de téléphone ?
		self.createLineEditList(self.m_client.phones(), self.m_phonesEditors, self.m_phoneEditorsContainer, self.clientOtherPhoneChanged, self.removePhone)
		self.createLineEditList(self.m_client.emails(), self.m_emailsEditors, self.m_emailEditorsContainer, self.clientOtherEmailChanged, self.removeEmail)
		
		# Mise à jour des numéro de téléphone
		if (self.m_client.phones().count() == 0) :
			self.m_ui.lineEditPhone.setText(QtCore.QString())
		else :
			self.m_ui.lineEditPhone.setText(self.m_client.phones()[0])
			for index in range(self.m_client.phones().count()-1) :
				self.m_phonesEditors[index][0].setText(self.m_client.phones()[index+1])
				
		# Mise à jour des emails
		if (self.m_client.emails().count() == 0) :
			self.m_ui.lineEditEmail.setText(QtCore.QString())
		else :
			self.m_ui.lineEditEmail.setText(self.m_client.emails()[0])
			for index in range(self.m_client.emails().count()-1) :
				self.m_emailsEditors[index][1].setText(self.m_client.emails()[index+1])
				
	def clientNameChanged(self) :
		self.m_client.setName(self.m_ui.lineEditName.text())

	def clientFirstNameChanged(self) :
		self.m_client.setFirstName(self.m_ui.lineEditFirstName.text())

	def clientPhoneChanged(self) :
		if (len(self.m_client.phones()) == 0) :
			self.m_client.phones().append(self.m_ui.lineEditPhone.text())
		else :
			self.m_client.phones()[0] = self.m_ui.lineEditPhone.text()

	def clientOtherPhoneChanged(self) :
		index = 1
		for phoneEditor in self.m_phonesEditors :
			if (self.sender() == phoneEditor[0]) :
				self.m_client.phones()[index] = phoneEditor[0].text()
				break
			index += 1

	def clientEmailChanged(self) :
		if (len(self.m_client.emails()) == 0) :
			self.m_client.emails().append(self.m_ui.lineEditEmail.text())
		else :
			self.m_client.emails()[0] = self.m_ui.lineEditEmail.text()

	def clientOtherEmailChanged(self) :
		index = 1
		for emailEditor in self.m_emailsEditors :
			if (self.sender() == emailEditor[0]) :
				self.m_client.emails()[index] = emailEditor[0].text()
				break
			index += 1
		
	def clientAddressChanged(self) :
		self.m_client.setAddress(self.m_ui.textEditAddress.toPlainText())
		
	def clientCommentChanged(self) :
		self.m_client.setComment(self.m_ui.textEditAddress.toPlainText())

	def createLineEditList(self, stringList, editorsList, container, onEditingFinished, onRemoveButtonClicked) :
		for editor in editorsList :
			sip.delete(editor[0])
			sip.delete(editor[1])
		if (container.layout() != None) :
			sip.delete(container.layout())
			
		editorsList[:] = []
		if stringList.count() <= 1 :
			container.hide()
		else :
			container.show()
			layout = QtGui.QGridLayout()
			layout.setContentsMargins (0, 0, 0, 0)
			container.setLayout(layout)
			for index in range(stringList.count()-1) :
				lineEdit = QtGui.QLineEdit()
				pushButtonRemove = QtGui.QPushButton()
				pushButtonRemove.setMinimumSize(QtCore.QSize(20, 20))
				pushButtonRemove.setMaximumSize(QtCore.QSize(20, 20))
				pushButtonRemove.setIcon(QtGui.QIcon(":/resources/remove.png"))
				pushButtonRemove.setIconSize(QtCore.QSize(12, 12))
				pushButtonRemove.setFlat(True)
				layout.addWidget(lineEdit, index, 0)
				layout.addWidget(pushButtonRemove, index, 1)
				lineEdit.editingFinished.connect(onEditingFinished)
				pushButtonRemove.clicked.connect(onRemoveButtonClicked)
				pushButtonRemove.setVisible(not self.m_isReadOnly)
				editorsList.append((lineEdit, pushButtonRemove))
