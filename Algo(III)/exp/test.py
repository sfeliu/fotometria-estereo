import sys
import subprocess
from ranges import *

# if len(sys.argv) < 5:
# 	print("usage:\ngen.py numProb numInst numIt caso")
# 	exit(1)

#idea: si es el ej 2, sus variaciones tendran numProb 21,22, etc..

tipo = sys.argv[1]
numProb = int(tipo)

if numProb == 21: #n1 = n2, variamos n1, m=n-1, dos path
	N = Nbase21
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst21
	avgsNoPoda = [0] * numInst21

	while iteracion < numInst21:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt21):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt21
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt21


		N += Ninc21
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst21):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst21):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_NoPoda.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 22: #n1 = n2, variamos n1, m=constante, dos grafos sin aristas casi
	N = Nbase22
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst22
	avgsNoPoda = [0] * numInst22

	while iteracion < numInst22:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt22):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt22
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt22


		N += Ninc22
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst22):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst22):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_NoPoda.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 23: #n2,m2 fijo, variamos n1, m1=n1-1, un path, un grafo que se mantenga igual
	N = Nbase23
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst23
	avgsNoPoda = [0] * numInst23

	while iteracion < numInst23:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt23):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt23
			
			# avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			# avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt23

		sys.stdout.write("\n")
		N += Ninc23
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst23):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	# outNoPoda = ""
	# for x in xrange(0,numInst23):
	# 	outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	# with open("out/"+tipo+"_NoPoda.out","w") as text_file:
	# 	text_file.write(outNoPoda) 

elif numProb == 29: #n2,m2 fijo, variamos n1, m1=n1-1, un path, un grafo que se mantenga igual
	N = Nbase29
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst29
	while iteracion < numInst29:
		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"
		print("ejecutando para "+nombreArchivo)
		for x in xrange(0,numIt29):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt29
		sys.stdout.write("\n")
		N += Ninc29
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst29):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

elif numProb == 24: #n2,m2 fijo, variamos n1, m1 constante
	N = Nbase24
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst24
	avgsNoPoda = [0] * numInst24

	while iteracion < numInst24:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt24):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt24
			
			# avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			# avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt24

		sys.stdout.write("\n")
		N += Ninc24
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst24):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	# outNoPoda = ""
	# for x in xrange(0,numInst24):
	# 	outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	# with open("out/"+tipo+"_NoPoda.out","w") as text_file:
	# 	text_file.write(outNoPoda) 

elif numProb == 25:
	N = Nbase25
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst25
	avgsNoPoda = [0] * numInst25

	while iteracion < numInst25:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt25):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt25
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt25

		sys.stdout.write("\n")
		N += Ninc25
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst25):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst25):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_NoPoda.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 26:
	N = Nbase26
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst26
	avgsNoPoda = [0] * numInst26

	while iteracion < numInst26:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt26):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt26
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt26

		sys.stdout.write("\n")
		N += Ninc26
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst26):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst26):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_NoPoda.out","w") as text_file:
		text_file.write(outNoPoda) 
elif numProb == 27:
	N = Nbase27
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst27
	avgsNoPoda = [0] * numInst27

	while iteracion < numInst27:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt27):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt27
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt27

		sys.stdout.write("\n")
		N += Ninc27
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst27):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst27):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_NoPoda.out","w") as text_file:
		text_file.write(outNoPoda) 

if numProb == 28: #n1 = n2, variamos n1, m=n-1, dos path
	N = Nbase28
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst28
	avgsNoPoda = [0] * numInst28

	while iteracion < numInst28:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt28):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob2NoPoda "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt28
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt28

		sys.stdout.write("\n")
		N += Ninc28
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst28):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst28):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_NoPoda.out","w") as text_file:
		text_file.write(outNoPoda) 
elif numProb == 31: #g1 es completo, n2 fijo
	pass
elif numProb == 32: #
	pass

