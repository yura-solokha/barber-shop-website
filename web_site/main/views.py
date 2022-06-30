from django.shortcuts import render
from barbers.models import Barbers
from barbers.views import barbers

def index(request):
    data = Barbers.objects.all()
    context = {
        'data': data
    }
    return render(request, 'main/index.html')

