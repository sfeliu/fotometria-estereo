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
        uchar& operator()(const uint i, const uint j, const uint k) const;

        uchar* data() const;
        uint width() const;
        uint height() const;

        void cargarImagen();
        void cargarImagen(const string f);
        void guardarImagen(const string f) const;
        vector<punto> generarMascara() const;
        void aplicarMascara(vector<punto> *m);
        void eliminarMascara();
        bool enmascarado() const;
        
        double brillo(const uint i, const uint j) const;
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
        
        bool inicio();
        bool fin();
        double brillo();
        
    private:
        PPM* _ppm;
        punto _pos;
        uint _indice;
};