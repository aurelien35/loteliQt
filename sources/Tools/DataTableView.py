# -*- coding: utf-8 -*-
		  
import math
from PyQt4					import QtCore, QtGui
from DataTableView_ui		import Ui_DataTableView
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *

class DataTableView(QtGui.QFrame) :

	# Signaux
	rowSelected			= QtCore.pyqtSignal(int)
	rowClicked			= QtCore.pyqtSignal(int)
	rowDoubleClicked	= QtCore.pyqtSignal(int)
	
	def __init__(self, parent=None) :
		super(DataTableView, self).__init__(parent)
		
		# Membres
		self.m_ui					= Ui_DataTableView()
		self.m_db					= DataBase()
		self.m_query				= None
		self.m_data					= None
		self.m_labels				= []
		self.m_model				= QtGui.QStandardItemModel()
		self.m_rowFactory			= DataTableView.defaultRowFactory
		self.m_rowsCount			= 0
		self.m_rowsPerPage			= 70
		self.m_pagesCount			= 0
		self.m_currentPage			= 0
		self.m_currentFirstIndex	= 0
		self.m_currentLastIndex		= 0
		
		# Ui
		self.m_ui.setupUi(self)
		self.m_ui.tableView.setModel(self.m_model)
		self.m_selectionModel = self.m_ui.tableView.selectionModel()
		
		# Connexions
		self.m_ui.pushButtonPreviousPage.clicked.connect(self.previousPage)
		self.m_ui.pushButtonNextPage.clicked.connect(self.nextPage)
		self.m_ui.comboBoxCurrentPage.currentIndexChanged.connect(self.setCurrentPage)
		self.m_ui.tableView.clicked.connect(self.itemClicked)
		self.m_ui.tableView.doubleClicked.connect(self.itemDoubleClicked)
		self.m_selectionModel.selectionChanged.connect(self.itemSelectionChanged)

	def query(self) :
		return self.m_query
		
	def setQuery(self, query) :
		self.m_query				= query
		self.m_data					= None
		self.m_rowsCount			= 0
		self.m_pagesCount			= 0
		self.m_currentPage			= 0
		self.m_currentFirstIndex	= 0
		self.m_currentLastIndex		= 0

		self.m_model.setRowCount(0)
		if (self.m_query != None) :
			self.m_data = self.m_db.selectData(self.m_query)
			
			if (self.m_data != None) :
				if (self.m_rowFactory != None) :
					self.m_rowsCount	= len(self.m_data)
					self.m_pagesCount	= int(max(0, math.floor(self.m_rowsCount / self.m_rowsPerPage)))
					self.m_ui.comboBoxCurrentPage.clear()
					for pageNumber in range(self.m_pagesCount + 1) :
						self.m_ui.comboBoxCurrentPage.addItem(u"Page {0}/{1}".format(pageNumber+1, self.m_pagesCount+1))
		self.updateModel()
		self.m_ui.tableView.resizeColumnsToContents()
				
	def data(self) :
		return self.m_data
				
	def row(self, rowIndex) :
		return self.m_data[rowIndex]
				
	def rowsCount(self) :
		return self.m_rowsCount
				
	def query(self) :
		return self.m_query
		
	def labels(self) :
		return self.m_labels
			
	def setLabels(self, labels) :
		self.m_labels = labels
		if (self.m_labels == None) :
			self.m_labels = []

		labelsQStringList = strList2QStringList(self.m_labels)
		self.m_model.setHorizontalHeaderLabels(labelsQStringList)
		self.m_model.setColumnCount(labelsQStringList.count())
		self.m_ui.tableView.resizeColumnsToContents()
		
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
		self.m_currentFirstIndex	= self.m_currentPage * self.m_rowsPerPage
		self.m_currentLastIndex		= (self.m_currentPage+1) * self.m_rowsPerPage
		currentData					= self.m_data[self.m_currentFirstIndex:self.m_currentLastIndex]
		
		self.m_model.setRowCount(0)
		if (self.m_rowFactory != None) :
			rowIndex = 0;
			for row in currentData :
				items = self.m_rowFactory(row)
				self.m_model.appendRow(items)
				for item in items :
					item.setData(QtCore.QVariant(int(rowIndex)), QtCore.Qt.UserRole)
				rowIndex += 1
				
		self.m_ui.comboBoxCurrentPage.setCurrentIndex(self.m_currentPage)
		self.m_ui.tableView.resizeRowsToContents()
		self.itemSelectionChanged()

	def itemClicked(self, modelIndex) :
		self.rowClicked.emit(modelIndex.data(QtCore.Qt.UserRole).toPyObject())
		
	def itemDoubleClicked(self, modelIndex) :
		self.rowDoubleClicked.emit(modelIndex.data(QtCore.Qt.UserRole).toPyObject())
		
	def itemSelectionChanged(self) :
		selectedRow = -1
		selectedRows = self.m_selectionModel.selectedRows()
		if (selectedRows != None) :
			if (len(selectedRows) > 0) :
				selectedRow = selectedRows[0].data(QtCore.Qt.UserRole).toPyObject()
		self.rowSelected.emit(selectedRow)
		
	@staticmethod
	def defaultRowFactory(data) :
		result = []
		for value in data :
			result.append(QtGui.QStandardItem(str2QString(unicode(value))))
		return result
		