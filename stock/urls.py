from django.urls import path

from . import views

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path('<int:pk>', views.details, name="details")
]