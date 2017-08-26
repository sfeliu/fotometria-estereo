#include <set>
#include <queue>
#include <math.h>
#include <unistd.h>
#include "heuristicaAux.cpp"
using namespace std;

#define vecindad 1 //1 para swap de un arreglo, 2 para swap y corrimiento
#define critParada 3 //1 para cantidad de iteraciones fija, 2 para cant iteraciones sin mejora, 3 para vecindad vacia y crit2
#define maxIteracionesCrit1 10
#define maxIteracionSinMejoraCrit2 10
#define sizeListaTabuDinamico true

void llenarPosicionesRestantes(vector<int>& V,int primerVacio){
	vector<bool> existente(V.size(),false);

	for (int i = 0; i < primerVacio; ++i){
		existente[V[i]] = true;
	}

	for (int i = 0; i < existente.size(); ++i){
		if(!existente[i]){
			V[primerVacio] = i;
			primerVacio++;
		}
	}
}

bool criterioDeParada(int valorMax,const vector<int>& localMap1,const vector<int>& localMap2){

	if(critParada == 1){
		static int numeroIteracion = 0;
		numeroIteracion++;
		return numeroIteracion > maxIteracionesCrit1;
	} else if(critParada == 2){
		static int ultimoMax = -1;
		static int cantIterSinMejoras = 0;
		if(valorMax > ultimoMax){
			ultimoMax = valorMax;
			cantIterSinMejoras = 0;
		} else {
			cantIterSinMejoras++;
		}
		return cantIterSinMejoras > maxIteracionSinMejoraCrit2;
	} else if(critParada == 3){
		//for (int i = 0; i < localMap1.size(); ++i){cout << localMap1[i] << " ";}cout << ". ";
		//for (int i = 0; i < localMap2.size(); ++i){cout << localMap2[i] << " ";}cout << endl;
		static int ultimoMax = -1;
		static int cantIterSinMejoras = 0;
		if(valorMax > ultimoMax){
			ultimoMax = valorMax;
			cantIterSinMejoras = 0;
		} else {
			cantIterSinMejoras++;
		}
		return (cantIterSinMejoras > maxIteracionSinMejoraCrit2) || (localMap1.size() == 0 && localMap2.size() == 0);
	}
}

void actualizarTabu(int& maxTabuSize, queue<vector<int> >& tabuQ1, queue<vector<int> >& tabuQ2, set<pair<vector<int>,vector<int> > >& tabuSet, const vector<int>& solucion1, const vector<int>& solucion2, bool maxQueVecindadPrevia){

	//si tengo capacidad maxima, remuevo la primera solucion que agregue
	//cout << maxTabuSize << " " << maxQueVecindadPrevia << "      ";
	if(sizeListaTabuDinamico){
		static int cantIterSinMejoria = 0;
		if (maxQueVecindadPrevia) cantIterSinMejoria = 0;
		else cantIterSinMejoria++;
		if(cantIterSinMejoria > maxIteracionSinMejoraCrit2/2) maxQueVecindadPrevia = true;

		static set<pair<vector<int>,vector<int> > > maxLocalesAlcanzados;
		pair<vector<int>,vector<int> > solucionActual = make_pair(solucion1,solucion2);
		if (maxQueVecindadPrevia){
			set< pair< vector<int>,vector<int> > >::iterator it = maxLocalesAlcanzados.find(solucionActual);
			if (it == maxLocalesAlcanzados.end()){
				maxLocalesAlcanzados.insert(solucionActual);
			} else {
				maxTabuSize *= 2;
			}
		}
	}

	if(tabuSet.size() == maxTabuSize){
		vector<int> solRemovida1 = tabuQ1.front();
		tabuQ1.pop();
		vector<int> solRemovida2 = tabuQ2.front();
		tabuQ2.pop();
		tabuSet.erase(make_pair(solRemovida1,solRemovida2));
	}

	//agrego la nueva
	tabuQ1.push(solucion1);
	tabuQ2.push(solucion2);
	tabuSet.insert(make_pair(solucion1,solucion2));
}

bool esTabu(const vector<int>& localMap1, const vector<int>& localMap2, const set< pair< vector<int>,vector<int> > >& tabuSet){
	set< pair< vector<int>,vector<int> > >::iterator it = tabuSet.find(make_pair(localMap1,localMap2));
	return it != tabuSet.end();
}

