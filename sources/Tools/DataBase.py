# -*- coding: utf-8 -*-
		  
import sqlite3

def DataBaseRowFactory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

PersistentConnexion				= sqlite3.connect('./data/loteli.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
PersistentConnexion.row_factory	= DataBaseRowFactory

def cursor() :
	return PersistentConnexion.cursor()

def select(query, values={}) :
	cursor = PersistentConnexion.cursor()
	cursor.execute(query, values)
	result = cursor.fetchall()
	if (result == None) :
		result = []
	return result
	
def selectOne(query, values={}) :
	cursor = PersistentConnexion.cursor()
	cursor.execute(query, values)
	result = cursor.fetchall()
	if (result != None) :
		if (len(result) == 1) :
			return result[0]
	return None

def insert(query, values={}) :
	cursor = PersistentConnexion.cursor()
	cursor.execute(query, values)
	PersistentConnexion.commit()
	return cursor.lastrowid

def update(query, values={}) :
	cursor = PersistentConnexion.cursor()
	cursor.execute(query, values)
	PersistentConnexion.commit()
