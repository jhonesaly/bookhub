from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher', 'price', 'quantity')
    search_fields = ('id', 'title', 'author', 'publisher')
    list_filter = ('publisher', 'author')
    ordering = ('title',)

admin.site.register(Book, BookAdmin)