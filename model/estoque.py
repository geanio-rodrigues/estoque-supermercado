class Estoque:


    def __init__(self):
        self.__itens = {}


    def adicionar(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("A Quantidade deve ser maior que zero")

        codigo = produto.codigo

        if codigo in self.__itens:
            self.__itens[codigo]["quantidade"] += quantidade
        else:
            self.__itens[codigo] = {
                "produto": produto, 
                "quantidade": quantidade
            }

    
    def remover(self, produto, quantidade):
        if codigo not in self.__itens:
            return False

        if self.__itens[codigo]["quantidade"] < quantidade:
            return False

        self.__itens[codigo]["quantidade"] -= quantidade
        return True


    def listar(self):
        return self.__itens