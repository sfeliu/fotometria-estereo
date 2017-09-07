#include "matriz_esparza.h"

using namespace std;

MatrizEsparza::MatrizEsparza() : _dicc(), _filas(0), _columnas(0), _traspuesta(false) {}

MatrizEsparza::MatrizEsparza(const int n) : _dicc(), _filas(n), _columnas(n), _traspuesta(false) {}

MatrizEsparza::MatrizEsparza(const int f, const int c) : _filas(f), _columnas(c), _traspuesta(false) {}

void MatrizEsparza::swap(MatrizEsparza &o) {
    std::swap(_filas, o._filas);
    std::swap(_columnas, o._columnas);
    std::swap(_traspuesta, o._traspuesta);
    std::swap(_dicc, o._dicc);
}

double& MatrizEsparza::elem(const int i, const int j) {
    if (i < 0 || j < 0)
        throw domain_error("Los indices de fila y columna deben ser no negativos.");
    pair<int, int> pos;
    if (_traspuesta) pos = make_pair(j,i);
    else pos = make_pair(i,j);
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
    else pos = make_pair(i,j);
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
    return *this;
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

bool MatrizEsparza::esCuadrada() const {
    return filas() == columnas();
}

MatrizEsparza& MatrizEsparza::backwardSubstitution(MatrizEsparza &x, const MatrizEsparza &b) {
    if (b.filas() != filas())
        throw domain_error("La cantidad de filas de la matriz parametro debe coincidicar con la de la matriz.");
    x = MatrizEsparza(columnas(), b.columnas());
    for (int i = x.filas()-1; i >= 0; --i) {
        for (int k = 0; k < x.columnas(); ++k) {
            x.elem(i,k) = b(i,k);
            for (int j = i + 1; j < x.filas(); ++j) {
                x.elem(i,k) -= (*this)(i,j) * x(j,k);
            }
            x.elem(i,k) /= (*this)(i,i);
        }
    }
    return x;
}

MatrizEsparza& MatrizEsparza::forwardSubstitution(MatrizEsparza &x, const MatrizEsparza &b) {
    if (b.filas() != filas())
        throw domain_error("La cantidad de filas de la matriz parametro debe coincidicar con la de la matriz.");
    x = MatrizEsparza(columnas(), b.columnas());
    for (int i = 0; i < x.filas(); ++i) {
        for (int k = 0; k < x.columnas(); ++k) {
            x.elem(i,k) = b(i,k);
            for (int j = 0; j < i; ++j) {
                x.elem(i,k) -= (*this)(i,j) * x(j,k);
            }
            x.elem(i,k) /= (*this)(i,i);
        }
    }
    return x;
}

MatrizEsparza& MatrizEsparza::factorizacionCholesky(MatrizEsparza &L) const {
    if (!esCuadrada())
        throw domain_error("La matriz debe ser cuadrada.");
    int n = filas();
    L = MatrizEsparza(n);
    for (int j = 0; j < n; ++j) {
        L.elem(j,j) = (*this)(j,j);
        for (int k = 0; k < j; ++k)
            L.elem(j,j) -= pow(L(j,k), 2);
        if (leq(L(j,j), 0))
            throw domain_error("La matriz no tiene factorizacion Cholesky.");
        L.elem(j,j) = pow(L(j,j), 0.5);
        for (int i = j+1; i < n; ++i) {
            L.elem(i,j) = (*this)(i,j);
            for (int k = 0; k < j; ++k)
                L.elem(j,j) -= pow(L(i,k)*L(j,k), 2);
            L.elem(i,j) /= L(j,j);
        }
    }
    return L;
}

MatrizEsparza& MatrizEsparza::factorizacionCholeskyBanda(const int p, MatrizEsparza &L) const {
    if (!esCuadrada())
        throw domain_error("La matriz debe ser cuadrada.");
    int n = filas();
    L = MatrizEsparza(n);
    for (int j = 0; j < n; ++j) {
        L.elem(j,j) = (*this)(j,j);
        for (int k = max(0, j-p); k < j; ++k)
            L.elem(j,j) -= pow(L(j,k), 2);
        if (leq(L(j,j), 0))
            throw domain_error("La matriz no tiene factorizacion Cholesky.");
        L.elem(j,j) = pow(L(j,j), 0.5);
        for (int i = j+1; i < min(n, j+p+1); ++i) {
            L.elem(i,j) = (*this)(i,j);
            for (int k = max(0, i-p); k < j; ++k)
                L.elem(j,j) -= pow(L(i,k)*L(j,k), 2);
            L.elem(i,j) /= L(j,j);
        }
    }
    return L;
}

MatrizEsparza& MatrizEsparza::multiplicarPorTraspuestaBanda(const int p, const int q) {
    _verificarBanda(p, q);
    MatrizEsparza A(filas());
    int h = filas() <= columnas() ? filas() : min(filas(), columnas() + q);
    for (int i = 0; i < h; ++i) {
        for (int j = i; j < min(h, i+q+1); ++j) {
            A.elem(i,j) = 0;
            for (int k = max(0, max(i,j)-q); k < min(columnas(), min(i,j)+p+1); ++k)
                A.elem(i,j) += (*this)(i,k) * (*this)(j,k);
            A.elem(j,i) = A(i,j);
        }
    }
    swap(A);
    return *this;
}

void MatrizEsparza::_verificarRango(const int i, const int j) const {
    if (!(0 <= i && i < filas() && 0 <= j && j < columnas()))
        throw domain_error("Los indices de fila y/o columna estan fuera de rango.");
}

void MatrizEsparza::_verificarBanda(const int p, const int q) const {
    if (p+1 > columnas() || q+1 > filas())
        throw domain_error("La banda no puede superar la cantidad filas y columnas.");
}