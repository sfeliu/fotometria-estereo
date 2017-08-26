import sys
import os
import matplotlib.pyplot as plt
import math
from ranges import *
import numpy as np

tipo = sys.argv[1]
numProb = int(tipo)

fig = plt.figure()

ax = fig.add_subplot(111)

if numProb==21:
	titulo = u"Arbol vs completo, ambos crecen"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	with open("out/"+tipo+"_NoPoda.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase21,Nbase21 + Ninc21*len(resPoda), Ninc21)

	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")
	plt.xlabel("N")

	

elif numProb==22:
	titulo = u"Arbol vs completo, completo fijo"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	with open("out/"+tipo+"_NoPoda.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase22,Nbase22 + Ninc22*len(resPoda), Ninc22)
	floats = np.arange(Nbase22,Nbase22 + (Ninc22)*len(resPoda), 0.1)
	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")
	plt.xlabel("N del arbol")

	# bruto=[pow(float(i),float(i)) for i in floats]
	# c=0.1
	# x_cero = int(float(len(resNoPoda)))
	# while(c*bruto[len(bruto)-1]>resNoPoda[len(resNoPoda)-1]):
	# 	c=0.5*c
	# c=c*2
	# teorico=[c*float(i) for i in bruto]
	# ax.plot(floats,teorico , color='green',label=u'Valor teorico')

elif numProb==23:
	titulo = u"Arbol vs min-clique, ambos crecen"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	# with open("out/"+tipo+"_NoPoda.out") as f:
	# 		resNoPoda = [float(line) for line in f]
	x = xrange(Nbase23,Nbase23 + Ninc23*len(resPoda), Ninc23)

	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	# ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")
	plt.xlabel("N1")

elif numProb==24:
	titulo = u"Arbol vs min-clique, arbol crece"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	# with open("out/"+tipo+"_NoPoda.out") as f:
	# 		resNoPoda = [float(line) for line in f]
	x = xrange(Nbase24,Nbase24 + Ninc24*len(resPoda), Ninc24)

	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	# ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")
	plt.xlabel("N")

elif numProb==25:
	titulo = u"Arbol vs min-clique: crece M del min-clique"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	with open("out/"+tipo+"_NoPoda.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase25,Nbase25 + Ninc25*len(resPoda), Ninc25)

	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")

	plt.xlabel("M")

elif numProb==26:
	titulo = u"Completo vs min-clique: ambos crecen"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	x = xrange(Nbase26,Nbase26 + Ninc26*len(resPoda), Ninc26)
	with open("out/"+tipo+"_NoPoda.out") as f:
			resNoPoda = [float(line) for line in f]
	ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")
	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	plt.xlabel("N")

elif numProb==27:
	titulo = u"Completo vs min-clique: crece el min-clique"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	x = xrange(Nbase27,Nbase27 + Ninc27*len(resPoda), Ninc27)
	with open("out/"+tipo+"_NoPoda.out") as f:
			resNoPoda = [float(line) for line in f]
	ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")
	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	plt.xlabel("N1")

if numProb==28:
	titulo = u"Completo vs min-clique: crece M del min-clique"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	with open("out/"+tipo+"_NoPoda.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase28,Nbase28 + Ninc28*len(resPoda), Ninc28)

	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	ax.plot(x, resNoPoda, color='red', label=u"Backtracking sin poda")
	plt.xlabel("M")

if numProb==41:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase41,Nbase41 + Ninc41*len(resVec1), Ninc41)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase41,Nbase41 + Ninc41*len(resVec1), Ninc41)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==42:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase42,Nbase42 + Ninc42*len(resVec1), Ninc42)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase42,Nbase42 + Ninc42*len(resVec1), Ninc42)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==43:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase43,Nbase43 + Ninc43*len(resVec1), Ninc43)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase43,Nbase43 + Ninc43*len(resVec1), Ninc43)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==44:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase44,Nbase44 + Ninc44*len(resVec1), Ninc44)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase44,Nbase44 + Ninc44*len(resVec1), Ninc44)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==45:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase45,Nbase45 + Ninc45*len(resVec1), Ninc45)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase45,Nbase45 + Ninc45*len(resVec1), Ninc45)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==46:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase46,Nbase46 + Ninc46*len(resVec1), Ninc46)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase46,Nbase46 + Ninc46*len(resVec1), Ninc46)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==47:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase47,Nbase47 + Ninc47*len(resVec1), Ninc47)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase47,Nbase47 + Ninc47*len(resVec1), Ninc47)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==48:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase48,Nbase48 + Ninc48*len(resVec1), Ninc48)

	ax1.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax1.plot(x, resVec2, color='red', label=u"Greedy 2")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_greedy1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_greedy2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase48,Nbase48 + Ninc48*len(resVec1), Ninc48)

	ax2.plot(x, resVec1, color='blue', label=u"Greedy 1")
	ax2.plot(x, resVec2, color='red', label=u"Greedy 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")