elif numProb == 41: #n1 = n2, variamos n1, m=n-1 
	N = Nbase41
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst41
	avgsGreedy2 = [0] * numInst41
	aristasGreedy1 = [0] * numInst41
	aristasGreedy2 = [0] * numInst41

	while iteracion < numInst41:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt41):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = int(f.readline().split()[1])
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy2[iteracion] = int(f.readline().split()[1])
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt41
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt41
		N += Ninc41
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst41):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst41):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst41):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst41):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 42: #n1 = n2, variamos n1, m=n-1 
	N = Nbase42
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst42
	avgsGreedy2 = [0] * numInst42
	aristasGreedy1 = [0] * numInst42
	aristasGreedy2 = [0] * numInst42

	while iteracion < numInst42:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt42):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = f.readline().split()[1]
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				print f.readline().split()[0]
				print f.readline().split()[1]
				aristasGreedy2[iteracion] = f.readline().split()[1]
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt42
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt42
		N += Ninc42
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst42):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst42):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst42):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst42):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 43: #n1 = n2, variamos n1, m=n-1 
	N = Nbase43
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst43
	avgsGreedy2 = [0] * numInst43
	aristasGreedy1 = [0] * numInst43
	aristasGreedy2 = [0] * numInst43

	while iteracion < numInst43:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt43):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = int(f.readline().split()[1])
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy2[iteracion] = int(f.readline().split()[1])
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt43
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt43
		N += Ninc43
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst43):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst43):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst43):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst43):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 44: #n1 = n2, variamos n1, m=n-1 
	N = Nbase44
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst44
	avgsGreedy2 = [0] * numInst44
	aristasGreedy1 = [0] * numInst44
	aristasGreedy2 = [0] * numInst44

	while iteracion < numInst44:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt44):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = int(f.readline().split()[1])
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy2[iteracion] = int(f.readline().split()[1])
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt44
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt44
		N += Ninc44
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst44):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst44):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst44):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst44):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 45: #n1 = n2, variamos n1, m=n-1 
	N = Nbase45
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst45
	avgsGreedy2 = [0] * numInst45
	aristasGreedy1 = [0] * numInst45
	aristasGreedy2 = [0] * numInst45

	while iteracion < numInst45:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt45):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = int(f.readline().split()[1])
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy2[iteracion] = int(f.readline().split()[1])
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt45
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt45
		N += Ninc45
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst45):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst45):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst45):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst45):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 46: #n1 = n2, variamos n1, m=n-1 
	N = Nbase46
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst46
	avgsGreedy2 = [0] * numInst46
	aristasGreedy1 = [0] * numInst46
	aristasGreedy2 = [0] * numInst46

	while iteracion < numInst46:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt46):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = int(f.readline().split()[1])
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy2[iteracion] = int(f.readline().split()[1])
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt46
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt46
		N += Ninc46
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst46):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst46):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst46):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst46):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 47: #n1 = n2, variamos n1, m=n-1 
	N = Nbase47
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst47
	avgsGreedy2 = [0] * numInst47
	aristasGreedy1 = [0] * numInst47
	aristasGreedy2 = [0] * numInst47

	while iteracion < numInst47:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt47):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = int(f.readline().split()[1])
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy2[iteracion] = int(f.readline().split()[1])
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt47
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt47
		N += Ninc47
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst47):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst47):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst47):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst47):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 48: #n1 = n2, variamos n1, m=n-1 
	N = Nbase48
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsGreedy1 = [0] * numInst48
	avgsGreedy2 = [0] * numInst48
	aristasGreedy1 = [0] * numInst48
	aristasGreedy2 = [0] * numInst48

	while iteracion < numInst48:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt48):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy1[iteracion] = int(f.readline().split()[1])
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob4greedy2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasGreedy2[iteracion] = int(f.readline().split()[1])
			
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]+runtimePoda
			avgsGreedy1[iteracion] = avgsGreedy1[iteracion]/numIt48
			
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]+runtimeNoPoda
			avgsGreedy2[iteracion] = avgsGreedy2[iteracion]/numIt48
		N += Ninc48
		iteracion += 1
	outPoda = ""
	for x in xrange(0,numInst48):
		outPoda = outPoda + str(avgsGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst48):
		outNoPoda = outNoPoda + str(avgsGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.out","w") as text_file:
		text_file.write(outNoPoda) 

	outArV1 = ""
	for x in xrange(0,numInst48):
		outArV1 = outArV1 + str(aristasGreedy1[x])+"\n"

	with open("out/"+tipo+"_greedy1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst48):
		outArV2 = outArV2 + str(aristasGreedy2[x])+"\n"

	with open("out/"+tipo+"_greedy2.res","w") as text_file:
		text_file.write(outArV2) 

elif numProb == 51: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase51
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst51
	avgsVecindad2 = [0] * numInst51
	aristasVec1 = [0] * numInst51
	aristasVec2 = [0] * numInst51

	while iteracion < numInst51:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt51):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt51
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt51


		N += Ninc51
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst51):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst51):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst51):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst51):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 52: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase52
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst52
	avgsVecindad2 = [0] * numInst52
	aristasVec1 = [0] * numInst52
	aristasVec2 = [0] * numInst52

	while iteracion < numInst52:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt52):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt52
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt52


		N += Ninc52
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst52):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst52):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst52):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst52):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 


