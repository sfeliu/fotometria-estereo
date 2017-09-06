#include "matriz.h"
#include "ppm.h"
#include "fputils.h"
//#include "utils.h"
//#include "chol_alu.h"
#include <sstream>
#include <random>
#include <chrono>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

double random01(){
    return ((double) rand() / (RAND_MAX));
}

double random02(){
    std::mt19937_64 rng;
    // initialize the random number generator with time-dependent seed
    uint64_t timeSeed = std::chrono::high_resolution_clock::now().time_since_epoch().count();
    std::seed_seq ss{uint32_t(timeSeed & 0xffffffff), uint32_t(timeSeed>>32)};
    rng.seed(ss);
    // initialize a uniform distribution between 0 and 1
    std::uniform_real_distribution<double> unif(0, 1);
    // ready to generate random numbers
    const int nSimulations = 10;
    double randomNumber;
    for (int i = 0; i < nSimulations; i++)
    {
        double currentRandomNumber = unif(rng);
        randomNumber = currentRandomNumber;
    }
    return randomNumber;
}

double get_duration(clock_t start) {
    return (clock() - start) / (double) CLOCKS_PER_SEC;
}

Matriz randomMatriz(int f, int c){
    int tamano = f*c;
    double matrizRandom[tamano];
    for(int i=0; i<tamano; i++) {
        matrizRandom[i] = random02();
    }
    Matriz r(f,c,matrizRandom,tamano);
    return r;
}

Matriz randomMatrizSDP(int n){
    Matriz r1 = randomMatriz(n,n);
    //r1.print();
    Matriz r2 = r1.traspuesta();
    //r2.print();
    r1 = r1*r2;
    //r1.print();
    Matriz i = Matriz::Identidad(n);
    //i.print();
    i = i*n*n;
    //i.print();
    r1 = r1+i;
    //r1.print();
    return r1;
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
        // TODO
        return pts[0];
    }
}

Matriz matrizDeIntensidades(const vector<PPM> &ppms, const int x, const int y) {
    Matriz m = Matriz(ppms.size(), 1);
    for (int i = 0; i < (int)ppms.size(); ++i) {
        m(i,0) = ppms[i].intensidad(x,y);
    }
    return m;
}

int main() {
    /*int tamano = 50000;
    vector<Matriz> terminosIndependientes;
    for(int i=0; i<tamano; i++){
        Matriz temporal = Matriz(3,1);
        temporal(0,0) = random02();
        temporal(1,0) = random02();
        temporal(2,0) = random02();
        terminosIndependientes.push_back(temporal);
    }
    Matriz random = randomMatrizSDP(3);
    //random.print();
    //random.print();
    Matriz b(3);
    Matriz p = Matriz(3);
    p(0,0) = 20;
    clock_t start = clock();
    for(int i=0;i<tamano;i++){
        random.eliminacionGaussiana(b);
    }
    clock_t end = clock();
    double segs = (double) (end - start) / CLOCKS_PER_SEC;
    cout << "Pasaron " << segs << " segundos.\n";
    return 0;*/
    
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
    clock_start = clock();
    
    string mate_src_path;
    //cin >> mate_src_path;
    mate_src_path = "mate.txt"; cout << endl;
    cout << "Cargando imagenes... " << flush;

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
    
    cout << "listo (" << get_duration(clock_start) << " s)" << endl;

    
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
    
    cout << "listo (" << get_duration(clock_start) << " s)" << endl;


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
    
    cout << "listo (" << get_duration(clock_start) << " s)" << endl;

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
    
    cout << "listo (" << get_duration(clock_start) << " s)" << endl;

    cout << "Sistema calibrado existosamente" << endl << endl;

    }
    
    
    // 2. Reconstruccion del modelo 3D
    
    
    // 2.1. Lectura de imagenes del modelo a reconstruir
    cout << "RECONSTRUICCION DEL MODELO 3D" << endl;
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
    
    
    // 2.2. Construccion del campo normal y estimacion de profundidades
    
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
    for (int y = modelo_mask_pts.first.y; y <= modelo_mask_pts.second.y; ++y) {
        for (int x = modelo_mask_pts.first.x; x <= modelo_mask_pts.second.x; ++x) {
            // Resolucion de ecuacion Sn = b <=> PSn = Pb <=> LUn = Pb
            Matriz Pb = P * matrizDeIntensidades(modelo, x, y);
            Matriz m; L.forwardSubstitution(m, Pb); // resuelvo ecuacion Lm = Pb (m = Un)
            Matriz n; U.backwardSubstitution(n, m); // resuelvo ecuacion Un = m
            double norma2 = n.normaF();
            if (!eq(norma2, 0))
                n = (1/norma2) * n; // normalizo el vector para obtener la normal
            // Escribo coordenadas en archivos de texto
            normales_x << n(0,0) << ',';
            normales_y << n(1,0) << ',';
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
            v(f,0) = -n(1,0);
            ++f;
        }
    }
    normales_x.close();
    normales_y.close();
    normales_z.close();
    
    // Estimo las profundidades
    Matriz &M_t = M.trasponer();
    Matriz b = M_t*v;
    Matriz &A = M_t.multiplicarPorTraspuestaBanda(N, w);
    Matriz C; A.factorizacionCholesky(C); // A = CC_t
    // Resolucion de ecuacion Az = b <=> CC_tz = b
    Matriz u; C.forwardSubstitution(u, b); // resuelvo ecuacion Cu = b (u = C_tz)
    Matriz z; C.trasponer().backwardSubstitution(z, b); // resuelvo ecuacion C_tz = u


    return 0;   
}