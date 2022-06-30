from multiprocessing import context
from tkinter import SE
from django.shortcuts import render
from .models import Barbers

def barbers(request):
    data = Barbers.objects.all()
    context = {
        'data': data
    }
    return render(request, 'main/index.html', context)
