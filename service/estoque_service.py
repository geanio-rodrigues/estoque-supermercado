from model.estoque import Estoque

class EstoqueService:

    def __init__(self, estoque: Estoque):
        self.estoque = estoque

    
    def entrada_produto(self, produto, quantidade):
        self.estoque.adicionar(produto, quantidade)

    
    def saida_produto(self, codigo, quantidade):
        sucesso  = self.estoque.remover(codigo, quantidade)
        if not sucesso:
            raise ValueError("Quantidade insuficiente ou produto inexistente.")

    
    def exibir_estoque(self):
        print("\n=== ESTOQUE ATUAL ===")
        for item in self.estoque.listar().values():
            produto = item["produto"]
            quantidade = item["quantidade"]
            print(f"{produto} | Quantidade: {quantidade}")