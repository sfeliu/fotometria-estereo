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
        const uchar& operator()(const int i, const int j, const int k) const;

        uchar* data() const;
        int width() const;
        int height() const;
        //int sumaDeVecindad(punto p);
        //PPM::punto puntoDeMayorVecindad(vector<PPM::punto> pts);

        void cargarImagen();
        void cargarImagen(const string f);
        void guardarImagen(const string f) const;
        pair<punto, punto> generarMascara() const;
        
        double brillo(const int x, const int y) const;
        
    private:
        string _filename;
        uchar* _data;
        int _width;
        int _height;
        PPM_LOADER_PIXEL_TYPE _pt;
};