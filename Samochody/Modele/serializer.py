from .models import Modele
from rest_framework import serializers

class ModeleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modele
        fields = ['Id', 'Marka', 'Model', 'Rok', 'Przebieg', 'Pojemnosc_Silnika', 'Rodaj_Paliwa', 'Cena', 'Opis']