#include "matriz.h"
#include "ppmloader.h"

int main() {
    // 1. Calibracion del sistema
    double dirs[] = {0.403259, 0.480808, 0.778592, 0.0982272, 0.163712, 0.981606, -0.0654826, 0.180077, 0.98147};
    Matriz S = Matriz(3, 3, dirs, 9);
    S.trasponer();
    S.print();

    // 2. Reconstruccion del modeo 3D

    // 2.1. Construccion del campo normal

    // 2.2. Estimacion de la profundidad

    return 0;
}