if numProb==51:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol vs completo, crecen ambos"
	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase51,Nbase51 + Ninc51*len(resVec1), Ninc51)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")

	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase51,Nbase51 + Ninc51*len(resVec1), Ninc51)

	ax2.plot(x, resVec1, linewidth = 3.0, linestyle='--', color='blue', label=u"Vecindad 1")
	ax2.plot(x, resVec2, color='red', label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==52:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol vs completo, crecen ambos"
	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase52,Nbase52 + Ninc52*len(resVec1), Ninc52)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")

	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase52,Nbase52 + Ninc52*len(resVec1), Ninc52)

	ax2.plot(x, resVec1, linewidth = 4.0, linestyle='--', color='blue', label=u"Vecindad 1")
	ax2.plot(x, resVec2, color='red',linewidth=3.0, label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==53:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol vs min-clique: ambos crecen en N"
	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase53,Nbase53 + Ninc53*len(resVec1), Ninc53)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")

	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase53,Nbase53 + Ninc53*len(resVec1), Ninc53)

	ax2.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax2.plot(x, resVec2, color='red', label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==54:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol vs min-clique: crece el arbol"
	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase54,Nbase54 + Ninc54*len(resVec1), Ninc54)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")


	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase54,Nbase54 + Ninc54*len(resVec1), Ninc54)

	ax2.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax2.plot(x, resVec2,linewidth=2.0, color='red', label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==55:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels


	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase55,Nbase55 + Ninc55*len(resVec1), Ninc55)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")

	titulo = u"Arbol vs min-clique: crece M del min-clique"
	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase55,Nbase55 + Ninc55*len(resVec1), Ninc55)

	ax2.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax2.plot(x, resVec2, color='red', label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("M")

if numProb==56:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Completo vs min-clique: crecen ambos en N"
	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase56,Nbase56 + Ninc56*len(resVec1), Ninc56)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")

	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase56,Nbase56 + Ninc56*len(resVec1), Ninc56)

	ax2.plot(x, resVec1,linewidth=3.0,linestyle='--', color='blue', label=u"Vecindad 1")
	ax2.plot(x, resVec2, color='red', label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==57:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Completo vs min-clique: crece min-clique"
	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase57,Nbase57 + Ninc57*len(resVec1), Ninc57)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")


	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase57,Nbase57 + Ninc57*len(resVec1), Ninc57)

	ax2.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax2.plot(x, resVec2, color='red', label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==58:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Completo vs min-clique: crece el M de min-clique"
	with open("out/"+tipo+"_vec1.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase58,Nbase58 + Ninc58*len(resVec1), Ninc58)

	ax1.plot(x, resVec1, color='blue', label=u"Vecindad 1")
	ax1.plot(x, resVec2, color='red', label=u"Vecindad 2")


	with open("out/"+tipo+"_vec1.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase58,Nbase58 + Ninc58*len(resVec1), Ninc58)

	ax2.plot(x, resVec1, color='blue',linewidth=3.0,linestyle='--', label=u"Vecindad 1")
	ax2.plot(x, resVec2, color='red', label=u"Vecindad 2")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==60:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Longitud de lista tabu, estatica vs dinamica"
	with open("out/"+tipo+"_din.out") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_est.out") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase60,Nbase60 + Ninc60*len(resVec1), Ninc60)

	ax1.plot(x, resVec1, color='blue', linewidth=3.0,linestyle="--", label=u"Dinamica")

	ax1.plot(x, resVec2, color='red', label=u"Estatica")


	with open("out/"+tipo+"_din.res") as f:
			resVec1 = [float(line) for line in f]
	with open("out/"+tipo+"_est.res") as f:
			resVec2 = [float(line) for line in f]
	x = xrange(Nbase60,Nbase60 + Ninc60*len(resVec1), Ninc60)

	ax2.plot(x, resVec1, color='blue', linewidth=3.0,linestyle="--", label=u"Dinamica")
	ax2.plot(x, resVec2, color='red', label=u"Estatica")
	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==61:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels


	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase61,Nbase61 + Ninc61*len(resVec1C1), Ninc61)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1,color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3,  color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black',label=u"Vecindad 1, Criterio 3")

	titulo = u"Arbol vs completo, ambos crecen"
	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase61,Nbase61 + Ninc61*len(resVec1C1), Ninc61)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")



	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==62:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol vs completo, completo fijo"
	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase62,Nbase62 + Ninc62*len(resVec1C1), Ninc62)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1, color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3, color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black', label=u"Vecindad 1, Criterio 3")

	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase62,Nbase62 + Ninc62*len(resVec1C1), Ninc62)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==63:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol vs min-clique, crecen ambos"
	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase63,Nbase63 + Ninc63*len(resVec1C1), Ninc63)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1, color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3, color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase63,Nbase63 + Ninc63*len(resVec1C1), Ninc63)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==64:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol vs min-clique, crece el arbol en N"
	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase64,Nbase64 + Ninc64*len(resVec1C1), Ninc64)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1, color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3, color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase64,Nbase64 + Ninc64*len(resVec1C1), Ninc64)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==65:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase65,Nbase65 + Ninc65*len(resVec1C1), Ninc65)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1, color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3, color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black', label=u"Vecindad 1, Criterio 3")

	titulo = u"Arbol vs min-clique, sube el M de min-clique"
	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase65,Nbase65 + Ninc65*len(resVec1C1), Ninc65)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==66:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Completo vs min-clique, ambos crecen en N"
	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase66,Nbase66 + Ninc66*len(resVec1C1), Ninc66)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase66,Nbase66 + Ninc66*len(resVec1C1), Ninc66)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==67:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Completo vs min-clique, crece en N min-clique"
	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase67,Nbase67 + Ninc67*len(resVec1C1), Ninc67)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black', label=u"Vecindad 1, Criterio 3")

	titulo = u"Completo vs min-clique, sube min-clique"
	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase67,Nbase67 + Ninc67*len(resVec1C1), Ninc67)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==68:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels


	with open("out/"+tipo+"_vec1crit1.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase68,Nbase68 + Ninc68*len(resVec1C1), Ninc68)

	with open("out/"+tipo+"_vec2crit1.out") as f:
			resVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.out") as f:
			resVec2C3 = [float(line) for line in f]

	ax1.plot(x, resVec1C1, color='blue', label=u"Vecindad 1, Criterio 1")
	ax1.plot(x, resVec2C3, color='red', label=u"Vecindad 2, Criterio 3")
	ax1.plot(x, resVec2C1, color='green', label=u"Vecindad 2, Criterio 1")
	ax1.plot(x, resVec1C3, color='black', label=u"Vecindad 1, Criterio 3")

	titulo = u"Completo vs min-clique: crece en M el min-clique"
	with open("out/"+tipo+"_vec1crit1.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec1crit3.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase68,Nbase68 + Ninc68*len(resVec1C1), Ninc68)

	with open("out/"+tipo+"_vec2crit1.res") as f:
			edgesVec2C1 = [float(line) for line in f]
	with open("out/"+tipo+"_vec2crit3.res") as f:
			edgesVec2C3 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, linewidth=3.0, linestyle='--', color='blue', label=u"Vecindad 1, Criterio 1")
	ax2.plot(x, edgesVec2C3, linewidth=3.0, linestyle='-.', color='red', label=u"Vecindad 2, Criterio 3")
	ax2.plot(x, edgesVec2C1, linewidth=3.0, linestyle=':', color='green', label=u"Vecindad 2, Criterio 1")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Vecindad 1, Criterio 3")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==31:
	titulo = u"Arbol vs completo, ambos crecen"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	with open("out/"+tipo+"_cografo.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase31,Nbase31 + Ninc31*len(resPoda), Ninc31)

	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	ax.plot(x, resNoPoda, color='red', label=u"Algoritmo exacto para cografo")
	plt.xlabel("N")

if numProb==32:
	titulo = u"Arbol vs completo, ambos crecen"

	with open("out/"+tipo+"_cografo.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase32,Nbase32 + Ninc32*len(resNoPoda), Ninc32)
	ax.plot(x, resNoPoda, color='red', label=u"Algoritmo exacto para cografo")
	plt.xlabel("N")

if numProb==33:
	titulo = u"Arbol vs completo, ambos crecen"
	with open("out/"+tipo+"_Poda.out") as f:
			resPoda = [float(line) for line in f]
	with open("out/"+tipo+"_cografo.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase33,Nbase33 + Ninc33*len(resPoda), Ninc33)

	ax.plot(x, resPoda, color='blue', label=u"Backtracking con poda")
	ax.plot(x, resNoPoda, color='red', label=u"Algoritmo exacto para cografo")
	plt.xlabel("N")

if numProb==34:
	titulo = u"Arbol vs completo, ambos crecen"

	with open("out/"+tipo+"_cografo.out") as f:
			resNoPoda = [float(line) for line in f]
	x = xrange(Nbase34,Nbase34 + Ninc34*len(resNoPoda), Ninc34)
	ax.plot(x, resNoPoda, color='red', label=u"Algoritmo exacto para cografo")
	plt.xlabel("N")

if numProb==71:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase71,Nbase71 + Ninc71*len(resVec1C1), Ninc71)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase71,Nbase71 + Ninc71*len(resVec1C1), Ninc71)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==72:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase72,Nbase72 + Ninc72*len(resVec1C1), Ninc72)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase72,Nbase72 + Ninc72*len(resVec1C1), Ninc72)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==73:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase73,Nbase73 + Ninc73*len(resVec1C1), Ninc73)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase73,Nbase73 + Ninc73*len(resVec1C1), Ninc73)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==74:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase74,Nbase74 + Ninc74*len(resVec1C1), Ninc74)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase74,Nbase74 + Ninc74*len(resVec1C1), Ninc74)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")

