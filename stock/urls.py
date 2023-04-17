from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name="list"),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name="detail")
]