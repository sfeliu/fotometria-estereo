from random import randint
import sys
import os
from ranges import *

# if len(sys.argv) < 5:
# 	print("usage:\ngen.py numProb numInst numIt caso")
# 	exit(1)

tipo = sys.argv[1]
numProb = int(tipo)

if numProb == 21: #arbol vs completo, subir al mismo tiempo
	N = Nbase21
	iteraciones = numInst21
	print("generando instancias de "+str(numProb))
	while iteraciones > 0: 
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 " + str(N-3) + " 0"
		parametroG2 = "9 " + str(N) + " 0"

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc21
		iteraciones -= 1

elif numProb == 22: #arbol vs completo, completo fijo
	N = Nbase22
	iteraciones = numInst22

	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % (Nbase22)
		parametroG2 = "9 %d 0" % (N)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc22
		iteraciones -= 1	 

	pass
elif numProb == 23: #arbol vs minclique, suben los dos
	N = Nbase23
	iteraciones = numInst23
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "9 %d 0" % N 

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc23
		iteraciones -= 1	
	pass

elif numProb == 24: #arbol vs minclique, sube solo el arbol
	N = Nbase24
	iteraciones = numInst24
	M = Nbase24*2
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (Nbase24+1,2*Nbase24)
		parametroG2 = "9 %d 0" % N

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc24
		iteraciones -= 1

elif numProb == 25: #minclique vs arbol, sube M miniclique
	M = Nbase25
	iteraciones = numInst25
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "8 %d %d" % (Nbase25+1,M)
		parametroG2 = "9 %d 0" % Nbase25

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc25
		iteraciones -= 1

elif numProb == 26: #completo vs minclique, suben los dos
	N = Nbase26
	iteraciones = numInst26
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = N*2
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % int(N-3)
		parametroG2 = "8 %d %d" % (N,M)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc26
		iteraciones -= 1
elif numProb == 27: #completo vs minclique, sube minclique
	N = Nbase27
	iteraciones = numInst27
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = Nbase27*2
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "1 %d 0" % Nbase27

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc27
		iteraciones -= 1

elif numProb == 28: #completo vs minclique, sube M minclique
	M = Nbase28
	iteraciones = numInst28
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "8 %d %d" % (Nbase28,M)
		parametroG2 = "1 %d 0" % Nbase28

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc28
		iteraciones -= 1

elif numProb == 41: #arbol vs completo, subir al mismo tiempo
	N = Nbase41
	iteraciones = numInst41
	print("generando instancias de "+str(numProb))
	while iteraciones > 0: 
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 " + str(N-3) + " 0"
		parametroG2 = "9 " + str(N) + " 0"

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc41
		iteraciones -= 1

elif numProb == 42: #arbol vs completo, completo fijo
	N = Nbase42
	iteraciones = numInst42

	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % (Nbase42)
		parametroG2 = "9 %d 0" % (N)
		print parametroG2
		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc42
		iteraciones -= 1	 

	pass
elif numProb == 43: #arbol vs minclique, suben los dos
	N = Nbase43
	iteraciones = numInst43
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "9 %d 0" % N 

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc43
		iteraciones -= 1	
	pass

elif numProb == 44: #arbol vs minclique, sube solo el arbol
	N = Nbase44
	iteraciones = numInst44
	M = Nbase44*2
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (Nbase44+1,2*Nbase44)
		parametroG2 = "9 %d 0" % N

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc44
		iteraciones -= 1

elif numProb == 45: #minclique vs arbol, sube M miniclique
	M = Nbase45
	iteraciones = numInst45
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "8 %d %d" % (Nbase45+1,M)
		parametroG2 = "9 %d 0" % Nbase45

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc45
		iteraciones -= 1

elif numProb == 46: #completo vs minclique, suben los dos
	N = Nbase46
	iteraciones = numInst46
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = N*2
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % int(N-3)
		parametroG2 = "8 %d %d" % (N,M)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc46
		iteraciones -= 1
elif numProb == 47: #completo vs minclique, sube minclique
	N = Nbase47
	iteraciones = numInst47
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = Nbase47*2
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "1 %d 0" % Nbase47

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc47
		iteraciones -= 1

