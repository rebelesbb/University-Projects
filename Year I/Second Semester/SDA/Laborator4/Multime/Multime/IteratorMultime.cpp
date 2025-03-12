#include "IteratorMultime.h"
#include "Multime.h"
#include <exception>

/**
 * Caz favorabil: theta(1)
 * Caz defavorabil: theta(m)
 */
IteratorMultime::IteratorMultime(const Multime& m) : multime(m){
	curent = multime.m;
	for(int i = 0; i < multime.m; ++i)
		if (multime.elems[i] != NULL_TELEM)
		{
			curent = i;
			break;
		}
}

/**
 * Caz favorabil: theta(1)
 * Caz defavorabil: theta(m)
 */
void IteratorMultime::prim() {
	for (int i = 0; i < multime.m; ++i)
		if (multime.elems[i] != NULL_TELEM)
		{
			curent = i;
			break;
		}
}

/**
 * Caz favorabil: theta(1)
 * Caz defavorabil: theta(m) el pe poz 0 si m-1
 */
void IteratorMultime::urmator() {
	if (!valid())
		throw std::exception();
	curent++;
	while (curent < multime.m)
		if (multime.elems[curent] == NULL_TELEM)
			curent++;
		else break;
}

/**
 * theta(1) 
 */
TElem IteratorMultime::element() const {
	if (!valid())
		throw std::exception();
	return multime.elems[curent];
}

/**
 * theta(1)
 */
bool IteratorMultime::valid() const {
	if (curent < multime.m)
		return true;
	return false;
}
