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
# cursor.execute("""
#     INSERT INTO clientes(nome, idade, cpf)
#     VALUES ('Joao', 26, '123.456.789-01')
#                """)
# conn.commit()
# print("Dados inseridos!")

#Solicitando dados ao usuário
# nome = str(input("Informe o seu nome: "))
# idade = str(input("Informe a sua idade: "))
# cpf = str(input("Informe o seu CPF: "))

#Inserindo dados na tabela atraves de dados fornecidos pelo usuário
# cursor.execute("""
#     INSERT INTO clientes(nome, idade, cpf)
#     VALUES (?, ?, ?)
#                """, (nome, idade, cpf))
# conn.commit()
# print("Dados inseridos!")

#Imprimindo os dados da table
# cursor.execute("""
#     SELECT * FROM clientes
#     WHERE id = 2;
# """)
# captura = cursor.fetchall()
# for linha in captura:
#     print(linha)

# Deletando um registro
# cursor.execute("""
#     DELETE FROM clientes
#     WHERE id = 3
# """)
# conn.commit()
# print("Dados excluídos com sucesso!")

# Alterando a tabela com a inserção de uma nova coluna 
cursor.execute("""
    ALTER TABLE clientes
    ADD COLUMN cidade VARCHAR(30);
""")
conn.commit()
print("Tabela alterada!")

conn.close()
