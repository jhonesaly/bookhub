from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookListView, name="list"),
    path('books/<int:pk>/', views.BookDetailView, name="detail")
]