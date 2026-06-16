from django.test import TestCase

import json

from rest_framework.test import APITestCase

from estoque.models import Produto


# Create your tests here.

class TestListamgemdeProdutos(APITestCase):
    def test_listagem_vazio(self):
        reponse = self.client.get("/api/produtos/")
        data = json.loads(reponse.content)
        self.assertEqual(data, [])

    def test_listagem_com_produto(self):
        dados = {
            "nome": "TV",
            "modelo": "Samsung Smart TV 55 UHD 4K U8600F 2025",
            "quantidade_estoque": 10,
            "valor": 3000
            }
        self.client.post("/api/produtos/",dados)
        reponse = self.client.get("/api/produtos/")
        data = json.loads(reponse.content)
        self.assertEqual(data, [{
        "id": 1,
        "nome": "TV",
        "modelo": "Samsung Smart TV 55 UHD 4K U8600F 2025",
        "quantidade_estoque": 10,
        "quantidade_vendido": 0,
        "notas_usuario": "0.00",
        "valor": "3000.00"
        }])

class TestCriandoProduto(APITestCase):
    def test_criacao_de_produto(self):
        dados = {
            "nome": "TV",
            "modelo": "Samsung Smart TV 55 UHD 4K U8600F 2025",
            "quantidade_estoque": 10,
            "valor": 3000
            }
        self.client.post("/api/produtos/",dados)
        reponse = self.client.get("/api/produto/1/")
        data = json.loads(reponse.content)
        self.assertDictEqual(data, {
        "id": 1,
        "nome": "TV",
        "modelo": "Samsung Smart TV 55 UHD 4K U8600F 2025",
        "quantidade_estoque": 10,
        "quantidade_vendido": 0,
        "notas_usuario": "0.00",
        "valor": "3000.00"
        })
    def test_retorna_erro_400(self):
        dados = {
            "nome": "TV",
            "modelo": "Samsung Smart TV 55 UHD 4K U8600F 2025",
            "quantidade_estoque": 10,
            "valor": -3000
            }
        reponse = self.client.post("/api/produtos/",dados, format="json")
        self.assertEqual(reponse.status_code, 400)

class TestEditarProduto(APITestCase):
    def test_edita_o_valor_do_produto(self):
        dados = {
            "nome": "TV",
            "modelo": "Samsung Smart TV 55 UHD 4K U8600F 2025",
            "quantidade_estoque": 10,
            "valor": 3000
            }
        reponse = self.client.post("/api/produtos/",dados, format="json")
        dados_editados = {"valor":"2999.00"}
        reponse_patch = self.client.patch("/api/produto/1/", dados_editados)
        reponse_get = self.client.get("/api/produto/1/", format="json")
        data = json.loads(reponse_get.content)
        self.assertEqual(data["valor"],dados_editados["valor"])

class TestDeletaProduto(APITestCase):
    def test_deleta_produto(self):
        dados = {
            "nome": "TV",
            "modelo": "Samsung Smart TV 55 UHD 4K U8600F 2025",
            "quantidade_estoque": 10,
            "valor": 3000
            }
        reponse = self.client.post("/api/produtos/",dados, format="json")
        reponse_delete = self.client.delete("/api/produto/1/", format="json")
        data = Produto.objects.get(id=1)
        self.assertEqual(data.disponivel_produto , False)


