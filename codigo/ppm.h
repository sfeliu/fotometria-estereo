#include <string>
#include <vector>
#include <algorithm>
#include "ppmloader.h"

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;

class PPM {
    public:
        struct punto {
            punto() : x(0), y(0) {};
            punto(const uint x, const uint y) : x(x), y(y) {}
            uint x, y;
        };
        
        PPM();
        PPM(const PPM &o);
        PPM(const string f);
        ~PPM();

        PPM& operator=(PPM o);
        uchar& operator()(const uint i, const uint j, const uint k);

        uchar* data();
        uint width();
        uint height();

        void cargarImagen();
        void cargarImagen(const string f);
        void guardarImagen(const string f);
        vector<punto> generarMascara();
        void aplicarMascara(vector<punto> *m);
        void eliminarMascara();
        bool enmascarado();
        
        double brillo(const uint x, const uint y);
        double brilloMaximo();
        vector<punto> puntosMasBrillantes();
        
        class iterador;
        iterador it();

    private:
        string _filename;
        uchar* _data;
        uint _width;
        uint _height;
        PPM_LOADER_PIXEL_TYPE _pt;
        vector<punto>* _mascara;
};

class PPM::iterador {
    public:
        iterador(PPM *ppm);
        
        punto pos();
        
        uchar& operator[](const uint k);
        void operator++();
        void operator--();
        
        bool hayAnterior();
        bool haySiguiente();
        double brillo();
        
    private:
        PPM* _ppm;
        punto _pos;
        uint _indice;
};