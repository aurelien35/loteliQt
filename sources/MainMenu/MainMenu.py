from PyQt4				import QtCore, QtGui
from MainMenu_ui		import Ui_MainMenu
from Client.ClientForm	import ClientForm
from Tools.ModalDialog	import ShowModalDialog
from Tools.ModalDialog	import ModalDialog
from Tools.DataBase		import DataBase

class MainMenu(QtGui.QFrame) :

	def __init__(self) :
		super(MainMenu, self).__init__()
		
		self.m_ui = Ui_MainMenu()
		self.m_ui.setupUi(self)
		self.m_ui.buttonWeb.clicked.connect(self.launchBrowser)

	def launchBrowser(self) :
		clientForm = ClientForm()
		if (ShowModalDialog(clientForm, "Ajouter un client", "Ok", "Annuler") == ModalDialog.Result.Ok) :
			db = DataBase()
			db.insertClient(clientForm.client())
