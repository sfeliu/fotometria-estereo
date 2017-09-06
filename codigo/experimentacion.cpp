#include "matriz.h"
#include "ppm.h"
#include "fputils.h"
#include <sstream>
#include <random>
#include <chrono>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

double random01(){
    return ((double) rand() / (RAND_MAX));
}

double random02(){
    std::mt19937_64 rng;
    // initialize the random number generator with time-dependent seed
    uint64_t timeSeed = std::chrono::high_resolution_clock::now().time_since_epoch().count();
    std::seed_seq ss{uint32_t(timeSeed & 0xffffffff), uint32_t(timeSeed>>32)};
    rng.seed(ss);
    // initialize a uniform distribution between 0 and 1
    std::uniform_real_distribution<double> unif(0, 1);
    // ready to generate random numbers
    const int nSimulations = 10;
    double randomNumber;
    for (int i = 0; i < nSimulations; i++)
    {
        double currentRandomNumber = unif(rng);
        randomNumber = currentRandomNumber;
    }
    return randomNumber;
}

double random03(int n){

    unsigned int time_ui = static_cast<unsigned int>( time(NULL) );
    srand( time_ui + n);
    return ((double) rand() / (RAND_MAX));
}

Matriz randomMatriz(int f, int c){
    int tamano = f*c;
    double matrizRandom[tamano];
    for(int i=0; i<tamano; i++) {
        matrizRandom[i] = random02();
    }
    Matriz r(f,c,matrizRandom,tamano);
    return r;
}

Matriz randomMatrizSDP(int n){
    Matriz r1 = randomMatriz(n,n);
    //r1.print();
    Matriz r2 = r1.traspuesta();
    //r2.print();
    r1 = r1*r2;
    //r1.print();
    Matriz i = Matriz::Identidad(n);
    //i.print();
    i = i*n*n;
    //i.print();
    r1 = r1+i;
    //r1.print();
    return r1;
}

Matriz eliminacionGaussiana(Matriz a,Matriz b) {
    int f = 0, c = 0;
    Matriz nueva = a;
    while (f < nueva.filas() && c < nueva.columnas()) {
        // Busco fila de pivoteo parcial
        int i = f; // fila de pivoteo parcial
        for (int k = i + 1; k < nueva.filas(); ++k) {
            if (fabs(nueva(i,c)) < fabs(nueva(k,c)))
                i = k;
        }
        if (!eq(nueva(i,c), 0)) { // si hay fila de pivoteo parcial
            // Hago el pivoteo (se rompe el invariante de banda p, q)
            b.permutarFila(f, i);
            nueva.permutarFila(f, i);
            for (int k = f + 1; k < nueva.filas(); ++k) {
                if (!eq(nueva(k,c), 0)) {
                    double m = nueva(k,c) / nueva(f,c);
                    b.restarMultiploDeFila(k, f, m);
                    nueva.restarMultiploDeFila(k, f, m);
                }
            }
            ++f;
        }
        ++c;
    }
    return nueva;
}

void testEliminacionGaussiana(vector<Matriz> terminosIndependientes, int filas){
    cout<<"Empezando prueba de eliminación gaussiana con " << terminosIndependientes.size() << " terminos independientes" << endl;
    int tamano = terminosIndependientes.size();
    Matriz random = randomMatrizSDP(filas);
    clock_t start = clock();
    for(int i=0;i<tamano;i++){
        Matriz A = eliminacionGaussiana(random, terminosIndependientes[i]);
        Matriz x; A.backwardSubstitution(x,terminosIndependientes[i]);
    }
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
}


void testFactorizacionCholesky(vector<Matriz> terminosIndependientes, int filas){
    cout<<"Empezando prueba de factorización de Chelosky con " << terminosIndependientes.size() << " terminos independientes" << endl;
    int tamano = terminosIndependientes.size();
    Matriz random = randomMatrizSDP(filas);
    clock_t start = clock();
    Matriz L, Lt;
    random.factorizacionCholesky(L);
    Lt = L.traspuesta();
    for(int i=0;i<tamano;i++){
        Matriz m; L.forwardSubstitution(m, terminosIndependientes[i]); // resuelvo ecuacion Lm = Pb (m = Un)
        Matriz n; Lt.backwardSubstitution(n, m); // resuelvo ecuacion Un = m
    }
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
}


void testFactorizacionLU(vector<Matriz> terminosIndependientes, int filas){
    cout<<"Empezando prueba de factorización LU con " << terminosIndependientes.size() << " terminos independientes" << endl;
    int tamano = terminosIndependientes.size();
    Matriz random = randomMatrizSDP(filas);
    clock_t start = clock();
    Matriz L,P,U;
    random.factorizacionPLU(P,L,U);
    for(int i=0;i<tamano;i++){
        Matriz Pb = P * terminosIndependientes[i];
        Matriz m; L.forwardSubstitution(m, Pb); // resuelvo ecuacion Lm = Pb (m = Un)
        Matriz n; U.backwardSubstitution(n, m); // resuelvo ecuacion Un = m
    }
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
}

int main(){
    int tamano = 1000;
    cout<<"Coloque la cantidad de terminos independientes que quiera testear: ";
    cin >> tamano;
    cout<<"Coloque la cantidad de filas de la matriz que quiera testear: ";
    int filas;
    cin >> filas;
    vector<Matriz> terminosIndependientes;
    for(int i=0; i<tamano; i++){
        Matriz temporal = Matriz(filas,1);
        for(int j=0; j<filas;j++){
            temporal(j,0) = random03(j);
        }
        terminosIndependientes.push_back(temporal);
    }
    cout<<endl<<"Ingrese el número del que se quiera testear: eliminación gaussiana: 1 - factorización LU: 2 - factorización Cholesky: 3"<< endl;
    int modo = 3;
    cin >> modo;
    if(modo == 1){
        testEliminacionGaussiana(terminosIndependientes, filas);
    }else if(modo == 2){
        testFactorizacionLU(terminosIndependientes, filas);
    }else{
        testFactorizacionCholesky(terminosIndependientes, filas);
    }
    return 0;
}