if numProb==75:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase75,Nbase75 + Ninc75*len(resVec1C1), Ninc75)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase75,Nbase75 + Ninc75*len(resVec1C1), Ninc75)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")	

if numProb==76:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase76,Nbase76 + Ninc76*len(resVec1C1), Ninc76)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase76,Nbase76 + Ninc76*len(resVec1C1), Ninc76)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")	

if numProb==77:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase77,Nbase77 + Ninc77*len(resVec1C1), Ninc77)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase77,Nbase77 + Ninc77*len(resVec1C1), Ninc77)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")	

if numProb==78:
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	# Turn off axis lines and ticks of the big subplot
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

	# Set common labels

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.out") as f:
			resVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.out") as f:
			resVec1C3 = [float(line) for line in f]
	x = xrange(Nbase78,Nbase78 + Ninc78*len(resVec1C1), Ninc78)

	with open("out/"+tipo+"_6.out") as f:
			resVec2C1 = [float(line) for line in f]


	ax1.plot(x, resVec1C1, color='blue', label=u"Heuristica Golosa")
	ax1.plot(x, resVec2C1, color='green', label=u"Tabu search")
	ax1.plot(x, resVec1C3, color='black', label=u"Heuristica busqueda local")

	titulo = u"Arbol binario completo y Grafo con clique minimo n/4"
	with open("out/"+tipo+"_4.res") as f:
			edgesVec1C1 = [float(line) for line in f]
	with open("out/"+tipo+"_5.res") as f:
			edgesVec1C3 = [float(line) for line in f]
	x = xrange(Nbase78,Nbase78 + Ninc78*len(resVec1C1), Ninc78)

	with open("out/"+tipo+"_6.res") as f:
			edgesVec2C1 = [float(line) for line in f]

	ax2.plot(x, edgesVec1C1, color='blue', label=u"Heuristica Golosa")
	ax2.plot(x, edgesVec2C1, color='green', label=u"Tabu search")
	ax2.plot(x, edgesVec1C3, color='black', label=u"Heuristica busqueda local")


	ax2.set_ylabel("Cantidad de aristas")
	ax1.set_title(titulo)
	ax1.set_ylabel("Tiempo en segundos")
	plt.xlabel("N")	

if numProb < 40:
	ax.set_title(u'Tiempos de ejecucion, '+titulo)
	plt.ylabel("Tiempo en segundos")
	# plt.legend(loc=2)
else:
	# Shrink current axis's height by 10% on the bottom
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.2,
	                 box.width, box.height * 0.8])

	# Put a legend below current axis
	ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
	          fancybox=True, shadow=True, ncol=5)
plt.show()

		