elif numProb == 53: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase53
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst53
	avgsVecindad2 = [0] * numInst53
	aristasVec1 = [0] * numInst53
	aristasVec2 = [0] * numInst53

	while iteracion < numInst53:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt53):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt53
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt53


		N += Ninc53
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst53):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst53):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst53):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst53):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 54: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase54
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst54
	avgsVecindad2 = [0] * numInst54
	aristasVec1 = [0] * numInst54
	aristasVec2 = [0] * numInst54

	while iteracion < numInst54:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt54):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt54
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt54


		N += Ninc54
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst54):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst54):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst54):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst54):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 55: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase55
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst55
	avgsVecindad2 = [0] * numInst55
	aristasVec1 = [0] * numInst55
	aristasVec2 = [0] * numInst55

	while iteracion < numInst55:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt55):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt55
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt55


		N += Ninc55
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst55):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst55):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst55):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst55):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 56: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase56
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst56
	avgsVecindad2 = [0] * numInst56
	aristasVec1 = [0] * numInst56
	aristasVec2 = [0] * numInst56

	while iteracion < numInst56:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt56):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt56
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt56


		N += Ninc56
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst56):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst56):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst56):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst56):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 57: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase57
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst57
	avgsVecindad2 = [0] * numInst57
	aristasVec1 = [0] * numInst57
	aristasVec2 = [0] * numInst57

	while iteracion < numInst57:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt57):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt57
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt57


		N += Ninc57
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst57):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst57):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst57):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst57):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 


elif numProb == 58: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase58
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst58
	avgsVecindad2 = [0] * numInst58
	aristasVec1 = [0] * numInst58
	aristasVec2 = [0] * numInst58

	while iteracion < numInst58:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt58):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./5vecindad2 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt58
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt58


		N += Ninc58
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst58):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_vec1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst58):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_vec1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst58):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_vec2.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst58):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_vec2.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 60: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase60
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVecindad1 = [0] * numInst60
	avgsVecindad2 = [0] * numInst60
	aristasVec1 = [0] * numInst60
	aristasVec2 = [0] * numInst60

	while iteracion < numInst60:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt60):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6dinamico "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6estatico "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2[iteracion] = int(f.readline().split()[1])

			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]+runtimePoda
			avgsVecindad1[iteracion] = avgsVecindad1[iteracion]/numIt60
			
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]+runtimeNoPoda
			avgsVecindad2[iteracion] = avgsVecindad2[iteracion]/numIt60


		N += Ninc60
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst60):
		outPoda = outPoda + str(avgsVecindad1[x])+"\n"

	with open("out/"+tipo+"_din.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst60):
		outArV1 = outArV1 + str(aristasVec1[x])+"\n"

	with open("out/"+tipo+"_din.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst60):
		outArV2 = outArV2 + str(aristasVec2[x])+"\n"

	with open("out/"+tipo+"_est.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst60):
		outNoPoda = outNoPoda + str(avgsVecindad2[x])+"\n"

	with open("out/"+tipo+"_est.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 61: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase61
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst61:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt61):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt61
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt61

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt61
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt61


		N += Ninc61
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst61):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst61):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst61):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst61):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst61):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst61):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst61):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst61):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 62: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase62
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst62:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt62):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt62
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt62

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt62
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt62


		N += Ninc62
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst62):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst62):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst62):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst62):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst62):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst62):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst62):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst62):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 63: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase63
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst63:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt63):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt63
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt63

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt63
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt63


		N += Ninc63
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst63):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst63):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst63):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst63):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst63):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst63):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst63):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst63):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 64: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase64
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst64:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt64):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt64
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt64

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt64
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt64


		N += Ninc64
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst64):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst64):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst64):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst64):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst64):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst64):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst64):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst64):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 65: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase65
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst65:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt65):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt65
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt65

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt65
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt65


		N += Ninc65
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst65):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst65):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst65):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst65):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst65):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst65):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst65):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst65):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 66: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase66
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst66:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt66):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt66
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt66

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt66
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt66


		N += Ninc66
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst66):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst66):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst66):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst66):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst66):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst66):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst66):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst66):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 67: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase67
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst67:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt67):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt67
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt67

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt67
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt67


		N += Ninc67
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst67):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst67):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst67):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst67):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst67):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst67):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst67):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst67):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

