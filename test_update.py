#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='frank',
    db='test',
    charset='utf8'
)

cursor = conn.cursor()

sql_insert = "insert into user(userid, username) value(12, ')"

sql_update = "update user set username='Alex' where userid=9"

sql_delete = "delete from user where userid<3"

cursor.execute(sql_insert)
print cursor.rowcountNickWww

cursor.execute(sql_update)
print cursor.rowcount

cursor.execute(sql_delete)
print cursor.rowcount

conn.commit()

cursor.close()

conn.close()
