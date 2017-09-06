#ifndef __MATRIZ_ESPARZA_H__
#define __MATRIZ_ESPARZA_H__

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

        double& elem(const int i, const int j);
        double operator()(const int i, const int j) const;
        MatrizEsparza& operator*(const MatrizEsparza &o) const;

        MatrizEsparza& trasponer();
        MatrizEsparza traspuesta() const;

        int filas() const;
        int columnas() const;

        MatrizEsparza& multiplicarPorTraspuestaBanda(const int p, const int q);

    private:
        map<pair<int, int>, double> _dicc;
        int _filas, _columnas;
        bool _traspuesta;

        void _verificarRango(const int i, const int j) const;
};

#endif //__MATRIZ_ESPARZA_H__