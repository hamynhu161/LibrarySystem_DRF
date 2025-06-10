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
    
    # luo objekti ja kutsu save() funktiota
    def create(self, validated_data):
        lainaus = Lainaus(**validated_data)     #puruta data, jotta Django voi ymmärtää ja luoda Lainaus-objektin ennen mukautetun logiikkasi suorittamista models:ssa
        lainaus.save()  
        return lainaus

    # Päivitä jokainen ominaisuus manuaalisesti
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save() 
        return instance