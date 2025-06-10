from rest_framework import viewsets
from .models import Kirja, Asiakas, Lainaus
from .serializers import KirjatSerializer, AsiakasSerializer, LainausSerializer

'''Ao. metodi osaa tehdä kaikki crud toiminnot ja hakea kirjat:
    - kaikki kirjat: /api/kirjat
    - kirjan id:llä: /api/kirjat/id
    - kirjan otsikolla: /api/kirjat/?otsikko=joku_otsikko
'''
class KirjaViewSet(viewsets.ModelViewSet):
    serializer_class = KirjatSerializer
    def get_queryset(self):
        queryset = Kirja.objects.all()
        otsikko = self.request.query_params.get("otsikko")    
        if otsikko is not None:
            queryset = queryset.filter(otsikko=otsikko)
        return queryset    

'''Ao. metodi osaa tehdä kaikki crud toiminnot ja hakea asiakkaat:
    - kaikki asiakkaat: /api/asiakkaat
    - asiakkaan id:llä: /api/asiakkaat/id
    - asiakkaan nimellä: /api/asiakkaat/?nimi=joku_nimi 
'''
class AsiakasViewSet(viewsets.ModelViewSet):
    serializer_class = AsiakasSerializer
    def get_queryset(self):
        queryset = Asiakas.objects.all()
        nimi = self.request.query_params.get("nimi")    
        if nimi is not None:
            queryset = queryset.filter(nimi=nimi)
        return queryset    
    
'''Ao. metodi osaa tehdä kaikki crud toiminnot ja hakea lainaukset:
    - kaikki lainaukset: /api/lainaukset
    - lainauksen id:llä: /api/lainaukset/id
    - lainaukset kirjan id:llä: /api/lainaukset/?kirja=kirja_id
    - lainaukset asiakkaan id:llä: /api/lainaukset/?asiakas=asiakas_id 
'''
class LainausViewSet(viewsets.ModelViewSet):
    serializer_class = LainausSerializer
    def get_queryset(self):
        queryset = Lainaus.objects.all()
        kirja = self.request.query_params.get("kirja")    
        asiakas = self.request.query_params.get("asiakas")
        if kirja is not None:
            queryset = queryset.filter(kirja=kirja)
        if asiakas is not None:
            queryset = queryset.filter(asiakas = asiakas)
        return queryset    
