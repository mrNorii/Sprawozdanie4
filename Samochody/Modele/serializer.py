from .models import Modele
from rest_framework import serializers

class ModeleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modele
        fields = ['id','Marka', 'Model', 'Rok', 'Przebieg', 'Pojemnosc_Silnika', 'Rodzaj_Paliwa', 'Cena', 'Opis', 'Zdjecie']