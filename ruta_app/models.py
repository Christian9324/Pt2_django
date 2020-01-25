from __future__ import unicode_literals

from django.db import models

class Rutas(models.Model):
	idRuta =  models.AutoField(primary_key=True)
	estacionInicio = models.IntegerField(default=0)
	estacionDestino = models.IntegerField(default=0)
	rutaNodos = models.TextField()

	def __str__(self):
		return  "%d, %s"%(self.idRuta, self.rutaNodos)


class tablaSuma(models.Model):
	idOperacion =  models.AutoField(primary_key=True)
	dato1 = models.IntegerField(default=0)
	dato2 = models.IntegerField(default=0)
	resultado = models.IntegerField(default=0)

	def __str__(self):
		return  "%d, %s"%(self.idOperacion, self.resultado)


class rutasProcesar(models.Model):
	idProcesar =  models.AutoField(primary_key=True)
	estacionInicioP = models.IntegerField(default=0)
	estacionDestinoP = models.IntegerField(default=0)

	def __str__(self):
		return  "%d, %s, %s"%(self.idProcesar, self.estacionInicioP, self.estacionDestinoP)


class Usuario(models.Model):
	idUsuario =  models.AutoField(primary_key=True)
	nickname = models.CharField(max_length = 150)
	correo = models.CharField(max_length = 254)
	password = models.CharField(max_length = 128)

	def __str__(self):
		return  "%d, %s"%(self.idUsuario, self.nickname)