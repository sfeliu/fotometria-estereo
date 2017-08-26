#include <string>
#include <vector>
#include <algorithm>
#include "ppmloader.h"

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;

class PPM {
    public:
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
        
        double brillo(const uint i, const uint j) const;
        double brilloMaximo() const;
        vector<pair<uint, uint>> puntosMasBrillantes() const;

    private:
        string _filename;
        uchar* _data;
        uint _width;
        uint _height;
        PPM_LOADER_PIXEL_TYPE _pt;
};