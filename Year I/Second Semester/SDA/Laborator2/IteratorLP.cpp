#include "IteratorLP.h"
#include "Lista.h"
#include <exception>

/**
 * Overall: theta(1)
 */
IteratorLP::IteratorLP(Lista& l):lista(l) {
	curent = lista.primul;
}

/**
 * Overall: theta(1)
 */
void IteratorLP::prim(){
	curent = lista.primul;
}

/**
 * Overall: theta(1)
 */
void IteratorLP::urmator(){
    if(!valid())
        throw std::exception();
	curent = curent->urm;
}

/**
 * Overall: theta(1)
 */
bool IteratorLP::valid() const{
	if(curent == nullptr)
        return false;
	return true;
}

/**
 * Overall: theta(1)
 */
TElem IteratorLP::element() const{
	if(!valid())
        throw std::exception();
    return curent->continut;
}

/**
 * Best case: theta(1)
 * Worst case: theta(n)
 * Overall: O(n)
 */
TElem IteratorLP::elimina() {
    TElem element_curent = TELEM_NULL;
    if(!valid())
        throw std::exception();

    Nod *nod_curent = curent;
    element_curent = curent->continut;

    if(curent == lista.primul && lista.dimensiune == 1)
    {
        curent = lista.primul = lista.ultimul= nullptr;
    }
    else if(curent != lista.primul) {
        Nod *previous = lista.primul;

        while (previous->urm != curent)
            previous = previous->urm;

        previous->urm = curent->urm;
        curent = curent->urm; //in caz ca e ultimul va deveni null
    }
    else if(curent == lista.primul)
    {
            curent = curent->urm;
    }


    lista.dimensiune--;
    delete[] nod_curent;

    return element_curent;
}


/**
 * Subalgoritm elimina()
 * element_curent <- TELEM_NULL {-1}
 * Daca !valid() atunci
 *  @arunca exceptie
 *
 *  Daca curent = lista.primul si lista.primul!=lista.ultimul atunci
 *      curent<-nullptr
 *      primul<-nullptr
 *      lista.ultimul <-nullptr
 *      altfel Daca curent != lista.primul atunci
 *          previous = lista.primul
 *          Cat timp [previous].urm != curent executa
 *          previous <- [previous].urm
 *
 */



///CURSUL 6