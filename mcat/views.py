from django.shortcuts import render
from django.http import HttpRequest
from dat.models import Resource # accidentally put down the mcat resources in the DAT resources tab in the admin webpage

# Create your views here.
def index(request):
    resources = Resource.objects.all()
    return render(request, 'mcat.html', resources)