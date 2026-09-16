-- ========================================
-- 03 - ATUALIZAR DADOS
-- ========================================

UPDATE clientes
SET telefone = '11911112222'
WHERE id_cliente = 1;

UPDATE produtos
SET preco = 54.90
WHERE id_produto = 1;

UPDATE produtos
SET estoque = 45
WHERE id_produto = 1;

UPDATE pedido
SET status = 'Enviado'
WHERE id_pedido = 1;