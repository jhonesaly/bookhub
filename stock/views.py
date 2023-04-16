from django.shortcuts import render
from django.http import HttpResponse
from stock.forms import BookForm

def index(request):
    return HttpResponse("Hello, world. You're at index.")

def form(request):
    return render(request, "form.html")