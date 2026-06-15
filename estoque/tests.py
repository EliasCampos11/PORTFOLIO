import json
from urllib import response
from rest_framework.test import APITestCase

# Create your tests here.
class TestListagemEstoque(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/produtos/")
        data = json.loads(response.content)
        self.assertEqual(data, [])
        
    def test_listagem_com_produtos(self):
        produto_data = {"nome": "Mouse","modelo":"LG", "valor":100.00, "quantidade_estoque":10} 
        self.client.post("/api/produtos/", produto_data)
        response = self.client.get("/api/produtos/")
        data = json.loads(response.content)
        self.assertEqual(data, [{
                        "id": 1,
                        "nome": "Mouse",
                        "modelo": "LG",
                        "quantidade_estoque": 10,
                        "valor": "100.00",
                        "notas_usuario": "0.00",
                        "produto_disponivel": True,
                        "quantidade_vendido": 0
}])

class TestCriacaoProduto(APITestCase):
    def test_criar_produto(self):
        produto_data = {"nome": "Mouse","modelo":"LG", "valor":100.00, "quantidade_estoque":10} 
        self.client.post("/api/produtos/", produto_data)
        response = self.client.get("/api/produtos/1/")
        data = json.loads(response.content) 
        self.assertEqual(data, {
                        "id": 1,
                        "nome": "Mouse",
                        "modelo": "LG",
                        "quantidade_estoque": 10,
                        "valor": "100.00",
                        "notas_usuario": "0.00",
                        "produto_disponivel": True,
                        "quantidade_vendido": 0})
    
    def test_criar_produto_com_dados_invalidos(self):
        produto_data = {"nome": "Mouse", "modelo":"LG", "valor":-100.00, "quantidade_estoque":10}        
        response_post = self.client.post("/api/produtos/", produto_data, format='json') 
        # response_get = self.client.get("/api/produtos/1/", format='json') 
        data_post= json.loads(response_post.content)
        self.assertEqual(data_post, {
                "valor": [
                            "O valor não pode ser negativo."
                        ]
})
        
class TestEditarProduto(APITestCase):
    def test_editar_produto(self): 
        produto_data = {"nome": "Mouse", "modelo":"LG", "valor":100.00, "quantidade_estoque":10} 
        response_post = self.client.post("/api/produtos/", produto_data, format='json') 
        edited_data = {"nome": "Mouse2"}
        
        response_patch = self.client.patch("/api/produtos/1/", edited_data, format='json')
        response_get = self.client.get("/api/produtos/1/", format="json")
        asserted_data = json.loads(response_get.content)
        self.assertEqual(response_patch.status_code, 200)
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(asserted_data["nome"], edited_data["nome"])
    
    def test_editar_produto_invalido(self):
        produto_data = {"nome": "Mouse", "modelo":"LG", "valor":100.00, "quantidade_estoque":10}
        edited_data = {"valor": -100.00}
        response_post = self.client.post("/api/produtos/", produto_data, format="json")
        response_patch = self.client.patch("/api/produtos/1/", edited_data, format="json")
        response_data = json.loads(response_patch.content)
        self.assertEqual(response_data["valor"], ["O valor não pode ser negativo."])
        
class TestDeletarProduto(APITestCase):
    def test_deletar_produto(self):
        produto_data = {"nome": "Mouse", "modelo":"LG", "valor":100.00, "quantidade_estoque":10}
        response_post = self.client.post("/api/produtos/", produto_data, format="json")
        
        response_delete = self.client.delete("/api/produtos/1/", format="json")
        self.assertEqual(response_delete.status_code, 204)
        
        response_get = self.client.get("/api/produtos/1/", format="json")
        response_data = json.loads(response_get.content)
        self.assertEqual(response_data["produto_disponivel"], False)
    
    def test_deletar_produto_inexistente(self):
        response_delete = self.client.delete("/api/produtos/1/", format="json")
        self.assertEqual(response_delete.status_code, 404)
        
        
