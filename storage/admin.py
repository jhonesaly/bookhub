from django.contrib import admin
from django.utils.html import format_html
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher', 'price', 'quantity', 'cover_image')
    search_fields = ('id', 'title', 'author', 'publisher')
    list_filter = ('publisher', 'author')
    ordering = ('title',)

    def cover_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.cover.url) if obj.cover else '')

    cover_image.short_description = 'Cover Image'

admin.site.register(Book, BookAdmin)
