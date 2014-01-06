# -*- coding: utf-8 -*-
		  
from PyQt4					import QtCore, QtGui
from DataTableView_ui		import Ui_DataTableView
from Tools.StringConvert	import *

class DataTableView(QtGui.QFrame) :

	def __init__(self) :
		super(DataTableView, self).__init__()

		self.m_ui			= Ui_DataTableView()
		self.m_query		= None
		self.m_data			= None
		self.m_columns		= None
		self.m_model		= QtGui.QStandardItemModel()
		self.m_rowsPerPage	= 100
		self.m_pagesCount	= 0
		self.m_currentPage	= 0
		
		self.m_ui.setupUi(self)
		self.m_ui.tableView.setModel(self.m_model)
		
	def query(self) :
		return self.m_query
		
	def setQuery(self, query) :
		self.m_query = query
		# TODO : executer la requete et remplir "self.m_data"
			
	def columns(self) :
		return self.m_columns
			
	def setColumns(self, columns) :
		self.m_columns = columns
		if (self.m_columns == None) :
			self.m_model.setColumnCount(0)
			self.m_model.setRowCount(0)
			self.m_model.setHorizontalHeaderLabels(labelsList)
		else :
			self.m_model.setColumnCount(len(self.m_columns))
			self.m_model.setRowCount(0)
			self.m_model.setHorizontalHeaderLabels(strList2QStringList(self.m_columns.keys()))

		self.updateModel()
		
	def previousPage(self) :
		# TODO
		
	def nextPage(self) :
		# TODO
		
	def updateModel(self) :
		# TODO
