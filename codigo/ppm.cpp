#include <iostream>
#include <stdexcept>
#include "ppm.h"

using namespace std;

void PPM::_cargarImagen(const string f) {
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

PPM::PPM() : _data(NULL) {}

PPM::PPM(const PPM &o) {
    _cargarImagen(o._filename);
}

PPM::PPM(const string f) {
    _cargarImagen(f);
}

PPM::~PPM() {
    delete[] _data;
}

PPM& PPM::operator=(PPM o) {
    swap(_data, o._data);
    swap(_width, o._width);
    swap(_height, o._height);
    swap(_pt, o._pt);
    return *this;
}

uint PPM::operator()(const uint i, const uint j, const uint k) {
    if(i >= _height)
        throw std::runtime_error("El direccionamiento vertical no puede ser mayor a la altura.");
    if(j >= _width)
        throw std::runtime_error("El direccionamiento horizontal no puede ser mayor al ancho.");
    if(k >= 3)
        throw std::runtime_error("El indice de color debe estar entre 0 y 2 inclusive.");
    return _data[i*_width*3 + j*3 + k];
}

const uint PPM::operator()(const uint i, const uint j, const uint k) const {
    if(i >= _height)
        throw std::runtime_error("El direccionamiento vertical no puede ser mayor a la altura.");
    if(j >= _width)
        throw std::runtime_error("El direccionamiento horizontal no puede ser mayor al ancho.");
    if(k >= 3)
        throw std::runtime_error("El indice de color debe estar entre 0 y 2 inclusive.");
    return _data[i*_width*3 + j*3 + k];
}

uchar* PPM::data() { return _data; }
const uchar* PPM::data() const { return _data; }

uint PPM::width() { return _width; }
const uint PPM::width() const { return _width; }

uint PPM::height() { return _height; }
const uint PPM::height() const { return _height; }

void PPM::guardarImagen(const string f) const {
    bool ret = SavePPMFile(f.c_str(), _data, _width, _height, _pt, NULL);
    if (!ret) {
        cout << "ERROR: no se pudo guardar el archivo" << endl;
    }
}

const double PPM::brillo(const uint i, const uint j) const {
    double suma = 0;
    for (uint k = 0; i < 3; ++k) {
        suma += (double)(*this)(i,j,k);
    }
    return suma / 3;
}

const double PPM::brilloMaximo() const {
    double max = 0;
    for (uint i = 0; i < _height; ++i) {
        for (uint j = 0; j < _width; ++j) {
            if (max < brillo(i,j))
                max = brillo(i,j);
        }
    }
    return max;
}

const vector<pair<uint, uint>> PPM::puntosMasBrillantes() const {
    double max = brilloMaximo();
    vector<pair<uint, uint>> pts;
    for (uint i = 0; i < _height; ++i) {
        for (uint j = 0; j < _width; ++j) {
            if (brillo(i,j) == max)
                pts.emplace_back(i,j);
        }
    }
    return pts;
}