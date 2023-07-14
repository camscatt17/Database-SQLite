import sqlite3

conn = sqlite3.connect('Pratica2/pratica2.db')
cursor = conn.cursor()

#Criando table pessoa
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoa(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL, 
        idade INTEGER,
        cidade VARCHAR(30) NOT NULL,
        estado VARCHAR(20) NOT NULL,
        cpf VARCHAR(11) NOT NULL
    );
""")
print("Tabela criada com sucesso!")

# Inserindo os dados na table
lista = [
    ('Jorge', 27, 'Florianopolis', 'Santa Catarina', '123.456.789-10'),
    ('Marcia', 18, 'Joao Pessoa', 'Paraiba', '321.654.987-01'),
    ('Cicero', 43, 'Recife', 'Pernambuco', '231.564.879-82'),
    ('Lara', 15, 'Fortaleza', 'Ceara', '132.645.798-61'),
    ('Enzo', 12, 'Belo Horizonte', 'Minas Gerais', '213.485.765-38')
]

cursor.executemany("""
    INSERT INTO pessoa(nome, idade, cidade, estado, cpf)
    VALUES (?,?,?,?,?)               
""", (lista))
conn.commit()
print("Dados inseridos com sucesso!")

# Busca por pessoas abaixo de 18 anos
cursor.execute("""
    SELECT * FROM pessoa
    WHERE idade < 18;
""")
captura = cursor.fetchall()
for linha in captura:
    print(linha)

#Deletando os dados das pessoas que tenham idade abaixo de 18 anos
cursor.execute("""
    DELETE FROM pessoa
    WHERE idade < 18;
""")
conn.commit()
print("Dados excluídos com sucesso!")

# Alterando a tabela adicionando uma nova coluna EMAIL
cursor.execute("""
    ALTER TABLE pessoa
    ADD COLUMN email VARCHAR(100);
""")
conn.commit() 
print("Coluna email adicionada com sucesso!")

# Atualização dos dados através de dados fornecidos pelo usuário
nome = input("Informe o seu nome: ")
email1 = 'jorgeFloripa@email.com'
email2 = 'marciaJP@email.com'
email3 = 'ciceroRE@email.com'
email4 = 'laraFT@email.com'
email5 = 'enzoBH@email.com'

cursor.execute("""
    UPDATE pessoa
    SET email = ?
    WHERE nome = ?    
""", (email5, nome))
conn.commit()
print("Email inserido com sucesso!")

# Exibindo os dados
cursor.execute("""
SELECT * FROM pessoa;
""")
dados = cursor.fetchall()
for pessoa in dados:
    print(pessoa)
conn.close()