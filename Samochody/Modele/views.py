from django.shortcuts import render
from django.http import HttpResponse
from .models import Modele

# Create your views here.

def index(request):
    ask = Modele.objects.all()
    return HttpResponse(ask)