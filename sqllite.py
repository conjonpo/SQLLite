import sqlite3

conn = sqlite3.connect('collegeteams.db')

print ("Opened database successfully")

conn.execute("DELETE from FOOTBALL where ID = 10;")
conn.commit()

print ("Success")

conn.close()