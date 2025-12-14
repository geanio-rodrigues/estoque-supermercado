from model.categoria import Categoria
from model.fornecedor import Fornecedor


class Produto:

    def __init__(self, codigo, nome, preco, categoria, fornecedor):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.fornecedor = fornecedor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def categoria(self):
        return self.__categoria

    @property
    def fornecedor(self):
        return self.__fornecedor

    @codigo.setter
    def codigo(self, novo_codigo):
        if not isinstance(novo_codigo, int) or novo_codigo <= 0:
            raise ValueError("O código deve ser um número inteiro maior que 0")
        self.__codigo = novo_codigo
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome do produto deve ser um texto não vazio")
        self.__nome = novo_nome

    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)) or novo_preco < 0:
            raiser ValueError("O preço deve ser um número maior que 0")
        self.__preco = floar(novo_preco)

    @categoria.setter
    def categoria(self, nova_categoria):
        if not isinstance(nova_categoria, Categoria):
            raise ValueError("Categoria inválida")
        self.__categoria = nova_categoria

    @fornecedor.setter
    def fornecedor(self, novo_fornecedor):
        if not isinstance(novo_fornecedor, Fornecedor):
            raise ValueError("Fornecedor inválido")
        self.__fornecedor = novo_fornecedor

    def __str__(self):
        return (
            f"[{self.codigo}] {self.nome} | "
            f"R$ {self.preco:.2f} | Categoria: {self.categoria}"
        )