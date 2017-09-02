#include "matriz.h"
#include "ppm.h"
#include <sstream>
#include <iostream>
#include <fstream>

int sumaDeVecindad(const PPM &ppm, PPM::punto p){
	int resultado = 0;
	for(int i = -1; i < 2; i++){
		resultado = resultado + ppm.intensidad(p.x+i, p.y);//((*this)(x+i,y,0) + (*this)(x+i,y,1) + (*this)(x+i,y,2));
		for(int j = -1; j < 2; j++){
			resultado = resultado + ppm.intensidad(p.x, p.y+j);//((*this)(x,y+j,0) + (*this)(x,y+j,1) + (*this)(x,y+j,2))
		}
	}
	return resultado;
}


PPM::punto puntoDeMayorVecindad(const PPM &ppm ,vector<PPM::punto> pts){
    PPM::punto res = pts[0];
    for(int i = 1; i < pts.size(); i++){
        if(sumaDeVecindad(ppm,res) < sumaDeVecindad(ppm, pts[i]) ){
            res = pts[i];
        }
    }
    return res;
}


PPM::punto puntoDeMayorIntensidad(const PPM &ppm, pair<PPM::punto, PPM::punto> masc) {
    vector<PPM::punto> pts;
    pts.push_back(masc.first); // inserto un primer punto para simplificar el algoritmo que sigue
    int sigPos = 1; // posicion del vector para insertar el siguiente punto
    double intensidadMax = -1;
    // Recorro la imagen (usando la mascara) y voy guardando los puntos de mayor intensidad
    for (int y = masc.first.y; y < masc.second.y; ++y) {
        for (int x = masc.first.x; x < masc.second.x; ++x) {
            double intensidad = ppm.intensidadEnVecindad(x, y, 4);
            //double intensidad = ppm.intensidad(x, y);
            if (intensidadMax == intensidad) {
                // Si la siguiente posicion esta definida, le asigno el valor directamente
                // Si no, hago push back
                if (sigPos < (int)pts.size())
                    pts[sigPos] = PPM::punto(x,y);
                else
                    pts.push_back(PPM::punto(x,y));
                ++sigPos;
            } else if (intensidadMax < intensidad) {
                // "Vacio" el vector y pongo al punto como primer elemento
                pts[0] = PPM::punto(x,y);
                sigPos = 1;
                intensidadMax = intensidad;
            }
        }
    }
    // Si hay un unico punto lo devuelvo
    // Si no, elijo uno
    if (sigPos == 1) {
        return pts[0];
    } else {
        printf("%d\n", sigPos);
        return puntoDeMayorVecindad(ppm, pts);
    }
}

void conseguir_Todas_Posibilidades(){
    std::vector< Matriz > filas;
    double fila0[3] = {0.403259,0.480808,0.778592};
    Matriz f0(1,3,fila0,3);
    filas.push_back(f0);
    double fila1[3] = {0.0982272,0.163712,0.981606};
    Matriz f1(1,3,fila1,3);
    filas.push_back(f1);
    double fila2[3] = {-0.0654826,0.180077,0.98147};
    Matriz f2(1,3,fila2,3);
    filas.push_back(f2);
    double fila3[3] = {-0.127999,0.431998,0.892745};
    Matriz f3(1,3,fila3,3);
    filas.push_back(f3);
    double fila4[3] = {-0.328606,0.485085,0.810377};
    Matriz f4(1,3,fila4,3);
    filas.push_back(f4);
    double fila5[3] = {-0.110339,0.53593,0.837021};
    Matriz f5(1,3,fila5,3);
    filas.push_back(f5);
    double fila6[3] = {0.239071,0.41439,0.878138};
    Matriz f6(1,3,fila6,3);
    filas.push_back(f6);
    double fila7[3] = {0.0642302,0.417497,0.906406};
    Matriz f7(1,3,fila7,3);
    filas.push_back(f7);
    double fila8[3] = {0.12931,0.339438,0.931698};
    Matriz f8(1,3,fila8,3);
    filas.push_back(f8);
    double fila9[3] = {0.0323953,0.340151,0.939813};
    Matriz f9(1,3,fila9,3);
    filas.push_back(f9);
    double fila10[3] = {0.0985318,0.0492659,0.993914};
    Matriz f10(1,3,fila10,3);
    filas.push_back(f10);
    double fila11[3] = {-0.16119,0.354617,0.921013};
    Matriz f11(1,3,fila11,3);
    filas.push_back(f11);
    ofstream todas;
    vector<double> numeros_condicion;
    todas.open("todas_las_matrices.txt");
    for (uint i=0; i<10; ++i){
        for (uint j=i+1; j<11; ++j){
            for (uint k=j+1; k<12; ++k){
                //  todas << "F1 " << filas.at(i)(0,0) << " , " << filas.at(i)(0,1) << " , " << filas.at(i)(0,2) << "\n";
                //todas << "F2 " << filas.at(j)(0,0) << " , " << filas.at(i)(0,1) << " , " << filas.at(i)(0,2) << "\n";
                //  todas << "F3 " << filas.at(k)(0,0) << " , " << filas.at(i)(0,1) << " , " << filas.at(i)(0,2) << "\n\n";
                todas << filas.at(i)(0,0) << ',' << filas.at(i)(0,1) << ',' << filas.at(i)(0,2) << ',';
                todas << filas.at(j)(0,0) << ',' << filas.at(i)(0,1) << ',' << filas.at(i)(0,2) << ',';
                todas << filas.at(k)(0,0) << ',' << filas.at(i)(0,1) << ',' << filas.at(i)(0,2) << "\n";

            }
        }
    }
    todas.close();
}

