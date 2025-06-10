from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"kirjat", views.KirjaViewSet, basename="otsikko")  
router.register(r"asiakkaat", views.AsiakasViewSet, basename="nimi")   
router.register(r"lainaukset", views.LainausViewSet, basename="id")   

urlpatterns = [
    path("", include((router.urls, "app"))),        
]