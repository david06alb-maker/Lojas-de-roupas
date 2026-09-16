from banco import conectar


def cadastrar_cliente():
    print("\n=== CADASTRAR CLIENTE ===")

    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    conexao = conectar()

    if conexao is None:
        print("Não foi possível conectar ao PostgreSQL.")
        return

    cursor = None

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT COALESCE(MAX(id_cliente), 0) + 1
            FROM public.clientes
        """)

        id_cliente = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO public.clientes
            (id_cliente, nome, email, telefone, cpf)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_cliente, nome, email, telefone, cpf))

        conexao.commit()

        print("\nCliente cadastrado com sucesso!")

    except Exception as erro:
        conexao.rollback()
        print("\nErro ao cadastrar cliente:")
        print(erro)

    finally:
        if cursor is not None:
            cursor.close()

        conexao.close()


def listar_clientes():
    print("\n>>> A FUNÇÃO LISTAR_CLIENTES FOI CHAMADA <<<")

    conexao = conectar()

    if conexao is None:
        print("ERRO: não foi possível conectar ao PostgreSQL.")
        return

    print(">>> CONEXÃO COM POSTGRESQL OK <<<")

    cursor = None

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id_cliente, nome, email, telefone, cpf
            FROM public.clientes
            ORDER BY id_cliente;
        """)

        clientes = cursor.fetchall()

        print("\n========== CLIENTES ==========")
        print("Quantidade encontrada:", len(clientes))

        for cliente in clientes:
            print(
                f"ID: {cliente[0]} | "
                f"Nome: {cliente[1]} | "
                f"Email: {cliente[2]} | "
                f"Telefone: {cliente[3]} | "
                f"CPF: {cliente[4]}"
            )

    except Exception as erro:
        print("\nERRO AO LISTAR CLIENTES:")
        print(erro)

    finally:
        if cursor is not None:
            cursor.close()

        conexao.close()