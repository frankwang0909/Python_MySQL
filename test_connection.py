#!/usr/bin/env python
# -*- coding: utf-8 -*-


import MySQLdb

conn  = MySQLdb.Connect(
		host = '127.0.0.1',
		port = 3306,
		user = 'root',
		passwd = 'frank',
		db = 'test',
		charset = 'utf8'
	)

# 获取交互对象

cursor = conn.cursor()

print cursor

print conn 