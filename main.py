import mysql.connector
from cliente import Cliente
from prestador import Prestador


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SHIPPuuden300',
    database='fretex',
)

cursor = conexao.cursor()

prestador = Prestador(cursor, conexao)

cliente = Cliente(cursor, conexao)

print("Cavalo")

escolha = -1
while escolha != '0':
    print("""BEM VINDO AO FRETEX SOMOS PAU PRA TODA OBRA!!
    Para prosseguir selecione alguma das opções a seguir:\n
        0 - Para sair do aplicativo!
        1 - Para entrar como um prestador!
        2 - Para entrar como um cliente! """)

    escolha = input("Digite uma opção:  ")

    if escolha == '1':
        tipo='prestador'
        cpf = prestador.verificar_cadastro(tipo)
        decisao = -1
        while decisao != '4':
            print("""O que deseja fazer agora?
                           1 - Buscar Frete
                           2 - Para Iniciar frete
                           3 - Para Editar informações de Perfil
                           4 - Para Deslogar""")
            decisao = input("Digite sua opção: ")
            if decisao == '1' :
                prestador.bucar_cliente()
        else:
            print("Usuário Deslogado!!\n")
            print("Voltando para o Menu inicial\n\n")

    elif escolha == '2':
        tipo = 'cliente'
        cpf = cliente.verificar_cadastro(tipo)

        decisao = '0'
        while decisao != '5':
            print("""O que deseja fazer agora?
                    1 - Para solicitar frete
                    2 - Para acompanhar frete
                    3 - Para Alterar frete
                    4 - Para Editar informações de Perfil
                    5 - Para Deslogar""")
            decisao = input("Digite sua opção: ")
            if decisao == '1':
                cliente.solicitar_frete(cpf)
            elif decisao == '4':
                cliente.alterar_cadastro(cpf)
        else:
            print("Usuário Deslogado!\n")

    elif escolha == '0':
        print("Volte Sempre!!!")




cursor.close()
conexao.close()




