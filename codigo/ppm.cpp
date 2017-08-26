#include <iostream>
#include <stdexcept>
#include "ppm.h"

using namespace std;

void PPM::_cargarImagen(const string f) {
    _data = NULL;
    _width = 0;
    _height = 0;
    _pt = PPM_LOADER_PIXEL_TYPE_INVALID;
    bool cargado = LoadPPMFile(&_data, (int*)&_width, (int*)&_height, &_pt, f.c_str());
    if (!cargado || _width == 0 || _height == 0/* || _pt! = PPM_LOADER_PIXEL_TYPE_RGB_8B*/) {
        throw std::runtime_error("Fallo al leer la imagen.");
    }
}

PPM::PPM() {
    cout << "Ingrese la ruta de la imagen: ";
    string f;
    cin >> f;
    _cargarImagen(f);
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