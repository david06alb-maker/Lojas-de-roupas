# Roteiro dos Slides — 30 minutos

## Slide 1 — Capa
**Loja de Roupas — Sistema de Gerenciamento**

Nome dos integrantes, turma e disciplina.

## Slide 2 — Ideia do projeto
Criamos um sistema simples para organizar clientes, produtos, categorias e pedidos de uma loja de roupas.

## Slide 3 — Por que escolhemos o tema?
- Tema fácil de compreender.
- Permite trabalhar com vendas e estoque.
- Possui relacionamentos claros entre tabelas.
- Permite criar funcionalidades no Python.

## Slide 4 — Problema
Uma loja precisa organizar:
- clientes;
- produtos;
- categorias;
- estoque;
- pedidos.

## Slide 5 — Solução
Sistema que centraliza essas informações em um banco de dados e oferece operações básicas por meio de Python.

## Slide 6 — DER
Mostrar o DER criado no DrawDB e explicar as cinco tabelas.

## Slide 7 — Tabela cliente
Explicar PK, dados do cliente e relacionamento com pedido.

## Slide 8 — Tabela categoria
Explicar a classificação dos produtos.

## Slide 9 — Tabela produto
Explicar preço, tamanho, estoque e FK da categoria.

## Slide 10 — Tabela pedido
Explicar cliente, data e status.

## Slide 11 — Tabela item_pedido
Explicar por que ela existe: um pedido pode possuir produtos e cada item registra quantidade e preço.

## Slide 12 — CREATE TABLE
Mostrar partes do script de criação.

## Slide 13 — INSERT
Mostrar a população das tabelas.

## Slide 14 — UPDATE
Demonstrar atualização de preço/estoque usando WHERE.

## Slide 15 — DELETE
Demonstrar exclusão de um registro específico usando WHERE.

## Slide 16 — Consultas
Mostrar consultas que respondem perguntas como:
- Quais produtos têm estoque baixo?
- Quais produtos custam mais de R$ 100?
- Quanto vale cada pedido?
- Quais produtos são mais vendidos?

## Slide 17 — Python
Explicar a divisão em módulos:
- main.py
- banco.py
- clientes.py
- produtos.py
- pedidos.py

## Slide 18 — Funções
Mostrar que cada operação foi organizada em uma função.

## Slide 19 — Listas e dicionários
Mostrar exemplos usados no arquivo dados.py e explicar a diferença:
- lista: coleção ordenada;
- dicionário: dados organizados em chave e valor.

## Slide 20 — Estruturas de decisão
Mostrar `if`, `elif` e `else` usados no menu.

## Slide 21 — Estruturas de repetição
Mostrar o `while` responsável por manter o menu funcionando até o usuário escolher sair.

## Slide 22 — SQLite
Explicar que a aplicação Python usa SQLite localmente, conforme solicitado no enunciado.

## Slide 23 — Demonstração
Executar o programa e demonstrar:
1. listar produtos;
2. cadastrar cliente;
3. atualizar estoque;
4. criar pedido;
5. listar pedidos.

## Slide 24 — Organização do GitHub
Mostrar as pastas e arquivos do projeto.

## Slide 25 — Fontes
Apresentar as fontes consultadas para aprender PostgreSQL, Python, SQLite e modelagem de banco.

## Slide 26 — Conclusão
Explicar o que a equipe aprendeu e como Banco de Dados e Python foram integrados.

## Divisão sugerida da apresentação

### Integrante 1
- Slides 1–12
- DER e PostgreSQL

### Integrante 2
- Slides 13–26
- SQL, Python, SQLite e demonstração

A divisão pode ser alterada para que os dois integrantes demonstrem partes do código que realmente fizeram.
