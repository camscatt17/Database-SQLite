import database
print("Sys Login")
print("Para Criar conta tecle 1 e para fazer login 2")

option = int(input())

if(option == 1):
    user = input("Usuario: ")
    senha = input("Senha: ")
    email = input("Email: ")

    database.cursor.execute("""INSERT INTO DataClients(user, senha, email)
                               VALUES (?,?,?)""", (user, senha, email))
    database.conn.commit()
    print("Conta criada com sucesso!")

elif(option == 2):
    user = input("Usuario: ")
    senha = input("Senha: ")
    database.cursor.execute("""SELECT * FROM DataClients""")
    dados = database.cursor.fetchall()
    # Uma forma simples de se fazer verificação de credenciais
    for row in dados:
        if(user in row and senha in row):
            print("Bem vindo!")
else:
    print("Informe valores de 1 a 2 para prosseguir!")

