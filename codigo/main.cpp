#include "matriz.h"
#include "ppm.h"
#include <sstream>
#include <iostream>
#include <fstream>

Matriz computarIntensidades(PPM ppms[], const uint n, const uint f, const uint c) {
    double intensidades[n];
    for (uint i = 0; i < n; ++i) {
        intensidades[i] = ppms[i].brillo(f,c);
    }
    Matriz m = Matriz(n, 1, intensidades, n);
    return m;
}

int main() {
    // 1. Calibracion del sistema
    double dirs[] = {0.403259, 0.480808, 0.778592, 0.0982272, 0.163712, 0.981606, -0.0654826, 0.180077, 0.98147};
    Matriz S = Matriz(3, 3, dirs, 9);
    S.trasponer();
    S.invertir();

    PPM imgs[3];
    for (uint i = 0; i < 3; ++i) {
        stringstream f;
        f << "/Users/pablo2martin/MetNum/Metodos_TP1/codigo/buda/buda." << i << ".ppm";
        imgs[i].cargarImagen(f.str());
    }
    ofstream x, y, z;
    x.open("normalesX");
    y.open("normalesY");
    z.open("normalesZ");
    for (uint i = 0; i < imgs[0].width(); ++i) {
        for (uint j = 0; j < imgs[0].height(); ++j) {
            Matriz b = computarIntensidades(imgs, 3, i, j);
            Matriz m = S * b;
            if (m.normaF() != 0)
                m = (1 / m.normaF()) * m;
            x << m(0,0) << ',';
            y << m(1,0) << ',';
            z << m(2,0) << ',';
            if (j == imgs[0].height()-1)
                x << "\n";
        }
    }
    x.close();
    y.close();
    z.close();
    
    /*PPM mascara = PPM("/Users/pablo2martin/MetNum/Metodos_TP1/codigo/mate/mate.mask.ppm");
    auto mask = mascara.generarMascara();
    for (auto it = mask.begin(); it != mask.end(); ++it) {
        mascara((*it).x, (*it).y, 0) = 255;
        mascara((*it).x, (*it).y, 1) = 0;
        mascara((*it).x, (*it).y, 2) = 0;
    }
    mascara.guardarImagen("/Users/pablo2martin/MetNum/Metodos_TP1/codigo/mate2/mate.mask.ppm");
    PPM imgs[12];
    for (int i = 0; i < 12; ++i) {
        stringstream f;
        f << "/Users/pablo2martin/MetNum/Metodos_TP1/codigo/mate/mate." << i << ".ppm";
        imgs[i].cargarImagen(f.str());
        imgs[i].aplicarMascara(&mask);
        imgs[i].eliminarMascara();
        auto v = imgs[i].puntosMasBrillantes();
        for (uint j = 0; j < v.size(); ++j) {
            imgs[i](v.at(j).x, v.at(j).y, 0) = 255;
            imgs[i](v.at(j).x, v.at(j).y, 1) = 0;
            imgs[i](v.at(j).x, v.at(j).y, 2) = 0;
        }
        stringstream o;
        o << "/Users/pablo2martin/MetNum/Metodos_TP1/codigo/mate2/mate." << i << ".ppm";
        imgs[i].guardarImagen(o.str());
    }*/

    // 2. Reconstruccion del modeo 3D

    // 2.1. Construccion del campo normal

    // 2.2. Estimacion de la profundidad

    return 0;
}