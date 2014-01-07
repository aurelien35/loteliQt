# -*- coding: utf-8 -*-
		  
import math
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
		self.m_labels		= []
		self.m_model		= QtGui.QStandardItemModel()
		self.m_rowFactory	= DefaultRowFactory()
		self.m_rowsCount	= 0
		self.m_rowsPerPage	= 70
		self.m_pagesCount	= 0
		self.m_currentPage	= 0
		
		self.m_ui.setupUi(self)
		self.m_ui.tableView.setModel(self.m_model)
		self.m_ui.pushButtonPreviousPage.clicked.connect(self.previousPage)
		self.m_ui.pushButtonNextPage.clicked.connect(self.nextPage)
		self.m_ui.comboBoxCurrentPage.currentIndexChanged.connect(self.setCurrentPage)
		
	def query(self) :
		return self.m_query
		
	def setQuery(self, query) :
		self.m_query		= query
		self.m_data			= self.m_db.selectData(self.m_query)
		self.m_rowsCount	= 0
		self.m_pagesCount	= 0
		self.m_currentPage	= 0
		
		self.m_model.setRowCount(0)
		
		if (self.m_data != None) :
			if (self.m_rowFactory != None) :
				self.m_rowsCount	= len(self.m_data)
				self.m_pagesCount	= int(max(0, math.floor(self.m_rowsCount / self.m_rowsPerPage)))
				self.m_ui.comboBoxCurrentPage.clear()
				for pageNumber in range(self.m_pagesCount + 1) :
					self.m_ui.comboBoxCurrentPage.addItem(u"Page {0}/{1}".format(pageNumber+1, self.m_pagesCount+1))
				self.updateModel()
				
	def labels(self) :
		return self.m_labels
			
	def setLabels(self, labels) :
		self.m_labels = labels
		if (self.m_labels == None) :
			self.m_labels = []

		self.m_model.setColumnCount(len(self.m_labels))
		self.m_model.setHorizontalHeaderLabels(strList2QStringList(self.m_labels))
		
	def rowFactory(self) :
		return self.m_rowFactory
		
	def setRowFactory(self, rowFactory) :
		self.m_rowFactory = rowFactory
		
	def setCurrentPage(self, currentPage) :
		self.m_currentPage = min(max(0, currentPage), self.m_pagesCount)
		self.updateModel()

	def previousPage(self) :
		self.setCurrentPage(self.m_currentPage - 1)
		
	def nextPage(self) :
		self.setCurrentPage(self.m_currentPage + 1)
		
	def updateModel(self) :
		firstIndex	= self.m_currentPage * self.m_rowsPerPage
		lastIndex	= (self.m_currentPage+1) * self.m_rowsPerPage
		currentData	= self.m_data[firstIndex:lastIndex]
		
		self.m_model.setRowCount(0)
		for row in currentData :
			self.m_model.appendRow(self.m_rowFactory.createRow(row))
		self.m_ui.comboBoxCurrentPage.setCurrentIndex(self.m_currentPage)

class DefaultRowFactory(object) :

	def createRow(self, data) :
		result = []
		for value in data :
			result.append(QtGui.QStandardItem(str2QString(value)))
		return result
		