"""database create."""
import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''DROP TABLE IF EXISTS student''')
print "Opened database successfully"

conn.execute('CREATE TABLE student(name TEXT, addr TEXT, city TEXT, pin TEXT,blood_group TEXT)')
print "Table created successfully";
conn.close()
