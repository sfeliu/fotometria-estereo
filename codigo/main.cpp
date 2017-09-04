#include "matriz.h"
#include "ppm.h"
#include "fputils.h"
//#include "utils.h"
//#include "chol_alu.h"
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

double random01(){
    return ((double) rand() / RAND_MAX);
}

Matriz randomMatriz(int n){
    int tamano = n*n;
    double matrizRandom[tamano];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            matrizRandom[i+j] = random01();
        }
    }
    Matriz r(n,n,matrizRandom,tamano);
    return r;
}

PPM::punto puntoDeMayorIntensidad(const PPM &ppm, pair<PPM::punto, PPM::punto> mask) {
    vector<PPM::punto> pts;
    pts.push_back(mask.first); // inserto un primer punto para simplificar el algoritmo que sigue
    int sigPos = 1; // posicion del vector para insertar el siguiente punto
    double intensidadMax = -1;
    // Recorro la imagen (usando la maskara) y voy guardando los puntos de mayor intensidad
    for (int y = mask.first.y; y < mask.second.y; ++y) {
        for (int x = mask.first.x; x < mask.second.x; ++x) {
            double intensidad = ppm.intensidadEnVecindad(x, y, 4);
            //double intensidad = ppm.intensidad(x, y);
            if (eq(intensidadMax, intensidad)) {
                // Si la siguiente posicion esta definida, le asigno el valor directamente
                // Si no, hago push back
                if (sigPos < (int)pts.size())
                    pts[sigPos] = PPM::punto(x,y);
                else
                    pts.push_back(PPM::punto(x,y));
                ++sigPos;
            } else if (lt(intensidadMax, intensidad)) {
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
        return pts[0];
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
    /*Matriz random = randomMatriz(1000);
    Matriz b(1000);
    clock_t start = clock();
    random.eliminacionGaussJordan(b);
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
    return 0;*/
    
    // 1. Calibracion del sistema
    
    ifstream calibracion_in("calibracion.txt");
    vector<Matriz> dirsI;
    if (calibracion_in.is_open()) {
        int dirs_cant;
        calibracion_in >> dirs_cant;
        for (int k = 0; k < dirs_cant; ++k) {
            dirsI.push_back(Matriz(3, 1));
            for (int i = 0; i < 3; ++i)
                calibracion_in >> dirsI[k](i,0);
        }
        calibracion_in.close();
    } else {

    // 1.1. Lectura de imagenes mate
    cout << "Calibracion del sistema" << endl;
    cout << "Ingrese el archivo de texto de rutas del modelo mate: ";
    string mate_src_path;
    //cin >> mate_src_path;
    mate_src_path = "mate.txt"; cout << endl;
    ifstream mate_src(mate_src_path);
    if (!mate_src.is_open()) throw runtime_error("ERROR: no se pudo abrir el archivo");
    int mate_cant;
    mate_src >> mate_cant; // leo la cantidad de imagenes que no son mascara
    mate_src.ignore(numeric_limits<std::streamsize>::max(), '\n'); // voy hasta la proxima linea
    vector<PPM> mate(mate_cant);
    PPM mate_mask;
    {
        string ruta;
        for (int i = 0; i < mate_cant; ++i) {
            getline(mate_src, ruta);
            mate[i].cargarImagen(ruta);
        }
        mate_mask.cargarImagen(ruta);
    }
    
    // 1.2. Obtenencion de direcciones de iluminacion
    pair<PPM::punto, PPM::punto> mate_mask_pts = mate_mask.generarMascara(); // obtengo puntos de la mascara
    int radio = (mate_mask_pts.second.x - mate_mask_pts.first.x + 1) / 2; // radio de la esfera
    PPM::punto centro(mate_mask_pts.first.x + radio - 1, mate_mask_pts.first.y + radio - 1); // centro de la esfera
    ofstream calibracion_out;
    calibracion_out.open("calibracion.txt");
    calibracion_out << mate_cant << '\n';
    for (int i = 0; i < mate_cant; ++i) {
        PPM::punto pt = puntoDeMayorIntensidad(mate[i], mate_mask_pts);
        dirsI.push_back(Matriz(3,1));
        dirsI[i](0,0) = pt.x - centro.x; // coordenada x
        dirsI[i](1,0) = pt.y - centro.y; // coordenada y
        dirsI[i](2,0) = pow(pow(radio, 2) - pow(dirsI[i](0,0), 2) - pow(dirsI[i](1,0), 2), 0.5); // coordenada z
        dirsI[i] = dirsI[i] * (1 / (double)radio); // normalizo el vector
        calibracion_out << dirsI[i](0,0) << ' ';
        calibracion_out << dirsI[i](1,0) << ' ';
        calibracion_out << dirsI[i](2,0) << '\n';
    }
    calibracion_out.close();

    }
    // 2. Reconstruccion del modelo 3D
    
    // 2.1. Eleccion de direcciones de iluminacion
    int elecDirsI[4] = {0, 4, 10}; // menor numero de condición
    //int elecDirsI[4] = {3, 4, 8}; // mayor numero de condición
    Matriz S(3); // matriz de direcciones de iluminacion
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            S(i,j) = dirsI[elecDirsI[i]](j,0);
        }
    }
    
    // 2.2. Lectura de imagenes del modelo a reconstruir
    cout << "Reconstruccion del modelo 3D" << endl;
    cout << "Ingrese el archivo de texto de rutas del modelo a reconstruir: ";
    string modelo_src_path;
    //cin >> modelo_src_path;
    modelo_src_path = "caballo.txt"; cout << endl;
    ifstream modelo_src(modelo_src_path);
    if (!modelo_src.is_open()) throw runtime_error("ERROR: no se pudo abrir el archivo");
    vector<PPM> modelo(3);
    PPM modelo_mask;
    {
        int modelo_cant;
        modelo_src >> modelo_cant; // leo la cantidad de imagenes que no son mascara
        modelo_src.ignore(numeric_limits<std::streamsize>::max(), '\n'); // voy hasta la proxima linea
        int j = 0;
        string ruta;
        // Leo imagenes que corresponden a las direcciones de luz elegidas unicamente
        for (int i = 0; i <= modelo_cant; ++i) {
            getline(modelo_src, ruta);
            if (j < 3 && i == elecDirsI[j]) {
                modelo[j].cargarImagen(ruta);
                ++j;
            }
        }
        modelo_mask.cargarImagen(ruta); // cargar mascara
    }
    
    // 2.3. Construccion del campo normal y estimacion de profundidades
    
    pair<PPM::punto, PPM::punto> modelo_mask_pts = modelo_mask.generarMascara(); // obtengo puntos de la mascara
    
    // Creo archivos de texto para guardar los datos
    ofstream normales_x, normales_y, normales_z;
    normales_x.open("ejemplo2/normalesX.txt");
    normales_y.open("ejemplo2/normalesY.txt");
    normales_z.open("ejemplo2/normalesZ.txt");
    
    // Datos para la estimacion de profundidades
    int w = modelo_mask_pts.second.x - modelo_mask_pts.first.x + 1; // ancho de mascara
    int h = modelo_mask_pts.second.y - modelo_mask_pts.first.y + 1; // alto de mascara
    modelo_mask_pts.second.x -= w*0.95;
    modelo_mask_pts.second.y -= h*0.95;
    w = modelo_mask_pts.second.x - modelo_mask_pts.first.x + 1;
    h = modelo_mask_pts.second.y - modelo_mask_pts.first.y + 1;
    int N = w*h; // cantidad total de pixeles en la mascara
    Matriz M(2*N, N); // matriz de coeficientes del sistema de ecuaciones 11 y 12
    Matriz v(2*N, 1); // matriz de terminos independientes del sistema de ecuaciones 11 y 12
    int f = 0; // fila en matriz M
    
    // Obtengo la factorizacion PLU de S
    Matriz P, L, U;
    S.factorizacionPLU(P, L, U); // PS = LU
    //S.invertir();
    for (int y = modelo_mask_pts.first.y; y <= modelo_mask_pts.second.y; ++y) {
        for (int x = modelo_mask_pts.first.x; x <= modelo_mask_pts.second.x; ++x) {
            // Resolucion de ecuacion Sn = b <=> PSn = Pb <=> LUn = Pb
            Matriz Pb = P * matrizDeIntensidades(modelo, x, y);
            Matriz m; L.forwardSubstitution(m, Pb); // resuelvo ecuacion Lm = Pb (m = Un)
            Matriz n; U.backwardSubstitution(n, m); // resuelvo ecuacion Un = m
            //Matriz n = S * matrizDeIntensidades(modelo, x, y);
            double norma2 = n.normaF();
            if (!eq(norma2, 0))
                n = (1/norma2) * n; // normalizo el vector para obtener la normal
            // Escribo coordenadas en archivos de texto
            normales_x << n(0,0) << ',';
            normales_y << -n(1,0) << ',';
            normales_z << n(2,0) << ',';
            if (x == modelo_mask_pts.second.x - 1) {
                normales_x << endl;
                normales_y << endl;
                normales_z << endl;
            }
            // Defino los coeficientes correspondientes al pixel en ĺa matriz M
            int c_xy = (y - modelo_mask_pts.first.y)*w + (x - modelo_mask_pts.first.x);
            int c_x1y = c_xy + 1;
            int c_xy1 = c_xy + w;
            // Ecuacion 11
            M(f, c_xy) = -n(2,0);
            if (c_x1y < N) M(f, c_x1y) = n(2,0);
            v(f,0) = -n(0,0);
            ++f;
            // Ecuacion 12
            M(f, c_xy) = -n(2,0);
            if (c_xy1 < N) M(f, c_xy1) = n(2,0);
            v(f,0) = n(1,0);
            ++f;
        }
    }
    normales_x.close();
    normales_y.close();
    normales_z.close();
    
    // Estimo las profundidades
    Matriz &M_t = M.trasponer();
    Matriz b = M_t*v;
    Matriz &A = M_t.multiplicarPorTraspuesta();
    Matriz C; A.factorizacionCholesky(C); // A = CC_t
    // Resolucion de ecuacion Az = b <=> CC_tz = b
    Matriz u; C.forwardSubstitution(u, b); // resuelvo ecuacion Cu = b (u = C_tz)
    Matriz z; C.trasponer().backwardSubstitution(z, b); // resuelvo ecuacion C_tz = u
    

    return 0;   
}