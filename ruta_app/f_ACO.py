import numpy as np 
import random as ran 
import os

##--- Lee y recupera la informacion de las 
##---------conexiones y los nodos 

def openFile(ruta):
   data = open(ruta,"r")
   return data

# Recuperar Datos de un archivo con 1 columna
def formatA(data):
	matrix = []
	for line in data:
		a = float(line)
		matrix.append(a)
	
	return matrix

# Recuperar Datos de un archivo con 2 columnas
def formatC(data):
   matrix = []
   for line in data:
      matrix.append([int(x) for x in line.strip().split(" ")])
   return matrix

# Recuperar Datos de un archivo con 2 filas 
def formatD(data):
	x = []
	y = []
	matrix = []
	for line in data:
		a = line.split()
		x.append(float(a[0]))
		y.append(float(a[1]))

	matrix = [y, x]
	
	return matrix

#Funcion para actualizar la feromona para cada corrida
def actualizar(matriz_f, delta_feromona, nodos_paso, Num_nodos, fact_evap):
	mat_new = matriz_f
	mj = []
	mj1 = []

	for s in nodos_paso:
		mj = sorted(list(set(s)))
		mj1.append(mj)


	for i in range(Num_nodos):
		mat_new[3][i] = ((1 - fact_evap ) * mat_new[3][i])

	subir = 0
		
	for s2 in nodos_paso:
		for s3 in s2:
			mat_new[3][s3] = mat_new[3][s3] + delta_feromona[subir]
		subir +=1


	return mat_new


def contar_guardar_ruta(rutas_b, conteo_b, ruta):

	if( (ruta in rutas_b) == False):
		rutas_b.append(ruta)
		conteo_b.append(1)
	else:
		conteo_b[rutas_b.index(ruta)] += 1


	return [rutas_b, conteo_b]



def ACO(v_1, v_2):

	#ruta1 = "/home/chris/Escritorio/hormiga python/LM.aco";
	ruta1 = os.path.abspath('data_ACO/LM.aco')
	data1 = openFile(ruta1)
	conexiones = formatC(data1)

	#ruta2 = "/home/chris/Escritorio/hormiga python/d1.aco";
	ruta2 = os.path.abspath('data_ACO/d1.aco')
	data2 = openFile(ruta2)
	d = formatD(data2)

	#ruta3 = "/home/chris/Escritorio/hormiga python/v_distancias.aco"
	ruta3 = os.path.abspath('data_ACO/v_distancias.aco')
	data3 = openFile(ruta3)
	v_distancia = formatA(data3)

	##-----------------Coneccion y nodos base--------------------------

	#conexiones = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 5], [3, 4], [3, 5], [4, 5]]
	#d = [[0, 9, 2, 1, 5], [0, 1, 2, 7, 4]]

	for rsd12 in d:
		nodos = len(rsd12)

	##---------------------------------------------------------------
	nodo_final = int(v_1)

	nodo_ini = int(v_2)
	#-------------- se inicializan las variables -------------
	phi = 0.1

	Q = 0.5

	matriz_datos = []
	v_visibilidad = []
	tau_ini = []
	alpha = 1
	beta = 1
	L_f_c = []
	bandera = 0

	#------algunas variables aux en conteo de rutas

	rutas = []
	conteo = []

	#-------------------------------------

	#print(conexiones)
	#print("\n\n")

	#---------- se inicializan valores de tabla
	for coor in conexiones:
		#p1 = coor[0]
		#p2 = coor[1]
		#dis = (((d[0][p2-1]-d[0][p1-1])**2)+((d[1][p2-1]-d[1][p1-1])**2))**0.5
		#v_distancia.append(dis)
		tau_ini.append(0.01)

	for coor in v_distancia:
		etha = 1/coor
		v_visibilidad.append(etha)
	#---------------------------------------

	##se crea la tabla de datos
	matriz_datos = [conexiones,v_distancia,v_visibilidad, tau_ini]


	##inicia las corridas
	for chris in range(1400):

		N_hormiga = 0

		# se envian un numero de hormigas
		while N_hormiga < 4:

			recorrido_n = []

			recorrido_ari = []

			L = []

			#nodo donde inicia la hormiga
			nodob = nodo_ini
			recorrido_n.append(nodob)

			#ax.plot(d[0][nodob-1],d[1][nodob-1], marker='o', linestyle=':', color='b')
			#print("\nhormiga %s"%(N_hormiga+1))

			###----------------------- inicia ACO ------------------------
			while nodob != nodo_final:

				#--- verifica que conexiones tiene el nodo inicial
				arista=[]
				conec_aux = []
				for il in conexiones:
					if(nodob == il[0]):
						arista.append(il[1])
					elif(nodob == il[1]):
						arista.append(il[0])

				#--- Metodo para confirmar si ya paso por otro nodo 

				if (len(recorrido_n) > 1):
					nodo_aux = recorrido_n[len(recorrido_n)-2]
					#print("se quito el nodo %s"%nodo_aux)
					arista.remove(nodo_aux)

				#print("#####--puede pasar por ----#####")
				#print(arista)
				#print(conec_aux)
				#--------------------------------------------------

				if (not arista):
					bandera = 1
					break

				for il in arista:
					conec_aux.append([nodob,il])


				#ordenas los aristas de forma correcta
				for f in conec_aux:
					if(f[0]>f[1]):
						f.sort()

				#obtienes coordenadas
				pos = []
				iln = 0
				iln1 = 0
				tam = len(conec_aux)


				for el in conexiones:
					if(conec_aux[iln][0] == el[0]):
						if(conec_aux[iln][1] == el[1]):
							pos.append(iln1) 
							if(iln<tam-1):
								iln = iln + 1
					iln1 = iln1 + 1

				#print(pos)

				suma = 0

				for dat in pos:
					datos = matriz_datos[2][dat]*matriz_datos[3][dat]
					suma = suma + datos

				proba_exac = []
				proba_sum = []
				suma1 = 0

				for dat in pos:
					datos = ((matriz_datos[3][dat]**alpha)*(matriz_datos[2][dat])**beta)/suma
					suma1 = suma1 + datos
					proba_sum.append([suma1-datos,suma1])	
					proba_exac.append(datos)

				#print("///-----vector de probabilidades-----///")
				#print(proba_sum)
				#print("&&&-----probabilidad por nodo--------&&&")
				#print(proba_exac)

				#term_aux = input()

				proba_usar = ran.random()

				#print(proba_usar)

				##--- define por probabilidad a donde va la hormiga
				nodoc = 0
				#print("!!!-----probabilidad aleatoria usada--!!!")
				#print(proba_usar)

				for s in range(len(proba_sum)):
					if(proba_usar > proba_sum[s][0] and proba_usar <= proba_sum[s][1]):
						nodoc = s
						#print("nodo %s"%nodoc)

	#------------------hacia donde va la hormiga -------------------------------------------
				#print(nodoc)
				#term_aux = input()
				#----------------------------------------------

				L.append([matriz_datos[1][pos[nodoc]], pos[nodoc]])
				recorrido_n.append(arista[nodoc])
				recorrido_ari.append([nodob,arista[nodoc]])

				#print("===-----distancia, conexion[]--------===")
				#print(L)

				for f in recorrido_ari:
					if(f[0]>f[1]):
						f.sort()

				#ax.plot(d[0][nodob-1],d[1][nodob-1], marker='o', linestyle=':', color='k')

				nodob = arista[nodoc]

				#ax.plot(d[0][nodob-1],d[1][nodob-1], marker='o', linestyle=':', color='b')

				#term_aux = input()
			
			if(bandera == 1):
				L[len(L)-1][0] = 100000000;
				bandera=0

			#print(L)
			L_f_c.append(L)

			#print("\n+++------Recorrido aristas--------+++")
			#print(recorrido_ari)
	##--------------------------	VER RECORRIDO UNITARIO ---------------------------
			#print(recorrido_n)
			#qqwer=input()
