#include "matriz.h"
#include "ppm.h"
#include <sstream>
#include <iostream>
#include <fstream>

Matriz obtenerIntensidades(vector<PPM> &ppms, const int x, const int y) {
    Matriz m = Matriz(ppms.size(), 1);
    for (int i = 0; i < (int)ppms.size(); ++i) {
        m(i,0) = ppms[i].brillo(x,y);
    }
    return m;
}

int main() {
    // 1. Calibracion del sistema
    double dirs[] = {0.403259, 0.480808, 0.778592, 0.0982272, 0.163712, 0.981606, -0.0654826, 0.180077, 0.98147};
    Matriz S = Matriz(3, 3, dirs, 9);
    S.trasponer();
    S.invertir();

    vector<PPM> imgs(3);
    for (int i = 0; i < 3; ++i) {
        stringstream f;
        f << "buda/buda." << i << ".ppm";
        imgs[i].cargarImagen(f.str());
    }
    PPM mask = PPM("buda/buda.mask.ppm");
    auto m = mask.generarMascara();
    ofstream xFile, yFile, zFile;
    xFile.open("ejemplo2/normalesX.txt");
    yFile.open("ejemplo2/normalesY.txt");
    zFile.open("ejemplo2/normalesZ.txt");
    int ultimoY = mask.width();
    for (int y = m.first.y; y <= m.second.y; ++y) {
        for (int x = m.first.x; x <= m.second.x; ++x) {
            if (y > ultimoY) {
                xFile << "\n";
                yFile << "\n";
                zFile << "\n";
            }
            ultimoY = y;
            Matriz b = obtenerIntensidades(imgs, x, y);
            Matriz n = S * b;
            if (n.normaF() != 0)
                n = (1 / n.normaF()) * n;
            xFile << n(0,0) << ',';
            yFile << n(1,0) << ',';
            zFile << n(2,0) << ',';
        }
    }
    xFile.close();
    yFile.close();
    zFile.close();
    /*
    PPM mascara = PPM("mate/mate.mask.ppm");
    auto mask = mascara.generarMascara();
    for (auto it = mask->begin(); it != mask->end(); ++it) {
        mascara((*it).x, (*it).y, 0) = 255;
        mascara((*it).x, (*it).y, 1) = 0;
        mascara((*it).x, (*it).y, 2) = 0;
    }
    mascara.guardarImagen("mate2/mate.mask.ppm");
    PPM imgs[12];
    for (int i = 0; i < 12; ++i) {
        stringstream f;
        f << "mate/mate." << i << ".ppm";
        imgs[i].cargarImagen(f.str());
        imgs[i].aplicarMascara(mask);
        imgs[i].eliminarMascara();
        auto v = imgs[i].puntosMasBrillantes();
        for (int j = 0; j < v.size(); ++j) {
            imgs[i](v.at(j).x, v.at(j).y, 0) = 255;
            imgs[i](v.at(j).x, v.at(j).y, 1) = 0;
            imgs[i](v.at(j).x, v.at(j).y, 2) = 0;
        }
        stringstream o;
        o << "mate2/mate." << i << ".ppm";
        imgs[i].guardarImagen(o.str());
    }*/

    // 2. Reconstruccion del modeo 3D

    // 2.1. Construccion del campo normal

    // 2.2. Estimacion de la profundidad

    return 0;
}