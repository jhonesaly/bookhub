from django.db import models
from django.utils.html import format_html
from django.conf import settings

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    resume = models.TextField()
    photo = models.ImageField(upload_to='media/author', blank=True)

    def __str__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name 
class Book(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ManyToManyField(Author, blank=True) #many-to-many relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category", blank=True) #one-to-many relationship
    publisher = models.CharField(max_length=255)
    edition = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    year = models.IntegerField()
    num_pages = models.IntegerField()
    language = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='media/book', blank=True)

    def __str__(self): 
        return self.title