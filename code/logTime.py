#!/usr/bin/python
import time
import sqlite3

def logTime(cur):
    current_time = readTime()
    cur.execute("INSERT INTO logtime (xdate, xtime) VALUES ('%s','%s')" % ( current_time[0], current_time[1] ) )   

def readTime():
    return time.strftime("%Y-%m-%d %H-%M-%S").split(' ')
    
#Open the SQL Connection
conn = sqlite3.connect('testTime.db')

db_cursor = conn.cursor()

#db_cursor.execute("CREATE TABLE logtime (xdate text, xtime text)")

#db_cursor.execute("INSERT INTO logtime (xdate, xtime) VALUES ('2016-02-24','12-32-00')"  )

logTime(db_cursor)


#Close the SQL Connection
conn.commit()
conn.close()
