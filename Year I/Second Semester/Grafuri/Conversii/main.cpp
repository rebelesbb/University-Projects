#include "MatriceAdiacenta.h"
#include "MatriceIncidenta.h"
#include "ListaAdiacenta.h"
#include "MatriceAdiacenta_MatriceIncidenta.h"
#include "MatriceAdiacenta_ListaAdiacenta.h"
#include "MatriceIncidenta_MatriceAdiacenta.h"
#include "MatriceIncidenta_ListaAdiacenta.h"
#include "ListaAdiacenta_MatriceAdiacenta.h"
#include "ListaAdiacenta_MatriceIncidenta.h"
#include "GOrientat_MatriceIncidenta.h"
using namespace std;

int main() {
    matriceAdicaenta();
    matriceIncidenta();
    listaAdiacenta();
    matriceAdiacenta_matriceIncidenta();
    matriceAdiacenta_listaAdiacenta();
    matriceIncidenta_matriceAdiacenta();
    matriceIncidenta_listaAdiacenta();
    listaAdiacenta_matriceAdiacenta();
    listaAdiacenta_matriceIncidenta();
    orientatMatriceIncidenta();
}
