from rest_framework import serializers
from .models import Kirja, Asiakas, Lainaus

class KirjatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kirja
        fields = ['id', 'otsikko', 'kirjoittaja', 'isbn', 'saatavissa']

class AsiakasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiakas
        fields = ['id', 'nimi', 'puhelin', 'email']

class LainausSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lainaus
        fields = ['id', 'kirja', 'asiakas', 'lainattu_aika', 'palautettu_aika']