#include <iostream>
#include <stdexcept>
#include "ppm.h"

using namespace std;

PPM::PPM() : _data(NULL) {}

PPM::PPM(const PPM &o) {
    cargarImagen(o._filename);
}

PPM::PPM(const string f) {
    cargarImagen(f);
}

PPM::~PPM() {
    delete[] _data;
}

PPM& PPM::operator=(PPM o) {
    swap(_filename, o._filename);
    swap(_data, o._data);
    swap(_width, o._width);
    swap(_height, o._height);
    swap(_pt, o._pt);
    return *this;
}

uchar& PPM::operator()(const int x, const int y, const int k) {
    if(y >= height())
        throw std::runtime_error("El direccionamiento vertical no puede ser mayor a la altura.");
    if(x >= width())
        throw std::runtime_error("El direccionamiento horizontal no puede ser mayor al ancho.");
    if(k >= 3)
        throw std::runtime_error("El indice de color debe estar entre 0 y 2 inclusive.");
    return _data[y*_width*3 + x*3 + k];
}

const uchar& PPM::operator()(const int x, const int y, const int k) const {
    if(y >= height())
        throw std::runtime_error("El direccionamiento vertical no puede ser mayor a la altura.");
    if(x >= width())
        throw std::runtime_error("El direccionamiento horizontal no puede ser mayor al ancho.");
    if(k >= 3)
        throw std::runtime_error("El indice de color debe estar entre 0 y 2 inclusive.");
    return _data[y*_width*3 + x*3 + k];
}

uchar* PPM::data() const { return _data; }

int PPM::width() const { return _width; }

int PPM::height() const { return _height; }

void PPM::cargarImagen() {
    string f;
    cin >> f;
    cargarImagen(f);
}

void PPM::cargarImagen(const string f) {
    _filename = f;
    _data = NULL;
    _width = 0;
    _height = 0;
    _pt = PPM_LOADER_PIXEL_TYPE_INVALID;
    bool cargado = LoadPPMFile(&_data, (int*)&_width, (int*)&_height, &_pt, f.c_str());
    if (!cargado || _width == 0 || _height == 0/* || _pt! = PPM_LOADER_PIXEL_TYPE_RGB_8B*/) {
        throw std::runtime_error("Fallo al leer la imagen.");
    }
}

void PPM::guardarImagen(const string f) const {
    bool ret = SavePPMFile(f.c_str(), _data, _width, _height, _pt, NULL);
    if (!ret) {
        cout << "ERROR: no se pudo guardar el archivo" << endl;
    }
}


pair<PPM::punto, PPM::punto> PPM::generarMascara() const {
    int y_t, y_b, x_l, x_r;
    // Busco borde superior
    for (y_t = 0; y_t < height(); ++y_t) {
        for (int x = 0; x < width(); ++x) {
            if (intensidad(x,y_t) != 0)
                goto __listo_y_t;
        }
    }
    __listo_y_t:;
    // Busco borde inferior
    for (y_b = height()-1; 0 <= y_b; --y_b) {
        for (int x = 0; x < width(); ++x) {
            if (intensidad(x,y_b) != 0)
                goto __listo_y_b;
        }
    }
    __listo_y_b:;
    // Busco borde izquierdo
    for (x_l = 0; x_l < width(); ++x_l) {
        for (int y = 0; y < height(); ++y) {
            if (intensidad(x_l,y) != 0)
                goto __listo_x_l;
        }
    }
    __listo_x_l:;
    // Busco borde derecho
    for (x_r = width()-1; 0 <= x_r; --x_r) {
        for (int y = 0; y < height(); ++y) {
            if (intensidad(x_r,y) != 0)
                goto __listo_x_r;
        }
    }
    __listo_x_r:;
    if (y_b < 0) // todos los puntos tienen intensidad cero
        return make_pair(punto(0, 0), punto(width()-1, height()-1));
    else
        return make_pair(punto(x_l, y_t), punto(x_r, y_b));
}

double PPM::intensidad(const int x, const int y) const {
    return 0.299*(*this)(x,y,0) + 0.587*(*this)(x,y,1) + 0.114*(*this)(x,y,2);
}

double PPM::intensidadEnVecindad(const int x, const int y, const int grado) const {
    double suma = 0;
    int cuenta = 0;
    for (int ix = max(0, x - grado - 1); ix <= min(width()-1, x + grado); ++ix) {
        for (int iy = max(0, y - grado - 1); iy <= min(height()-1, y + grado); ++iy) {
            suma += intensidad(ix, iy);
            ++cuenta;
            //printf("(%d, %d) ", ix, iy);
        }
        //printf("\n");
    }
    if (cuenta == 0)  printf("aaaaaaaaaaaaaaaaaaaa\n");
        //printf("\n");
    return suma/cuenta;
}