from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name="nome", max_length=255)
    price_in_sale = models.DecimalField(verbose_name="preço", max_digits=6, decimal_places=2)
    regular_price = models.DecimalField(verbose_name="preço normal/de fabrica", max_digits=6, decimal_places=2)
    description = models.TextField(verbose_name="descrição", blank=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["price_in_sale"]

    def __str__(self) -> str:
        return self.name