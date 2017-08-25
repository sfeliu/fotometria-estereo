#include <string>
#include <stdexcept>
#include <cmath>
#include "matriz.h"

using namespace std;

typedef unsigned int uint;

void Matriz::_crearMatriz(const uint f, const uint c) {
    if (f == 0 || c == 0) {
        throw domain_error("Error: la cantidad de filas y columnas debe ser mayor a cero.");
    }
    _filas = f;
    _columnas = c;
    _traspuesta = false;
    _matriz = new double*[_filas];
    for (uint i = 0; i < _filas; ++i) {
        _matriz[i] = new double[_columnas]();
    }
    _cols = new uint[_columnas];
    for (uint i = 0; i < _columnas; ++i) {
        _cols[i] = i;
    }
}

Matriz::Matriz(const Matriz &o) {
    _crearMatriz(o._filas, o._columnas);
    for (uint i = 0; i < _filas; ++i) {
        for (uint j = 0; j < _columnas; ++j) {
            (*this)(i,j) = o(i,j);
        }
    }
}

Matriz::Matriz(const uint n) {
    _crearMatriz(n, n);
    for (uint i = 0; i < n; ++i) {
        (*this)(i,i) = 1;
    }
}

Matriz::Matriz(const uint f, const uint c) {
    _crearMatriz(f, c);
}

Matriz::Matriz(const uint f, const uint c, const double a[], const uint n) {
    _crearMatriz(f, c);
    uint i = 0, j = 0, k = 0;
    while (k < n) {
        (*this)(i,j) = a[k];
        j = (j+1) % c;
        i = j == 0 ? i+1 : i;
        ++k;
    }
}

Matriz::~Matriz() {
    for (uint i = 0; i < _filas; ++i) {
        delete[] _matriz[i];
    }
    delete[] _matriz;
}

Matriz& Matriz::operator=(Matriz o) {
    swap(_filas, o._filas);
    swap(_columnas, o._columnas);
    swap(_matriz, o._matriz);
    return *this;
}

double& Matriz::operator()(const uint i, const uint j) {
    if (_traspuesta)
        return _matriz[j][_cols[i]];
    else
        return _matriz[i][_cols[j]];
}

const double& Matriz::operator()(const uint i, const uint j) const {
    if (_traspuesta)
        return _matriz[j][_cols[i]];
    else
        return _matriz[i][_cols[j]];
}

Matriz& Matriz::operator*(const Matriz &o) const {
    if (columnas() != o.filas()) {
        throw domain_error("Error: la multiplicación no esta definida estos tipos de matrices");
    }
    Matriz *res = new Matriz(filas(), o.columnas());
    for (uint i = 0; i < filas(); ++i) {
        for (uint j = 0; j < o.columnas(); ++j) {
            for (uint k = 0; k < columnas(); ++k) {
                (*res)(i,j) += (*this)(i,k) * o(k,j);
            }
        }
    }
    return *res;
}

uint Matriz::filas() const {
    return _traspuesta ? _columnas : _filas;
}

uint Matriz::columnas() const {
    return _traspuesta ? _filas : _columnas;
}

bool Matriz::esCuadrada() const {
    return _filas == _columnas;
}

void Matriz::trasponer() {
    _traspuesta = !_traspuesta;
}

bool Matriz::eliminacionGaussiana(Matriz &b) {
    uint f = 0, c = 0;
    bool invertible = esCuadrada();
    while (f < filas() && c < columnas()) {
        uint i = f;
        for (uint k = i + 1; k < filas(); ++k) {
            if ((*this)(i,c) < (*this)(k,c))
                i = k;
        }
        if ((*this)(i,c) != 0) { // tener en cuenta error de redondeo
            permutarFila(f, i);
            b.permutarFila(f, i);
            for (uint k = f + 1; k < filas(); ++k) {
                if ((*this)(k,c) != 0) { // tener en cuenta error de redondeo
                    restarMultiploDeFila(k, f, (*this)(k,c) / (*this)(f,c));
                    b.restarMultiploDeFila(k, f, (*this)(k,c) / (*this)(f,c));
                }
            }
            ++f;
        } else {
            invertible = false;
        }
        ++c;
    }
    return invertible;
}

bool Matriz::eliminacionGaussJordan(Matriz &b) {
    uint f = 0, c = 0;
    bool invertible = esCuadrada();
    while (f < filas() && c < columnas()) {
        uint i = f;
        for (uint k = i + 1; k < filas(); ++k) {
            if ((*this)(i,c) < (*this)(k,c))
                i = k;
        }
        if ((*this)(i,c) != 0) { // tener en cuenta error de redondeo
            permutarFila(f, i);
            b.permutarFila(f, i);
            multiplicarFilaPorEscalar(f, 1 / (*this)(f,c));
            for (uint k = 0; k < filas(); ++k) {
                if (k != f && (*this)(k,c) != 0) { // tener en cuenta error de redondeo
                    restarMultiploDeFila(k, f, (*this)(k,c));
                    b.restarMultiploDeFila(k, f, (*this)(k,c));
                }
            }
            ++f;
        } else {
            invertible = false;
        }
        ++c;
    }
    return invertible;
}

void Matriz::permutarFila(const uint i, const uint j) {
    _verificarRango(i, 0);
    _verificarRango(j, 0);
    if (_traspuesta)
        swap(_cols[i], _cols[j]);
    else
        swap(_matriz[i], _matriz[j]);
}

void Matriz::multiplicarFilaPorEscalar(const uint i, const double c) {
    for (uint j = 0; j < columnas(); ++j)
        (*this)(i,j) *= c;
}

void Matriz::restarMultiploDeFila(const uint i, const uint j, const double c) {
    _verificarRango(i, 0);
    _verificarRango(j, 0);
    for (uint k = 0; k < columnas(); ++k)
        (*this)(i, k) -= c * (*this)(j,k);
}

bool Matriz::invertir() {
    if (!esCuadrada()) {
        throw domain_error("La matriz no es cuadrada.");
    }
    Matriz A(*this);
    Matriz b(filas());
    bool invertible = A.eliminacionGaussJordan(b);
    if (invertible) *this = b;
    return invertible;
}

const double Matriz::norma2() const {
    double suma = 0;
    for (uint i = 0; i < filas(); ++i) {
        for (uint j = 0; j < columnas(); ++j) {
            suma += pow((*this)(i,j), 2);
        }
    }
    return pow(suma, 0.5);
}

void Matriz::_verificarRango(const uint f, const uint c) {
    if (!(f < filas() && c < columnas()))
        throw domain_error("Los indices de fila y/o columna estan fuera de rango.");
}