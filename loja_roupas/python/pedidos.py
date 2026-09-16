from banco import conectar


def criar_pedido():
    id_cliente = int(input("ID do cliente: "))
    id_produto = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))

    conexao = conectar()

    if conexao is None:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT preco, estoque
            FROM produtos
            WHERE id_produto = %s
            """,
            (id_produto,)
        )

        produto = cursor.fetchone()

        if produto is None:
            print("\nProduto não encontrado.")
            return

        preco = produto[0]
        estoque = produto[1]

        if quantidade > estoque:
            print("\nEstoque insuficiente.")
            return

        valor_total = preco * quantidade

        cursor.execute(
            """
            SELECT COALESCE(MAX(id_pedido), 0) + 1
            FROM pedido
            """
        )

        id_pedido = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO pedido
            (
                id_pedido,
                data_pedido,
                status,
                valor_total,
                id_cliente
            )
            VALUES
            (
                %s,
                CURRENT_DATE,
                %s,
                %s,
                %s
            )
            """,
            (
                id_pedido,
                "Pendente",
                valor_total,
                id_cliente
            )
        )

        cursor.execute(
            """
            INSERT INTO itens_pedidos
            (
                id_item,
                quantidade,
                preco_unitario,
                id_pedido,
                id_produto
            )
            VALUES
            (
                (
                    SELECT COALESCE(MAX(id_item), 0) + 1
                    FROM itens_pedidos
                ),
                %s,
                %s,
                %s,
                %s
            )
            """,
            (
                quantidade,
                preco,
                id_pedido,
                id_produto
            )
        )

        cursor.execute(
            """
            UPDATE produtos
            SET estoque = estoque - %s
            WHERE id_produto = %s
            """,
            (quantidade, id_produto)
        )

        conexao.commit()

        print("\nPedido criado com sucesso!")
        print(f"Número do pedido: {id_pedido}")
        print(f"Valor total: R$ {valor_total:.2f}")

    except Exception as erro:
        conexao.rollback()
        print("\nErro ao criar pedido:")
        print(erro)

    finally:
        cursor.close()
        conexao.close()


def listar_pedidos():
    conexao = conectar()

    if conexao is None:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                p.id_pedido,
                c.nome,
                p.data_pedido,
                p.status,
                p.valor_total
            FROM pedido p
            JOIN clientes c
                ON p.id_cliente = c.id_cliente
            ORDER BY p.id_pedido
            """
        )

        pedidos = cursor.fetchall()

        print("\n========== PEDIDOS ==========")

        if not pedidos:
            print("Nenhum pedido encontrado.")

        else:
            for pedido in pedidos:
                print(
                    f"Pedido: {pedido[0]} | "
                    f"Cliente: {pedido[1]} | "
                    f"Data: {pedido[2]} | "
                    f"Status: {pedido[3]} | "
                    f"Total: R$ {pedido[4]:.2f}"
                )

    except Exception as erro:
        print("\nErro ao listar pedidos:")
        print(erro)

    finally:
        cursor.close()
        conexao.close()