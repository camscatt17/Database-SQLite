import sqlite3
import io

conn = sqlite3.connect('DatabaseRecuperada.db')
cursor = conn.cursor()

f = io.open('DatabaseBackup.sql', 'r')
sql = f.read()
cursor.executescript(sql)
print("Banco de Dados Recuperados")
print("Salvo como DatabaseRecuperada.db")
conn.close()