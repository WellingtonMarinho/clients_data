from django.db import models


class ItensDoPedido(models.Model):
    produto = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.produto.name


class Pedido(models.Model):
    cliente = models.ForeignKey('People', on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(ItensDoPedido)

    def __str__(self):
        return self.cliente.name