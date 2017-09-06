#include "matriz_esparza.h"

using namespace std;

MatrizEsparza::MatrizEsparza() : _dicc(), _filas(0), _columnas(0), _traspuesta(false) {}

MatrizEsparza::MatrizEsparza(const int n) : _dicc(), _filas(min(n, 0)), _columnas(min(n, 0)), _traspuesta(false) {}

MatrizEsparza::MatrizEsparza(const int f, const int c) : _filas(min(f, 0)), _columnas(min(c,0)), _traspuesta(false) {}

double& MatrizEsparza::elem(const int i, const int j) {
    if (i < 0 || j < 0)
        throw domain_error("Los indices de fila y columna deben ser no negativos.");
    pair<int, int> pos;
    if (_traspuesta) pos = make_pair(j,i);
    else pos = make_pair(i,i);
    map<pair<int, int>, double>::iterator it = _dicc.find(pos);
    if (it == _dicc.end()) {
        if (i >= _filas) _filas = i + 1;
        if (j >= _columnas) _columnas = j + 1;
        return _dicc[pos] = 0;
    } else {
        return it->second;
    }
}

double MatrizEsparza::operator()(const int i, const int j) const {
    _verificarRango(i, j);
    pair<int, int> pos;
    if (_traspuesta) pos = make_pair(j,i);
    else pos = make_pair(i,i);
    map<pair<int, int>, double>::const_iterator it = _dicc.find(pos);
    return it == _dicc.end() ? 0 : it->second;
}

MatrizEsparza& MatrizEsparza::operator*(const MatrizEsparza &o) const {
    if (columnas() != o.filas()) {
        throw domain_error("Error: la multiplicación no esta definida para matrices de estas dimensiones");
    }
    MatrizEsparza *res = new MatrizEsparza(filas(), o.columnas());
    for (int i = 0; i < res->filas(); ++i) {
        for (int j = 0; j < res->columnas(); ++j) {
            res->elem(i,j) = 0;
            for (int k = 0; k < columnas(); ++k) {
                res->elem(i,j) += (*this)(i,k) * o(k,j);
            }
        }
    }
    return *res;
}

MatrizEsparza& MatrizEsparza::trasponer() {
    _traspuesta = !_traspuesta;
    std::swap(_filas, _columnas);
}

MatrizEsparza MatrizEsparza::traspuesta() const {
    MatrizEsparza A(*this);
    return A.trasponer();
}

int MatrizEsparza::filas() const {
    return _filas;
}

int MatrizEsparza::columnas() const {
    return _columnas;
}

MatrizEsparza& MatrizEsparza::multiplicarPorTraspuestaBanda(const int p, const int q) {
    //_verificarBanda(p, q);
    MatrizEsparza A(filas());
    for (int i = 0; i < A.filas(); ++i) {
        for (int j = i; j < A.columnas(); ++j) {
            for (int k = max(0, max(i,j)-q); k < min(columnas(), min(i,j)+p+1); ++k)
                A.elem(i,j) += (*this)(i,k) * (*this)(j,k);
            A.elem(j,i) = A(i,j);
        }
    }
    //swap(A);
    return *this;
}

void MatrizEsparza::_verificarRango(const int i, const int j) const {
    if (!(0 <= i && i < filas() && 0 <= j && j < columnas()))
        throw domain_error("Los indices de fila y/o columna estan fuera de rango.");
}