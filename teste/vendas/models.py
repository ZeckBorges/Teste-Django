from django.db import models
from vendedor.models import Vendedor
from produtos.models import Produto

class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, default=1)
    data_venda = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Venda #{self.id}"
