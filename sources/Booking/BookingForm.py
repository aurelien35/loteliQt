# -*- coding: utf-8 -*-

import sip
from PyQt4					import QtCore, QtGui
from Tools.DatePicker		import SelectDate
from Tools.StringConvert	import *
from Booking				import Booking
from BookingForm_ui			import Ui_BookingForm

class BookingForm(QtGui.QFrame) :

	def __init__(self, parent=None) :
		super(BookingForm, self).__init__(parent)
		
		# Membres
		self.m_ui				= Ui_BookingForm()
		self.m_isReadOnly		= False
		self.m_booking			= None
		self.m_clientsEditors	= []
		self.m_roomsEditors		= []
		
		# Initialisation
		self.m_ui.setupUi(self)
		
		# Connexions
		self.m_ui.pushButtonSelectStartDate.clicked.connect(self.selectStartDate)
		self.m_ui.lineEditDays.textEdited.connect(self.bookingDaysChanged)
		self.m_ui.pushButtonSelectEndDate.clicked.connect(self.selectEndDate)
		self.m_ui.textEditComment.textChanged.connect(self.bookingCommentChanged)

		# Etat initial
		self.setReadOnly(False)
		self.setBooking(None)
		
	def isReadOnly(self) :
		return self.m_isReadOnly

	def setReadOnly(self, readOnly) :
		self.m_isReadOnly = readOnly
		effectiveReadOnly = self.m_isReadOnly
		if (effectiveReadOnly == False) :
			if (self.m_booking == None) :
				effectiveReadOnly = True
		self.m_ui.pushButtonSelectStartDate.setVisible(not effectiveReadOnly)
		self.m_ui.lineEditDays.setReadOnly(effectiveReadOnly)
		self.m_ui.pushButtonSelectEndDate.setVisible(not effectiveReadOnly)
		for clientEditor in self.m_clientsEditors :
			clientEditor[0].setReadOnly(effectiveReadOnly)
			clientEditor[1].setVisible(not effectiveReadOnly)
		for roomEditor in self.m_roomsEditors :
			roomEditor[0].setReadOnly(effectiveReadOnly)
			roomEditor[1].setVisible(not effectiveReadOnly)
		self.m_ui.textEditComment.setReadOnly(effectiveReadOnly)

	def booking(self) :
		return self.m_booking

	def setBooking(self, booking) :
		self.m_booking = booking
		self.updateClientsEditors()
		self.updateRoomsEditors()
		self.updateFormsValues()
		self.setReadOnly(self.isReadOnly())

	def reloadBooking(self) :
		if (self.m_booking != None) :
			self.setBooking(DataBase().loadBooking(self.m_booking.id()))
			
	def updateFormsValues(self) :
		if (self.m_booking != None) :
			self.m_ui.lineEditStartDate.setText(date2QString(self.m_booking.date()))
			self.m_ui.lineEditDays.setText(str(self.m_booking.days()))
			self.m_ui.lineEditEndDate.setText(date2QString(self.m_booking.endDate()))
			self.m_ui.textEditComment.setText(str2QString(self.m_booking.comment()))
		
			# Mise à jour des clients
			index = 0
			for editor in self.m_clientsEditors :
				client = self.m_booking.clients()[index]
				editor[0].setText(u"{0} {1}".format(client.name(), client.firstName()))
				index += 1
					
			# Mise à jour des chambres
			index = 0
			for editor in self.m_roomsEditors :
				room = self.m_booking.rooms()[index]
				editor[0].setText(u"{0} {1}".format(room.number(), room.name()))
				index += 1
				
		else :
			self.m_ui.lineEditStartDate.setText(QtCore.QString())
			self.m_ui.lineEditDays.setText(QtCore.QString())
			self.m_ui.lineEditEndDate.setText(QtCore.QString())
			self.m_ui.textEditComment.setText(QtCore.QString())
		
			# Mise à jour des clients
			for editor in self.m_clientsEditors :
				editor[0].setText(QtCore.QString())
					
			# Mise à jour des chambres
			for editor in self.m_roomsEditors :
				editor[0].setText(QtCore.QString())
				
	def updateClientsEditors(self) :
		for editor in self.m_clientsEditors :
			sip.delete(editor[0])
			sip.delete(editor[1])
		if (self.m_ui.clientsContainer.layout() != None) :
			sip.delete(self.m_ui.clientsContainer.layout())
			
		self.m_clientsEditors[:]	= []
		clientsCount				= 0
		if (self.m_booking != None) :
			clientsCount = len(self.m_booking.clients())
		if (clientsCount == 0) :
			clientsCount = 1
		
		self.m_ui.clientsContainer.setLayout(QtGui.QGridLayout(self.m_ui.clientsContainer))
		self.m_ui.clientsContainer.layout().setContentsMargins (0, 0, 0, 0)
			
		for index in range(clientsCount) :
			lineEdit = QtGui.QLineEdit()
			pushButton = QtGui.QPushButton()
			pushButton.setMinimumSize(QtCore.QSize(20, 20))
			pushButton.setMaximumSize(QtCore.QSize(20, 20))
			pushButton.setIconSize(QtCore.QSize(12, 12))
			pushButton.setFlat(True)
			self.m_ui.clientsContainer.layout().addWidget(lineEdit, index, 0)
			self.m_ui.clientsContainer.layout().addWidget(pushButton, index, 1)
			lineEdit.editingFinished.connect(self.clientChanged)
			pushButton.setVisible((not self.m_isReadOnly) and (self.m_booking != None))
			self.m_clientsEditors.append((lineEdit, pushButton))
			if (index == 0) :
				pushButton.clicked.connect(self.addClient)
				pushButton.setIcon(QtGui.QIcon(":/resources/add.png"))
			else :
				pushButton.clicked.connect(self.removeClient)
				pushButton.setIcon(QtGui.QIcon(":/resources/remove.png"))
				
	def updateRoomsEditors(self) :
		for editor in self.m_roomsEditors :
			sip.delete(editor[0])
			sip.delete(editor[1])
		if (self.m_ui.roomsContainer.layout() != None) :
			sip.delete(self.m_ui.roomsContainer.layout())
			
		self.m_roomsEditors[:]	= []
		roomsCount				= 0
		if (self.m_booking != None) :
			roomsCount = len(self.m_booking.rooms())
		if (roomsCount == 0) :
			roomsCount = 1
		
		self.m_ui.roomsContainer.setLayout(QtGui.QGridLayout(self.m_ui.roomsContainer))
		self.m_ui.roomsContainer.layout().setContentsMargins (0, 0, 0, 0)
			
		for index in range(roomsCount) :
			lineEdit = QtGui.QLineEdit()
			pushButton = QtGui.QPushButton()
			pushButton.setMinimumSize(QtCore.QSize(20, 20))
			pushButton.setMaximumSize(QtCore.QSize(20, 20))
			pushButton.setIconSize(QtCore.QSize(12, 12))
			pushButton.setFlat(True)
			self.m_ui.roomsContainer.layout().addWidget(lineEdit, index, 0)
			self.m_ui.roomsContainer.layout().addWidget(pushButton, index, 1)
			lineEdit.editingFinished.connect(self.roomChanged)
			pushButton.setVisible((not self.m_isReadOnly) and (self.m_booking != None))
			self.m_roomsEditors.append((lineEdit, pushButton))
			if (index == 0) :
				pushButton.clicked.connect(self.addRoom)
				pushButton.setIcon(QtGui.QIcon(":/resources/add.png"))
			else :
				pushButton.clicked.connect(self.removeRoom)
				pushButton.setIcon(QtGui.QIcon(":/resources/remove.png"))
				
	def selectStartDate(self) :
		if (self.m_booking != None) :
			self.m_booking.setDate(SelectDate(self.m_ui.pushButtonSelectStartDate, self.m_booking.date()))
			self.updateFormsValues()
			
	def bookingDaysChanged(self) :
		if (self.m_booking != None) :
			days = int(self.m_ui.lineEditDays.text())
			self.m_booking.setDays(days)
			self.updateFormsValues()
				
	def selectEndDate(self) :
		if (self.m_booking != None) :
			endDate = SelectDate(self.m_ui.pushButtonSelectStartDate, self.m_booking.endDate())
			if (endDate != None) :
				if (endDate > self.m_booking.date()) :
					self.m_booking.setDays((endDate - self.m_booking.date()).days)
					self.updateFormsValues()
			
	def addClient(self) :
		if (self.m_booking != None) :
			print "TODO : addClient : ouvrir une popup de choix / creation de client"

	def removeClient(self) :
		if (self.m_booking != None) :
			print "TODO : removeClient"

	def clientChanged(self) :
		if (self.m_booking != None) :
			print "TODO : clientChanged"
			
	def addRoom(self) :
		if (self.m_booking != None) :
			print "TODO : addRoom : ouvrir une popup de choix de chambre"

	def removeRoom(self) :
		if (self.m_booking != None) :
			print "TODO : removeRoom"

	def roomChanged(self) :
		if (self.m_booking != None) :
			print "TODO : roomChanged"
				
	def bookingCommentChanged(self) :
		if (self.m_booking != None) :
			self.m_booking.setComment(QString2str(self.m_ui.textEditComment.toPlainText()))
