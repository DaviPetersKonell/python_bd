from conexao import conecta_db

def consultar(conexao):
    print("consultar")

def inserir(conexao):
    print("inserir")

def menu_vendas(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Categoria        |")
    print("|--------------------------------|")
    print("|     1 - Consultar Vendas       |")
    print("|     2 - Inserir Venda          |")
    print("|     3 - Sair do Sistema        |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")