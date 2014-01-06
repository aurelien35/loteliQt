# -*- coding: utf-8 -*-
		  
from PyQt4					import QtCore, QtGui
from DataTableView_ui		import Ui_DataTableView
from Tools.StringConvert	import *

class DataTableView(QtGui.QFrame) :

	def __init__(self) :
		super(DataTableView, self).__init__()

		self.m_ui		= Ui_DataTableView()
		self.m_query	= None
		self.m_columns	= {}
		self.m_model	= QtGui.QStandardItemModel()
		
		self.m_ui.setupUi(self)
		self.m_ui.tableView.setModel(self.m_model)
		
	def query(self) :
		return self.m_query
		
	def setQuery(self, query) :
		self.m_query = query
			
	def columns(self) :
		return self.m_columns
			
	def setColumns(self, columns) :
		self.m_columns = columns
		labelsList = QtCore.QStringList()
		for key in columns
			labelsList.append(str2QString(key))
		self.m_model.setVerticalHeaderLabels(labelsList)

	