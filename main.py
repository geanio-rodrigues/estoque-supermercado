from model.categoria import Categoria
from model.fornecedor import Fornecedor
from model.produto import Produto
from model.estoque import Estoque
from service.estoque_service import EstoqueService

def menu_principal():
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Adicionar (Cadastros e Entradas)")
    print("2 - Remover (Exclusões e Saídas)")
    print("3 - Listar (Relatórios)")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def menu_adicionar():
    print("\n--- MENU ADICIONAR ---")
    print("1 - Nova Categoria")
    print("2 - Novo Fornecedor")
    print("3 - Novo Produto (Já insere no estoque)")
    print("4 - Entrada de Estoque (Produto existente)")
    print("0 - Voltar")
    return input("Escolha: ")

def menu_remover():
    print("\n--- MENU REMOVER ---")
    print("1 - Excluir Categoria")
    print("2 - Excluir Fornecedor")
    print("3 - Excluir Produto (Cadastro completo)")
    print("4 - Saída de Estoque (Baixa de quantidade)")
    print("0 - Voltar")
    return input("Escolha: ")

def menu_listar():
    print("\n--- MENU LISTAR ---")
    print("1 - Listar Categorias")
    print("2 - Listar Fornecedores")
    print("3 - Listar Estoque Geral")
    print("0 - Voltar")
    return input("Escolha: ")

def main():
    categorias = []
    fornecedores = []
    produtos = []

    estoque = Estoque()
    estoque_service = EstoqueService(estoque)

    while True:
        opcao = menu_principal()

        try:
            # FLUXO 1: ADICIONAR
            if opcao == "1":
                sub_op = menu_adicionar()
                
                if sub_op == "1":
                    nome = input("Nome da categoria: ")
                    categorias.append(Categoria(nome))
                    print("Categoria adicionada.")

                elif sub_op == "2":
                    nome = input("Nome do fornecedor: ")
                    telefone = int(input("Telefone: "))
                    fornecedores.append(Fornecedor(nome, telefone))
                    print("Fornecedor adicionado.")

                elif sub_op == "3":
                    if not categorias or not fornecedores:
                        print("Erro: Cadastre categorias e fornecedores antes.")
                        continue

                    if len(produtos) == 0:
                        codigo = 1
                    else:
                        codigo = max(p.codigo for p in produtos) + 1
                    
                    print(f"--> Criando produto com Código: {codigo}")

                    nome = input("Nome: ")
                    preco = float(input("Preço: "))

                    print("\nCategorias:")
                    for i, c in enumerate(categorias): print(f"{i} - {c}")
                    cat = categorias[int(input("Escolha a categoria: "))]

                    print("\nFornecedores:")
                    for i, f in enumerate(fornecedores): print(f"{i} - {f}")
                    forn = fornecedores[int(input("Escolha o fornecedor: "))]

                    novo_produto = Produto(codigo, nome, preco, cat, forn)
                    produtos.append(novo_produto)

                    qtd_input = input("Quantidade inicial no estoque (Enter para 0): ")
                    qtd_inicial = int(qtd_input) if qtd_input.strip() else 0
                    
                    estoque_service.entrada_produto(novo_produto, qtd_inicial)
                    print(f"Produto cadastrado com {qtd_inicial} unidades.")

                elif sub_op == "4":
                    if not produtos:
                        print("Nenhum produto cadastrado.")
                        continue
                    for p in produtos: print(p)
                    
                    codigo = int(input("Código do produto: "))
                    qtd = int(input("Quantidade a adicionar: "))
                    
                    produto_encontrado = next((p for p in produtos if p.codigo == codigo), None)
                    if produto_encontrado:
                        estoque_service.entrada_produto(produto_encontrado, qtd)
                        print("Estoque atualizado.")
                    else:
                        print("Produto não encontrado.")

            # REMOVER
            elif opcao == "2":
                sub_op = menu_remover()

                if sub_op == "1":
                    if not categorias:
                        print("Nenhuma categoria para remover.")
                    else:
                        for i, c in enumerate(categorias): print(f"{i} - {c}")
                        categorias.pop(int(input("Índice para remover: ")))
                        print("Categoria removida.")

                elif sub_op == "2":
                    if not fornecedores:
                        print("Nenhum fornecedor para remover.")
                    else:
                        for i, f in enumerate(fornecedores): print(f"{i} - {f}")
                        fornecedores.pop(int(input("Índice para remover: ")))
                        print("Fornecedor removido.")

                elif sub_op == "3":
                    if not produtos:
                        print("Nenhum produto para remover.")
                    else:
                        for i, p in enumerate(produtos): print(f"{i} - {p}")
                        idx = int(input("Índice para remover: "))
                        produtos.pop(idx)
                        print("Produto removido do sistema.")

                elif sub_op == "4":
                    if not produtos:
                        print("Nenhum produto cadastrado.")
                    else:
                        codigo = int(input("Código do produto: "))
                        qtd = int(input("Quantidade a remover: "))
                        estoque_service.saida_produto(codigo, qtd)
                        print("Saída registrada.")

            # LISTAR
            elif opcao == "3":
                sub_op = menu_listar()

                if sub_op == "1":
                    if not categorias:
                        print("--- Nenhuma categoria encontrada ---")
                    else:
                        print("\n--- LISTA DE CATEGORIAS ---")
                        for c in categorias: print(c)

                elif sub_op == "2":
                    if not fornecedores:
                        print("--- Nenhum fornecedor encontrado ---")
                    else:
                        print("\n--- LISTA DE FORNECEDORES ---")
                        for f in fornecedores: print(f)

                elif sub_op == "3":
                    # O método listar() do estoque já retorna um dict vazio se não tiver nada
                    if not estoque.listar():
                        print("--- Estoque vazio ---")
                    else:
                        estoque_service.exibir_estoque()

            elif opcao == "0":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida.")

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()