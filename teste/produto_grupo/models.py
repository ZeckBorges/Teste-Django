from django.db import models

class GrupoProduto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    # Outros campos relevantes

    def __str__(self):
        return self.nome
