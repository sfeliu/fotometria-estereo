#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct arista{
int u;
int v;
arista(int a, int b){
	u = a;
	v = b;
}
};

int posicion(const vector<int>& V, int i){
	if(V.size() == 0) return 0;
	int p;
	for (p = 0; p < V.size(); ++p){
		if (i == V[p]) return p;
	}
	return p;
}

typedef vector<vector<int> > grafo;
struct subgrafo{
	grafo graph;
	vector<int> indexOriginales;

	//construye un subgrafo con donde cada nodo i del subgrafo corresponde al nodo i del grafo
	subgrafo(const grafo& H){
		graph = H;
		indexOriginales.resize(H.size());
		for (int i = 0; i < H.size(); ++i){
			indexOriginales[i] = i;
		}
	}

	//dado un subgrafo, construye un subgrafo que solo contiene los nodos indicados en nodos
	subgrafo(const subgrafo& H, vector<int> nodos){
		graph.resize(nodos.size());
		indexOriginales.resize(nodos.size());
		//cout << nodos.size() << endl;

		vector<int> preim(H.graph.size(),-1);
		//preim contendra la posicion de cada nodo de H en nodos, se usara para agregar vecinos luego mas rapido
		//si nodos = 4,5,6 y subgrafo tiene 0-6, preimagen contendra, -1,-1,-1,-1,0,1,2
		for (int i = 0; i < nodos.size(); ++i){
			preim[nodos[i]] = i;
		}
		//para cada nodo en nodos
		for (int i = 0; i < nodos.size(); ++i)
		{
			int nodo = nodos[i];

			//para cada vecino del nodo actual, si esta en mi nuevo subgrafo, lo mantengo como vecino
			//para nodo, su nueva posicion en el subgrafo nuevo sera i
			for (int j = 0; j < H.graph[nodo].size(); ++j)
			{
				int vecino = H.graph[nodo][j];
				if( posicion(nodos, vecino) < nodos.size() ) 
					graph[i].push_back(preim[vecino]);  
			}
			//actualizo los indices al grafo original
			indexOriginales[i] = H.indexOriginales[nodo];
		}
	}
};


vector<int> bfs(const grafo& G, int nodoInicial, vector<int>& numComponente, int label){
	//Inicializo un arreglo para marcar cuando visito los nodos
	vector<bool> visited(G.size(), 0);

	vector<int> previous(G.size());
	int v=nodoInicial;
	//Mientras queden vertices sin visitar, asigno a v un vertice sin visitar
	visited[v]=true;
	numComponente[v] = label;
	queue<int> C;
	C.push(v);

	int w, z;
	while(!C.empty()){
		w=C.front();
		C.pop();

		for(int i = 0; i <G[w].size(); i++){
			z=G[w][i];

			if(!visited[z]){
				visited[z]=true;
				//marco como perteneciente a la componente actual
				numComponente[z] = label;
				previous[z]=w;
				C.push(z);
			}
		}
	}
	return previous;
}

vector<vector<int> > encontrarComponentes(const grafo& G){
	//devuelve las diferentes componentes del grafo, en una lista de listas de nodos

	vector<int> numComponente(G.size(),-1);
	int proxComponente = 0;
	//para cada nodo, veo si esta en una comp conexa nueva, en cuyo caso la marco en numComponente
	for (int i = 0; i < G.size(); ++i){

		if (numComponente[i] == -1){
			bfs(G,i,numComponente,proxComponente);
			proxComponente++;
		}
	}

	//si proxComponente = 3, existen 3 componentes 0,1,2
	vector<vector<int> > res(proxComponente);
	//ya tengo numComponente con los numero de componente de cada nodo.
	//procedo a armar las listas de componentes
	for (int i = 0; i < G.size(); ++i){
		res[numComponente[i]].push_back(i);
	}

	return res;
}

vector<subgrafo> crearSubgrafosDisjuntos(const vector<vector<int> >& compConexas,const subgrafo& G){
	vector<subgrafo> res;
	for (int i = 0; i < compConexas.size(); ++i){
		res.push_back(subgrafo(G,compConexas[i]));
		//cout << "pushee subgrafo disjunto del complemento: " << i << endl; 
	}
	return res;
}

grafo complemento(const grafo& G){
	grafo res(G.size());
	for (int i = 0; i < res.size(); ++i){
		//para cada nodo

		//para cada arista posible, distinta de si mismo
		for (int j = 0; j < res.size(); ++j){
			//la agrego si no esta en G
			if( i != j && posicion(G[i],j) == G[i].size() ){
				res[i].push_back(j);
			}
		}
	}
	return res;
}