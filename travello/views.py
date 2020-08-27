from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.


def index(request):
    des1 = Destination()
    des1.name = "Mumbai"
    des1.desc = "City that never Sleeps"
    des1.price = 300
    
    return render(request, 'index.html', {'des1':des1} )