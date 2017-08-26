#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct arista{
int u;
int v;
arista(int a, int b){
	u = a;
	v = b;
}
};

typedef vector<vector<int> > grafo;

grafo g1, g2;
int maxComun = -1;
vector<int> mapeoOptimo;
int N1, M1, N2, M2;

void parseEntrada(){
	cin >> N1 >> M1 >> N2 >> M2;
	g1.resize(N1);
	g2.resize(N2);

	int e1,e2;
	for (int i = 0; i < M1; ++i){
		cin >> e1 >> e2;
		g1[e1].push_back(e2);
		g1[e2].push_back(e1);

	}
	for (int i = 0; i < M2; ++i){
		cin >> e1 >> e2;
		g2[e1].push_back(e2);
		g2[e2].push_back(e1);
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
		s3 << mapeoOptimo[i];
		mapeo1 += s3.str()+" ";
	}
	mapeo1+="\n";

	string mapeo2="";
	for (int i = 0; i < g2.size(); ++i){
		stringstream s4;
		s4 << i;
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

bool sonVecinos(grafo& g, int i, int j){
	return binary_search(g[i].begin(), g[i].end(), j);
}


int posicion(const vector<int>& V, int i){
	if(V.size() == 0) return max(M1,M2);
	int p;
	for (p = 0; p < V.size(); ++p){
		if (i == V[p]) return p;
	}
	return p;
}

bool poda(int mapProx,int comunNuevo, int comunMax){
	/*idea: si mapProx=4, g2: 1 2 3 4 5, d(4)=3,d(5)=2,comunNuevo=4,comunMax=10
	como a lo sumo se podran agregar 5 aristas mas (aunque (4,5) este contada dos veces), no se puede alcanzar comunMax
	se devuelve false cuando es inutil seguir la rama de ejecucion*/
	int diferencia = comunMax - comunNuevo;
	for (int i = mapProx; i < g2.size(); ++i)
	{
		diferencia -= g2[i].size();
		if(diferencia <= 0) return false;
	}
	return true;
}

vector<int> backtracking( vector<int>& mapeoActual, int comunActual, int mapProx, vector<bool>& /*posiciones de g1*/ noMapeadas){

	//para el siguiente nodo a agregar, pruebo cada mapeo para él
	if(mapProx < g2.size()){
		for (int i = 0; i < noMapeadas.size(); ++i){
			if(noMapeadas[i]){				

				//cout << mapProx << endl;
				int comunNuevo = comunActual;
				noMapeadas[i] = false;
				mapeoActual[mapProx] = i; //mapProx se mapea a i
				
				//me fijo las conexiones de ese nuevo mapeo
				for (int t = 0; t < g2[mapProx].size(); ++t){
					//mapProx se mapea a i, vecino se mapea a mapeoActual[vecino]
					int vecino = g2[mapProx][t];
					if(vecino < mapProx && (posicion(g1[i],mapeoActual[vecino]) < g1[i].size())){
						++comunNuevo;
					}
				}

				//llamo recursivamente si se cumple la poda
				if(!poda(mapProx+1, comunNuevo, maxComun))	
					backtracking(mapeoActual, comunNuevo, mapProx+1, noMapeadas);

				//reemplazo la solucion actual si corresponde
				if ( mapProx == g2.size()-1 && maxComun < comunNuevo ){
					maxComun = comunNuevo;
					mapeoOptimo = mapeoActual;
				}

				noMapeadas[i] = true;
				mapeoActual[mapProx] = -1;
			}
		}
	}
	return mapeoOptimo;
}


vector<arista> llamarBacktracking(){

	//renombramos los grafos de forma que g1 sea el que mas nodos tiene
	if(g1.size() < g2.size()){
		grafo gAux = g1;
		g1 = g2;
		g2 = gAux;
	}
	vector<int> mapInicial(g2.size(),-1);
	vector<bool> b(g1.size(),true);
	backtracking(mapInicial,0,0,b); //llamo con la posicion proxima como 0, devuelve el mapeo optimo

	vector<arista> res;
	for (int i = 0; i < g2.size(); ++i){	
		for (int j = 0; j < g2[i].size(); ++j){
			int unMapi = mapeoOptimo[i];
			int unMapv = mapeoOptimo[g2[i][j]];			
			if( unMapi <= unMapv ){
				//para cada arista en g2, veo si, desaplicando el mapeo, esta en g1
				if(posicion(g1[unMapi],unMapv) < g1[unMapi].size())
					res.push_back( arista(i,g2[i][j]) );
			}
		}
	}
	return res;
}


int main(int argc, char const *argv[]){
	parseEntrada();
	cout << stringSalida( llamarBacktracking() );
	return 0;
}