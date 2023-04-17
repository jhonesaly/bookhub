from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListView, name="list"),
    path('<int:pk>', views.BookDetailView, name="detail")
]