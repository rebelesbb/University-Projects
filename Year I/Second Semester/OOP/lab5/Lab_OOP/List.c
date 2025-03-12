#include "List.h"
#include <stdlib.h>
#include <string.h>

MyList* createList() {
    /*
     * Returneaza o lista nous
     * return: MyList
     */
    MyList* list = malloc(sizeof(MyList));
    list->lungime = 0;
    list->capacitate = 10;
    list->elems = malloc(list->capacitate * sizeof(ElementType));

    return list;
}

void destroyList(MyList* list, DestroyFunction destrFunc)
{
    for (int i = 0; i < list->lungime; i++)
        destrFunc(list->elems[i]);

    free(list->elems);
    free(list);
}

void expand(MyList* list) {
    /*
     * Dubleaza capacitatea listei date
     * list: pointer catre lista MyList
     * post: capacitatea va fi dublata
     */
    list->capacitate *= 2;
    list->elems = realloc(list->elems, list->capacitate * sizeof(ElementType));
}

ElementType get_element(MyList* list, int index)
{
    return list->elems[index];
}

char get_initial(char* word)
{
    return word[0];
}


void store(MyList* list, ElementType element)
{
    if (list->lungime + 1 > list->capacitate)
        expand(list);
    list->elems[list->lungime] = element;
    (list->lungime)++;
}

void delete(MyList* list, int position, DestroyFunction destrFunc)
{
    destrFunc(list->elems[position]);
    for(int index = position; index < list->lungime - 1; index++)
        list->elems[index] = list->elems[index + 1];
    list->lungime--;
}

void modify(MyList* list, ElementType new_element, int position, DestroyFunction destrFunc)
{
    ElementType previous_element = get_element(list, position);
    list->elems[position] = new_element;
    destrFunc(previous_element);
}

void copyElems(MyList* src, MyList* dest, CopyFunction copyFunc) {
    /*
     * Face o copie a elems din lista sursa in lista destinatie
     * src: MyList
     * dest: pointer MyList
     * post: se va creea o noua tablou elems
     */

    for (int i = 0; i < src->lungime; i++) {
        store(dest,copyFunc(src->elems[i]));
    }
}

///service
void add_medicament(Medicament* med, MyList* list) {
    /*
     * Adauga medicamentul in lista
     * med: Medicament
     * list: pointer MyList
     * post: medicamentul va fi adaugat in lista
     */
    int exists = 0;
    for (int i = 0; i < list->lungime; i++) {
        if (get_cod(list->elems[i]) == med->cod) {
            exists = 1;
            set_cantitate(get_element(list, i),
                          get_cantitate(get_element(list, i)) + med->cantitate);
            destroyMed(med);
            ///printf("%d", get_cantitate(get_element(list, i)));
            break;
        }
    }
    if (exists == 0) {
       if(list->lungime > list->capacitate)
           expand(list);
        store(list, med);
    }

}

void delete_medicament(int cod, MyList* list) {
    /*
     * Sterge medicamentul cu codul dat din lista
     * cod: int, codul medicamentului
     * list: pointer MyList
     * post: medicamentul va fi sters din lista, daca exista
     */
    int i = 0;
    while (i < list->lungime && get_cod(list->elems[i]) != cod) i++;

    delete(list, i, (DestroyFunction) destroyMed);
}

void modify_medicament(int cod, double conc, char nume[50], MyList* list) {
    /*
     * Modifica medicamentul cu codul dat din lista, folosind concentratia si numele dat
     * cod: int, codul medicamentului
     * concentratie: double, > 0, concentratia
     * nume: cstring, max 50 char, numele
     * list: pointer MyList
     * post: medicamentul va fi modificat in lista, daca exista
     */
    int i = 0;
    while (i < list->lungime && get_cod(list->elems[i]) != cod) i++;

    if (i < list->lungime) {
        Medicament* new_med = createMed(cod, nume, conc, get_cantitate(get_element(list, i)));
        modify(list, new_med, i, (DestroyFunction) destroyMed);
    }
}

int compare_nume(Medicament a, Medicament b)
{
    /* Returneaza 1 daca numele lui a e mai "mic" sau egal lexicografic ca numele lui b, 0 daca nu
     * a: Medicament
     * b: Medicament
     * return: 1 daca a "<=" b lexicografic, 0 daca nu
     */
    return (strcmp(a.nume, b.nume) <= 0);
}

int compare_cantitate_cresc(Medicament a, Medicament b)
{
    /* Returneaza 1 daca cantitaea lui a e < cantitaealui b, 0 daca nu
     * a: Medicament
     * b: Medicament
     * return: 1 daca cantitate a < cantitate b, 0 daca nu
     */
    return (a.cantitate < b.cantitate);
}

int compare_cantitate_descresc(Medicament a, Medicament b)
{
    /* Returneaza 1 daca cantitaea lui a e > cantitaea lui b, 0 daca nu
     * a: Medicament
     * b: Medicament
     * return: 1 daca cantitate a > cantitate b, 0 daca nu
     */
    return (a.cantitate > b.cantitate);
}

int compare_cantitate_concentratie(Medicament a, Medicament b)
{
    if(get_cantitate(&a) < get_cantitate(&b) ||
      (get_cantitate(&a) == get_cantitate(&b) && get_concentratie(&a) < get_concentratie(&b)))
        return 1;
    return 0;
}

MyList* sort_meds(MyList* list, CompareFunction compare) {
    /*
     * Returneaza o lista noua care contine medicamentele sortate dupa nume sau cantitate(descrescator/crescator)
     * list: MyList
     * optiune: int, 0 - dupa nume, 1 - dupa cantitate(crescator), 2 - dupa cantiate(descrescator)
     * return: MyList, lista sortata
     */
     MyList* new_list = createList();
     copyElems(list, new_list, (CopyFunction) copyMed);

     for (int i = 0; i < new_list->lungime - 1; i++) {
         for (int j = i + 1; j < new_list->lungime; j++) {
             if (compare(new_list->elems[i], new_list->elems[j]) != 1) {
                 Medicament* aux = new_list->elems[i];
                 new_list->elems[i] = new_list->elems[j];
                 new_list->elems[j] = aux;
             }
         }
     }

     return new_list;
}

MyList* filter_meds(MyList* list, int optiune, int filtru) {
    /*
    * Returneaza o lista noua care contine medicamentele filtrate (cantitate mai mica de N / nume incepand cu o litera)
    * list: MyList
    * optiune: int, 1 - filtrare dupa cantitate, 2 - filtrare dupa prima litera din nume
    * filtru: daca optiune = 1: cantitatea ceruta, daca optiune = 2: (ascii) litera ceruta
    *         daca optiune = 3: concentratia ceruta
    * return: MyList, lista filtrata
    */
    MyList* new_list = createList();

    if (optiune == 1) {
        filtru = (int) (filtru);
        for (int i = 0; i < list->lungime; i++) {
            if (get_cantitate(list->elems[i]) < filtru) {
                Medicament* new_med = copyMed(get_element(list,i));
                store(new_list,new_med);
            }
        }
    } else if (optiune == 2) {
        for (int i = 0; i < list->lungime; i++) {
            if (get_initial(get_nume(list->elems[i])) == (char) filtru) {
                Medicament* new_med = copyMed(get_element(list,i));
                store(new_list,new_med);
            }
        }
    } else if(optiune == 3)
    {
        for(int i = 0; i < list->lungime; i++) {
            if (get_cantitate(list->elems[i]) > filtru) {
                Medicament* new_med = copyMed(get_element(list,i));
                store(new_list,new_med);
            }
        }
    }

    return new_list;
}

