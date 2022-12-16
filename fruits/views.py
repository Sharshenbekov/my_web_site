from django.shortcuts import render, redirect
from .models import Fruits
from .forms import FruitForm
from django.views.generic import DetailView, UpdateView


def index(request):
    fruits = Fruits.objects.all()
    return render(request, 'fruits.html', {'fruits': fruits})


def create(request):
    error = ''
    form = FruitForm(request.POST)
    data = {
        'form': form,
        'error': error
    }
    if request.method == 'POST':
        print(form.data)
        if form.is_valid():
            form.save()
            print('OK')
        else:
            'Error'
        return redirect('/fruits')

    return render(request, 'create.html', data)

#


def add_fruit(request):
    if request.method == 'GET':
        return render(request, 'add_fruit.html')

    if request.method == 'POST':
        print(request.POST)
        return redirect('index')
