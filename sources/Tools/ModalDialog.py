# -*- coding: utf-8 -*-

from PyQt4			import QtCore, QtGui
from ModalDialog_ui	import Ui_ModalDialog

def ShowModalDialog(dialogContent, title, okText=None, cancelText=None, otherText=None, acceptSignal=None, position=None) :
	result = QtGui.QDialog.Rejected
	if (dialogContent != None) :
		blocker = ModalDialogBlocker()
		blocker.open()
		dialog = ModalDialog(dialogContent, title, okText, cancelText, otherText, position)
		if (acceptSignal != None) :
			acceptSignal.connect(dialog.accept)
		result = dialog.exec_()
		blocker.close()		
	return result

class ModalDialogBlocker(QtGui.QDialog) :

	def __init__(self) :
		super(ModalDialogBlocker, self).__init__()

		self.setAttribute(QtCore.Qt.WA_TranslucentBackground);
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint);
		self.setGeometry(QtGui.QDesktopWidget().screenGeometry(0))
		
		frame = QtGui.QFrame(self)
		frame.setGeometry(QtGui.QDesktopWidget().screenGeometry(0))
		frame.setAutoFillBackground(True)
		palette = frame.palette()
		palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(QtGui.QColor(0, 0, 0, 165)))
		frame.setPalette(palette)
		
	def keyPressEvent(self, event) :
		event.ignore()

class ModalDialog(QtGui.QDialog) :
	class Result :
		Ok		= QtGui.QDialog.Accepted
		Cancel	= QtGui.QDialog.Rejected
		Other	= 2
	
	def __init__(self, dialogContent, title, okText, cancelText, otherText, position) :
		super(ModalDialog, self).__init__()

		# Membres
		self.m_ui			= Ui_ModalDialog()
		self.m_content		= dialogContent
		self.m_position		= position
		self.m_screenRect	= QtGui.QDesktopWidget().screenGeometry(0)
		
		# Initialisation
		self.m_ui.setupUi(self)
		self.m_ui.containerLayout.addWidget(dialogContent)
		self.m_ui.buttonOk.installEventFilter(self)
		self.m_ui.buttonCancel.installEventFilter(self)
		self.m_ui.buttonOther.installEventFilter(self)
		
		# Connexions
		self.finished.connect(self.aboutToClose)
		self.m_ui.buttonOk.clicked.connect(self.accept)
		self.m_ui.buttonCancel.clicked.connect(self.reject)
		self.m_ui.buttonOther.clicked.connect(self.buttonOtherClicked)
		
		#Etat initial
		self.m_ui.labelTitle.setText(title)
		if (okText == None) :
			self.m_ui.buttonOk.hide()
		else :
			self.m_ui.buttonOk.setText(okText)
		if (cancelText == None) :
			self.m_ui.buttonCancel.hide()
		else :
			self.m_ui.buttonCancel.setText(cancelText)
		if (otherText == None) :
			self.m_ui.buttonOther.hide()
		else :
			self.m_ui.buttonOther.setText(otherText)
		
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint);
		self.adjustSize()
		
	def buttonOtherClicked(self) :
		self.done(ModalDialog.Result.Other)
		
	def resizeEvent(self, event) :
		super(ModalDialog, self).resizeEvent(event)
		if (self.m_position != None) :
			self.move(self.m_position)
		else :
			self.move(self.m_screenRect.center() - self.rect().center())
		
	def keyPressEvent(self, event) :
		event.ignore()
		
	def resizeEvent(self, event) :
		super(ModalDialog, self).resizeEvent(event)
		if (self.m_position != None) :
			self.move(self.m_position)
		else :
			self.move(self.m_screenRect.center() - self.rect().center())
	
	def aboutToClose(self) :
		self.m_content.hide()
		self.m_content.setParent(None)

	def eventFilter(self, object, event) :
		if (event.type() == QtCore.QEvent.KeyPress) :
			return True;
			
		return super(ModalDialog, self).eventFilter(object, event)
