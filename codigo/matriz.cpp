#include "matriz.h"

using namespace std;

void Matriz::_crearMatriz(const int f, const int c) {
    if (f <= 0 || c <= 0) {
        throw domain_error("Error: la cantidad de filas y columnas debe ser mayor a cero.");
    }
    _filas = f;
    _columnas = c;
    _traspuesta = false;
    _matriz = new double*[_filas];
    for (int i = 0; i < _filas; ++i) {
        _matriz[i] = new double[_columnas]();
    }
    _cols = new int[_columnas];
    for (int i = 0; i < _columnas; ++i) {
        _cols[i] = i;
    }
}

Matriz::Matriz() : _filas(0), _columnas(0), _matriz(NULL), _traspuesta(false), _cols(NULL) {}

Matriz::Matriz(const Matriz &o) {
    _crearMatriz(o._filas, o._columnas);
    for (int i = 0; i < _filas; ++i) {
        for (int j = 0; j < _columnas; ++j) {
            (*this)(i,j) = o(i,j);
        }
    }
}

Matriz::Matriz(const int n) {
    _crearMatriz(n, n);
    for (int i = 0; i < n; ++i) {
        (*this)(i,i) = 1;
    }
}

Matriz::Matriz(const int f, const int c) {
    _crearMatriz(f, c);
}

Matriz::Matriz(const int f, const int c, const double a[], const int n) {
    _crearMatriz(f, c);
    int i = 0, j = 0, k = 0;
    while (k < n) {
        (*this)(i,j) = a[k];
        j = (j+1) % c;
        i = j == 0 ? i+1 : i;
        ++k;
    }
}

Matriz::~Matriz() {
    for (int i = 0; i < _filas; ++i) {
        delete[] _matriz[i];
    }
    delete[] _matriz;
}

Matriz& Matriz::operator=(Matriz o) {
    swap(_filas, o._filas);
    swap(_columnas, o._columnas);
    swap(_traspuesta, o._traspuesta);
    swap(_matriz, o._matriz);
    swap(_cols, o._cols);
    return *this;
}

double& Matriz::operator()(const int i, const int j) {
    _verificarRango(i,j);
    if (_traspuesta)
        return _matriz[j][_cols[i]];
    else
        return _matriz[i][_cols[j]];
}

const double& Matriz::operator()(const int i, const int j) const {
    _verificarRango(i,j);
    if (_traspuesta)
        return _matriz[j][_cols[i]];
    else
        return _matriz[i][_cols[j]];
}

Matriz& Matriz::operator*(const Matriz &o) const {
    if (columnas() != o.filas()) {
        throw domain_error("Error: la multiplicación no esta definida para matrices de estas dimensiones");
    }
    Matriz *res = new Matriz(filas(), o.columnas());
    for (int i = 0; i < filas(); ++i) {
        for (int j = 0; j < o.columnas(); ++j) {
            for (int k = 0; k < columnas(); ++k) {
                (*res)(i,j) += (*this)(i,k) * o(k,j);
            }
        }
    }
    return *res;
}

Matriz& Matriz::operator*(const double c) const {
    Matriz *res = new Matriz(filas(), columnas());
    for (int i = 0; i < filas(); ++i) {
        for (int j = 0; j < columnas(); ++j) {
            (*res)(i,j) += (*this)(i,j) * c;
        }
    }
    return *res;
}

int Matriz::filas() const {
    return _traspuesta ? _columnas : _filas;
}

int Matriz::columnas() const {
    return _traspuesta ? _filas : _columnas;
}

bool Matriz::esCuadrada() const {
    return _filas == _columnas;
}

void Matriz::trasponer() {
    _traspuesta = !_traspuesta;
}

bool Matriz::eliminacionGaussiana(Matriz &b) {
    int f = 0, c = 0;
    bool invertible = esCuadrada();
    while (f < filas() && c < columnas()) {
        int i = f;
        for (int k = i + 1; k < filas(); ++k) {
            if (fabs((*this)(i,c)) < fabs((*this)(k,c)))
                i = k;
        }
        if (!eq((*this)(i,c), 0)) {
            b.permutarFila(f, i);
            permutarFila(f, i);
            for (int k = f + 1; k < filas(); ++k) {
                if (!eq((*this)(k,c), 0)) {
                    b.restarMultiploDeFila(k, f, (*this)(k,c) / (*this)(f,c));
                    restarMultiploDeFila(k, f, (*this)(k,c) / (*this)(f,c));
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
    int f = 0, c = 0;
    bool invertible = esCuadrada();
    while (f < filas() && c < columnas()) {
        int i = f;
        for (int k = i + 1; k < filas(); ++k) {
            if (fabs((*this)(i,c)) < fabs((*this)(k,c)))
                i = k;
        }
        if (!eq((*this)(i,c), 0)) { // tener en cuenta error de redondeo
            b.permutarFila(f, i);
            permutarFila(f, i);
            b.multiplicarFilaPorEscalar(f, 1 / (*this)(f,c));
            multiplicarFilaPorEscalar(f, 1 / (*this)(f,c));
            for (int k = 0; k < filas(); ++k) {
                if (k != f && !eq((*this)(k,c), 0)) { // tener en cuenta error de redondeo
                    b.restarMultiploDeFila(k, f, (*this)(k,c));
                    restarMultiploDeFila(k, f, (*this)(k,c));
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

void Matriz::permutarFila(const int i, const int j) {
    _verificarRango(i, 0);
    _verificarRango(j, 0);
    if (_traspuesta)
        swap(_cols[i], _cols[j]);
    else
        swap(_matriz[i], _matriz[j]);
}

void Matriz::multiplicarFilaPorEscalar(const int i, const double c) {
    for (int j = 0; j < columnas(); ++j)
        (*this)(i,j) *= c;
}

void Matriz::restarMultiploDeFila(const int i, const int j, const double c) {
    _verificarRango(i, 0);
    _verificarRango(j, 0);
    for (int k = 0; k < columnas(); ++k)
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

double Matriz::normaF() const {
    double suma = 0;
    for (int i = 0; i < filas(); ++i) {
        for (int j = 0; j < columnas(); ++j) {
            suma += pow((*this)(i,j), 2);
        }
    }
    return pow(suma, 0.5);
}

void Matriz::_verificarRango(const int f, const int c) const {
    if (!(0 <= f && f < filas() && 0 <= c && c < columnas()))
        throw domain_error("Los indices de fila y/o columna estan fuera de rango.");
}

Matriz& operator*(const double c, const Matriz &m) {
    return m * c;
}