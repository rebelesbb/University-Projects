#include "IteratorMD.h"
#include "MD.h"

using namespace std;

/**
 * theta(1)
 */
IteratorMD::IteratorMD(const MD& _md): md(_md) {
	curent = md.prim;
}

/**
 * theta(1)
 */
TElem IteratorMD::element() const{
	if (!valid())
		throw std::exception();
	return md.elemente[curent];
}

/**
 * theta(1)
 */
bool IteratorMD::valid() const {
	if(curent == -1)
		return false;
	return true;
}

/**
 * theta(1)
 */
void IteratorMD::urmator() {
	if (!valid())
		throw std::exception();
	curent = md.urm[curent];
}

/**
 * theta(1)
 */
void IteratorMD::prim() {
	curent = md.prim;
}