#			print("@@@------imprime L_f_c------------@@@")
			#print(L_f_c)

			[rutas, conteo] = contar_guardar_ruta(rutas, conteo, recorrido_n)

			N_hormiga += 1
	#---------- Actualizacion de feromona ------------
		L_h_d = []
		L_pos = []
		L_pos_234 = []
		#--- calcula el coste del camino
		for prueba in L_f_c:
			d_suma = 0
			for prueba1 in prueba:
				d_suma = d_suma + prueba1[0]
			L_h_d.append(d_suma)

		for dfgt in L_f_c:
			for trew in dfgt:
				L_pos.append(trew[1])
			#print(L_pos)
			L_pos_234.append(L_pos)
			L_pos = []

		#print(L_pos)
		#print(L_pos_234)
		#------------------------------
		#-- se saca el delta de la feromona
		delta_fero = []

		for prueba in L_h_d:
			delta_fero.append(Q/prueba)
		#------- eliminar nodos repetidos -------
		L_pos_234_f = []
		L_pos_234_aux = []
		for i in L_pos_234:
			for ii in i:
				if ii not in L_pos_234_aux:
					L_pos_234_aux.append(ii)
			L_pos_234_f.append(L_pos_234_aux)
			L_pos_234_aux = []

		#print("Delta feromona ")
		#print(delta_fero)
		#print("$$$---nodos para actualizar feromona ---$$$")
		#print(L_pos_234_f)
		#------------------------------------

		#---- se agrega la delta de feromona a los nodos 

		matriz_datos = actualizar(matriz_datos, delta_fero, L_pos_234_f, len(conexiones), phi)

		L_f_c.clear()
	#--------------- MOSTRAR  CORRIDAS   ----------------------
		#print("\n Termina corrida " + str(chris +1 ))
		#print(matriz_datos)

	#-------------------------------------------------
	#print("\n \n Matriz actualizada")
	#print(matriz_datos)
	#print(rutas)

	#print(conteo)

	#print(rutas[conteo.index(max(conteo))])

	return rutas[conteo.index(max(conteo))]
