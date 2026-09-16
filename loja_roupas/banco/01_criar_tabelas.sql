-- ========================================
-- 01 - CRIAR TABELAS
-- ========================================

DROP TABLE IF EXISTS itens_pedidos CASCADE;
DROP TABLE IF EXISTS pedido CASCADE;
DROP TABLE IF EXISTS produtos CASCADE;
DROP TABLE IF EXISTS categorias CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;

CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(14),
    cpf VARCHAR(14)
);

CREATE TABLE categorias (
    id_categoria INTEGER PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(200)
);

CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    preco DECIMAL(10,2) NOT NULL,
    tamanho VARCHAR(10),
    cor VARCHAR(30),
    estoque INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,

    FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
);

CREATE TABLE pedido (
    id_pedido INTEGER PRIMARY KEY,
    data_pedido DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    valor_total DECIMAL(10,2),
    id_cliente INTEGER NOT NULL,

    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
);

CREATE TABLE itens_pedidos (
    id_item INTEGER PRIMARY KEY,
    quantidade INTEGER NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,

    FOREIGN KEY (id_pedido)
        REFERENCES pedido(id_pedido),

    FOREIGN KEY (id_produto)
        REFERENCES produtos(id_produto)
);