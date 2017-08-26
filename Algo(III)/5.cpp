#include "heuristicaAux.cpp"
using namespace std;

#define vecindad 1 //1 para swap de un arreglo, 2 para swap y corrimiento

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

void compararContraMax(const vector<int>& localMap1, const vector<int>& localMap2, int& valorMax,vector<arista> &resMax,vector<int> &maxMap1,vector<int> &maxMap2){
	vector<arista> resLocal;				
	aristasEnComun(g1,g2,localMap1,localMap2,resLocal);
	int valorLocal = resLocal.size();
	//cout << "max: " << valorMax << " local value: " << valorLocal << endl;
	if(valorLocal > valorMax){
		valorMax = valorLocal;
		resMax = resLocal;
		maxMap1 = localMap1;
		maxMap2 = localMap2;
	}
}

vector<arista> busqLocal(){
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

	/*
	defino la vecindad como:
	mapeos a1 y a2 son vecinos de b1 y b2 si y solo si 
	b1 difiere de a1 por un swap, y b2 difiere de a2 por un swap
	*/
	vector<int> localMap1(maxMap1);
	vector<int> localMap2(maxMap2);

	int valorMaxVecindadAnterior = -1;

	//sigo solo si no soy mejor que todos mis vecinos (si no estoy en un maximo local)
	while(valorMaxVecindadAnterior < valorMax){
		valorMaxVecindadAnterior = valorMax;

		if(vecindad == 2){
			shift1Right(localMap1);
		}

		for (int i = 0; i < localMap2.size(); ++i){
			for (int j = i+1; j < localMap1.size(); ++j){
				//para cada posicion, hago un swap con todos los elementos delante suyo (los de atras ya fueron hechos)
				swap(localMap1[i],localMap1[j]);
				compararContraMax(localMap1,localMap2,valorMax,resMax,maxMap1,maxMap2);
				swap(localMap1[i],localMap1[j]);
			}
		}
	
		localMap1 = maxMap1;
		localMap2 = maxMap2;
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

	cout << stringSalida( busqLocal() );
	return 0;
}