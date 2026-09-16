-- ========================================
-- 02 - INSERIR DADOS
-- ========================================

INSERT INTO clientes VALUES
(1, 'João Silva', 'joao@email.com', '11999999999', '111.111.111-11'),
(2, 'Maria Santos', 'maria@email.com', '11988888888', '222.222.222-22'),
(3, 'Pedro Oliveira', 'pedro@email.com', '11977777777', '333.333.333-33'),
(4, 'Ana Souza', 'ana@email.com', '11966666666', '444.444.444-44'),
(5, 'Lucas Costa', 'lucas@email.com', '11955555555', '555.555.555-55');

INSERT INTO categorias VALUES
(1, 'Camisetas', 'Camisetas masculinas e femininas'),
(2, 'Calças', 'Calças jeans e casuais'),
(3, 'Vestidos', 'Vestidos para diferentes ocasiões'),
(4, 'Jaquetas', 'Jaquetas para diferentes estilos'),
(5, 'Acessórios', 'Acessórios para complementar o visual');

INSERT INTO produtos VALUES
(1, 'Camiseta Básica', 'Camiseta confortável de algodão', 49.90, 'M', 'Branca', 50, 1),
(2, 'Camiseta Estampada', 'Camiseta com estampa moderna', 59.90, 'G', 'Azul', 35, 1),
(3, 'Calça Jeans', 'Calça jeans de estilo casual', 129.90, 'M', 'Azul', 25, 2),
(4, 'Calça Jogger', 'Calça confortável para o dia a dia', 99.90, 'G', 'Preta', 30, 2),
(5, 'Vestido Casual', 'Vestido leve e confortável', 149.90, 'M', 'Preto', 20, 3),
(6, 'Jaqueta Jeans', 'Jaqueta jeans moderna', 179.90, 'G', 'Azul', 15, 4),
(7, 'Bolsa Casual', 'Bolsa para uso diário', 89.90, 'Único', 'Marrom', 40, 5);

INSERT INTO pedido VALUES
(1, '2026-09-10', 'Pendente', 109.80, 1),
(2, '2026-09-11', 'Pago', 129.90, 2),
(3, '2026-09-12', 'Enviado', 149.90, 3),
(4, '2026-09-13', 'Entregue', 179.90, 4),
(5, '2026-09-14', 'Pago', 89.90, 5);

INSERT INTO itens_pedidos VALUES
(1, 1, 49.90, 1, 1),
(2, 1, 59.90, 1, 2),
(3, 1, 129.90, 2, 3),
(4, 1, 149.90, 3, 5),
(5, 1, 179.90, 4, 6),
(6, 1, 89.90, 5, 7);