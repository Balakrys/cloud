import sqlite3
conn = sqlite3.connect('datbas.db')
conn.execute('''DROP TABLE IF EXISTS LOGI''')
conn.execute('CREATE TABLE LOGI(name TEXT,mail TEXT,password TEXT,confirm TEXT,gender TEXT)')
conn.close()

