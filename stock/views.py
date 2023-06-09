from django.views.generic import ListView, DetailView
from .models import Book, Author, Category


class BookListView(ListView):
    model = Book
    template_name = 'stock/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book
    template_name = 'stock/book_detail.html'
    context_object_name = 'book'


class AuthorListView(ListView):
    model = Author
    template_name = 'stock/author_list.html'
    context_object_name = 'author_list'


class CategoryListView(ListView):
    model = Category
    template_name = 'stock/category_list.html'
    context_object_name = 'category_list'
