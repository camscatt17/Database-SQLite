import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS DataClients(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        senha TEXT NOT NULL, 
        email TEXT NOT NULL
    );
""")

conn.commit()