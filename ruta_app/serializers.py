from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ruta_app.models import Rutas, Usuario


class RutasGetSerializer(ModelSerializer):
	class Meta:
		model = Rutas
		fields = [
			'estacionInicio',
			'estacionDestino',
			'rutaNodos',
			]

class RutasSetSerializer(ModelSerializer):
	class Meta:
		model = Rutas
		fields = [
			'estacionInicio',
			'estacionDestino',
			]


class UserGetSerializer(ModelSerializer):
	class Meta:
		model = Usuario
		fields = [
			'nickname',
			'password',
			]

class UserSetSerializer(ModelSerializer):
	class Meta:
		model = Usuario
		fields = [
			'nickname',
			'password',
			'correo',
			]