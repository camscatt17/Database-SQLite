#Importando a biblioteca
import sqlite3

#Conectar ao banco de dados
conn = sqlite3.connect('database.db')

#Criar um cursor que irá nos permitir navegar entre os registros
cursor = conn.cursor()

#Criar table
cursor.execute("""

    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER, 
        cpf VARCHAR(11) NOT NULL
    );
    
""")
print("Tabela Criada!")

conn.close()
