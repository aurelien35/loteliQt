# -*- coding: utf-8 -*-
		  
from PyQt4					import QtCore, QtGui
from DataTableView_ui		import Ui_DataTableView
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *

class DataTableView(QtGui.QFrame) :

	def __init__(self) :
		super(DataTableView, self).__init__()

		self.m_ui			= Ui_DataTableView()
		self.m_db			= DataBase()
		self.m_query		= None
		self.m_data			= None
		self.m_labels		= None
		self.m_model		= QtGui.QStandardItemModel()
		self.m_rowFactory	= DefaultRowFactory()
		self.m_rowsPerPage	= 100
		self.m_pagesCount	= 0
		self.m_currentPage	= 0
		
		self.m_ui.setupUi(self)
		self.m_ui.tableView.setModel(self.m_model)
		self.m_ui.pushButtonPreviousPage.clicked.connect(self.previousPage)
		self.m_ui.pushButtonNextPage.clicked.connect(self.nextPage)
		
	def query(self) :
		return self.m_query
		
	def setQuery(self, query) :
		self.m_query	= query
		self.m_data		= self.m_db.selectData(self.m_query)
		
		self.m_model.clear()
		self.setLabels(self.m_labels)
		
		if (self.m_data != None) :
			if (self.m_rowFactory != None) :
				for row in self.m_data :
					self.m_model.appendRow(self.m_rowFactory.createRow(row))
				
	def labels(self) :
		return self.m_labels
			
	def setLabels(self, labels) :
		self.m_labels = labels
		if (self.m_labels == None) :
			self.m_model.setColumnCount(0)
			self.m_model.setRowCount(0)
			self.m_model.setHorizontalHeaderLabels(QtCore.QStringList())
		else :
			self.m_model.setColumnCount(len(self.m_labels))
			self.m_model.setRowCount(0)
			self.m_model.setHorizontalHeaderLabels(strList2QStringList(self.m_labels))
		
	def rowFactory(self) :
		return self.m_rowFactory
		
	def setRowFactory(self, rowFactory) :
		self.m_rowFactory = rowFactory
		
	def previousPage(self) :
		self.m_currentPage -= 1
		if (self.m_currentPage < 0) :
			self.m_currentPage = 0
		self.updateModel()
		
	def nextPage(self) :
		self.m_currentPage += 1
		if (self.m_currentPage > self.m_pagesCount) :
			self.m_currentPage = self.m_pagesCount
		self.updateModel()
		
	def updateModel(self) :
		# TODO
		self.m_model.sortRole()

class DefaultRowFactory(object) :

	def createRow(self, data) :
		result = []
		for value in data :
			result.append(QtGui.QStandardItem(str2QString(value)))
		return result
		