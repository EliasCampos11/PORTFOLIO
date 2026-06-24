from django.db import models

# Create your models here.
class Produto(models.Model):

    vendedor = models.ForeignKey('auth.User', related_name="produtos", on_delete=models.CASCADE )
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField()
    quantidade_vendido = models.IntegerField(default=0.0)
    notas_usuario = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel_produto = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nome} <{self.modelo}>"
