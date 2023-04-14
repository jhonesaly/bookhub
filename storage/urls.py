from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
]