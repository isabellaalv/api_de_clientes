from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    ultima_compra = models.DateField()
    endereco = models.CharField(max_length=100)
    foto = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
