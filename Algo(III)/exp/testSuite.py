#!/usr/bin/python

import sys
import getopt
import subprocess
import time
import platform
import os.path


def comparar(grafo1, grafo2):
	grafo1Tam = (0,0)
	grafo2Tam = (0,0)

	with open(grafo1,'r') as f:
	    first_line = f.readline().strip()
	    grafo1Tam = [int(word) for word in first_line.split()]

	with open(grafo2,'r') as f:
	    first_line = f.readline().strip()
	    grafo2Tam = [int(word) for word in first_line.split()]

	porcentajeNodos = grafo2Tam[0] * 100 / grafo1Tam[0]
	porcentajeAristas = grafo2Tam[1] * 100 / grafo1Tam[1]

	resultado = (porcentajeNodos, porcentajeAristas)

	return resultado

def main(argv):
	#si se usa un archivo de entrada no se usa un generador de grafos
	archivoEntradaTMP = 'grafos_generados_time_' + str(time.time())
	archivoEntrada = archivoEntradaTMP +'.in'
	archivoSalida = archivoEntradaTMP +'.out'
	archivoExacto = archivoEntradaTMP +'.exacto'
	archivoResultados = archivoEntradaTMP +'.resultados'
	seDebeGenerar = True
	#si se usa un generador de grafos no se usa un archivo de entrada
	argumentosParaGeneradorDeGrafos = ''
	#ejercicio para ejecutar
	ejercicio = ''
	#parametros para testing
	cantIteraciones = 1
	compararConExacto = False
	comparacion = (0,0)
	
	#intenta levantar argumentos, devuelve las opciones si no funciona
	try:
		opts, args = getopt.getopt(argv,"e:chi:o:t:n:",["ifile=","ofile="])
	except getopt.GetoptError as err:
		print( str(err) )  # will print something like "option -a not recognized"
		sys.exit(2)
	#recorre los argumentos para poblar las variables
	for opt, arg in opts:
		if opt == '-h':
			print( '-h help \n -e <ejercicio> \n -i <archivoEntrada> \n -t <opciones> \n -c <compararConExacto>')
		elif opt == '-t':
			argumentosParaGeneradorDeGrafos = arg
		elif opt in ("-i", "--ifile"):
			archivoEntrada = arg +'.in'
			archivoSalida = arg +'.out'
			archivoExacto = arg +'.exacto'
			archivoResultados = arg +'.resultados'
		if opt == '-e':
			ejercicio = arg
		if opt == '-c':
			compararConExacto = True
			if os.path.isfile(archivoExacto) :
				seDebeGenerar = False
		if opt == '-n':
			cantIteraciones = arg
	
	#se detecta la plataforma para poder ejecutar en windows
	plat = platform.system()
	#se crean o abren los archivos temporales para ir pasando a los diferentes subprocesos	
	#ejecutar herramientas y ejercicios, luego graficar una salida favorable a la lectura.
	
	#generar grafos si no se usan grafos de entrada, caso contrario ya estan levantados del archivo.
	if archivoEntrada == archivoEntradaTMP+'.in' :
		grafosGenerados = open(archivoEntrada, 'w+')
		if plat == 'Linux':
			grafosGenerados.write(subprocess.check_output(["./Generator" + argumentosParaGeneradorDeGrafos]))
		else:
			grafosGenerados.write(subprocess.check_output(["Generator.exe" + argumentosParaGeneradorDeGrafos]))
		grafosGenerados.close()

	mcs = open(archivoSalida, 'w+')
	#ejecutar el ejercicio a testear.
	start = time.time()
	if plat == 'Linux':
		mcs.write(subprocess.check_output("./"+ejercicio +" < "+ archivoEntrada, shell=True))
	else:
		mcs.write(subprocess.check_output(ejercicio +".exe < "+ archivoEntrada, shell=True))
	elapsed = (time.time() - start)
	#cerrar el archivo del mcs
	mcs.close()
	
	#si se pide el porcentaje de optimalidad, se compara con el resultado del exacto.
	if compararConExacto:
		#Si el MCS exacto no fue especificado antes, se lo genera mediante el ejercicio 2.
		if seDebeGenerar:
			#abrir el archivo del resultado exacto para escribir el resultado.
			resultadoExacto = open(archivoExacto, 'w+')
			if plat == 'Linux':
				resultadoExacto.write(subprocess.check_output("./prob2 + < "+ archivoEntrada, shell=True))
			else:
				resultadoExacto.write(subprocess.check_output("prob2.exe + < "+ archivoEntrada, shell=True))
			#cerrar el archivo de resultadoExacto
			resultadoExacto.close()
		#se grafica mostrando los resultados del ejercicio actual, el tiempo que tardo, y la comparacion con el exacto.
		comparacion = comparar(archivoExacto, archivoSalida)
	
	salidaTexto = open(archivoResultados, 'w+')
	salidaTexto.write('porcentaje cubierto de nodos: '+ str(comparacion[0]) +'\nporcentaje cubierto de aristas: ' + str(comparacion[1]) +'\ntiempo de ejecucion: ' + str(elapsed))
	salidaTexto.close()

	#imprimir los resultados con los graficos de los grafos.
	subprocess.check_output("python graficador.py "+ archivoEntrada + " " + archivoSalida + " " + str(elapsed) + " " + str(comparacion[0]) + " " + str(comparacion[1]), shell=True)

if __name__ == "__main__":
	main(sys.argv[1:])

   #porcentajeOptimalidad = comparar(resultadoEjercicio, resultadoExacto)
   #graficar(resultadoEjercicio, tiempoDeEjecucion, resultadoExacto)