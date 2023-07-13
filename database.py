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

#Inserindo dados na tabela
cursor.execute("""
    INSERT INTO clientes(nome, idade, cpf)
    VALUES ('Joao', 26, '123.456.789-01')
               """)
conn.commit()
print("Dados inseridos!")

#Solicitando dados ao usuário
nome = str(input("Informe o seu nome: "))
idade = str(input("Informe a sua idade: "))
cpf = str(input("Informe o seu CPF: "))

#Inserindo dados na tabela atraves de dados fornecidos pelo usuário
cursor.execute("""
    INSERT INTO clientes(nome, idade, cpf)
    VALUES (?, ?, ?)
               """, (nome, idade, cpf))
conn.commit()
print("Dados inseridos!")



conn.close()
