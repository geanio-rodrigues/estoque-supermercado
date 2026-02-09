-- Tabela Categoria
CREATE TABLE Categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela Fornecedor
CREATE TABLE Fornecedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj CHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(20)
);

-- Tabela Produto
CREATE TABLE Produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL CHECK (preco >= 0),
    categoria_id INT NOT NULL,
    fornecedor_id INT NOT NULL, 

    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
        ON DELETE RESTRICT,
    FOREIGN KEY (fornecedor_id) REFERENCES Fornecedores(id)
        ON DELETE RESTRICT
);

CREATE INDEX idx_produto_nome on Produtos(nome);