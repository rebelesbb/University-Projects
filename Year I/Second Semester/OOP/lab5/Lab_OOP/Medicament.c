#include "Medicament.h"
#include <stdlib.h>
#include <string.h>

Medicament* createMed(int cod, char nume[50], double conc, int cant)
{
    /*
     * Returneaza un medicament cu codul, numele, concentratia si cantiatea data
     * pre:
     * cod: int, >= 0, codul
     * nume: cstring, max 50 char, numele
     * concentratie: double, > 0, concentratia
     * cantitate: int, > 0, cantatea
     *
     * return: struct Medicament cu datele date
     */
    Medicament* med = malloc(sizeof(Medicament));
    set_cod(med, cod);
    med->nume = (char*)malloc((strlen(nume) + 1) * sizeof(char));
    set_nume(med, nume);
    set_cantitate(med, cant);
    set_concentratie(med, conc);
    return med;
}

int get_cod(Medicament* med)
{
    return med->cod;
}

char* get_nume(Medicament* med)
{
    return med->nume;
}

double get_concentratie(Medicament* med)
{
    return med->concentratie;
}

int get_cantitate(Medicament* med)
{
    return med->cantitate;
}

void set_cod(Medicament* med, int cod)
{
    med->cod = cod;
}

void set_nume(Medicament* med, char* nume)
{
    if(sizeof(char) * (strlen(med->nume) + 1) < sizeof(char) * (strlen(nume) + 1))
        med->nume = (char*)realloc(med->nume, sizeof(char) * (strlen(nume) + 1));
    strcpy_s(med->nume,strlen(nume) + 1,nume);
}

void set_concentratie(Medicament* med, double concentratie)
{
    med->concentratie = concentratie;
}

void set_cantitate(Medicament* med, int cantitate)
{
    med->cantitate = cantitate;
}

Medicament* copyMed(Medicament* med)
{
    Medicament* med_copy = createMed(get_cod(med),
                                     get_nume(med),
                                     get_concentratie(med),
                                     get_cantitate(med));
    return med_copy;
}

void destroyMed(Medicament* med)
{
    free(med->nume);
    free(med);
}

int validateMed(Medicament* med) {
    /*
     * Valideaza medicamentul dat
     * med: struct Medicament
     * return: 0 daca totul e ok, 1 daca medicamentul e invalid
     */
    if (med->cantitate <= 0)
        return 1;
    if (med->cod < 0)
        return 1;
    if (med->concentratie < 0)
        return 1;
    if (strlen(med->nume) <= 0)
        return 1;

    return 0;
}