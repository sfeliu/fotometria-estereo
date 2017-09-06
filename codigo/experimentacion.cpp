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

void testEliminacionGaussiana(vector<Matriz> terminosIndependientes){
    //cout<<"Empezando prueba de eliminación gaussiana con " << terminosIndependientes.size() << " terminos independientes" << endl;
    int tamano = terminosIndependientes.size();
    Matriz random = randomMatrizSDP(3);
    clock_t start = clock();
    for(int i=0;i<tamano;i++){
        random.eliminacionGaussiana(terminosIndependientes[i]);
        Matriz x; random.backwardSubstitution(x,terminosIndependientes[i]);
        double norma2 = x.normaF();
        if (!eq(norma2, 0))
            x = (1/norma2) * x; // normalizo el vector para obtener la normal
    }
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
}


void testFactorizacionCholesky(vector<Matriz> terminosIndependientes){
    cout<<"Empezando prueba de factorización de Chelosky con " << terminosIndependientes.size() << " terminos independientes" << endl;
    int tamano = terminosIndependientes.size();
    Matriz random = randomMatrizSDP(3);
    clock_t start = clock();
    Matriz L, Lt;
    random.factorizacionCholesky(L);
    Lt = L.traspuesta();
    for(int i=0;i<tamano;i++){
        Matriz m; L.forwardSubstitution(m, random); // resuelvo ecuacion Lm = Pb (m = Un)
        Matriz n; Lt.backwardSubstitution(n, m); // resuelvo ecuacion Un = m
        random.eliminacionGaussiana(terminosIndependientes[i]);
        double norma2 = n.normaF();
        if (!eq(norma2, 0))
            n = (1/norma2) * n; // normalizo el vector para obtener la normal
    }
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
}


void testFactorizacionLU(vector<Matriz> terminosIndependientes){
    cout<<"Empezando prueba de factorización LU con " << terminosIndependientes.size() << " terminos independientes" << endl;
    int tamano = terminosIndependientes.size();
    Matriz random = randomMatrizSDP(3);
    clock_t start = clock();
    Matriz L,P,U;
    random.factorizacionPLU(P,L,U);
    for(int i=0;i<tamano;i++){
        Matriz Pb = P * terminosIndependientes[i];
        Matriz m; L.forwardSubstitution(m, Pb); // resuelvo ecuacion Lm = Pb (m = Un)
        Matriz n; U.backwardSubstitution(n, m); // resuelvo ecuacion Un = m
        double norma2 = n.normaF();
        if (!eq(norma2, 0))
            n = (1/norma2) * n; // normalizo el vector para obtener la normal
    }
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
}

int main(){
    int tamano = 500;
    //cout<<"Coloque la cantidad de terminos independientes que quiera testear: ";
    //cin >> tamano;
    vector<Matriz> terminosIndependientes;
    for(int i=0; i<tamano; i++){
        Matriz temporal = Matriz(3,1);
        temporal(0,0) = random02();
        temporal(1,0) = random02();
        temporal(2,0) = random02();
        terminosIndependientes.push_back(temporal);
    }
    //cout<<endl<<"Ingrese el número del que se quiera testear: eliminación gaussiana: 1 - factorización LU: 2 - factorización Cholesky: 3"<< endl;
    int modo = 1;
    //cin >> modo;
    if(modo == 1){
        testEliminacionGaussiana(terminosIndependientes);
    }else if(modo == 2){
        testFactorizacionLU(terminosIndependientes);
    }else{
        testFactorizacionCholesky(terminosIndependientes);
    }
    return 0;
}