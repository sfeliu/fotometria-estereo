#ifndef __MATRIZ_H__
#define __MATRIZ_H__

#include "fputils.h"
#include <stdio.h>
#include <algorithm>
#include <string>
#include <cmath>
#include <stdexcept>

class Matriz {
    public:
        Matriz();
        Matriz(const Matriz &o); // constructor por copia
        Matriz(const int n); // matriz nula de nxn
        Matriz(const int f, const int c); // matriz nula de fxn
        Matriz(const int f, const int c, const double a[], const int n); // construye una matriz de fxc a partir de un arreglo de tamanio n
        ~Matriz();
        
        static Matriz Identidad(const int n);

        Matriz& operator=(Matriz o);
        double& operator()(const int i, const int j);
        const double& operator()(const int i, const int j) const;
        Matriz& operator*(const Matriz &o) const;
        Matriz& operator*(const double c) const;

        int filas() const;
        int columnas() const;
        bool esCuadrada() const;
        void trasponer();

        bool eliminacionGaussiana();
        bool eliminacionGaussiana(Matriz &b);
        bool eliminacionGaussJordan(Matriz &b);
        void factorizacionPLU(Matriz &P, Matriz &L, Matriz &U);
        Matriz backwardSubstitution(Matriz &b);
        Matriz forwardSubstitution(Matriz &b);
        void permutarFila(const int i, const int j);
        void multiplicarFilaPorEscalar(const int i, const double c);
        void restarMultiploDeFila(const int i, const int j, const double c);
        void dividirFilaPorEscalar(const int i, const double c);
        bool invertir();
        Matriz matrizLU();

        double normaF() const;

        void print() const {
            for (int i = 0; i < filas(); ++i) {
                for (int j = 0; j < columnas(); ++j) {
                    printf("%.8f    ", (*this)(i,j));
                }
                printf("\n");
            }
        }

    private:
        int _filas, _columnas;
        double **_matriz;
        bool _traspuesta;
        int *_cols;

        void _crearMatriz(const int f, const int c);
        void _verificarRango(const int f, const int c) const;
        bool _eliminacionGaussiana(Matriz *b); // devuelve true si la matriz es no singular
};

Matriz& operator*(const double c, const Matriz &m);

#endif //__MATRIZ_H__