elif numProb == 68: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase68
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsVec1C1 = [0] * numInst61
	avgsVec2C1 = [0] * numInst61
	avgsVec1C3 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristasVec1C1 = [0] * numInst61
	aristasVec1C3 = [0] * numInst61
	aristasVec2C1 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst68:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt68):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C1[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit1 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C1[iteracion] = int(f.readline().split()[1])

			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]+runtimePoda
			avgsVec1C1[iteracion] = avgsVec1C1[iteracion]/numIt68
			
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]+runtimeNoPoda
			avgsVec2C1[iteracion] = avgsVec2C1[iteracion]/numIt68

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./6vec1crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec1C3[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]+runtimePoda
			avgsVec1C3[iteracion] = avgsVec1C3[iteracion]/numIt68
			
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt68


		N += Ninc68
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst68):
		outPoda = outPoda + str(avgsVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst68):
		outArV1 = outArV1 + str(aristasVec1C1[x])+"\n"

	with open("out/"+tipo+"_vec1crit1.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst68):
		outArV2 = outArV2 + str(aristasVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst68):
		outNoPoda = outNoPoda + str(avgsVec2C1[x])+"\n"

	with open("out/"+tipo+"_vec2crit1.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst68):
		outPoda = outPoda + str(avgsVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst68):
		outArV1 = outArV1 + str(aristasVec1C3[x])+"\n"

	with open("out/"+tipo+"_vec1crit3.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst68):
		outArV2 = outArV2 + str(aristasVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst68):
		outNoPoda = outNoPoda + str(avgsVec2C3[x])+"\n"

	with open("out/"+tipo+"_vec2crit3.out","w") as text_file:
		text_file.write(outNoPoda) 

if numProb == 31: #n1 = n2, variamos n1, m=n-1, dos path
	N = Nbase31
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst31
	avgsNoPoda = [0] * numInst31

	while iteracion < numInst31:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt31):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob3 "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt31
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt31


		N += Ninc31
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst31):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst31):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_cografo.out","w") as text_file:
		text_file.write(outNoPoda) 

if numProb == 33: #n1 = n2, variamos n1, m=n-1, dos path
	N = Nbase33
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgsPoda = [0] * numInst33
	avgsNoPoda = [0] * numInst33

	while iteracion < numInst33:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt33):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob2Poda "+nombreArchivo, shell=True))
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob3 "+nombreArchivo, shell=True))
			
			avgsPoda[iteracion] = avgsPoda[iteracion]+runtimePoda
			avgsPoda[iteracion] = avgsPoda[iteracion]/numIt33
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt33


		N += Ninc33
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst33):
		outPoda = outPoda + str(avgsPoda[x])+"\n"

	with open("out/"+tipo+"_Poda.out","w") as text_file:
		text_file.write(outPoda) 

	outNoPoda = ""
	for x in xrange(0,numInst33):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_cografo.out","w") as text_file:
		text_file.write(outNoPoda) 


