from django.contrib import admin
from .models import Book, Author, Category

class BookAdmin(admin.ModelAdmin):

    list_display = ['title', 'price', 'view_name_category', 'get_authors']
    search_fields = ['title'] #search by name
    list_filter = ['year'] #filter by year

    @admin.display(ordering='view_name_category')
    def view_name_category(self, obj):
        return obj.category.name

    def get_authors(self, obj):
        for author in obj.author.all():
            return author.name
        #return [author.name for author in obj.author.all()]


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Category)
