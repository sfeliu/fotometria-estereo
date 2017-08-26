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
    swap(_data, o._data);
    swap(_width, o._width);
    swap(_height, o._height);
    swap(_pt, o._pt);
    return *this;
}

uchar& PPM::operator()(const uint i, const uint j, const uint k) {
    if(i >= _height)
        throw std::runtime_error("El direccionamiento vertical no puede ser mayor a la altura.");
    if(j >= _width)
        throw std::runtime_error("El direccionamiento horizontal no puede ser mayor al ancho.");
    if(k >= 3)
        throw std::runtime_error("El indice de color debe estar entre 0 y 2 inclusive.");
    return _data[i*_width*3 + j*3 + k];
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

vector<PPM::punto> PPM::generarMascara() {
    vector<PPM::punto> mascara;
    for (uint i = 0; i < _height; ++i) {
        for (uint j = 0; j < _width; ++j) {
            if (brillo(i,j) != 0)
                mascara.emplace_back(i,j);
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

double PPM::brillo(const uint i, const uint j) {
    return ((*this)(i,j,0) + (*this)(i,j,1) + (*this)(i,j,2)) / 3;
}

double PPM::brilloMaximo() {
    double max = 0;
    for (PPM::iterador it = this->it(); !it.fin(); ++it) {
        if (max < it.brillo())
            max = it.brillo();
    }
    return max;
}

vector<PPM::punto> PPM::puntosMasBrillantes() {
    double max = brilloMaximo();
    vector<PPM::punto> pts;
    for (PPM::iterador it = this->it(); !it.fin(); ++it) {
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

PPM::iterador::iterador(PPM *ppm) : _ppm(ppm), _indice(0) {
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
        _pos = _ppm->_mascara->at(++_indice);
    } else {
        _pos.y = (_pos.y+1) % _ppm->width();
        if (_pos.y == 0) ++_pos.x;
    }
}

void PPM::iterador::operator--() {
    if (_ppm->enmascarado()) {
        _pos = _ppm->_mascara->at(--_indice);
    } else {
        _pos.y = _pos.y == 0 ? _ppm->width()-1 : _pos.y-1;
        if (_pos.y == _ppm->width()-1) --_pos.x;
    }
}

bool PPM::iterador::inicio() {
    return _ppm->enmascarado() ? _indice == 0 : _pos.x == 0 && _pos.y == 0;
}

bool PPM::iterador::fin() {
    return _ppm->enmascarado()
        ? _indice == _ppm->_mascara->size()-1
        : _pos.x == _ppm->height()-1 && _pos.y == _ppm->width()-1;
}

double PPM::iterador::brillo() {
    return _ppm->brillo(_pos.x, _pos.y);
}