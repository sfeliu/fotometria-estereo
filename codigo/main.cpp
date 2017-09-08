#include "fputils.h"
#include "ppm.h"
#include "matriz.h"
#include "matriz_esparza.h"
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <ctime>
#include <stdexcept>
#include <set>

double get_duration(clock_t start) {
    return (clock() - start) / (double) CLOCKS_PER_SEC;
}

PPM::punto puntoDeMayorIntensidad(const PPM &ppm, pair<PPM::punto, PPM::punto> mask) {
    vector<PPM::punto> pts;
    pts.push_back(mask.first); // inserto un primer punto para simplificar el algoritmo que sigue
    int sigPos = 1; // posicion del vector para insertar el siguiente punto
    double intensidadMax = -1;
    // Recorro la imagen (usando la maskara) y voy guardando los puntos de mayor intensidad
    for (int y = mask.first.y; y < mask.second.y; ++y) {
        for (int x = mask.first.x; x < mask.second.x; ++x) {
            double intensidad = ppm.intensidadEnVecindad(x, y, 6);
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
    // Devuelvo el primero de los puntos de mayor intensidad
    return pts[0];
}

Matriz matrizDeIntensidades(const vector<PPM> &ppms, const int x, const int y) {
    Matriz m = Matriz(ppms.size(), 1);
    for (int i = 0; i < (int)ppms.size(); ++i) {
        m(i,0) = ppms[i].intensidad(x,y);
    }
    return m;
}

int main() {

    clock_t clock_start;

    // 1. Calibracion del sistema

    int dirs_cant;
    int elecDirsI[3];
    Matriz S(3);

    ifstream calibracion_in("calibracion.txt");
    if (calibracion_in.is_open()) {
        // Leo la cantidad total de direcciones
        calibracion_in >> dirs_cant;
        // Leo la eleccion de direcciones realizada
        for (int i = 0; i < 3; ++i) calibracion_in >> elecDirsI[i];
        // Cargo las direcciones elegidas en S
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) calibracion_in >> S(i,j);
        }
        calibracion_in.close();
    } else {


    // 1.1. Lectura de imagenes mate

    cout << "CALIBRACION DEL SISTEMA" << endl;
    cout << "Ingrese el archivo de texto de rutas del modelo mate: ";

    string mate_src_path;
    //cin >> mate_src_path;
    mate_src_path = "mate.txt"; cout << endl;
    cout << "Cargando imagenes... " << flush;
    clock_start = clock();

    ifstream mate_src(mate_src_path);
    if (!mate_src.is_open()) throw runtime_error("ERROR: no se pudo abrir el archivo");

    mate_src >> dirs_cant; // leo la cantidad de imagenes (excluyendo mascara)
    mate_src.ignore(numeric_limits<std::streamsize>::max(), '\n'); // voy hasta la proxima linea
    vector<PPM> mate(dirs_cant);
    PPM mate_mask;
    {
        string ruta;
        for (int i = 0; i < dirs_cant; ++i) {
            getline(mate_src, ruta);
            mate[i].cargarImagen(ruta);
        }
        mate_mask.cargarImagen(ruta);
    }

    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;


    // 1.2. Obtenencion de direcciones de iluminacion

    cout << "Obteniendo direcciones de iluminacion... " << flush;
    clock_start = clock();

    pair<PPM::punto, PPM::punto> mate_mask_pts = mate_mask.generarMascara(); // obtengo puntos de la mascara
    int radio = (mate_mask_pts.second.x - mate_mask_pts.first.x + 1) / 2; // radio de la esfera
    PPM::punto centro(mate_mask_pts.first.x + radio - 1, mate_mask_pts.first.y + radio - 1); // centro de la esfera

    // Obtengo direcciones de iluminacion
    vector<Matriz> dirsI(dirs_cant, Matriz(3,1));
    for (int i = 0; i < dirs_cant; ++i) {
        PPM::punto pt = puntoDeMayorIntensidad(mate[i], mate_mask_pts);
        dirsI[i](0,0) = pt.x - centro.x; // coordenada x
        dirsI[i](1,0) = pt.y - centro.y; // coordenada y
        dirsI[i](2,0) = pow(pow(radio, 2) - pow(dirsI[i](0,0), 2) - pow(dirsI[i](1,0), 2), 0.5); // coordenada z
        dirsI[i] = dirsI[i] * (1 / (double)radio); // normalizo el vector
    }

    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;


    // 1.3. Eleccion de direcciones de iluminacion

    cout << "Seleccionando direcciones optimas... " << flush;
    clock_start = clock();

    // Elijo las direcciones que formen la matriz con menor numero de condicion para minimizar errores de estimacion
    double min_num_cond = INFINITY;
    for (int i = 0; i < dirs_cant-2; ++i) {
        for (int j = i+1; j < dirs_cant-1; ++j) {
            for (int k = j+1; k < dirs_cant; ++k) {
                Matriz A(3);
                A(0,0) = dirsI[i](0,0); A(0,1) = dirsI[i](1,0); A(0,2) = dirsI[i](2,0);
                A(1,0) = dirsI[j](0,0); A(1,1) = dirsI[j](1,0); A(1,2) = dirsI[j](2,0);
                A(2,0) = dirsI[k](0,0); A(2,1) = dirsI[k](1,0); A(2,2) = dirsI[k](2,0);
                double norma_A = A.normaF(); // guardo la norma de S
                // Aplico eliminacion Gaussiana ampliando con la matriz identidad para obtener la inversa de S
                Matriz I = Matriz::Identidad(3);
                A.eliminacionGaussiana(I);
                // Si existe la inversa calculo el numero de condicion
                if (!eq(A(2,2), 0)) {
                    Matriz B;
                    A.backwardSubstitution(B, I); // obtengo la inversa
                    double num_cond = norma_A * B.normaF();
                    // Actualizo el minimo numero de condicion y guardo los indices de las direcciones
                    if (lt(num_cond, min_num_cond)) {
                        min_num_cond = num_cond;
                        elecDirsI[0] = i;
                        elecDirsI[1] = j;
                        elecDirsI[2] = k;
                    }
                }
            }
        }
    }

    if (min_num_cond == INFINITY)
        throw runtime_error("ERROR: no hay direcciones de luz linealmente independientes");

    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;

    // Defino matriz S
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) S(i,j) = dirsI[elecDirsI[i]](j,0);
    }


    // 1.4. Exportacion de datos de calibracion
    cout << "Guardando datos de calibracion... " << flush;
    clock_start = clock();

    ofstream calibracion_out;
    calibracion_out.open("calibracion.txt");
    calibracion_out << dirs_cant << '\n';
    calibracion_out << elecDirsI[0] << ' ';
    calibracion_out << elecDirsI[1] << ' ';
    calibracion_out << elecDirsI[2] << '\n';
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) calibracion_out << S(i,j) << ' ';
        calibracion_out << '\n';
    }
    calibracion_out.close();

    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;

    cout << "Sistema calibrado existosamente" << endl << endl;

    }


    // 2. Reconstruccion del modelo 3D


    // 2.1. Lectura de imagenes del modelo a reconstruir
    cout << "RECONSTRUICCION DEL MODELO 3D" << endl;
    cout << "Ingrese el archivo de texto de rutas del modelo a reconstruir: ";

    string modelo_src_path;
    //cin >> modelo_src_path;
    modelo_src_path = "caballo.txt"; cout << endl;
    cout << "Cargando imagenes... " << flush;
    clock_start = clock();

    ifstream modelo_src(modelo_src_path);
    if (!modelo_src.is_open()) throw runtime_error("ERROR: no se pudo abrir el archivo");
    vector<PPM> modelo(3);
    PPM modelo_mask;
    {
        int modelo_cant;
        modelo_src >> modelo_cant; // leo la cantidad de imagenes (excluyendo mascara)
        if (modelo_cant != dirs_cant) throw runtime_error("ERROR: la cantidad de imagenes del modelo no coincide con la cantidad de direcciones de iluminacion provistas en la calibracion");
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

    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;


    // 2.2. Obtencion de normales

    cout << "Obteniendo normales... " << flush;
    clock_start = clock();

    pair<PPM::punto, PPM::punto> modelo_mask_pts = modelo_mask.generarMascara(); // obtengo puntos de la mascara
    int w = modelo_mask_pts.second.x - modelo_mask_pts.first.x + 1; // ancho de mascara
    int h = modelo_mask_pts.second.y - modelo_mask_pts.first.y + 1; // alto de mascara
    modelo_mask_pts.second.x -= w*0.986;
    modelo_mask_pts.second.y -= h*0.986;
    w = modelo_mask_pts.second.x - modelo_mask_pts.first.x + 1;
    h = modelo_mask_pts.second.y - modelo_mask_pts.first.y + 1;
    int N = w*h; // cantidad total de pixeles en la mascara
    vector<Matriz> normales(N);

    // Creo archivos de texto para guardar los datos
    ofstream normales_x, normales_y, normales_z;
    normales_x.open("normalesX.txt");
    normales_y.open("normalesY.txt");
    normales_z.open("normalesZ.txt");

    // Obtengo la factorizacion PLU de S
    {
        Matriz P, L, U;
        S.factorizacionPLU(P, L, U); // PS = LU
        int i = 0;
        for (int y = modelo_mask_pts.first.y; y <= modelo_mask_pts.second.y; ++y) {
            for (int x = modelo_mask_pts.first.x; x <= modelo_mask_pts.second.x; ++x) {

                // Resolucion de ecuacion 5: Sm = b <=> PSm = Pb <=> LUm = Pb
                Matriz Pb = P * matrizDeIntensidades(modelo, x, y);
                Matriz h; L.forwardSubstitution(h, Pb); // resuelvo ecuacion Lh = Pb (h = Um)
                Matriz m; U.backwardSubstitution(m, h); // resuelvo ecuacion Um = h
                double norma2 = m.normaF();
                Matriz n(3,1); // normal
                if (!eq(norma2, 0))
                    n = (1/norma2) * m; // normalizo el vector para obtener la normal
                normales[i] = n;
                ++i;

                // Escribo coordenadas en archivos de texto
                normales_x << n(0,0) << ',';
                normales_y << n(1,0) << ',';
                normales_z << n(2,0) << ',';

            }

            normales_x << endl;
            normales_y << endl;
            normales_z << endl;
        }
    }
    normales_x.close();
    normales_y.close();
    normales_z.close();

    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;


    // 2.3 Estimacion de profundidades

    cout << "Estimando profundidades... " << flush;
    clock_start = clock();

    // Construyo matrices M y v de ecuacion 13
    MatrizEsparza M(2*N, N); // matriz de coeficientes del sistema de ecuaciones 11 y 12
    MatrizEsparza v(2*N, 1); // matriz de terminos independientes del sistema de ecuaciones 11 y 12
    for (int i = 0; i < (int) normales.size(); ++i) {
        int f = 2 * i; // primera fila del pixel actual
        int c_xy = i; // columna del pixel actual (x,y)
        int c_x1y = i + 1; // columna del pixel (x+1,y)
        int c_xy1 = i + w; // columna del pixel (x,y+1)
        // Ecuacion 11
        M.elem(f, c_xy) = -normales[i](2,0);
        if (c_x1y < N) M.elem(f, c_x1y) = normales[i](2,0);
        v.elem(f,0) = -normales[i](0,0);
        // Ecuacion 12
        M.elem(f+1, c_xy) = -normales[i](2,0);
        if (c_xy1 < N) M.elem(f+1, c_xy1) = normales[i](2,0);
        v.elem(f+1,0) = -normales[i](1,0);
    }

    // Obtengo matrices A y b de ecuacion 15

    // Multiplico M_t por v
    cout << endl << "Multiplicando M_t por v... " << flush;
    clock_start = clock();
    MatrizEsparza &M_t = M.trasponer();
    MatrizEsparza b(M_t.filas(), v.columnas());
    for (int i = 0; i < b.filas(); ++i) {
        for (int j = 0; j < b.columnas(); ++j) {
            // Obtengo las columnas no nulas de la fila i de M_t
            vector<int> cols;
            int ec1_i = 2*i;
            cols.push_back(ec1_i);
            cols.push_back(ec1_i + 1);
            if (ec1_i - 2 >= 0) cols.push_back(ec1_i - 2);
            if (ec1_i - 2*w + 1 >= 0) cols.push_back(ec1_i - 2*w + 1);
            // Multiplico las filas
            for (vector<int>::iterator it = cols.begin(); it != cols.end(); ++it) {
                b.elem(i,j) += M_t(i,*it) * v(*it, j);
            }
        }
    }

    cout << endl << "Computando matriz A... " << flush;
    clock_start = clock();

    // Hago M_t * M
    MatrizEsparza A(M_t.filas());
    for (int i = 0; i < N; ++i) {
        for (int j = i; j < min(N, i+w+1); ++j) {
            set<int> cols;
            // Obtengo las columnas no nulas de la fila i
            int ec1_i = 2*i;
            cols.insert(ec1_i);
            cols.insert(ec1_i + 1);
            if (ec1_i - 2 >= 0) cols.insert(ec1_i - 2);
            if (ec1_i - 2*w + 1 >= 0) cols.insert(ec1_i - 2*w + 1);
            // Obtengo las columnas no nulas de la fila j
            int ec1_j = 2*j;
            cols.insert(ec1_j);
            cols.insert(ec1_j + 1);
            if (ec1_j - 2 >= 0) cols.insert(ec1_j - 2);
            if (ec1_j - 2*w + 1 >= 0) cols.insert(ec1_j - 2*w + 1);
            // Multiplico las filas
            for (set<int>::iterator it = cols.begin(); it != cols.end(); ++it) {
                A.elem(i,j) += M_t(i,*it) * M_t(j,*it);
            }
            A.elem(j,i) = A(i,j);
        }
    }

    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;
    // Resuelvo la ecuacion con factorizacion Cholesky: Ax = b <=> LL_tx = b
    //MatrizEsparza L, Q;
    MatrizEsparza B = A;
    cout << "Obteniendo factorizacion Cholesky... " << flush;
    clock_start = clock();
    MatrizEsparza Q;
    A.factorizacionCholeskyBanda(w, Q);
    //A.factorizacionCholeskyBanda(w, L);
    MatrizEsparza L = MatrizEsparza(N);
    for (int j = 0; j < N; ++j) {
        L.elem(j,j) = A(j,j);
        for (int k = max(0, j-w); k < j; ++k)
            L.elem(j,j) -= pow(L(j,k), 2);
        if (leq(L(j,j), 0))
            throw domain_error("La matriz no tiene factorizacion Cholesky.");
        L.elem(j,j) = pow(L(j,j), 0.5);
        vector<int> filas;
        if (j+1 < N) filas.push_back(j+1);
        if (j+w < N) filas.push_back(j+w);
        for (vector<int>::iterator it = filas.begin(); it != filas.end(); ++it) {
            L.elem(*it,j) = A(*it,j) / L(j,j);
        }
    }
    cout << endl;
    Q.print();
    if (L != Q) throw runtime_error("NO SON IGUALES");
    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;
    cout << "Hallandos solucion..." << flush;
    clock_start = clock();
    MatrizEsparza y(N, 1);
    L.forwardSubstitution(y, b); // resuelvo ecuacion Ly = b donde y = L_tx
    MatrizEsparza x(N, 1);
    L.trasponer().backwardSubstitution(x, y); // resuelvo ecuacion L_tx = y
    cout << "listo. [" << get_duration(clock_start) << " s]" << endl;


    // Exporto profundidades
    /*ofstream profundidades;
    profundidades.open("profundidades.txt");
    for (int i = 0; i < x.filas(); ++i) {
        profundidades << x(i,0) << ' ';
        if ((i+1) % w == 0) profundidades << endl;
    }

    profundidades.close();*/

    //cout << "listo. [" << get_duration(clock_start) << " s]" << endl;

    cout << "Modelo reconstruido exitosamente" << endl;


    return 0;
}
