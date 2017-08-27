#include <string>
#include <vector>
#include <algorithm>
#include "ppmloader.h"

using namespace std;

typedef unsigned char uchar;

class PPM {
    public:
        struct punto {
            punto() : x(0), y(0) {};
            punto(const int x, const int y) : x(x), y(y) {}
            int x, y;
        };
        
        PPM();
        PPM(const PPM &o);
        PPM(const string f);
        ~PPM();

        PPM& operator=(PPM o);
        uchar& operator()(const int i, const int j, const int k);

        uchar* data();
        int width();
        int height();

        void cargarImagen();
        void cargarImagen(const string f);
        void guardarImagen(const string f);
        vector<punto>* generarMascara();
        void aplicarMascara(vector<punto> *m);
        void eliminarMascara();
        bool enmascarado();
        
        double brillo(const int x, const int y);
        double brilloMaximo();
        vector<punto> puntosMasBrillantes();
        
        class iterador;
        iterador it();

    private:
        string _filename;
        uchar* _data;
        int _width;
        int _height;
        PPM_LOADER_PIXEL_TYPE _pt;
        vector<punto>* _mascara;
};

class PPM::iterador {
    public:
        iterador(PPM *ppm);
        
        punto pos();
        
        uchar& operator[](const int k);
        void operator++();
        void operator--();
        
        bool hayAnterior();
        bool haySiguiente();
        double brillo();
        
    private:
        PPM* _ppm;
        punto _pos;
        int _indMasc;
};