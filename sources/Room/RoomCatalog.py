# -*- coding: utf-8 -*-

import Room
import Tools.DataBase

def loadRoomCatalog() :
	# TODO : gestion des erreurs : lever une exception
	roomCatalog = {}
	roomsData = Tools.DataBase.select(u'''SELECT rowid, * FROM rooms ORDER BY rowid''')
	for roomData in roomsData :
		room			= Room.Room()
		room.m_id		= roomData["rowid"]
		room.m_number	= roomData["number"]
		room.m_name		= roomData["name"]
		roomCatalog[room.m_id] = room
			
	return roomCatalog

RoomCatalog = loadRoomCatalog()
