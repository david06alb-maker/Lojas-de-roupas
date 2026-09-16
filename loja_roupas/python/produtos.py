from banco import conectar


def cadastrar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    tamanho = input("Tamanho: ")
    cor = input("Cor: ")
    estoque = int(input("Estoque: "))
    id_categoria = int(input("ID da categoria: "))

    conexao = conectar()

    if conexao is None:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT COALESCE(MAX(id_produto), 0) + 1
            FROM produtos
            """
        )

        id_produto = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO produtos
            (
                id_produto,
                nome,
                descricao,
                preco,
                tamanho,
                cor,
                estoque,
                id_categoria
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                id_produto,
                nome,
                descricao,
                preco,
                tamanho,
                cor,
                estoque,
                id_categoria
            )
        )

        conexao.commit()

        print("\nProduto cadastrado com sucesso!")

    except Exception as erro:
        conexao.rollback()
        print("\nErro ao cadastrar produto:")
        print(erro)

    finally:
        cursor.close()
        conexao.close()


def listar_produtos():
    conexao = conectar()

    if conexao is None:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                p.id_produto,
                p.nome,
                p.descricao,
                p.preco,
                p.tamanho,
                p.cor,
                p.estoque,
                c.nome
            FROM produtos p
            JOIN categorias c
                ON p.id_categoria = c.id_categoria
            ORDER BY p.id_produto
            """
        )

        produtos = cursor.fetchall()

        print("\n========== PRODUTOS ==========")

        if not produtos:
            print("Nenhum produto encontrado.")

        else:
            for produto in produtos:
                print(
                    f"ID: {produto[0]} | "
                    f"Nome: {produto[1]} | "
                    f"Preço: R$ {produto[3]:.2f} | "
                    f"Tamanho: {produto[4]} | "
                    f"Cor: {produto[5]} | "
                    f"Estoque: {produto[6]} | "
                    f"Categoria: {produto[7]}"
                )

    except Exception as erro:
        print("\nErro ao listar produtos:")
        print(erro)

    finally:
        cursor.close()
        conexao.close()


def atualizar_estoque():
    id_produto = int(input("ID do produto: "))
    novo_estoque = int(input("Novo estoque: "))

    conexao = conectar()

    if conexao is None:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE produtos
            SET estoque = %s
            WHERE id_produto = %s
            """,
            (novo_estoque, id_produto)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("\nEstoque atualizado com sucesso!")
        else:
            print("\nProduto não encontrado.")

    except Exception as erro:
        conexao.rollback()
        print("\nErro ao atualizar estoque:")
        print(erro)

    finally:
        cursor.close()
        conexao.close()


def excluir_produto():
    id_produto = int(input("ID do produto que deseja excluir: "))

    conexao = conectar()

    if conexao is None:
        return

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            DELETE FROM produtos
            WHERE id_produto = %s
            """,
            (id_produto,)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("\nProduto excluído com sucesso!")
        else:
            print("\nProduto não encontrado.")

    except Exception as erro:
        conexao.rollback()
        print("\nNão foi possível excluir o produto.")
        print(erro)

    finally:
        cursor.close()
        conexao.close()