from django.db import models
from django.apps import apps
from produtos.models import Produto

class ItemVenda(models.Model):
    venda_id = models.PositiveIntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)



    def get_venda(self):
        Venda = apps.get_model('vendas', 'Venda')
        try:
            return Venda.objects.get(id=self.venda_id)
        except Venda.DoesNotExist:
            return None

    def __str__(self):
        return f"Item de Venda #{self.id} na venda #{self.venda_id}"
