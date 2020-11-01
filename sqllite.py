import sqlite3

conn = sqlite3.connect('collegeteams.db')

print ("Opened database successfully")

conn.execute("UPDATE FOOTBALL set POINTS = 33.8 where ID = 9")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT ID, team, conference, points from FOOTBALL")
for row in cursor:
   print ("RANK = ", row[0])
   print ("TEAM = ", row[1]) 
   print ("CONFERENCE = ", row[2])
   print ("POINTS = ", row[3], "\n")

print ("Success")

conn.close()