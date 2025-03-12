#ifndef UNTITLED_LIST_H
#define UNTITLED_LIST_H
#include "Medicament.h"

///list module

typedef void* ElementType;
typedef void (*DestroyFunction)(ElementType);
typedef ElementType (*CopyFunction)(ElementType);
typedef int (*CompareFunction)(ElementType*, ElementType*);

typedef struct {
    ElementType* elems;
    int lungime;
    int capacitate;
} MyList;

MyList* createList();

void destroyList(MyList* list, DestroyFunction destrFunc); //?????

ElementType get_element(MyList* list, int index);

void store(MyList* list, ElementType element);

void delete(MyList* list, int position, DestroyFunction destrFunc);

void copyElems(MyList* src, MyList* dest, CopyFunction copyFunc);

///meds functions

void add_medicament(Medicament* med, MyList* list);

void delete_medicament(int cod, MyList* list);

void modify_medicament(int cod, double conc, char nume[50], MyList* list);

int compare_nume(Medicament a, Medicament b);

int compare_cantitate_cresc(Medicament a, Medicament b);

int compare_cantitate_descresc(Medicament a, Medicament b);

MyList* sort_meds(MyList* list, CompareFunction compare);

MyList* filter_meds(MyList* list, int optiune, int filtru);

int compare_cantitate_concentratie(Medicament a, Medicament b);
#endif //UNTITLED_LIST_H
