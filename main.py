from model.categoria import Categoria
from model.fornecedor import Fornecedor
from model.produto import Produto
from model.estoque import Estoque
from service.estoque_service import EstoqueService


def menu():
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Adicionar categoria")
    print("2 - Remover categoria")
    print("3 - Listar categorias")
    print("4 - Adicionar fornecedor")
    print("5 - Remover fornecedor")
    print("6 - Listar fornecedores")
    print("7 - Adicionar produto")
    print("8 - Remover produto")
    print("9 - Aumentar estoque")
    print("10 - Diminuir estoque")
    print("11 - Listar produtos")
    print("12 - Listar estoque")
    print("0 - Sair")
    return input("Escolha: ")


def main():
    categorias = []
    fornecedores = []
    produtos = []

    estoque = Estoque()
    estoque_service = EstoqueService(estoque)

    while True:
        opcao = menu()

        try:
            # CATEGORIA
            if opcao == "1":
                nome = input("Nome da categoria: ")
                categorias.append(Categoria(nome))
                print("Categoria adicionada.")

            elif opcao == "2":
                for i, c in enumerate(categorias):
                    print(f"{i} - {c}")
                idx = int(input("Escolha para remover: "))
                categorias.pop(idx)
                print("Categoria removida.")

            elif opcao == "3":
                if not categorias:
                    print("Nenhuma categoria cadastrada.")
                for c in categorias:
                    print(c)

            # FORNECEDOR
            elif opcao == "4":
                nome = input("Nome do fornecedor: ")
                telefone = int(input("Telefone: "))
                fornecedores.append(Fornecedor(nome, telefone))
                print("Fornecedor adicionado.")

            elif opcao == "5":
                for i, f in enumerate(fornecedores):
                    print(f"{i} - {f}")
                idx = int(input("Escolha para remover: "))
                fornecedores.pop(idx)
                print("Fornecedor removido.")

            elif opcao == "6":
                if not fornecedores:
                    print("Nenhum fornecedor cadastrado.")
                for f in fornecedores:
                    print(f)

            # PRODUTO
            elif opcao == "7":
                if not categorias or not fornecedores:
                    print("Cadastre categorias e fornecedores antes.")
                    continue

                codigo = int(input("Código: "))
                nome = input("Nome: ")
                preco = float(input("Preço: "))

                print("\nCategorias:")
                for i, c in enumerate(categorias):
                    print(f"{i} - {c}")
                cat = categorias[int(input("Escolha: "))]

                print("\nFornecedores:")
                for i, f in enumerate(fornecedores):
                    print(f"{i} - {f}")
                forn = fornecedores[int(input("Escolha: "))]

                produto = Produto(codigo, nome, preco, cat, forn)
                produtos.append(produto)
                print("Produto cadastrado.")

            elif opcao == "8":
                for i, p in enumerate(produtos):
                    print(f"{i} - {p}")
                idx = int(input("Escolha para remover: "))
                produtos.pop(idx)
                print("Produto removido.")

            elif opcao == "9":
                for p in produtos:
                    print(p)
                codigo = int(input("Código do produto: "))
                qtd = int(input("Quantidade: "))
                produto = next(p for p in produtos if p.codigo == codigo)
                estoque_service.entrada_produto(produto, qtd)
                print("Estoque atualizado.")

            elif opcao == "10":
                codigo = int(input("Código do produto: "))
                qtd = int(input("Quantidade: "))
                estoque_service.saida_produto(codigo, qtd)
                print("Estoque atualizado.")

            elif opcao == "11":
                if not produtos:
                    print("Nenhum produto cadastrado.")
                for p in produtos:
                    print(p)

            elif opcao == "12":
                if not estoque.listar():
                    print("Estoque vazio.")
                else:
                    estoque_service.exibir_estoque()

            elif opcao == "0":
                print("Encerrando...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
