from clientes import cadastrar_cliente, listar_clientes
from produtos import (
    listar_produtos,
    cadastrar_produto,
    atualizar_estoque,
    excluir_produto
)
from pedidos import criar_pedido, listar_pedidos


def mostrar_menu():
    print("\n" + "=" * 40)
    print("           LOJA DE ROUPAS")
    print("=" * 40)
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Atualizar estoque")
    print("6 - Excluir produto")
    print("7 - Criar pedido")
    print("8 - Listar pedidos")
    print("0 - Sair")
    print("=" * 40)


def executar():
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            cadastrar_produto()

        elif opcao == "4":
            listar_produtos()

        elif opcao == "5":
            atualizar_estoque()

        elif opcao == "6":
            excluir_produto()

        elif opcao == "7":
            criar_pedido()

        elif opcao == "8":
            listar_pedidos()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

        input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    executar()