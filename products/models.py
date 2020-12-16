from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        self.title