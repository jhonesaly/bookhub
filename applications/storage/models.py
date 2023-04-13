from django.db import models

class Book(models.Model):
    id = models.CharField(max_length=100, primary_key=True) # id será o código de barras
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=200)
    edition = models.IntegerField()
    rating = models.FloatField()
    on_sale = models.BooleanField(default=False)
    stock_quantity = models.IntegerField()