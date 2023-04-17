from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'book'

class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'

