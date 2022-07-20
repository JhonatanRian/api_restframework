from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Solicitation(models.Model):
    product = models.ForeignKey(Product, verbose_name="produto",on_delete=models.CASCADE, related_name="solicitations")
    client = models.ForeignKey(User, verbose_name="cliente", on_delete=models.CASCADE, related_name="solicitations")
    quantity = models.IntegerField(verbose_name="quantidade que foi pedida")
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="valor do pedido", null=True)
    delivery_place = models.TextField(verbose_name="Local de entrega", blank=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-quantity"]

    def __str__(self) -> str:
        return f"cliente:{self.client} product:{self.product} quantidade:{self.quantity}"


class Finances(models.Model):
    invoice_all = models.DecimalField(verbose_name="Fatura total", max_digits=9, decimal_places=2, default=0)
    profit = models.DecimalField(verbose_name="Lucro", max_digits=9, decimal_places=2, default=0)