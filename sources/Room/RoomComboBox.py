# -*- coding: utf-8 -*-
		  
from PyQt4					import QtCore, QtGui
from Room					import Room
from Tools.DataBase			import DataBase
import RoomCatalog

class RoomComboBox(QtGui.QFrame) :

	# Signaux
	selectedRoomChanged = QtCore.pyqtSignal(int)
	
	def __init__(self, parent=None) :
		super(RoomComboBox, self).__init__(parent)

		# Membres
		self.m_isReadOnly	= False
		self.m_layout		= QtGui.QStackedLayout(self)
		self.m_comboBox		= QtGui.QComboBox(self)
		self.m_lineEdit		= QtGui.QLineEdit(self)
		
		self.m_layout.addWidget(self.m_comboBox)
		self.m_layout.addWidget(self.m_lineEdit)
		self.m_lineEdit.setReadOnly(True)
		
		self.setLayout(self.m_layout);
		
		# Initialisation
		self.m_comboBox.addItem(u"-----", None)
		for key in RoomCatalog.Instance :
			room = RoomCatalog.Instance[key]
			self.m_comboBox.addItem(room.fullName(), room)
		self.setSelectedRoom(None)
		
		# Connexions
		self.m_comboBox.currentIndexChanged.connect(self.onCurrentIndexChanged)
		
	def isReadOnly(self) :
		return self.m_isReadOnly
		
	def setReadOnly(self, readOnly) :
		self.m_isReadOnly = readOnly
		if (self.m_isReadOnly == False) :
			self.m_layout.setCurrentIndex(0)
		else :
			self.m_layout.setCurrentIndex(1)
	
	def selectedRoom(self) :
		return self.m_selectedRoom
	
	def setSelectedRoom(self, room) :
		self.m_selectedRoom = room
		self.m_comboBox.blockSignals(True)
		if (room == None) :
			self.m_lineEdit.setText(u"-----")
			self.m_comboBox.setCurrentIndex(0)
		else :
			self.m_lineEdit.setText(room.fullName())		
			self.m_comboBox.setCurrentIndex(room.id())
		self.m_comboBox.blockSignals(False)
	
	def onCurrentIndexChanged(self) :
		if (self.m_comboBox.currentIndex() == 0) :
			self.setSelectedRoom(None)
		else :
			self.setSelectedRoom(RoomCatalog.Instance[self.m_comboBox.currentIndex()])
		self.selectedRoomChanged.emit(self.m_comboBox.currentIndex())