if numProb == 32: #n1 = n2, variamos n1, m=n-1, dos path
	N = Nbase32
	iteracion = 0
	print("ejecutando para "+str(numProb))
	avgsNoPoda = [0] * numInst32

	while iteracion < numInst32:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt32):
			sys.stdout.write("%d, " % x)
		
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob3 "+nombreArchivo, shell=True))
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt32


		N += Ninc32
		iteracion += 1

	outNoPoda = ""
	for x in xrange(0,numInst32):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_cografo.out","w") as text_file:
		text_file.write(outNoPoda) 

if numProb == 34: #n1 = n2, variamos n1, m=n-1, dos path
	N = Nbase34
	iteracion = 0
	print("ejecutando para "+str(numProb))
	avgsNoPoda = [0] * numInst34

	while iteracion < numInst34:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt34):
			sys.stdout.write("%d, " % x)
		
			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob3 "+nombreArchivo, shell=True))
			
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]+runtimeNoPoda
			avgsNoPoda[iteracion] = avgsNoPoda[iteracion]/numIt34


		N += Ninc34
		iteracion += 1

	outNoPoda = ""
	for x in xrange(0,numInst34):
		outNoPoda = outNoPoda + str(avgsNoPoda[x])+"\n"

	with open("out/"+tipo+"_cografo.out","w") as text_file:
		text_file.write(outNoPoda) 


elif numProb == 71: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase71
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst61
	avgs5 = [0] * numInst61
	avgs6 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristas4 = [0] * numInst61
	aristas5 = [0] * numInst61
	aristas6 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst71:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt71):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt71
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt71

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt71
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt71


		N += Ninc71
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst71):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst71):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst71):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst71):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst71):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst71):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 
elif numProb == 72: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase72
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst61
	avgs5 = [0] * numInst61
	avgs6 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristas4 = [0] * numInst61
	aristas5 = [0] * numInst61
	aristas6 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst72:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt72):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt72
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt72

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt72
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt72


		N += Ninc72
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst72):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst72):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst72):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst72):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst72):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst72):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 
elif numProb == 73: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase73
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst61
	avgs5 = [0] * numInst61
	avgs6 = [0] * numInst61
	avgsVec2C3 = [0] * numInst61
	aristas4 = [0] * numInst61
	aristas5 = [0] * numInst61
	aristas6 = [0] * numInst61
	aristasVec2C3 = [0] * numInst61

	while iteracion < numInst73:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt73):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt73
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt73

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt73
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt73


		N += Ninc73
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst73):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst73):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst73):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst73):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst73):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst73):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 

elif numProb == 74: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase74
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst74
	avgs5 = [0] * numInst74
	avgs6 = [0] * numInst74
	avgsVec2C3 = [0] * numInst74
	aristas4 = [0] * numInst74
	aristas5 = [0] * numInst74
	aristas6 = [0] * numInst74
	aristasVec2C3 = [0] * numInst74

	while iteracion < numInst74:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt74):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt74
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt74

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt74
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt74


		N += Ninc74
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst74):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst74):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst74):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst74):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst74):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst74):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 

elif numProb == 75: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase75
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst75
	avgs5 = [0] * numInst75
	avgs6 = [0] * numInst75
	avgsVec2C3 = [0] * numInst75
	aristas4 = [0] * numInst75
	aristas5 = [0] * numInst75
	aristas6 = [0] * numInst75
	aristasVec2C3 = [0] * numInst75

	while iteracion < numInst75:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt75):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt75
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt75

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt75
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt75


		N += Ninc75
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst75):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst75):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst75):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst75):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst75):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst75):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 

elif numProb == 76: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase76
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst76
	avgs5 = [0] * numInst76
	avgs6 = [0] * numInst76
	avgsVec2C3 = [0] * numInst76
	aristas4 = [0] * numInst76
	aristas5 = [0] * numInst76
	aristas6 = [0] * numInst76
	aristasVec2C3 = [0] * numInst76

	while iteracion < numInst76:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt76):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt76
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt76

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt76
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt76


		N += Ninc76
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst76):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst76):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst76):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst76):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst76):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst76):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 