if numProb == 48: #completo vs minclique, sube M minclique
	M = Nbase48
	iteraciones = numInst48
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "8 %d %d" % (Nbase48,M)
		parametroG2 = "1 %d 0" % Nbase48

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc48
		iteraciones -= 1

elif numProb == 51: #arbol vs completo, subir al mismo tiempo
	N = Nbase51
	iteraciones = numInst51
	print("generando instancias de "+str(numProb))
	while iteraciones > 0: 
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 " + str(N-3) + " 0"
		parametroG2 = "9 " + str(N) + " 0"

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc51
		iteraciones -= 1

elif numProb == 52: #arbol vs completo, completo fijo
	N = Nbase52
	iteraciones = numInst52

	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % (Nbase52)
		parametroG2 = "9 %d 0" % (N)
		print parametroG2
		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc52
		iteraciones -= 1	 

	pass
elif numProb == 53: #arbol vs minclique, suben los dos
	N = Nbase53
	iteraciones = numInst53
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "9 %d 0" % N 

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc53
		iteraciones -= 1	
	pass

elif numProb == 54: #arbol vs minclique, sube solo el arbol
	N = Nbase54
	iteraciones = numInst54
	M = Nbase54*2
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (Nbase54+1,2*Nbase54)
		parametroG2 = "9 %d 0" % N

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc54
		iteraciones -= 1

elif numProb == 55: #minclique vs arbol, sube M miniclique
	M = Nbase55
	iteraciones = numInst55
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "8 %d %d" % (Nbase55+1,M)
		parametroG2 = "9 %d 0" % Nbase55

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc55
		iteraciones -= 1

elif numProb == 56: #completo vs minclique, suben los dos
	N = Nbase56
	iteraciones = numInst56
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = N*2
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % int(N-3)
		parametroG2 = "8 %d %d" % (N,M)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc56
		iteraciones -= 1
elif numProb == 57: #completo vs minclique, sube minclique
	N = Nbase57
	iteraciones = numInst57
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = Nbase57*2
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "1 %d 0" % Nbase57

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc57
		iteraciones -= 1

if numProb == 58: #completo vs minclique, sube M minclique
	M = Nbase58
	iteraciones = numInst58
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "7 %d %d" % (Nbase58,M)
		parametroG2 = "1 %d 0" % Nbase58

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc58
		iteraciones -= 1

elif numProb==60: #Todo igual, salvo size dinamico vs estatico de la lista tabu
	N = Nbase60
	iteraciones = numInst60
	print("generando instancias de "+str(numProb))
	while iteraciones > 0: 
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "6 " + str(N) + " 0"
		parametroG2 = "6 " + str(N) + " 0"

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc60
		iteraciones -= 1


elif numProb == 61: #arbol vs completo, subir al mismo tiempo
	N = Nbase61
	iteraciones = numInst61
	print("generando instancias de "+str(numProb))
	while iteraciones > 0: 
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 " + str(N-3) + " 0"
		parametroG2 = "9 " + str(N) + " 0"

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc61
		iteraciones -= 1

elif numProb == 62: #arbol vs completo, completo fijo
	N = Nbase62
	iteraciones = numInst62

	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % (Nbase62)
		parametroG2 = "9 %d 0" % (N)
		print parametroG2
		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc62
		iteraciones -= 1	 

	pass
elif numProb == 63: #arbol vs minclique, suben los dos
	N = Nbase63
	iteraciones = numInst63
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "9 %d 0" % N 

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc63
		iteraciones -= 1	
	pass

elif numProb == 64: #arbol vs minclique, sube solo el arbol
	N = Nbase64
	iteraciones = numInst64
	M = Nbase64*2
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (Nbase64+1,2*Nbase64)
		parametroG2 = "9 %d 0" % N

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc64
		iteraciones -= 1

elif numProb == 65: #minclique vs arbol, sube M miniclique
	M = Nbase65
	iteraciones = numInst65
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "8 %d %d" % (Nbase65+1,M)
		parametroG2 = "9 %d 0" % Nbase65

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc65
		iteraciones -= 1

