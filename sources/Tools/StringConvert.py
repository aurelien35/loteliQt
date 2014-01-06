# -*- coding: utf-8 -*-
		  
def str2QString(text) :
	if (text == None) :
		return unicode("", 'utf-8')
	return unicode(text, 'utf-8')
	
def QString2str(text) :
	return str(text.toUtf8())
	
def date2str(date) :
	if (date == None) :
		return ""
	return date.strftime('%d/%m/%Y')
	
def date2QString(date) :
	return str2QString(date2str(date))
