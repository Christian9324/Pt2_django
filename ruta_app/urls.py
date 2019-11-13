from django.urls import path
from django.conf.urls import url, include
from ruta_app import views

urlpatterns = [
    url(r'^info/$', views.rutas_info),
    url(r'^create/$', views.ruta_set),
]