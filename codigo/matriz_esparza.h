#ifndef __MATRIZ_ESPARZA_H__
#define __MATRIZ_ESPARZA_H__

#include "fputils.h"
#include <map>
#include <algorithm>
#include <cmath>
#include <stdexcept>

using namespace std;

class MatrizEsparza {
    public:
        MatrizEsparza();
        MatrizEsparza(const int n);
        MatrizEsparza(const int f, const int c);

        void swap(MatrizEsparza &o);
        double& elem(const int i, const int j);
        double operator()(const int i, const int j) const;
        MatrizEsparza& operator*(const MatrizEsparza &o) const;

        MatrizEsparza& trasponer();
        MatrizEsparza traspuesta() const;

        int filas() const;
        int columnas() const;
        bool esCuadrada() const;

        MatrizEsparza& backwardSubstitution(MatrizEsparza &x, const MatrizEsparza &b);
        MatrizEsparza& forwardSubstitution(MatrizEsparza &x, const MatrizEsparza &b);
        MatrizEsparza& factorizacionCholesky(MatrizEsparza &L) const;
        MatrizEsparza& factorizacionCholeskyBanda(const int p, MatrizEsparza &L) const;

        MatrizEsparza& multiplicarPorTraspuestaBanda(const int p, const int q);

        void print() const {
            for (int i = 0; i < filas(); ++i) {
                for (int j = 0; j < columnas(); ++j) {
                    printf("%.8f    ", (*this)(i,j));
                }
                printf("\n");
            }
        }

    private:
        map<pair<int, int>, double> _dicc;
        int _filas, _columnas;
        bool _traspuesta;

        void _verificarRango(const int i, const int j) const;
        void _verificarBanda(const int p, const int q) const;
};

#endif //__MATRIZ_ESPARZA_H__