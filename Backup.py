import sqlite3
import io

conn = sqlite3.connect('database.db')

with io.open('DatabaseBackup.sql','w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)
print("Backup realizado com sucesso")
print("Salvo como DatabaseBackup.sql")