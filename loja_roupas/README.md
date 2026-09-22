# Loja de Roupas — Atividade Integrada Banco de Dados com Python

## Objetivo do projeto 

O projeto tem como objetivo desenvolver um sistema para gerenciamento de uma loja de roupas chamada Lume, utilizando Python integrado a um banco de dados relacional. 

O sistema será responsável por armazenar e organizar informações relacionadas aos clientes, produtos, categorias, endereços, pedidos, itens dos pedidos, formas de pagamento e avaliações. 

A aplicação deverá permitir o gerenciamento das informações da loja e possibilitar que os clientes realizem pedidos de produtos disponíveis no catálogo. 

## Tecnologias
- PostgreSQL
- SQL
- Python 3
- SQLite
- DrawDB
- GitHub

## Estrutura

```text
loja_roupas/
├── banco/
│   ├── 01_criar_tabelas.sql
│   ├── 02_inserir_dados.sql
│   ├── 03_atualizar_dados.sql
│   ├── 04_excluir_dados.sql
│   └── 05_consultas.sql
├── python/
│   ├── main.py
│   ├── banco.py
│   ├── clientes.py
│   ├── produtos.py
│   ├── pedidos.py
│   └── dados.py
├── der/
│   └── DER.md
├── slides/
│   └── roteiro_apresentacao.md
└── README.md
```

## Banco PostgreSQL

Crie um banco chamado `loja_roupas` no pgAdmin4.

Depois execute os arquivos da pasta `banco` nesta ordem:

1. `01_criar_tabelas.sql`
2. `02_inserir_dados.sql`
3. `03_atualizar_dados.sql`
4. `04_excluir_dados.sql`
5. `05_consultas.sql`

Os arquivos 03 e 04 possuem exemplos de `UPDATE` e `DELETE`. Eles são seguros para a demonstração porque trabalham com registros específicos.

## Projeto Python

O programa usa SQLite localmente. Ao executar `python/main.py`, o arquivo `python/loja_roupas.db` será criado automaticamente.

No terminal:

```bash
cd python
python main.py
```

## Objetivo do sistema

O sistema permite:
- cadastrar clientes;
- listar clientes;
- cadastrar produtos;
- listar produtos;
- atualizar estoque;
- excluir produtos;
- criar pedidos;
- consultar pedidos;
- demonstrar funções, listas, dicionários, módulos, decisões e repetições.

## Observação sobre PostgreSQL e SQLite

O enunciado solicita PostgreSQL na construção do banco e SQLite com Python. Por isso, o projeto apresenta as duas tecnologias separadamente:
- PostgreSQL: banco principal demonstrado nos scripts SQL;
- SQLite: banco local utilizado pela aplicação Python.

Isso evita depender de bibliotecas externas para a execução do programa Python.