void compararContraMax(const vector<int>& localMap1, const vector<int>& localMap2, int& maxValorLocal,vector<arista> &maxResLocal,vector<int> &maxMapLocal1,vector<int> &maxMapLocal2, const set< pair< vector<int>,vector<int> > >& tabuSet){
	vector<arista> resLocal;				
	aristasEnComun(g1,g2,localMap1,localMap2,resLocal);
	int valorLocal = resLocal.size();
	//solo elijo una nueva posicion si no es tabu
	if(valorLocal > maxValorLocal && !esTabu(localMap1,localMap2,tabuSet)){
		maxValorLocal = valorLocal;
		maxResLocal = resLocal;
		maxMapLocal1 = localMap1;
		maxMapLocal2 = localMap2;
	}
}

vector<arista> tabuSearch(int maxTabuSize){
	vector<arista> resMax;
	vector<int> maxMap1, maxMap2;
	int valorMax;

	maxMap1.resize(g1.size(),-1);
	maxMap2.resize(g2.size(),-1);
	//llamar a greedy y setear las estructuras anteriores
	greedy1(g1,g2,maxMap1,maxMap2);

	//como greedy no llena las posiciones de g1 mayores al tamaño de g2, hay que llenarlas con todos los nodos que no estan en el mapeo actual
	llenarPosicionesRestantes(maxMap1,g2.size());
	//llena resMax y seteo valorMax
	aristasEnComun(g1,g2,maxMap1,maxMap2,resMax);
	valorMax = resMax.size();

	/*defino la vecindad como:
	mapeos a1 y a2 son vecinos de b1 y b2 si y solo si 
	b1 difiere de a1 por un swap, y b2 difiere de a2 por un swap*/
	vector<int> localMap1(maxMap1);
	vector<int> localMap2(maxMap2);

	/*para evitar una estructura nueva, la posicion i de los vectores pertenece a la misma solucion, siendo cada una el mapeo de cada grafo*/
	set< pair< vector<int>,vector<int> > > tabuSet;
	queue<vector<int> > tabuQ1, tabuQ2;

	int	valorMaxVecindadAnterior = -1;
	bool veniaAscendiendo = false;
	while( !criterioDeParada(valorMax,localMap1,localMap2) ){

		vector<int> maxMapLocal1;
		vector<int> maxMapLocal2;
		int maxValorLocal = -1;
		vector<arista> maxResLocal;

		if(vecindad == 2){
			shift1Right(localMap1);
		}

		for (int i = 0; i < localMap2.size(); ++i){
			for (int j = i+1; j < localMap1.size(); ++j){
				//para cada posicion, hago un swap con todos los elementos delante suyo (los de atras ya fueron hechos)
				swap(localMap1[i],localMap1[j]);

				compararContraMax(localMap1,localMap2,maxValorLocal,maxResLocal,maxMapLocal1,maxMapLocal2,tabuSet);

				swap(localMap1[i],localMap1[j]);
			}
		}
		
		//si la solucion que encontre en esta vecindad es mejor que la global, reemplazo
		if(vecindad == 2){
			shift1Left(localMap1);
		}

		if(maxValorLocal > valorMax){
			maxMap1 = maxMapLocal1;
			maxMap2 = maxMapLocal2;
			valorMax = maxValorLocal;
			resMax = maxResLocal;
		}
		//actualizo la lista tabu
		//cout << "max: " << valorMaxVecindadAnterior << " " << maxValorLocal << "  ";
		actualizarTabu(maxTabuSize, tabuQ1, tabuQ2, tabuSet, localMap1, localMap2,
			valorMaxVecindadAnterior < maxValorLocal);
		//acutalizo los siguientes valores para que queden preparados para la proxima iteracion (es decir, yo voy a ser el anterior)
		valorMaxVecindadAnterior = maxValorLocal;
		//actualizo el mapeo local
		localMap1 = maxMapLocal1;
		localMap2 = maxMapLocal2;
	}

	mapeoG1 = maxMap1;
	mapeoG2 = maxMap2;
	return resMax;

}

int main(int argc, char const *argv[])
{
	parseEntrada();
	//renombramos los grafos de forma que g1 sea el que mas nodos tiene
	if(g1.size() < g2.size()){
		grafo gAux = g1;
		g1 = g2;
		g2 = gAux;
	}

	int maxTabuSize = pow(N1*N2,3);

	cout << stringSalida( tabuSearch(maxTabuSize) );
	return 0;
}