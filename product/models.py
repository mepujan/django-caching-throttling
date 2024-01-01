from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=999999, decimal_places=2)
    descriptions = models.TextField()

    def __str__(self) -> str:
        return self.name
