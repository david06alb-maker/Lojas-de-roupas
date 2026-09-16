# DER — Loja de Roupas

## Entidades

### CLIENTE
- id_cliente — PK
- nome
- email
- telefone
- cidade

### CATEGORIA
- id_categoria — PK
- nome
- descricao

### PRODUTO
- id_produto — PK
- nome
- tamanho
- preco
- estoque
- id_categoria — FK

### PEDIDO
- id_pedido — PK
- data_pedido
- status
- id_cliente — FK

### ITEM_PEDIDO
- id_item — PK
- quantidade
- preco_unitario
- id_pedido — FK
- id_produto — FK

## Relacionamentos

- Um **cliente** pode realizar vários **pedidos**.
- Um **pedido** pertence a um **cliente**.
- Uma **categoria** pode possuir vários **produtos**.
- Um **produto** pertence a uma **categoria**.
- Um **pedido** possui vários **itens de pedido**.
- Um **item de pedido** pertence a um **pedido**.
- Um **produto** pode aparecer em vários **itens de pedido**.

## Modelo resumido

```text
CLIENTE 1 ───────── N PEDIDO
                         |
                         | 1
                         |
                         N
                   ITEM_PEDIDO
                         N
                         |
                         | 1
                         |
                      PRODUTO
                         N
                         |
                         | 1
                         |
                    CATEGORIA
```

## Como montar no DrawDB

Crie as cinco tabelas:
`cliente`, `categoria`, `produto`, `pedido`, `item_pedido`.

Depois marque:
- PK nas chaves primárias;
- FK nas chaves estrangeiras;
- relacionamento `cliente.id_cliente -> pedido.id_cliente`;
- relacionamento `categoria.id_categoria -> produto.id_categoria`;
- relacionamento `pedido.id_pedido -> item_pedido.id_pedido`;
- relacionamento `produto.id_produto -> item_pedido.id_produto`.

Exporte o diagrama como imagem e coloque o arquivo exportado nesta pasta com o nome `DER.png`.
