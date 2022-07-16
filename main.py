import mysql.connector
from cliente import Cliente
from prestador import Prestador

print("Cavalo")
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SHIPPuuden300',
    database='fretex',
)

cursor = conexao.cursor()

prestador = Prestador()

cliente = Cliente()

print("Cavalo")

escolha = -1
while escolha != 0:
    print("""BEM VINDO AO FRETEX SOMOS PAU PRA TODA OBRA!!
    Para prosseguir selecione alguma das opções a seguir:\n
        0 - Para sair do aplicativo!
        1 - Para entrar como um prestador!
        2 - Para entrar como um cliente! """)

    escolha = input("Digite uma opção")

    if escolha == '1':

        prestador.verificar_cadastro()

    elif escolha == '2':

        cliente.verificar_cadastro()

    elif escolha == '0':
        print("Volte Sempre!!!")












