import psycopg2


def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="SUA SENHA AQUI"
        )

        return conexao

    except Exception as erro:
        print("Erro ao conectar com o PostgreSQL:")
        print(erro)
        return None