elif numProb == 66: #completo vs minclique, suben los dos
	N = Nbase66
	iteraciones = numInst66
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = N*2
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		parametroG1 = "1 %d 0" % int(N-3)
		parametroG2 = "8 %d %d" % (N,M)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc66
		iteraciones -= 1
elif numProb == 67: #completo vs minclique, sube minclique
	N = Nbase67
	iteraciones = numInst67
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = Nbase67*2
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "8 %d %d" % (N,2*N)
		parametroG2 = "1 %d 0" % Nbase67

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc67
		iteraciones -= 1

if numProb == 68: #completo vs minclique, sube M minclique
	M = Nbase68
	iteraciones = numInst68
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "7 %d %d" % (Nbase68,M)
		parametroG2 = "1 %d 0" % Nbase68

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc68
		iteraciones -= 1

if numProb == 31: #2 completos
	N = Nbase31
	iteraciones = numInst31
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "1 %d 0" % N
		parametroG2 = "1 %d 0" % (N-3)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc31
		iteraciones -= 1

if numProb == 32: #2 completos
	N = Nbase32
	iteraciones = numInst32
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "1 %d 0" % N
		parametroG2 = "1 %d 0" % (int(N/2))

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc32
		iteraciones -= 1

if numProb == 33: #2 completos
	N = Nbase33
	iteraciones = numInst33
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "4 %d 1" % N
		parametroG2 = "1 %d 0" % (N-3)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc33
		iteraciones -= 1

if numProb == 34: #2 completos
	N = Nbase34
	iteraciones = numInst34
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "4 %d 4" % N
		parametroG2 = "1 %d 0" % int(N/2)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc34
		iteraciones -= 1

if numProb == 71: #Path vs centipide, crecen iguales 
	N = Nbase71
	iteraciones = numInst71
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:

		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "11 %d 4" % N
		parametroG2 = "2 %d 0" % N

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc71
		iteraciones -= 1

if numProb == 72: #Path vs bipartito, crecen iguales 
	N = Nbase72
	iteraciones = numInst72
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M=2*N
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "10 %d %d" % (N,M)
		parametroG2 = "2 %d 0" % N

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc72
		iteraciones -= 1

if numProb == 73: #Path vs bipartito, crece el path
	N = Nbase73
	iteraciones = numInst73
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M=2*N
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "10 %d %d" % (Nbase73,Nbase73*2)
		parametroG2 = "2 %d 0" % N

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc73
		iteraciones -= 1

if numProb == 74: #Path vs bipartito, crece el M 
	M = Nbase74
	iteraciones = numInst74
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "10 %d %d" % (Nbase74,M)
		parametroG2 = "2 %d 0" % Nbase74

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc74
		iteraciones -= 1

if numProb == 75: #Centipede vs bipartito, crecen ambos
	N = Nbase75
	iteraciones = numInst75
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = 2*N
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "10 %d %d" % (N,M)
		parametroG2 = "11 %d 4" % (N)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc75
		iteraciones -= 1

if numProb == 76: #Centipede vs bipartito, crece bipartito
	N = Nbase76
	iteraciones = numInst76
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		M = 2*N
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "10 %d %d" % (N,M)
		parametroG2 = "11 %d 4" % (Nbase76)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc76
		iteraciones -= 1

if numProb == 77: #Centipede vs bipartito, crece centipede
	N = Nbase77
	iteraciones = numInst77
	M = 2*N
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		nombreArchivo = "in/%d_%d.in" % (numProb,N)
		parametroG1 = "10 %d %d" % (Nbase77,M)
		parametroG2 = "11 %d 4" % (N)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		N += Ninc77
		iteraciones -= 1

if numProb == 78: #Centipede vs bipartito, crece bipartito
	M = Nbase78
	iteraciones = numInst78
	print("generando instancias de "+str(numProb))
	while iteraciones > 0:
		nombreArchivo = "in/%d_%d.in" % (numProb,M)
		parametroG1 = "10 %d %d" % (Nbase78,M)
		parametroG2 = "11 %d 4" % (Nbase78)

		os.system("./gen " + parametroG1 + " " + parametroG2 + " > "+ nombreArchivo)
		print("generada instancia en "+nombreArchivo)

		M += Ninc78
		iteraciones -= 1