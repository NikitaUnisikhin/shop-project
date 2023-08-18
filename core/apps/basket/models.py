from django.db import models
from core.apps.catalog.models import Product


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    email = models.EmailField()


class Basket(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name
