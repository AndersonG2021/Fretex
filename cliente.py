import mysql.connector
from usuario import Usuario

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SHIPPuuden300',
    database='fretex',
)

cursor = conexao.cursor()

class Cliente(Usuario):

    def buscar_frete(self):
        print("Vamos buscar o seu fretinho fique relaxadinho!!")




cliente = Cliente()

cliente.logar()
cliente.cadastrar()
cliente.sair()

cursor.close()
conexao.close()