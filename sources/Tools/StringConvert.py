# -*- coding: utf-8 -*-

from PyQt4	import QtCore
		  
def str2QString(text) :
	if (text == None) :
		return unicode("", 'utf-8')
	return unicode(text, 'utf-8')
	
def strList2QStringList(strList) :
	result = QtCore.QStringList()
	if (strList != None) :
		for element in strList :
			result.append(str2QString(element))
	return result
	
def QString2str(text) :
	return str(text.toUtf8())
	
def date2str(date) :
	if (date == None) :
		return ""
	return date.strftime('%d/%m/%Y')
	
def date2QString(date) :
	return str2QString(date2str(date))
