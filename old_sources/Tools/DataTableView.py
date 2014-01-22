# -*- coding: utf-8 -*-
		  
import math
from PyQt4					import QtCore, QtGui
from DataTableView_ui		import Ui_DataTableView
from Tools.DataBase			import DataBase
from Tools.StringConvert	import *

def DefaultRowFactory(data, columns) :
	result = []
	for column in columns :
		value = ""
		if (data.has_key(column[1]) == True) :
			value = unicode(data[column[1]])
			if (u"¤" in value) :
				value = u"\n".join(filter(None, value.split(u"¤")))
		result.append(QtGui.QStandardItem(value))
	return result

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
		self.m_tokens				= None
		self.m_data					= None
		self.m_columns				= []
		self.m_model				= QtGui.QStandardItemModel()
		self.m_selectionModel		= None
		self.m_selectedRow			= -1
		self.m_rowFactory			= DefaultRowFactory
		self.m_rowsCount			= 0
		self.m_rowsPerPage			= 70
		self.m_pagesCount			= 0
		self.m_currentPage			= 0
		
		# Ui
		self.m_ui.setupUi(self)
		self.m_ui.tableView.setModel(self.m_model)
		self.m_ui.navigationBar.hide()
		self.m_selectionModel = self.m_ui.tableView.selectionModel()
		tableViewPalette = self.m_ui.tableView.palette()
		tableViewPalette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight,		tableViewPalette.brush(QtGui.QPalette.Active, QtGui.QPalette.Highlight))
		tableViewPalette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText,	tableViewPalette.brush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText))
		self.m_ui.tableView.setPalette(tableViewPalette)
		
		# Connexions
		self.m_ui.buttonPreviousPage.clicked.connect(self.previousPage)
		self.m_ui.buttonNextPage.clicked.connect(self.nextPage)
		self.m_ui.comboBoxCurrentPage.currentIndexChanged.connect(self.setCurrentPageIndex)
		self.m_ui.tableView.clicked.connect(self.itemClicked)
		self.m_ui.tableView.doubleClicked.connect(self.itemDoubleClicked)
		self.m_selectionModel.selectionChanged.connect(self.itemSelectionChanged)

	def query(self) :
		return (self.m_query, self.m_tokens)
		
	def setQuery(self, query, tokens, selectionKey=None) :
		# On recupere la selection courante
		selectedValue = None
		if ( (self.m_selectedRow >= 0) and (selectionKey != None) ) :
			selectedValue = self.m_data[self.m_selectedRow][selectionKey]
		
		# On remet la vue à zero
		self.m_ui.comboBoxCurrentPage.clear()
		self.m_query		= query
		self.m_tokens		= tokens
		self.m_data			= None
		self.m_rowsCount	= 0
		self.m_pagesCount	= 0
		self.m_currentPage	= 0
		self.m_selectedRow	= -1
		
		# On re-rempli le modele
		if (self.m_query != None) :
			self.m_data = self.m_db.selectData(self.m_query, self.m_tokens)
			
			# On recupere la nouvelle selection
			if ( (selectionKey != None) and (selectedValue) ) :
				rowIndex	= -1
				for element in self.m_data :
					rowIndex += 1
					if (element[selectionKey] == selectedValue) :
						self.m_selectedRow = rowIndex
						break;
		
			# On remplit la barre de navigation
			if (self.m_data != None) :
				if (self.m_rowFactory != None) :
					self.m_rowsCount	= len(self.m_data)
					self.m_pagesCount	= int(max(1, 1 + math.floor(self.m_rowsCount / self.m_rowsPerPage)))
					for pageNumber in range(self.m_pagesCount) :
						self.m_ui.comboBoxCurrentPage.addItem(u"Page {0}/{1}".format(pageNumber+1, self.m_pagesCount))
						
		self.m_ui.navigationBar.setVisible(self.m_pagesCount > 1)
		
		# On re-met à jour la selection
		self.m_currentPage = int(max(1, 1 + math.floor(self.m_selectedRow / self.m_rowsPerPage)))
		self.updateModel(self.m_selectedRow)
				
	def data(self) :
		return self.m_data
				
	def row(self, rowIndex) :
		return self.m_data[rowIndex]
				
	def rowsCount(self) :
		return self.m_rowsCount
		
	def columns(self) :
		return self.m_columns
			
	def setColumns(self, columns) :
		self.m_columns = columns
		if (self.m_columns == None) :
			self.m_columns = []

		labels = QtCore.QStringList()
		for column in self.m_columns :
			labels.append(column[0])
		self.m_model.setHorizontalHeaderLabels(labels)
		self.m_model.setColumnCount(labels.count())
		self.m_ui.tableView.resizeColumnsToContents()
		self.m_ui.tableView.horizontalHeader().setStretchLastSection(True)
		
	def rowFactory(self) :
		return self.m_rowFactory
		
	def setRowFactory(self, rowFactory) :
		self.m_rowFactory = rowFactory
		
	def setCurrentPage(self, currentPage) :
		currentPage = min(max(1, currentPage), self.m_pagesCount)
		if (self.m_currentPage != currentPage) :
			self.m_currentPage = currentPage
			self.updateModel(self.m_selectedRow)
		
	def setCurrentPageIndex(self, currentPageIndex) :
		self.setCurrentPage(currentPageIndex + 1)

	def previousPage(self) :
		self.setCurrentPage(self.m_currentPage - 1)
		
	def nextPage(self) :
		self.setCurrentPage(self.m_currentPage + 1)
		
	def updateModel(self, rowToSelect=-1) :
		if (rowToSelect >= 0) :
			self.m_selectionModel.blockSignals(True)

		currentFirstIndex	= (self.m_currentPage-1) * self.m_rowsPerPage
		currentLastIndex	= self.m_currentPage * self.m_rowsPerPage
		currentData			= self.m_data[currentFirstIndex:currentLastIndex]
		
		self.m_model.setRowCount(0)
		if (self.m_rowFactory != None) :
			rowIndex = currentFirstIndex
			for row in currentData :
				items = self.m_rowFactory(row, self.m_columns)
				self.m_model.appendRow(items)
				for item in items :
					item.setData(QtCore.QVariant(int(rowIndex)), QtCore.Qt.UserRole)
				rowIndex += 1
				
		self.m_ui.comboBoxCurrentPage.setCurrentIndex(self.m_currentPage - 1)
		self.m_ui.tableView.resizeRowsToContents()
		
		if (rowToSelect >= 0) :
			rowToSelect = rowToSelect - ((self.m_currentPage-1) * self.m_rowsPerPage);
			self.m_ui.tableView.selectRow(rowToSelect)
			self.m_ui.tableView.scrollTo(self.m_model.createIndex(rowToSelect, 0), QtGui.QAbstractItemView.EnsureVisible)
			self.m_selectionModel.blockSignals(False)

	def itemClicked(self, modelIndex) :
		self.rowClicked.emit(modelIndex.data(QtCore.Qt.UserRole).toPyObject())
		
	def itemDoubleClicked(self, modelIndex) :
		self.rowDoubleClicked.emit(modelIndex.data(QtCore.Qt.UserRole).toPyObject())
		
	def itemSelectionChanged(self) :
		self.m_selectedRow = -1
		selectedRows = self.m_selectionModel.selectedRows()
		if (selectedRows != None) :
			if (len(selectedRows) > 0) :
				self.m_selectedRow = selectedRows[0].data(QtCore.Qt.UserRole).toPyObject()
		self.rowSelected.emit(self.m_selectedRow)
