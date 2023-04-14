from django.db import models
from django.utils.html import format_html

# Create your models here.
class Book(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    edition = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    year = models.IntegerField()
    num_pages = models.IntegerField()
    language = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='media/', blank=True)