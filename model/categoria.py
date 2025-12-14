class Categoria:

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome da categoria deve ser um texto não vazio")
        self.__nome = novo_nome

    def __str__(self):
        return self.nome