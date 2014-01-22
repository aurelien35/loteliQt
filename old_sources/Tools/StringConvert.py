# -*- coding: utf-8 -*-

from PyQt4	import QtCore
		  
def str2QString(text) :
	if (text == None) :
		return QtCore.QString()
	return QtCore.QString(unicode(text))
	
def strList2QStringList(strList) :
	result = QtCore.QStringList()
	if (strList != None) :
		for element in strList :
			result.append(str2QString(element))
	return result
	
def QString2str(text) :
	return unicode(text)
	
def date2str(date) :
	if (date == None) :
		return ""
	return date.strftime('%d/%m/%Y')
	
def date2QString(date) :
	return str2QString(date2str(date))
