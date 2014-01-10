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

def ShowInfo(title, message) :
	return ShowMessage(title, u":/resources/info.png", message, "Ok")
	
def ShowError(title, message) :
	return ShowMessage(title, u":/resources/error.png", message, "Ok")
	
def ShowWarning(title, message) :
	return ShowMessage(title, u":/resources/warning.png", message, "Ok")
	
def ShowConfirmation(title, message, okText, cancelText) :
	return ShowMessage(title, u":/resources/question.png", message, okText, cancelText)
	
def ShowMessage(title, image, message, okText=None, cancelText=None, otherText=None) :
	modalMessageDialog = ModalMessageDialog(title, image, message, okText, cancelText, otherText)
	return modalMessageDialog.showDialog()

class ModalDialog(QtGui.QDialog) :

	class Result :
		Ok		= QtGui.QDialog.Accepted
		Cancel	= QtGui.QDialog.Rejected
		Other	= 2
	
	def __init__(self, title, okText=None, cancelText=None, otherText=None) :
		super(ModalDialog, self).__init__()

		# Membres
		self.m_uiModalDialog	= Ui_ModalDialog()
		self.m_position			= None
		self.m_screenRect		= QtGui.QDesktopWidget().screenGeometry(0)
		
		# Initialisation
		self.m_uiModalDialog.setupUi(self)
		self.m_uiModalDialog.buttonOk.installEventFilter(self)
		self.m_uiModalDialog.buttonCancel.installEventFilter(self)
		self.m_uiModalDialog.buttonOther.installEventFilter(self)
		
		# Connexions
		self.m_uiModalDialog.buttonOk.clicked.connect(self.buttonOkClicked)
		self.m_uiModalDialog.buttonCancel.clicked.connect(self.buttonCancelClicked)
		self.m_uiModalDialog.buttonOther.clicked.connect(self.buttonOtherClicked)
		
		#Etat initial
		self.m_uiModalDialog.labelTitle.setText(title)
		if (okText == None) :
			self.m_uiModalDialog.buttonOk.hide()
		else :
			self.m_uiModalDialog.buttonOk.setText(okText)
		if (cancelText == None) :
			self.m_uiModalDialog.buttonCancel.hide()
		else :
			self.m_uiModalDialog.buttonCancel.setText(cancelText)
		if (otherText == None) :
			self.m_uiModalDialog.buttonOther.hide()
		else :
			self.m_uiModalDialog.buttonOther.setText(otherText)
		
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint);
	
	def setContent(self, content, margin) :
		self.m_uiModalDialog.containerLayout.setContentsMargins(margin, margin, margin, margin)
		self.m_uiModalDialog.containerLayout.addWidget(content)
		content.show()

	def showDialog(self, position=None) :
		blocker = ModalDialogBlocker()
		blocker.open()
		self.m_position = position
		self.adjustSize()
		result = self.exec_()
		blocker.close()		
		return result
	
	def buttonOkClicked(self) :
		self.done(ModalDialog.Result.Ok)
		
	def buttonCancelClicked(self) :
		self.done(ModalDialog.Result.Cancel)
		
	def buttonOtherClicked(self) :
		self.done(ModalDialog.Result.Other)
		
	def keyPressEvent(self, event) :
		event.ignore()
		
	def resizeEvent(self, event) :
		super(ModalDialog, self).resizeEvent(event)
		if (self.m_position != None) :
			self.move(self.m_position)
		else :
			self.move(self.m_screenRect.center() - self.rect().center())

	def eventFilter(self, object, event) :
		if (event.type() == QtCore.QEvent.KeyPress) :
			return True;
		return super(ModalDialog, self).eventFilter(object, event)

class ModalMessageDialog(ModalDialog) :
	def __init__(self, title, image, message, okText=None, cancelText=None, otherText=None) :
		super(ModalMessageDialog, self).__init__(title, okText, cancelText, otherText)
		
		icone = QtGui.QLabel()
		icone.setPixmap(QtGui.QPixmap(image))	
		label = QtGui.QLabel(message)
		label.setWordWrap(True)
		label.setObjectName(u"labelDialogMessage")
		label.setMinimumSize(QtCore.QSize(200, 40))
		layout = QtGui.QHBoxLayout()
		layout.addWidget(icone)
		layout.addWidget(label)	
		content = QtGui.QFrame()
		content.setLayout(layout)
		self.setContent(content, 9)

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
