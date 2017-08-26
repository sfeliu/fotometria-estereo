#ifndef __MATRIZ_H__
#define __MATRIZ_H__

#include <stdio.h>
#include <algorithm>
#include <string>
#include <cmath>
#include <stdexcept>

typedef unsigned int uint;

class Matriz {
    public:
        Matriz(const Matriz &o); // constructor por copia
        Matriz(const uint n); // matriz identidad de nxn
        Matriz(const uint f, const uint c); // matriz nula de fxn
        Matriz(const uint f, const uint c, const double a[], const uint n); // construye una matriz de fxc a partir de un arreglo de tamanio n
        ~Matriz();

        Matriz& operator=(Matriz o);
        double& operator()(const uint i, const uint j);
        const double& operator()(const uint i, const uint j) const;
        Matriz& operator*(const Matriz &o) const;

        uint filas() const;
        uint columnas() const;
        bool esCuadrada() const;
        void trasponer();

        bool eliminacionGaussiana(Matriz &b);
        bool eliminacionGaussJordan(Matriz &b);
        void permutarFila(const uint i, const uint j);
        void multiplicarFilaPorEscalar(const uint i, const double c);
        void restarMultiploDeFila(const uint i, const uint j, const double c);
        void dividirFilaPorEscalar(const uint i, const double c);
        bool invertir();

        double normaF() const;

        void print() const {
            for (uint i = 0; i < filas(); ++i) {
                for (uint j = 0; j < columnas(); ++j) {
                    printf("%.2f    ", (*this)(i,j));
                }
                printf("\n");
            }
        }

    private:
        uint _filas, _columnas;
        double **_matriz;
        bool _traspuesta;
        uint *_cols;

        void _crearMatriz(const uint f, const uint c);
        void _verificarRango(const uint f, const uint c);
};

#endif //__MATRIZ_H__