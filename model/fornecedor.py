class Fornecedor:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome do fornecedor deve ser um texto não vazio")
        self.__nome = novo_nome
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone, int):
            raise ValueError("O telefone deve ser um número")
        self.__telefone = novo_telefone

    def __str__(self):
        return f"{self.nome} - Tel: {self.telefone}"