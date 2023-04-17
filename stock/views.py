from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'catalog.html'
    context_object_name = 'books'


