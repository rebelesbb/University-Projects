
#include <exception>

#include "IteratorLP.h"
#include "Lista.h"

#include <iostream>

/**
 * T(n) = 3 => theta(1)
 * Overall: theta(1)
 */
Lista::Lista() {
	primul = ultimul = nullptr;
    dimensiune = 0;
}

/**
 * Overall: theta(1)
 */
int Lista::dim() const {
	return dimensiune;
}

/**
 * Overall: theta(1)
 */
bool Lista::vida() const {
	if(primul == nullptr)
        return true;
    return false;
}

/**
 * Overall
 */
IteratorLP Lista::prim() {
    return IteratorLP(*this);
}

/**
 * Overall: theta(1)
 */
TElem Lista::element(IteratorLP poz) const {
	if(!poz.valid())
        throw std::exception();
    return poz.element();
}

/**
 * Daca elementul se afla pe prima sau ultima pozitie => theta(1)
 * altfel
 *  Cazul defavorabil ar fi cand elementul e pe pozitia n-1
 *   => T(n)= (n - 1) + 4 => theta(n)
 *          parcurgerea
 * Overall: O(n)
 */
TElem Lista::sterge(IteratorLP& poz) {
	Nod *elem_de_sters = poz.curent, *anterior;
    IteratorLP it(*this);
    TElem sters = TELEM_NULL;
    if(!poz.valid())
        throw std::exception();

    if(elem_de_sters == primul) {
        poz.urmator();
        sters = primul->continut;
        primul = primul->urm;
        delete[] elem_de_sters;
        dimensiune--;
    }
    else if(elem_de_sters == ultimul) {
        poz.urmator();
        sters = ultimul->continut;
        ultimul = nullptr;
        delete[] elem_de_sters;
        dimensiune--;
    }else {

        while (it.valid() && it.curent != elem_de_sters)
            anterior = it.curent, it.urmator();

        if (it.valid()) {
            poz.urmator();
            sters = elem_de_sters->continut;
            anterior->urm = elem_de_sters->urm;
            delete[] elem_de_sters;
            dimensiune--;
        }
    }

	return sters;
}

/**
 * Daca elementul este pe prima pozitie => T(n) = 1 => theta(1)
 * Daca elementul este ultimul => T(n) = n => theta(n)
 * Overall: O(n)
 */
IteratorLP Lista::cauta(TElem e) {
    IteratorLP it(*this);
    while(it.valid() && it.element() != e)
        it.urmator();
    return it;
}

/**
 * Functia element se executa in timp constant => T(n) = 1 + 1 => theta(1)
 * Overall:theta(1)
 */
TElem Lista::modifica(IteratorLP poz, TElem e) {
    if(!poz.valid())
        throw std::exception();
    TElem modificat = poz.element();
	poz.curent->continut=e;
	return modificat;
}

/**
 * Daca poz = 1 sau poz = n (elementul se adauga pe prima sau ultima pozitie)
 *  =>theta(1)
 * altfel
 *  Cazul defavorabil ar fi cand elementul se afla pe pozitia n-1
 *   => T(n)= (n - 1) + 4 => theta(n)
 *          parcurgerea
 * Overall: O(n)
 */
void Lista::adauga(IteratorLP& poz, TElem e) {
	IteratorLP it(*this);
    if(!poz.valid())
        throw std::exception();

    Nod* element_nou = new Nod;
    element_nou->continut=e;

    if(poz.curent == primul)
    {
        adaugaInceput(e);
    }
    else if(poz.curent == ultimul)
    {
        adaugaSfarsit(e);
    }
    else{
        while(it.valid() && it.curent->urm != poz.curent)
            it.urmator();
        if(it.valid())
        {
            Nod *x;
            element_nou->urm = poz.curent;
            it.curent->urm = element_nou;
            dimensiune++;
            poz.curent = element_nou;
        }
    }
}
/**
 * Daca lista este goala
 *  =>T(n) = 1 + 3 => theta(1)
 * altfel
 *  =>T(n) = 1 + 2 => theta(1)
 * Overall: theta(1)
 */
void Lista::adaugaInceput(TElem e) {

    Nod* element_nou = new Nod;
    element_nou->continut = e;

    if(primul == nullptr)
    {
        element_nou->urm = nullptr;
        primul = ultimul = element_nou;
    }
    else{
        element_nou->urm = primul;
        primul = element_nou;
    }
    dimensiune++;

}

/**
 * Daca lista este goala
 *  =>T(n) = 3 + 2 => theta(1)
 * altfel
 *  =>T(n) = 3 + 1 => theta(1)
 * Overall: theta(1)
 */
void Lista::adaugaSfarsit(TElem e) {
    Nod* element_nou = new Nod;
	element_nou->continut = e;
    element_nou->urm = nullptr;
    if(ultimul == nullptr)
    {
        ultimul = primul = element_nou;
    }
    else {
        ultimul->urm = element_nou;
        ultimul = element_nou;
    }
    dimensiune++;
}

/**
 * theta(n)
 */
Lista::~Lista() {
    Nod* x;
	while(primul!= nullptr) {
        x = primul->urm;
        delete[] primul;
        primul = x;
    }
}
