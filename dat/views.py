from django.shortcuts import render
from mcat.models import Resource # accidentally put down the dat resources in the MCAT resources tab in the admin webpage
from django.http import HttpRequest

# Create your views here.
def index(request):
    resources = Resource.objects.all()
    return render(request, 'dat.html', {'resources': resources})