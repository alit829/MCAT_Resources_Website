from django.shortcuts import render
from django.http import HttpRequest
from .models import Postlink


# Create your views here.
def index(request):
    links = Postlink.objects.all()
    return render(request, 'home.html', {'links': links})