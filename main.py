import mysql.connector
import time

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SHIPPuuden300',
    database='fretex',
)
cursor = conexao.cursor()

def criar_usuario(usuario):
    print("Para criar seu cadastro por favor preencha as informações a seguir:")
    if usuario == 1:
        tipo = "prestador"
    else:
        tipo="cliente"
    nome_prestador = input("Nome: ")
    cpf_prestador = input("CPF: ")
    email_prestador = input("E-mail: ")
    logradouro_prestador = input("Logradouro: ")
    cep_prestador = int(input("Cep: "))
    bairro_prestador = input("Bairro: ")
    cidade_prestador = input("Cidade: ")
    estado_prestador = input("Estado: ")
    pdr = input("Ponto de Referência: ")
    if usuario == 1:
        capacidade_prestador = input("Capacidade(pequena, média, ou grande): ")

        comando = f'INSERT INTO Usuário (CPF, Nome, email,Tipo, Capacidade) VALUES ("{cpf_prestador}","{nome_prestador}","{email_prestador}","{tipo}","{capacidade_prestador}")'
        cursor.execute(comando)
        conexao.commit()

        comando = f'INSERT INTO endereco_cadastro (CPF,Logradouro, CEP, Bairro, Cidade, Estado, Ponto_de_referencia) VALUES ("{cpf_prestador}","{logradouro_prestador}",{cep_prestador},"{bairro_prestador}","{cidade_prestador}","{estado_prestador}","{pdr}")'
        cursor.execute(comando)
        conexao.commit()
    else:

        comando = f'INSERT INTO Usuário (CPF, Nome, email,Tipo) VALUES ("{cpf_prestador}","{nome_prestador}","{email_prestador}","{tipo}")'
        cursor.execute(comando)
        conexao.commit()

        comando = f'INSERT INTO endereco_cadastro (CPF,Logradouro, CEP, Bairro, Cidade, Estado, Ponto_de_referencia) VALUES ("{cpf_prestador}","{logradouro_prestador}",{cep_prestador},"{bairro_prestador}","{cidade_prestador}","{estado_prestador}","{pdr}")'
        cursor.execute(comando)
        conexao.commit()

        print("Aguarde enquanto validamos seu e-mail", time.sleep(.05), ".", time.sleep(.05), ".", time.sleep(.05), ".")
        print("E-mail validado!! \n\n Seu cadastro foi efetuado com sucesso !!!")




usuario = -1
while usuario != 0:
    print("""BEM VINDO AO FRETEX SOMOS PAU PRA TODA OBRA!!
Para prosseguir selecione alguma das opções a seguir:\n
    0 - Para sair do aplicativo!
    1 - Para entrar como um prestador!
    2 - Para entrar como um cliente!
    \n""")

    usuario = int(input())

    if usuario == 1:
        print("Seja Bem vindo será uma honra ter você trabalhando conosco!!!")
        decisao=input("Você tem já tem um cadastro? y/n")

        if decisao == 'n':
            criar_usuario(usuario)
        else:
            cpf_prestador = input("Qual o seu CPF? \n")
            try:
                comando = f'SELECT CPF FROM usuário WHERE CPF = "{cpf_prestador}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if (len(resultado) > 0):
                    comando = f'SELECT Nome FROM usuário WHERE CPF = "{cpf_prestador}"'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()

                    for i in resultado:
                        nome_prestador = i[0]

                    print(f"Olá {nome_prestador} o que deseja fazer a seguir?\n")
                else:
                    print("Desculpe você ainda tem um registro no nosso sistema :\n")

                    decisao = input("Gostaria de criar um cadastro agora? y/n ")
                    if decisao == 'y':
                        criar_usuario(usuario)
                        decisao = 0
                    else:
                        decisao = 0
            except Exception as err:
                print("couldn't connect")
                print("General error :: ", err)


        decisao = input("Gostaria de buscar um frete agora (y/n): ")
        if decisao == 'y':
            comando = f'SELECT Nome FROM usuário WHERE Tipo = "cliente"'
            cursor.execute(comando)
            resultado = cursor.fetchall()

            if (len(resultado) > 0 ):
                print("Temos",len(resultado), "cliente(s) no momento:")
                for i in resultado:
                    nome= i[0]
                    print(nome)

            else:
                print("Não temos clientes no momento")
        else:
            print('Usuário deslogado!')
    #______________________________________________Fim do prestador________________________________________
    elif usuario == 2:
        decisao=input("""Seja Bem vindo será uma honra prestar serviços a você!!!
        Você tem já tem um cadastro? y/n""")

        if decisao == 'n':
            criar_usuario(usuario)

        else:
            cpf_cliente = input("Qual o seu CPF? ")

            try:
                comando = f'SELECT CPF FROM usuário WHERE CPF = "{cpf_cliente}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if (len(resultado) > 0):
                    comando = f'SELECT Nome FROM usuário WHERE CPF = "{cpf_cliente}"'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()

                    for i in resultado:
                        nome_usuario = i[0]
                else:
                    print("Desculpe você ainda tem um registro no nosso sistema :")

            except Exception as err:
                print("couldn't connect")
                print("General error :: ", err)


            print("Qual ação você deseja fazer? \n")
            decisao = input("1 - Para relziar um frete\n2 - Para voltar ao início")




        while decisao == '1':
            produto = input("Qual produto voce quer pôr?:\n")
            foto = input("Adicione uma foto: ")
            quant = int(input("Quantos desse item você irá levar? "))
            msg = input("observações")
            comando = f'INSERT INTO itens (Nome, Foto, Quantidade, Informações_Adicionais) VALUES ("{produto}","{foto}",{quant},"{msg}")'
            cursor.execute(comando)
            conexao.commit()
            print("Deseja adicionar mais algum produto? y/n")
            decisao = input()
        else:
            print("Voltando para o início")


    elif usuario == 0:

        print("VOLTE SEMPRE !!!")














