from django.shortcuts import render
from django.http import HttpResponse
from stock.forms import BookForm

def index(request):
    return HttpResponse("Hello, world. You're at index.")

def form(request):
    if request.method == "GET":
        form = BookForm()
        context = {
            'form': form
        }
        return render(request, "form.html", context=context)
    else: 
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            form = BookForm()
            context = {
                'form': form
            }
            return render(request, "form.html", context=context)

        