import mysql.connector
from usuario import Usuario



class Prestador(Usuario):
    cpf_usuario = ''
    d_i = ''
    d_f = ''
    nome_usuario = ''

    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def bucar_cliente(self):
        print("Vamos Verificar se existe algum cliente no momento em busca de um frete !!!\n")
        try:
            comando = f'SELECT Status FROM frete WHERE Status = "buscando"'
            self.cursor.execute(comando)
            resultado = self.cursor.fetchall()


            if len(resultado) > 0 :
                comando = f'SELECT CPF FROM frete WHERE Status = "buscando"'
                self.cursor.execute(comando)
                resultado = self.cursor.fetchall()

                for i in resultado:
                    self.cpf_usuario = i[0]

                comando = f'SELECT Nome FROM usuário WHERE CPF = "{self.cpf_usuario}"'
                self.cursor.execute(comando)
                resultado = self.cursor.fetchall()

                i = 0

                for i in resultado:
                    self.nome_usuario = i[0]

                print(f"Encontramos o cliente {self.nome_usuario} \n")

                comando = f'SELECT logradouro FROM endereco_frete WHERE CPF = "{self.cpf_usuario}" and Tipo = "inicial"'
                self.cursor.execute(comando)
                resultado = self.cursor.fetchall()

                i = 0

                for i in resultado:
                    self.d_i = i[0]

                comando = f'SELECT logradouro FROM endereco_frete WHERE CPF = "{self.cpf_usuario}" and Tipo = "final"'
                self.cursor.execute(comando)
                resultado = self.cursor.fetchall()

                for i in resultado:
                    self.d_f = i[0]

                print(f"Ele irá de {self.d_i}, para {self.d_f}")
                decisao = input("Deseja aceitar o frete e entrar em contato com o cliente para fecharem um valor? y/n:  ")

                if decisao == 'y':
                    comando = f'UPDATE frete SET Status = "aceito"'
                    self.cursor.execute(comando)
                    self.conexao.commit()
                elif decisao == 'n':
                    print("Putz que braba cara, infelizmente era o único cliente que tínhamos no momento.")
            else:
                print("Desculpe não há nenhum frete disponível no momento :/ \n")

        except Exception as err:
            print("couldn't connect")
            print("General error :: ", err)