Matriz matrizDeIntensidades(const vector<PPM> &ppms, const int x, const int y) {
    Matriz m = Matriz(ppms.size(), 1);
    for (int i = 0; i < (int)ppms.size(); ++i) {
        m(i,0) = ppms[i].intensidad(x,y);
    }
    return m;
}

int main() {
    // 1. Calibracion del sistema
    /*double a[] = {0.403259, 0.480808, 0.778592, -0.328606, 0.485085, 0.810377, 0.0985318, 0.0492659, 0.993914};
    Matriz A(3, 3, a, 9);
    A.trasponer();
    auto invA = A;
    invA.invertir();
    double condA = A.normaF()*invA.normaF();
    printf("%f\n", condA);

    double b[] = {-0.127999, 0.431998, 0.892745, -0.328606, 0.485085, 0.810377, 0.12931, 0.339438, 0.931698};
    Matriz B(3, 3, b, 9);
    B.trasponer();
    auto invB = B;
    invB.invertir();
    double condB = B.normaF()*invB.normaF();
    printf("%f\n", condB);*/

    // 1.1. Obtenencion de direcciones de iluminacion

    // Test de puntos de maxima intensidad
    PPM mate_mask_ppm = PPM("cromada/cromada.mask.ppm");
    PPM mates[12];
    PPM::punto pts[12];
    auto mate_masc = mate_mask_ppm.generarMascara();
    for (int i = 0; i < 12; ++i) {
        stringstream f;
        f << "cromada/cromada." << i << ".ppm";
        mates[i].cargarImagen(f.str());
        auto pt = puntoDeMayorIntensidad(mates[i], mate_masc);
        pts[i] = pt;
        mates[i](pt.x, pt.y, 0) = 255;
        mates[i](pt.x, pt.y, 1) = 0;
        mates[i](pt.x, pt.y, 2) = 0;
        stringstream o;
        o << "cromada2/cromada." << i << ".ppm";
        mates[i].guardarImagen(o.str());
    }
    double dirs[12][3];
    // 1.2. Obtencion de coordenadas z
    int r = (mate_masc.second.x - mate_masc.first.x + 1) / 2; // radio de la esfera
    PPM::punto c(mate_masc.first.x + r - 1, mate_masc.first.y + r - 1); // centro de la esfera
    mate_mask_ppm.guardarImagen("cromada2/cromada.mask.ppm");
    ofstream luces;
    luces.open("luces.txt");
    for (int i = 0; i < 12; ++i) {
        double x = pts[i].x - c.x;
        double y = pts[i].y - c.y;
        double z = pow(pow(r, 2) - pow(x, 2) - pow(y, 2), 0.5) / r;
        x /= r;
        y /= r;
        luces << x << ' ' << y << ' ' << z << "\n";
        dirs[i][0] = x;
        dirs[i][1] = y;
        dirs[i][2] = z;
    }
    luces.close();

    // Test de normales
    {
        //double dirs[] = {0.403259, 0.480808, 0.778592, -0.328606, 0.485085, 0.810377, 0.0985318, 0.0492659, 0.993914}; // 0, 4, 10
        //double dirs[] = {0.403259, 0.480808, 0.778592, 0.0982272, 0.163712, 0.981606, -0.0654826, 0.180077, 0.98147}; // 0, 1, 2
        Matriz S = Matriz(3, 3);
        S(0,0) = dirs[0][0]; S(0,1) = dirs[0][1]; S(0, 2) = dirs[0][2];
        S(1,0) = dirs[1][0]; S(1,1) = dirs[1][1]; S(1, 2) = dirs[1][2];
        S(2,0) = dirs[2][0]; S(2,1) = dirs[2][1]; S(2, 2) = dirs[2][2];
        //Matriz S = Matriz(3, 3, dirs, 9);
        //S.trasponer();
        S.invertir();

        vector<PPM> imgs(3);
        PPM asd = PPM("caballo/caballo.0.ppm");
        imgs[0].cargarImagen("caballo/caballo.0.ppm");
        imgs[1].cargarImagen("caballo/caballo.4.ppm");
        imgs[2].cargarImagen("caballo/caballo.10.ppm");
        PPM mask = PPM("caballo/caballo.mask.ppm");
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
                Matriz b = matrizDeIntensidades(imgs, x, y);
                Matriz n = S * b;
                if (n(0,0) + n(1,0) + n(2,0) != 0)
                    n = (1 / n.normaF()) * n;
                xFile << n(0,0) << ',';
                yFile << n(1,0) << ',';
                zFile << n(2,0) << ',';
            }
        }
        xFile.close();
        yFile.close();
        zFile.close();
    }

    // 2. Reconstruccion del modeo 3D

    // 2.1. Construccion del campo normal

    // 2.2. Estimacion de la profundidad

    return 0;
}