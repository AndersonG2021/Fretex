import mysql.connector
from usuario import Usuario
from main import Usuario

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SHIPPuuden300',
    database='fretex',
)

cursor = conexao.cursor()

class Prestador(Usuario):

    def buscar_frete(self):
        print("Vamos buscar o seu fretinho fique relaxadinho!!")








cursor.close()
conexao.close()
