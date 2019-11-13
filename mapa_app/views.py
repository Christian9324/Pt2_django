from __future__ import unicode_literals

from .serializers import puntoMapaSerializer
from rest_framework.generics import (CreateAPIView)
from rest_framework.views import APIView
from mapa_app.models import puntoMapa
from django.shortcuts import render

class puntoMapaCreateAPIView(CreateAPIView):
	serializer_class = puntoMapaSerializer
	queryset = puntoMapa.objects.all()

def lista_ubicaciones(request):
	posts = puntoMapa.objects.all()
	return render(request, 'mapa_app/lista_ubicaciones.html', {'posts' : posts} )