from django.contrib.auth.models import User
from django.db import models
from core.apps.catalog.models import Product


class Basket(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name
