#include "heuristicaAux.cpp"

using namespace std;

#define greedyNumber 1

vector<arista> llamarGreedy(int numeroAlgoritmo){

	//renombramos los grafos de forma que g1 sea el que mas nodos tiene
	if(g1.size() < g2.size()){
		grafo gAux = g1;
		g1 = g2;
		g2 = gAux;
	}

	mapeoG1.resize(g1.size());
	mapeoG2.resize(g2.size());
	// sera case selection para ver q algoritmo llamo
	switch(numeroAlgoritmo){
		case 1: greedy1(g1,g2,mapeoG1,mapeoG2);
				break;
		case 2: greedy2(g1,g2,mapeoG1,mapeoG2);
				break;
	}

	vector<arista> res;
	//dado el mapeo actual, busco las aristas en comun
	aristasEnComun(g1,g2,mapeoG1,mapeoG2,res);
	return res;
}

int main(int argc, char const *argv[]){
	parseEntrada();
	cout << stringSalida( llamarGreedy(greedyNumber) );
	return 0;
}