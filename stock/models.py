from django.db import models
from django.utils.html import format_html
from django.conf import settings

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    resume = models.TextField(blank=True)
    photo = models.ImageField(upload_to='media/author', blank=True)

    def __str__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name 
class Book(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ManyToManyField(Author, blank=True)  # n-n relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category", blank=True)  # 1-n relationship
    publisher = models.CharField(max_length=255, blank=True)
    edition = models.IntegerField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    quantity = models.IntegerField(blank=True)
    year = models.IntegerField(blank=True)
    num_pages = models.IntegerField(blank=True)
    language = models.CharField(max_length=50, blank=True)
    cover = models.ImageField(upload_to='media/book', blank=True)

    def __str__(self): 
        return self.title
