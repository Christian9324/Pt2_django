from django_proj.celery import app
from ruta_app.models import tablaSuma, Rutas, rutasProcesar
from ruta_app import f_ACO as aco_f


@app.task
def prueba_suma(x, y):
	tablaSuma.objects.create(dato1 = x, dato2 = y, resultado = x+y)
	return x + y
     
@app.task
def prueba_resta(x, y):
    return x - y

@app.task
def prueba_FACO(x, y):

	if (rutasProcesar.objects.filter(estacionInicioP = x, estacionDestinoP = y).exists() ):
		return "en proceso"

	else:

		if( Rutas.objects.filter(estacionInicio = x, estacionDestino = y).exists() ):
			return "ruta ya creada"

		else:
			rutasProcesar.objects.create(estacionInicioP = x, estacionDestinoP = y)
			res = aco_f.ACO( y, x)
			rutasProcesar.objects.filter(estacionInicioP = x, estacionDestinoP = y).delete()
			Rutas.objects.create(estacionInicio = x, estacionDestino = y, rutaNodos = str(res))
		
			return "operacion realizada"
