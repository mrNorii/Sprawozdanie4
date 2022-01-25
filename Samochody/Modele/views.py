from django.shortcuts import render
from django.http import HttpResponse
from .models import Modele
from rest_framework import viewsets
from .serializer import ModeleSerializer

# Create your views here.

def index(request):
    ask = Modele.objects.all()
    return HttpResponse(ask)

class ModeleViewSet(viewsets.ModelViewSet):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer

