import mysql.connector
from usuario import Usuario



class Cliente(Usuario):
    produto = ''
    foto = ''
    quant = ''
    msg = ''
    decisao = ''
    numero = ''
    data = ''
    tipo = ''

    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def solicitar_frete(self, cpf):
        self.cpf = cpf
        print("Primeiramente vamos descrever os itens a ser enviados \n")

    ######################## Adicionar Itens ##################################
        self.decisao = '-1'
        while self.decisao != 'n':

            self.produto = input("Qual Item você deseja  pôr?:\n")
            self.foto = input("Adicione uma foto deste iten: ")
            self.quant = int(input("Quantos desse item você irá levar? "))
            self.msg = input("observações")
            comando = f'INSERT INTO itens (Nome, Foto, Quantidade, Informações_Adicionais, CPF) VALUES ("{self.produto}","{self.foto}",{self.quant},"{self.msg}","{self.cpf}")'
            self.cursor.execute(comando)
            self.conexao.commit()
            print("Deseja adicionar mais algum produto? y/n")
            self.decisao = input()
        self.decisao = '-1'
    ############## Endereço Incial ##########################################

        print("Vamos Agora definir o endereço inicial do frete")
        self.logradouro = input("Logradouro: ")
        self.numero = int(input("Número: "))
        self.cep = int(input("Cep: "))
        self.bairro = input("Bairro: ")
        self.cidade = input("Cidade: ")
        self.estado = input("Estado: ")
        self.pdr = input("Ponto de Referência: ")
        self.tipo = 'inicial'
        self.data = input("Diga a data do frete: ")

        comando = f'INSERT INTO endereco_frete (ID_endereco_frete, CPF, Logradouro, CEP, Bairro, Cidade, Estado, Data, Ponto_de_referencia, Tipo ) VALUES ({self.numero},"{self.cpf}","{self.logradouro}",{self.cep},"{self.bairro}","{self.cidade}","{self.estado}","{self.data}","{self.pdr}","{self.tipo}")'
        self.cursor.execute(comando)
        self.conexao.commit()

    ################### Endereço Final ###################################

        print("Agora o endereço final do frete")
        self.logradouro = input("Logradouro: ")
        self.numero = int(input("Número: "))
        self.cep = int(input("Cep: "))
        self.bairro = input("Bairro: ")
        self.cidade = input("Cidade: ")
        self.estado = input("Estado: ")
        self.pdr = input("Ponto de Referência: ")
        self.tipo = 'final'

        comando = f'INSERT INTO endereco_frete (ID_endereco_frete, CPF, Logradouro, CEP, Bairro, Cidade, Estado, Data, Ponto_de_referencia, Tipo ) VALUES ({self.numero},"{self.cpf}","{self.logradouro}",{self.cep},"{self.bairro}","{self.cidade}","{self.estado}","{self.data}","{self.pdr}","{self.tipo}")'
        self.cursor.execute(comando)
        self.conexao.commit()


        comando = f'INSERT INTO frete (CPF,Status) VALUES ("{self.cpf}","buscando")'
        self.cursor.execute(comando)
        self.conexao.commit()


