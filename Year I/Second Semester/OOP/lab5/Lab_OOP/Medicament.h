#ifndef UNTITLED_MEDICAMENT_H
#define UNTITLED_MEDICAMENT_H
typedef struct {
    int cod;
    char* nume;
    double concentratie;
    int cantitate;
} Medicament;

Medicament* createMed(int cod, char nume[50], double conc, int cant);

int get_cod(Medicament* med);

char* get_nume(Medicament* med);

double get_concentratie(Medicament* med);

int get_cantitate(Medicament* med);

void set_cod(Medicament* med, int cod);

void set_nume(Medicament* med, char* nume);

void set_concentratie(Medicament* med, double concentratie);

void set_cantitate(Medicament* med, int cantitate);

Medicament* copyMed(Medicament* med);

void destroyMed(Medicament* med);

int validateMed(Medicament* med);

#endif //UNTITLED_MEDICAMENT_H
