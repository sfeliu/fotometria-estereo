#include <iostream>
#include <stdexcept>
#include "ppm.h"

using namespace std;

PPM::PPM() : _data(NULL), _mascara(NULL) {}

PPM::PPM(const PPM &o) {
    cargarImagen(o._filename);
    _mascara = o._mascara;
}

PPM::PPM(const string f) : _mascara(NULL) {
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
    swap(_mascara, o._mascara);
    return *this;
}

uchar& PPM::operator()(const uint x, const uint y, const uint k) {
    if(y >= height())
        throw std::runtime_error("El direccionamiento vertical no puede ser mayor a la altura.");
    if(x >= width())
        throw std::runtime_error("El direccionamiento horizontal no puede ser mayor al ancho.");
    if(k >= 3)
        throw std::runtime_error("El indice de color debe estar entre 0 y 2 inclusive.");
    return _data[y*_width*3 + x*3 + k];
}

uchar* PPM::data() { return _data; }

uint PPM::width() { return _width; }

uint PPM::height() { return _height; }

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

void PPM::guardarImagen(const string f) {
    bool ret = SavePPMFile(f.c_str(), _data, _width, _height, _pt, NULL);
    if (!ret) {
        cout << "ERROR: no se pudo guardar el archivo" << endl;
    }
}

vector<PPM::punto>* PPM::generarMascara() {
    uint y_t, y_b, x_l, x_r;
    // Busco borde superior
    for (y_t = 0; y_t < height(); ++y_t) {
        for (uint x = 0; x < width(); ++x) {
            if (brillo(x,y_t) != 0)
                goto __listo_y_t;
        }
    }
    __listo_y_t:;
    // Busco borde inferior
    for (y_b = height()-1; 0 <= (int)y_b; --y_b) {
        for (uint x = 0; x < width(); ++x) {
            if (brillo(x,y_b) != 0)
                goto __listo_y_b;
        }
    }
    __listo_y_b:;
    // Busco borde izquierdo
    for (x_l = 0; x_l < width(); ++x_l) {
        for (uint y = 0; y < height(); ++y) {
            if (brillo(x_l,y) != 0)
                goto __listo_x_l;
        }
    }
    __listo_x_l:;
    // Busco borde derecho
    for (x_r = width()-1; 0 <= (int)x_r; --x_r) {
        for (uint y = 0; y < height(); ++y) {
            if (brillo(x_r,y) != 0)
                goto __listo_x_r;
        }
    }
    __listo_x_r:;
    if (y_b < 0) return NULL; // todos los puntos tienen brillo cero
    vector<punto> *mascara = new vector<punto>[(x_r - x_l + 1)*(y_b - y_t + 1)];
    for (int y = y_t; y <= y_b; ++y) {
        for (int x = x_l; x <= x_r; ++x) {
            mascara->emplace_back(x,y);
        }
    }
    return mascara;
}

void PPM::aplicarMascara(vector<punto> *m) {
    _mascara = m;
}

void PPM::eliminarMascara() {
    _mascara = NULL;
}

bool PPM::enmascarado() {
    return _mascara != NULL;
}

double PPM::brillo(const uint x, const uint y) {
    return ((*this)(x,y,0) + (*this)(x,y,1) + (*this)(x,y,2)) / 3;
}

double PPM::brilloMaximo() {
    double max = 0;
    for (PPM::iterador it = this->it(); it.haySiguiente(); ++it) {
        if (max < it.brillo())
            max = it.brillo();
    }
    return max;
}

vector<PPM::punto> PPM::puntosMasBrillantes() {
    double max = brilloMaximo();
    vector<PPM::punto> pts;
    for (PPM::iterador it = this->it(); it.haySiguiente(); ++it) {
        if ((int)it.brillo() == (int)max)
            pts.push_back(it.pos());
    }
    return pts;
}

PPM::iterador PPM::it() {
    return iterador(this);
}

PPM::punto PPM::iterador::pos() {
    return _pos;
}

PPM::iterador::iterador(PPM *ppm) : _ppm(ppm), _indMasc(0) {
    if (_ppm->enmascarado())
        _pos = _ppm->_mascara->at(0);
    else
        _pos.x = _pos.y = 0;
}

uchar& PPM::iterador::operator[](const uint k) {
    return (*_ppm)(_pos.x, _pos.y, k);
}

void PPM::iterador::operator++() {
    if (_ppm->enmascarado()) {
        _pos = _ppm->_mascara->at(++_indMasc);
    } else {
        _pos.x = (_pos.x+1) % _ppm->width();
        if (_pos.x == 0) ++_pos.y;
    }
}

void PPM::iterador::operator--() {
    if (_ppm->enmascarado()) {
        _pos = _ppm->_mascara->at(--_indMasc);
    } else {
        _pos.x = _pos.x == 0 ? _ppm->width()-1 : _pos.x-1;
        if (_pos.x == _ppm->width()-1) --_pos.y;
    }
}

bool PPM::iterador::hayAnterior() {
    return _ppm->enmascarado() ? _indMasc > 0 : !(_pos.x == 0 && _pos.y == 0);
}

bool PPM::iterador::haySiguiente() {
    return _ppm->enmascarado()
        ? _indMasc < _ppm->_mascara->size()
        : _pos.x < _ppm->width() && _pos.y < _ppm->height();
}

double PPM::iterador::brillo() {
    return _ppm->brillo(_pos.x, _pos.y);
}