from django.db import models

# Create your models here.

class Modele(models.Model):
    Marka = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Rok = models.IntegerField(max_length=7)
    Przebieg = models.IntegerField(max_length=7)
    Pojemnosc_Silnika = models.IntegerField(max_length=4)
    Rodzaj_Paliwa = models.CharField(max_length=20)
    Cena = models.DecimalField(max_digits=12, decimal_places=2)
    Opis = models.TextField(blank=True)