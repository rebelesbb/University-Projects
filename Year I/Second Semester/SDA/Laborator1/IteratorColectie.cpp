#include "IteratorColectie.h"
#include "Colectie.h"
#include <exception>

///pentru complexitati n = nr. elemente din colectie

/*
 * T(n) = 1 + 1 + 1 = 3 => theta(1)
 */
IteratorColectie::IteratorColectie(const Colectie& c): col(c) {
	current = 0;
    fr_iterata = 1;
    total_iterat = 0;
}

/*
 * T(n) = 1 + 1 + 1 = 3 => theta(1)
 */
void IteratorColectie::prim() {
    current = 0;
    fr_iterata = 1;
    total_iterat = 0;
}

/*
 * Daca iteratorul nu e valid => theta(1) (operatia de validare se executa in theta(1))
 * altfel
 *  Daca parcurgem in continuare frecventa elementului curent => T(n) = 2 => theta(1)
 *  altfel
 *   => T(n) = 3 => theta(1)
 *   overall: theta(1)
 */
void IteratorColectie::urmator() {
    if(!valid()){
        throw std::exception();
    };
	if(col.colectie[current].frecventa > fr_iterata) {
        fr_iterata++;
        total_iterat++;
    }
    else{
        current++;
        fr_iterata = 1;
        total_iterat ++;
    }
}

/*
 * T(n) = 1 => theta(1)
 */
bool IteratorColectie::valid() const {
	if(this->total_iterat < col.dim())
        return true;
	return false;
}


/*
 * T(n) = 1 => theta(1)
 */
TElem IteratorColectie::element() const {
	if(valid())
        return col.colectie[current].element;
    else throw std::exception();
	return -1;
}
