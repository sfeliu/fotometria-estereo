#include "matriz_esparza.h"
#include <iostream>

using namespace std;

int main() {

    MatrizEsparza A;
    cout << A.elem(0, 10) << endl;
    cout << A.columnas() << endl;

    return 0;
}