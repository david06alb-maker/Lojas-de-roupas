-- ========================================
-- 05 - CONSULTAS
-- ========================================

SELECT * FROM clientes;

SELECT * FROM categorias;

SELECT * FROM produtos;

SELECT * FROM pedido;

SELECT * FROM itens_pedidos;

SELECT
    p.id_produto,
    p.nome AS produto,
    p.descricao,
    p.preco,
    p.tamanho,
    p.cor,
    p.estoque,
    c.nome AS categoria
FROM produtos p
JOIN categorias c
    ON p.id_categoria = c.id_categoria
ORDER BY p.id_produto;

SELECT
    pe.id_pedido,
    c.nome AS cliente,
    pe.data_pedido,
    pe.status,
    pe.valor_total
FROM pedido pe
JOIN clientes c
    ON pe.id_cliente = c.id_cliente
ORDER BY pe.id_pedido;

SELECT
    i.id_item,
    i.id_pedido,
    p.nome AS produto,
    i.quantidade,
    i.preco_unitario,
    (i.quantidade * i.preco_unitario) AS subtotal
FROM itens_pedidos i
JOIN produtos p
    ON i.id_produto = p.id_produto
ORDER BY i.id_item;

SELECT
    c.nome AS cliente,
    pe.id_pedido,
    pe.data_pedido,
    pe.status,
    p.nome AS produto,
    i.quantidade,
    i.preco_unitario,
    (i.quantidade * i.preco_unitario) AS subtotal
FROM clientes c
JOIN pedido pe
    ON c.id_cliente = pe.id_cliente
JOIN itens_pedidos i
    ON pe.id_pedido = i.id_pedido
JOIN produtos p
    ON i.id_produto = p.id_produto
ORDER BY pe.id_pedido;

SELECT
    c.nome AS categoria,
    COUNT(p.id_produto) AS quantidade_produtos
FROM categorias c
LEFT JOIN produtos p
    ON c.id_categoria = p.id_categoria
GROUP BY c.id_categoria, c.nome
ORDER BY c.id_categoria;