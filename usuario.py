import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SHIPPuuden300',
    database='fretex',
)
cursor = conexao.cursor()


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
    tipo = 'cliente'

    def logar(self):
        print("Você está logado")

    def verificar_cadastro(self):
        self.decisao = input("Você já possui cadastro? y/n")
        if self.decisao == 'n':
            self.cadastrar()
        else:
            self.cpf = input("Qual o seu CPF? \n")
            try:
                comando = f'SELECT CPF FROM usuário WHERE CPF = "{self.cpf}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if (len(resultado) > 0):
                    comando = f'SELECT Nome FROM usuário WHERE CPF = "{self.cpf}"'
                    cursor.execute(comando)
                    resultado = cursor.fetchall()

                    for i in resultado:
                        self.nome = i[0]

                    print(f"Olá {self.nome} o que deseja fazer a seguir?\n")
                else:
                    print("Desculpe você ainda tem um registro no nosso sistema :\n")
                    print("Mas não se preocupe vamos realizar seu cadastro agora!!")
                    self.cadastrar()

            except Exception as err:
                print("couldn't connect")
                print("General error :: ", err)

    def cadastrar(self):
        print("Para criar seu cadastro por favor preencha as informações a seguir:")
        self.nome = input("Nome: ")
        self.cpf = input("CPF: ")
        self.email = input("E-mail: ")
        self.logradouro = input("Logradouro: ")
        self.cep = int(input("Cep: "))
        self.bairro = input("Bairro: ")
        self.cidade = input("Cidade: ")
        self.estado = input("Estado: ")
        self.pdr = input("Ponto de Referência: ")

        comando = f'INSERT INTO Usuário (CPF, Nome, email,Tipo) VALUES ("{self.cpf}","{self.nome}","{self.email}","{self.tipo}")'
        cursor.execute(comando)
        conexao.commit()

        comando = f'INSERT INTO endereco_cadastro (CPF,Logradouro, CEP, Bairro, Cidade, Estado, Ponto_de_referencia) VALUES ("{self.cpf}","{self.logradouro}",{self.cep},"{self.bairro}","{self.cidade}","{self.estado}","{self.pdr}")'
        cursor.execute(comando)
        conexao.commit()

        print("Aguarde enquanto validamos seu e-mail")
        print("E-mail validado!! \n\n Seu cadastro foi efetuado com sucesso !!!")

    def sair(self):
        print("Volte Sempre!!")


cursor.close()
conexao.close()
