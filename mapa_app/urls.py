from django.urls import path
from django.conf.urls import url, include
from mapa_app import views

urlpatterns = [
    url(r'^create/$', views.puntoMapaCreateAPIView.as_view()),
    path('', views.lista_ubicaciones , name='lista_ubicaciones'),
]
