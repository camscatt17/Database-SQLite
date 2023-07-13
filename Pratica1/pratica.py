import sqlite3

con = sqlite3.connect('Pratica1/pratica1.db')
cursor = con.cursor()

# Criando a table pessoa
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoa(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL, 
        idade INTEGER, 
        cidade VARCHAR(30), 
        estado VARCHAR(20), 
        cpf VARCHAR(11) NOT NULL    
    );
""")
print("Tabela criada com sucesso!")

#Inserindo os dados na table
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

con.commit()
print("Dados inseridos com sucesso!")

# Fazendo o update de dados da tabela
nome = input("Informe o seu nome: ")
newCidade = input("Informe sua nova cidade: ")
newEstado = input("Informe seu novo estado: ")

cursor.execute("""
    UPDATE pessoa 
    SET cidade = ?, estado = ?
    WHERE nome = ?
""", (newCidade, newEstado, nome))
con.commit()
print("Seus dados foram atualizados com sucesso!")

#Imprimindo os dados da table
cursor.execute("""
    SELECT * FROM pessoa;
""")
captura = cursor.fetchall()
for linha in captura:
    print(linha)


con.close()
