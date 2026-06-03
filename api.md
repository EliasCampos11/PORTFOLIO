# LIMITAR A NOTA ATÉ 5 COM UM MINIMO DE 0
# QUANTIDADE VENDIDADE PADRÃO É ZERO


# API

Listar produtos: GET /produtos/
["Controle Remoto", "Cueca Box", "Cameras"]

Listar estoque: GET /estoque/
[
    {
        "produto": "quantidade"
        "Controle Remoto": 3,
        "Cueca Box": 5,
        "Cameras": 2,
    }
]

Exibir produto: GET /estoque/<id>
[
    {
        hidden"id": 1.
        "nome": "Nome_Produto",
        "modelo": "Modelo_Produto",
        "qnt_estoque": 3,
        "qnt_vendidos": 54,
        "valor": 3,99,
        "avaliação": "5/5 estrelas",
    }
    
]

Criar produto: POST /estoque/:
[
    {
        "nome": "Nome_Produto",
        "modelo": "Modelo_Produto",
        "qnt_estoque": 3,
        "valor": 3,99,
    }
]

Excluir produto: DELETE /estoque/<id>
...

Editar produto: PUT/PATCH /estoque/<id>
...