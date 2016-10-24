"""database create."""
import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";
conn.execute('''DROP TABLE IF EXISTS donar''')
conn.execute('''CREATE TABLE donar(state VARCHAR, city VARCHAR, blood VARCHAR)''')
conn.execute('''INSERT INTO donar VALUES('Arunachal Pradesh ','17',"AB-")''')
conn.execute('''INSERT INTO donar VALUES('INAR','18',"AB+")''')
print "Table created successfully"
conn.commit()

