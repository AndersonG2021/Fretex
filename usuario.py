import mysql.connector

class Usuario():
    nome = ''
    cpf = ''
    email = ''
    logradouro = ''
    cep = ''
    bairro = ''
    cidade = ''
    estado = ''
    pdr = ''
    tipo = ''
    senha = ''

    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def logar(self,tipo):
        self.tipo = tipo
        self.cpf = input("Qual o seu CPF? \n")
        self.senha = input("Digite sua Senha: ")
        try:
            comando = f'SELECT CPF FROM usuário WHERE CPF = "{self.cpf}"'
            self.cursor.execute(comando)
            resultado1 = self.cursor.fetchall()

            comando = f'SELECT Senha FROM usuário WHERE Senha = "{self.senha}"'
            self.cursor.execute(comando)
            resultado2 = self.cursor.fetchall()

            if (len(resultado1) > 0 and len(resultado2) > 0):
                comando = f'SELECT Nome FROM usuário WHERE CPF = "{self.cpf}"'
                self.cursor.execute(comando)
                resultado = self.cursor.fetchall()

                for i in resultado:
                    self.nome = i[0]

                print(f"Olá {self.nome} o que deseja fazer a seguir?\n")
            else:
                print("Desculpe você ainda tem um registro no nosso sistema :\n")
                print("Mas não se preocupe vamos realizar seu cadastro agora!!")
                self.cadastrar(self.tipo)

        except Exception as err:
            print("couldn't connect")
            print("General error :: ", err)

    def verificar_cadastro(self, tipo):
        self.tipo = tipo
        self.decisao = input("Você já possui cadastro? y/n ")
        if self.decisao == 'n':
            self.cadastrar(self.tipo)
        else:
            self.logar(self.tipo)
        return self.cpf

    def cadastrar(self, tipo):
        self.tipo = tipo
        print("Para criar seu cadastro por favor preencha as informações a seguir:")
        self.nome = input("Nome: ")
        self.senha = input("Digite sua senha: ")
        self.cpf = input("CPF: ")
        self.email = input("E-mail: ")
        self.logradouro = input("Logradouro: ")
        self.cep = int(input("Cep: "))
        self.bairro = input("Bairro: ")
        self.cidade = input("Cidade: ")
        self.estado = input("Estado: ")
        self.pdr = input("Ponto de Referência: ")

        comando = f'INSERT INTO usuário (CPF, Senha, Nome, email,Tipo) VALUES ("{self.cpf}","{self.senha}","{self.nome}","{self.email}","{self.tipo}")'
        self.cursor.execute(comando)
        self.conexao.commit()

        comando = f'INSERT INTO endereco_cadastro (CPF,Logradouro, CEP, Bairro, Cidade, Estado, Ponto_de_referencia) VALUES ("{self.cpf}","{self.logradouro}",{self.cep},"{self.bairro}","{self.cidade}","{self.estado}","{self.pdr}")'
        self.cursor.execute(comando)
        self.conexao.commit()

        print("Aguarde enquanto validamos seu e-mail")
        print("E-mail validado!! \n\n Seu cadastro foi efetuado com sucesso !!!")
        return self.cpf

    def alterar_cadastro(self,cpf):
        self.cpf = cpf
        decisao = -1
        while decisao != '0':
            decisao = input("""Qual dado você deseja alterar?
                    1 - Nome
                    2 - Endereço
                    0 - Voltar para o perfil""")

            if decisao == '1':
                print("Digite seu dados corretamente: ")
                self.nome = input("Digite Seu nome: ")
                self.email = input("Digite seu e-mail: ")
                self.senha = input("Digite sua senha: ")
                comando = f'UPDATE usuário SET Nome = "{self.nome}", email = "{self.email}", Senha = "{self.senha}" WHERE CPF = "{self.cpf}"'
                self.cursor.execute(comando)
                self.conexao.commit()

            if decisao == '2':
                print("Nos infome seu endereço corretamente: \n")
                self.logradouro = input("\nLogradouro: ")
                self.cep = int(input("\nCep: "))
                self.bairro = input("\nBairro: ")
                self.cidade = input("\nCidade: ")
                self.estado = input("\nEstado: ")
                self.pdr = input("\nPonto de Referência: ")
                comando = f'UPDATE endereco_cadastro SET Logradouro = "{self.logradouro}", CEP = "{self.cep}", Bairro = "{self.bairro}", Cidade = "{self.cidade}", Estado = "{self.estado}", Ponto_de_referencia = "{self.pdr}" WHERE CPF = "{self.cpf}"'
                self.cursor.execute(comando)
                self.conexao.commit()
            elif decisao == '0':
                comando = f'SELECT usuário.Nome, usuário.Email, usuário.Senha, endereco_cadastro.Logradouro, endereco_cadastro.CEP, endereco_cadastro.Bairro, endereco_cadastro.Cidade, endereco_cadastro.Estado, endereco_cadastro.Ponto_de_referencia FROM usuário INNER JOIN endereco_cadastro ON usuário.CPF = endereco_cadastro.CPF AND usuário.Tipo = "cliente"'
                self.resultado = 0
                self.cursor.execute(comando)
                resultado = self.cursor.fetchall()
                for i in resultado:
                    print(i)

                print("Seus dados foram alterados")
                print("Voltando para página de perfil !!\n\n")



    def sair(self):
        print("Volte Sempre!!")


