from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .views import KirjaViewSet, AsiakasViewSet, LainausViewSet
from .models import Kirja, Asiakas, Lainaus

class ViewSetTest(TestCase):
    def test_kirja_view_set(self):
        '''Kirjan lisäys ja haku onnistuu'''
        request = APIRequestFactory().get("")
        kirja_set = KirjaViewSet.as_view({'get': 'retrieve'})    
        kirja = Kirja.objects.create(otsikko="Mielenterveys elämäntaitona", kirjoittaja="Suomen Mielenterveys ry", isbn="9789527022740", saatavissa=True)
        
        response = kirja_set(request, pk=kirja.pk)
        # testataan että tulee oikea statuskoodi
        self.assertEqual(response.status_code, 200)
        # testataan että objekti luottiin juuri sellaiseksi kuin oli tarkoitus
        self.assertEqual(response.data, {'id': 1, 'otsikko': "Mielenterveys elämäntaitona", 'kirjoittaja': "Suomen Mielenterveys ry", 'isbn': "9789527022740", 'saatavissa': True})

    def test_asiakas_view_set(self):
        '''Asiakkaan lisäys ja haku onnistuu'''
        request = APIRequestFactory().get("")
        asiakas_set = AsiakasViewSet.as_view({'get': 'retrieve'})
        asiakas = Asiakas.objects.create(nimi="Pekka", puhelin="123456789", email="pekka@kuparinen.fi")

        response = asiakas_set(request, pk=asiakas.pk)
        # testataan että tulee oikea statuskoodi
        self.assertEqual(response.status_code, 200)
        # testataan että objekti luottiin juuri sellaiseksi kuin oli tarkoitus
        self.assertEqual(response.data, {'id': 1, 'nimi': "Pekka", 'puhelin': "123456789", 'email': "pekka@kuparinen.fi"})

    def test_lainaus_view_set(self):
        '''Lainauksen lisäys ja haku onnistuu'''
        request = APIRequestFactory().get("")

        # Kirjanlisääminen ja asiakkaanlisääminen vaativat tässä ensiksi luotavan lainauksen
        kirja_set = KirjaViewSet.as_view({'get': 'retrieve'})      
        kirja = Kirja.objects.create(otsikko="Oma Suomi 2", kirjoittaja="Finn Lectura", isbn="9789511470946", saatavissa=True)

        asiakas_set = AsiakasViewSet.as_view({'get': 'retrieve'})  
        asiakas = Asiakas.objects.create(nimi="Pekka", puhelin="123456789", email="pekka@kuparinen.fi")

        lainaus_set = LainausViewSet.as_view({'get': 'retrieve'})   
        lainaus = Lainaus.objects.create(kirja=kirja, asiakas=asiakas, lainattu_aika=datetime(2025, 6, 9, 12, 0, 0))
        response = lainaus_set(request, pk=lainaus.pk)
        # testataan että tulee oikea statuskoodi
        self.assertEqual(response.status_code, 200)
        # testataan että objekti luottiin juuri sellaiseksi kuin oli tarkoitus
        self.assertEqual(response.data, {'id': 1, 'kirja': 1, 'asiakas': 1, 'lainattu_aika': '2025-06-09T12:00:00Z', 'palautettu_aika': None})
        
