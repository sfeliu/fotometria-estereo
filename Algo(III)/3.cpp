#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include "3aux.cpp"

using namespace std;
int N1, M1, N2, M2;
vector<int> nodosRes;

struct nodoCoTree{
	int hojas;//si es hoja, vale 1, si no, contiene la cantidad de hojas alcanzables
	int tipo; //si  hojas=1, contiene numero de nodo, si no, 0 o 1 dependiendo de tipo de union (disjunta,joint)
	vector<vector<int> > nodosMax;
	/*nodosMax alojara los nodos que maximizan la cantidad de aristas del subgrafo 
	si es hoja, el maximo score para un nodo es 0,
	si hojas=2, el maximo score para un nodo es 0, para dos nodos es 1 (dependera del tipo)
	   hojas=3, los maximos nodosMax son score[0]=0,score[1]=0,score[2]=1,score[3]=3
	   hojas=4,..., score[4]=6
	   ...*/
	vector<int> scores;
	nodoCoTree* izq;
	nodoCoTree* der;

	nodoCoTree(bool esHoja, int type, nodoCoTree* I, nodoCoTree* D){
		tipo = type;
		izq = I;
		der = D;
		//ningun nodo interno tiene menos de dos hijos
		if(esHoja) hojas = 1;
		else hojas = izq->hojas + der->hojas;

		//no interesa calcular el score para subgrafos de tamaño mayor al completo
		int nodosAObservar = min(hojas+1,N2+1);
		scores.resize(nodosAObservar); //un vector por cada cantidad posible de nodos, o sea [0,..,hojas].
		nodosMax.resize(nodosAObservar);

		//para cada cantidad, busco la combinacion que maximiza la cantidad de aristas, y me guardo dichos nodos
		//si busco 0 nodos, no agrego ningun nodo y le pongo score 0
		scores[0]=0;
		//si busco 1 nodo, puede ocurrir que soy hoja o no, y el score sera 0
		scores[1]=0;
		if(esHoja) nodosMax[1].push_back(tipo); //me pongo a mi mismo
		else nodosMax[1].push_back(izq->nodosMax[1][0]); //pongo algun nodo cualquiera

		//si soy hoja, nodosAObservar=2, o sea que no entro aca
		vector<int>* ladoI;
		vector<int>* ladoD;
		int maxScore,scoreActual;
		for (int i = 2; i < nodosAObservar; ++i){
			maxScore = -1;
			//si busco para una cantidad n, las combinaciones posibles son (0,n),(1,n-1),(2,n-2),...,(n,0), o sea n+1
			for (int j = 0; j < i+1; ++j){
			
				if(izq->scores.size() > j && der->scores.size() > i-j){//hacer checkeo de sizes

					//sumo los scores de la izquierda mas la derecha, 
					//mas el join si corresponde: si estan unidos por un uno y estoy tomando nodos de ambos lados
					scoreActual = izq->scores[j]+der->scores[i-j];
					if(type==1 ) scoreActual += izq->nodosMax[j].size() * der->nodosMax[i-j].size();
					
					if(maxScore < scoreActual){
						maxScore = scoreActual;
						//me guardo esto para poder reconstruir los nodos despues, asi no copio todo ahora
						ladoI = &(izq->nodosMax[j]);
						ladoD = &(der->nodosMax[i-j]);
					}
				}
			}
			scores[i] = maxScore;
			nodosMax[i].resize(i);
			for (int h = 0; h < i; ++h){
				if(h < ladoI->size()){
					nodosMax[i][h] = (*ladoI)[h];
				}
				else{
					nodosMax[i][h] = (*ladoD)[h-ladoI->size()];
				}
			}
		}
	}

	~nodoCoTree(){
		if(izq) delete izq;
		if(der) delete der;
	}
};

grafo g1, g2;

