# README #

Instrucciones para testSuite.py:
Tener instalados los módulos que se detallan en los import al comienzo del archivo y de graficador.py

ejecutar con:
python testSuite.py -i <archivos de entrada> -e <ejercicio a probar> -c <comparar con exacto> -t <opciones para el generador>
<archivos de entrada> consiste de un conjunto de archivos (que puede estar incompleto)
archivoEntrada = arg +'.in'
archivoSalida = arg +'.out'
archivoExacto = arg +'.exacto'
donde .in es el archivo con los grafos, .out es la salida del ejercicio a ejecutar, .exacto es la salida generada por el ejercicio 2 con el mcs exacto.
<ejercicio a probar> es el programa del ejercicio a ejecutar (sin ./ o .exe) preferentemente con nombre de tipo probX
<comparar con exacto> si se usa la opción entonces se tiene en cuenta (o se genera) el archivo .exacto y se toma el porcentaje de nodos y aristas cubiertas (con regla de tres simple)
<opciones para el generador> si se especifican son parámetros que se pasan directamente al generador de grafos

salida:
Se generan todos los archivos faltantes en la cadena de ejecución pedida (.out, .exacto, .resultado) y un archivo .pdf con los gráficos de los grafos pedidos (usando el código de fran, que se basa en las aristas) y el porcentaje de aristas y nodos cubiertos, junto con el tiempo de ejecución del algoritmo a probar.

####

graficador:
llamarlo con "python graficador.py <grafos de entrada> <mcs> <tiempo de ejecución> <porcentaje nodos> <porcentaje aristas>

los parámetros pueden ser los últimos tres 0, pero actualmente no pueden no estar.

salida:
la salida es un archivo .pdf con el nombre de archivo de <grafos de entrada>.pdf donde figuran los porcentajes de optimalidad y el tiempo de ejecución pasados por parámetro.

####

DEBUG:
Para debuggear los problemas con archivos de entrada con ddd (o gdb) hay que cargar los programas y luego comenzar la ejecución con la cadena "run < <archivoEntrada>"