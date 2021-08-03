from finanace_db.common_external_libs import *

conn = sqlite3.connect('findb.sqlite') #makes a connection to DB or creates new if it doesn't exist
cur = conn.cursor() #db handle - like file opem for DB operations

cur.execute('DROP TABLE IF EXISTS Asset') #to allow multiple runs of the programm
cur.execute('DROP TABLE IF EXISTS Category') #to allow multiple runs of the programm
cur.execute('DROP TABLE IF EXISTS Provider') #to allow multiple runs of the programm
cur.execute('DROP TABLE IF EXISTS Currency') #to allow multiple runs of the programm

#DB Tables definition
cur.executescript('''
    CREATE TABLE IF NOT EXISTS Category (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    asset_class TEXT, 
    asset_subclass TEXT,
    UNIQUE(asset_class, asset_subclass)
    )
''')

cur.executescript('''
    CREATE TABLE IF NOT EXISTS Provider (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    name TEXT UNIQUE,
    to_rub REAL,
    to_usd REAL,
    to_eur REAL
    )
''')

cur.executescript('''
    CREATE TABLE IF NOT EXISTS Currency (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    name TEXT UNIQUE
    )
''')

cur.executescript('''
    CREATE TABLE IF NOT EXISTS Asset (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    name TEXT, 
    purchase_price REAL, 
    current_price REAL,
    category_id INTEGER,
    provider_id INTEGER,
    currency_id INTEGER
    )
''')

conn.commit()
cur.close()