nodoCoTree* conCoT(const subgrafo& G){
	//si es un solo nodo, devuelvo hoja
	if (G.graph.size() == 1){
		int valor = G.indexOriginales[0];
		nodoCoTree* yo = new nodoCoTree(true, valor, NULL, NULL);
		return yo;
	}
	
	vector<vector<int> > compConexas = encontrarComponentes(G.graph);
	//si no es conexo (longitud >1),
	if(compConexas.size() > 1){
		vector<subgrafo> subgrafos = crearSubgrafosDisjuntos(compConexas,G);
		vector<nodoCoTree*> subtrees(compConexas.size());

		//llamo recursivamente para cada comp conexa y guardo el resultado
		for (int i = 0; i < subtrees.size(); ++i){
			subtrees[i] = conCoT(subgrafos[i]);

		/*uno la primera con la segunda con 0,
		la 1+2 con la 3 con 0, etc*/
		}
		for (int i = 1; i < subtrees.size(); ++i){
			nodoCoTree* conexionDisjunta = new nodoCoTree(false, 0, subtrees[i-1], subtrees[i]);
			subtrees[i] = conexionDisjunta;
		}
		return subtrees[subtrees.size()-1];
	} else {
		//es conexo
		grafo H = complemento(G.graph);
		vector<vector<int> > compConexas = encontrarComponentes(H);

		vector<subgrafo> subgrafos = crearSubgrafosDisjuntos(compConexas,G);
		vector<nodoCoTree*> subtrees(compConexas.size());

		//llamo recursivamente para cada comp conexa y guardo el resultado
		for (int i = 0; i < subtrees.size(); ++i){
			subtrees[i] = conCoT(subgrafos[i]);

		/*uno la primera con la segunda con 0,
		la 1+2 con la 3 con 0, etc*/
		}
		for (int i = 1; i < subtrees.size(); ++i){
			nodoCoTree* conexionJoin = new nodoCoTree(false, 1, subtrees[i-1], subtrees[i]);
			subtrees[i] = conexionJoin;
		}
		return subtrees[subtrees.size()-1];
	}

}

void parseEntrada(){
	//asumir que g1 es cografo, g2 completo
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

string stringSalida(const vector<arista>& V){
	string res="";
	stringstream s1;
	s1 << nodosRes.size();

	stringstream s2;
	s2 << V.size();

	res += s1.str()+" "+s2.str()+"\n";


	string mapeo1="";
	for (int i = 0; i < nodosRes.size(); ++i){
		stringstream s3;
		s3 << nodosRes[i];
		mapeo1 += s3.str()+" ";
	}
	mapeo1+="\n";

	string mapeo2="";
	for (int i = 0; i < nodosRes.size(); ++i){
		stringstream s4;
		s4 << i;
		mapeo2 += s4.str()+" ";
	}
	mapeo2+="\n";

	res += mapeo1+mapeo2;

	for (int i = 0; i < V.size(); ++i){
		stringstream s5;
		s5 << V[i].u;
		stringstream s6;
		s6 << V[i].v;
		res += s5.str()+" "+s6.str()+"\n";
	}

	return res;
}


void printTree(nodoCoTree* p, int indent)
{
	//imprime el arbol de costado
    if(p != NULL) {
        if(p->der) {
            printTree(p->der, indent+4);
        }
        if (indent) {
            cout << setw(indent) << ' ';
        }
        if (p->der) cout<<" /\n" << setw(indent) << ' ';
        cout << p->tipo << ", ";
        for (int i = 0; i < p->nodosMax.size(); ++i){
        	cout << i << ": ";
        	for (int j = 0; j < p->nodosMax[i].size(); ++j){
        		cout << p->nodosMax[i][j] << " ";
        	}
        }
        cout << "\n ";
        if(p->izq) {
            cout << setw(indent) << ' ' <<" \\\n";
            printTree(p->izq, indent+4);
        }
    }
}
vector<arista> MCS(){
	if(g1.size() <= g2.size()){
		//si el cografo entra entero en el completo

		nodosRes.resize(g1.size());
		for (int i = 0; i < g1.size(); ++i){nodosRes[i] = i;}

	} else {
		//crear un subgrafo con G, llamando al constructor, que pone los indices como vienen
		subgrafo G_prima(g1);
		//llamar a conCoT
		nodoCoTree* raiz = conCoT(G_prima);
		//printTree(raiz,0);

		nodosRes = raiz->nodosMax[N2];
		delete raiz;

		//consideramos mapeados nodosRes[i] a i, para todo i
	}
	vector<arista> res;
	for (int i = 0; i < nodosRes.size(); ++i){
		int nodo = nodosRes[i];

		for (int j = 0; j < g1[nodo].size(); ++j){
			int unMapNodo = i;
			int vecino = g1[nodo][j];
			int unMapv = posicion(nodosRes,vecino);
			if( unMapv < nodosRes.size() && unMapNodo <= unMapv ){
				//para cada arista en nodosRes, la agrego a res
				res.push_back( arista(unMapNodo,unMapv) );
			}
		}
	}

	return res;
}

int main(int argc, char const *argv[]){
	parseEntrada();
	cout << stringSalida( MCS() );
	return 0;
}