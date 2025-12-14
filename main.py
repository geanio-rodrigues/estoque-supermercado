from model.categoria import Categoria
from model.fornecedor import Fornecedor
from model.produto import Produto
from model.estoque import Estoque
from service.estoque_service import EstoqueService


def mostrar_menu():
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar estoque")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    estoque = Estoque()
    estoque_service = EstoqueService(estoque)

    # Dados base para teste inicial
    categoria_padrao = Categoria("Alimentos")
    fornecedor_padrao = Fornecedor("Fornecedor Padrao", 8899999999)

    while True:
        opcao = mostrar_menu()

        try:
            if opcao == "1":
                codigo = int(input("Código do produto: "))
                nome = input("Nome do produto: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))

                produto = Produto(
                    codigo,
                    nome,
                    preco,
                    quantidade
                )

                estoque_service.entrada_produto(produto, quantidade)
                print("Produto adicionado com sucesso!")

            elif opcao == "2":
                codigo = int(input("Código do produto: "))
                quandiade = int(input("Quantidade para remover: "))

                estoque_service.saida_produto(codigo, quantidade)
                print("Produto removido com sucesso!")

            elif opcao == "3":
                estoque_service.exibir_estoque()

            elif opcao == "0":
                print("Encerrando o sistema...")

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as erro:
            print(f"Erro: {erro}")

        
if __name__ == "__main__":
    main()