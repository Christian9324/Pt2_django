from django.shortcuts import render, HttpResponse
from .tasks import prueba_suma, prueba_resta, prueba_FACO
from .forms import sumaForm, ACOForm

from . import f_ACO as aco_f

from .forms import ACOForm
from django.http import HttpResponseRedirect
from rest_framework.renderers import JSONRenderer

import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from ruta_app.models import Rutas
from ruta_app.serializers import RutasGetSerializer, RutasSetSerializer

import json

def index(request):

	if request.method == "POST":
		
		form = ACOForm(request.POST)

		if form.is_valid():
			d1 = form.cleaned_data['estacionInicio']
			d2 = form.cleaned_data['estacionDestino']

			resultado = prueba_FACO.delay(int(d1), int(d2))
	else:

   		form = ACOForm()

	return render(request, 'ruta_app/index.html', {'form' : form})

@csrf_exempt
def rutas_info(request):
    """
    todas las rutas guardadas
    """
    if request.method == 'GET':
        snippets = Rutas.objects.all()
        serializer = RutasGetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def ruta_set(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RutasSetSerializer(data=data)
        if serializer.is_valid():
        	datos = serializer.data
        	ini = datos.get('estacionInicio')
        	des = datos.get('estacionDestino')

        	res = prueba_FACO.delay(ini, des)

        	if (Rutas.objects.filter( estacionInicio = ini, estacionDestino = des).exists()):
        		ruta = Rutas.objects.get(estacionInicio = ini, estacionDestino = des)
        		serializer_ruta = RutasGetSerializer(ruta)
        		print(serializer_ruta.data)
        		return JsonResponse(serializer_ruta.data, status = 201)

        	else:
        		nuevo_serializer = {'estacionInicio': ini, 'estacionDestino': des, 'rutaNodos': '[E]'}
        		serializer_ruta = RutasGetSerializer(nuevo_serializer)
        		return JsonResponse(serializer_ruta.data, safe=False)



def pag(request):

	resultado = prueba_resta.delay(5, 6)

	return HttpResponse(resultado)
# Create your views here.



def plot(request):

    ruta1 = "/home/chris/Escritorio/hormiga python/LM.aco";
    data1 = aco_f.openFile(ruta1)
    conexiones = aco_f.formatC(data1)

    ruta2 = "/home/chris/Escritorio/hormiga python/d1.aco";
    data2 = aco_f.openFile(ruta2)
    d = aco_f.formatD(data2)
    # Creamos los datos para representar en el gráfico
    #conexiones = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 5], [3, 4], [3, 5], [4, 5]]
    #d = [[0, 9, 2, 1, 5], [0, 1, 2, 7, 4]]

    for rsd12 in d:
    	nodos = len(rsd12)

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    f.suptitle('Grafo', fontsize=16, fontweight='bold')

    ax = f.add_subplot(111)

    for g in range(nodos):
        ax.plot(d[0][g],d[1][g], marker='o', linestyle=':', color='b')
        ax.text(d[0][g]-0.004,d[1][g]+0.001, ''+str(g+1))

    for coor in conexiones:
    	p1 = coor[0]
    	p2 = coor[1]
    	ax.plot([d[0][p1-1],d[0][p2-1]],[d[1][p1-1], d[1][p2-1]], marker='o', linestyle=':', color='k')

    # Creamos los ejes
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response