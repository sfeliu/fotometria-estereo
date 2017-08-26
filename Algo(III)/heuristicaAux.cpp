#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <utility>
using namespace std;

int posicion(const vector<int>& V, int i);

struct arista{
int u;
int v;
arista(int a, int b){
	u = a;
	v = b;
}
};

struct conexion{
int index;
vector<int> V;
};
typedef vector<conexion> grafo;
typedef vector<vector<bool> > grafoMatriz;

grafo g1, g2;
grafoMatriz g1Matriz;
vector<int> mapeoG1,mapeoG2;
int N1, M1, N2, M2;

void parseEntrada(){
	cin >> N1 >> M1 >> N2 >> M2;
	g1.resize(N1);
	g2.resize(N2);

	vector<bool> vacio1(max(N1,N2),false);
	g1Matriz.resize(max(N1,N2),vacio1);

	for (int i = 0; i < g1.size(); ++i){g1[i].index = i;}
	for (int i = 0; i < g2.size(); ++i){g2[i].index = i;}

	int e1,e2;
	for (int i = 0; i < M1; ++i){
		cin >> e1 >> e2;
		g1[e1].V.push_back(e2);
		g1[e2].V.push_back(e1);
		if(N1>=N2){
		g1Matriz[e2][e1] = true;
		g1Matriz[e1][e2] = true;
		}

	}
	for (int i = 0; i < M2; ++i){
		cin >> e1 >> e2;
		g2[e1].V.push_back(e2);
		g2[e2].V.push_back(e1);
		if(N1<N2){
		g1Matriz[e2][e1] = true;
		g1Matriz[e1][e2] = true;
		}
	}
}

string stringSalida(vector<arista> V){
	string res="";
	stringstream s1;
	s1 << g2.size();

	stringstream s2;
	s2 << V.size();

	res += s1.str()+" "+s2.str()+"\n";


	string mapeo1="";
	for (int i = 0; i < g2.size(); ++i){
		stringstream s3;
		s3 << mapeoG1[i];
		mapeo1 += s3.str()+" ";
	}
	mapeo1+="\n";

	string mapeo2="";
	for (int i = 0; i < g2.size(); ++i){
		stringstream s4;
		s4 << mapeoG2[i];
		mapeo2 += s4.str()+" ";
	}
	mapeo2+="\n";

	if(N1 < N2) res += mapeo2+mapeo1; //N1 era el tamaño del g1 original, que puede haber swappeado a g2 durante la ejecucion
	else res += mapeo1+mapeo2;

	for (int i = 0; i < V.size(); ++i){
		stringstream s5;
		s5 << V[i].u;
		stringstream s6;
		s6 << V[i].v;
		res += s5.str()+" "+s6.str()+"\n";
	}

	return res;
}

int posicion(const vector<int>& V, int i){
	if(V.size() == 0) return max(M1,M2);
	int p;
	for (p = 0; p < V.size(); ++p){
		if (i == V[p]) return p;
	}
	return p;
}

bool compGrados(const conexion& nodo1, const conexion& nodo2){
	return nodo1.V.size() > nodo2.V.size();
}

void greedy1(grafo G1, grafo G2, vector<int>& MapG1, vector<int>& MapG2){
	//ideas:
	//llena mapeoRes 
	//tomar el nodo de mayor grado de cada grafo y matchearlos, etc

	//primero ordeno ambos grafos por grado
	sort(G1.begin(), G1.end(), compGrados);
	sort(G2.begin(), G2.end(), compGrados);

	for (int i = 0; i < G2.size(); ++i){
		MapG1[i] = G1[i].index;
		MapG2[i] = G2[i].index;
	}

}

int buscarMaxYRemover(grafo& g){
	int indiceMax = -1;
	int maxVecinos = 0;

	//busco el nodo de mayor grado
	for (int i = 0; i < g.size(); ++i){
		//printf("i: %d, vecinos: %lu\n", i, g[i].V.size());
		if(g[i].V.size() >= maxVecinos){
			maxVecinos = g[i].V.size();
			indiceMax = i;
		}
	}

	int indiceReal = g[indiceMax].index;
	//cout << "indice " << indiceMax << ", indice Real " << indiceReal << endl; 
	//remuevo al maximo del grafo (de sus vecinos y como nodo)
	for (int i = 0; i < g.size(); ++i){
		//cout << i << ": ";
		for (int j = 0; j < g[i].V.size(); ++j){
			//cout << j << endl;
			if(g[i].V[j] == indiceReal){
				g[i].V.erase(g[i].V.begin()+j);
				break;
			}
		}
	}

	g.erase(g.begin()+indiceMax);

	return indiceReal;
}

void greedy2(grafo G1, grafo G2, vector<int>& MapG1, vector<int>& MapG2){
	//ideas:
	//llena mapeoRes 
	//tomar el nodo de mayor grado de cada subgrafo (remuevo las aristas que ya conte una vez) y matchearlos, etc
	int iteraciones = G2.size();
	for (int i = 0; i < iteraciones; ++i){
		MapG1[i] = buscarMaxYRemover(G1);
		MapG2[i] = buscarMaxYRemover(G2);
	}
}

vector<int> reverseMap(const vector<int>& MapG){
	vector<int> res(MapG.size());
	for (int i = 0; i < MapG.size(); ++i){
		res[MapG[i]] = i;
	}
	return res;
}

void shift1Right(vector<int>& V){
	int vzero = V[V.size()-1];
	for (int i = V.size()-2; i >= 0; --i){
		V[i+1] = V[i];
	}
	V[0] = vzero;
}

void shift1Left(vector<int>& V){
	int vlast = V[0];
	for (int i = 1; i <= V[V.size()-1]; ++i){
		V[i-1] = V[i];
	}
	V[V.size()-1] = vlast;
}

vector<arista> aristasEnComun(const grafo& G1, const grafo& G2, const vector<int>& MapG1, const vector<int>& MapG2, vector<arista>& res){
//dado el mapeo actual, busco las aristas en comun
	vector<int> unMap1 = reverseMap(MapG1);
	vector<int> unMap2 = reverseMap(MapG2);

	for (int i = 0; i < G2.size(); ++i){
		int unMapi = unMap2[i];;
		for (int j = 0; j < G2[i].V.size(); ++j){
			int unMapv = unMap2[G2[i].V[j]];
			if( unMapi <= unMapv &&  g1Matriz[MapG1[unMapi]][MapG1[unMapv]])
				//para cada arista en G2, veo si, desaplicando el mapeo, esta en G1
				res.push_back( arista(unMapi,unMapv) );
		}
	}
	return res;
}