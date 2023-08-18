from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