elif numProb == 77: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase77
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst77
	avgs5 = [0] * numInst77
	avgs6 = [0] * numInst77
	avgsVec2C3 = [0] * numInst77
	aristas4 = [0] * numInst77
	aristas5 = [0] * numInst77
	aristas6 = [0] * numInst77
	aristasVec2C3 = [0] * numInst77

	while iteracion < numInst77:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt77):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt77
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt77

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt77
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt77


		N += Ninc77
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst77):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst77):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst77):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst77):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst77):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst77):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 

elif numProb == 78: #para el par de instancias minClique (8), arbol completo (9), n1 = n2, variamos n1 y m1
	N = Nbase78
	iteracion = 0
	print("ejecutando para "+str(numProb))

	avgs4 = [0] * numInst78
	avgs5 = [0] * numInst78
	avgs6 = [0] * numInst78
	avgsVec2C3 = [0] * numInst78
	aristas4 = [0] * numInst78
	aristas5 = [0] * numInst78
	aristas6 = [0] * numInst78
	aristasVec2C3 = [0] * numInst78

	while iteracion < numInst78:

		nombreArchivo = "in/"+tipo+"_"+str(N)+".in"

		print("ejecutando para "+nombreArchivo)

		for x in xrange(0,numIt78):
			sys.stdout.write("%d, " % x)
			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob4 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas4[iteracion] = int(f.readline().split()[1])

			runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./prob5 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas5[iteracion] = int(f.readline().split()[1])

			avgs4[iteracion] = avgs4[iteracion]+runtimePoda
			avgs4[iteracion] = avgs4[iteracion]/numIt78
			
			avgs5[iteracion] = avgs5[iteracion]+runtimeNoPoda
			avgs5[iteracion] = avgs5[iteracion]/numIt78

			runtimePoda = float(subprocess.check_output("sh exp/time.sh ./prob6 "+nombreArchivo, shell=True))
			with open("temp.txt","r",1) as f:
				aristas6[iteracion] = int(f.readline().split()[1])

			# runtimeNoPoda = float(subprocess.check_output("sh exp/time.sh ./6vec2crit3 "+nombreArchivo, shell=True))
			# with open("temp.txt","r",1) as f:
			# 	aristasVec2C3[iteracion] = int(f.readline().split()[1])

			avgs6[iteracion] = avgs6[iteracion]+runtimePoda
			avgs6[iteracion] = avgs6[iteracion]/numIt78
			
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]+runtimeNoPoda
			# avgsVec2C3[iteracion] = avgsVec2C3[iteracion]/numIt78


		N += Ninc78
		iteracion += 1

	outPoda = ""
	for x in xrange(0,numInst78):
		outPoda = outPoda + str(avgs4[x])+"\n"

	with open("out/"+tipo+"_4.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst78):
		outArV1 = outArV1 + str(aristas4[x])+"\n"

	with open("out/"+tipo+"_4.res","w") as text_file:
		text_file.write(outArV1) 

	outArV2 = ""
	for x in xrange(0,numInst78):
		outArV2 = outArV2 + str(aristas5[x])+"\n"

	with open("out/"+tipo+"_5.res","w") as text_file:
		text_file.write(outArV2) 

	outNoPoda = ""
	for x in xrange(0,numInst78):
		outNoPoda = outNoPoda + str(avgs5[x])+"\n"

	with open("out/"+tipo+"_5.out","w") as text_file:
		text_file.write(outNoPoda) 

		outPoda = ""
	for x in xrange(0,numInst78):
		outPoda = outPoda + str(avgs6[x])+"\n"

	with open("out/"+tipo+"_6.out","w") as text_file:
		text_file.write(outPoda) 

	outArV1 = ""
	for x in xrange(0,numInst78):
		outArV1 = outArV1 + str(aristas6[x])+"\n"

	with open("out/"+tipo+"_6.res","w") as text_file:
		text_file.write(outArV1) 