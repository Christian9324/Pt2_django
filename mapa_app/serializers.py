from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mapa_app.models import puntoMapa


class puntoMapaSerializer(ModelSerializer):
	class Meta:
		model = puntoMapa
		fields = [
			'title',
			'latitud',
			'longitud',
			]