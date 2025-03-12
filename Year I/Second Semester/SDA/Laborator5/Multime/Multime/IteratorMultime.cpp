#include "IteratorMultime.h"
#include "Multime.h"
#include <exception>
#include <iostream>

// O(n)
IteratorMultime::IteratorMultime(const Multime& m): mult(m) {
	prim();
}

// theta(1)
TElem IteratorMultime::element() const {
	if (!valid())
		throw std::exception();
	return mult.elemente[curent];
}

// theta(1)
bool IteratorMultime::valid() const {
	if (curent == -1)
		return false;
	return true;
}

/*
Caz favorabil: theta(1)
Caz defavorabil: theta(n)
Overall: O(n)
*/
void IteratorMultime::urmator() {
	if (!valid())
		throw std::exception();

	S.pop();
	if (mult.dreapta[curent] != -1)
	{
		curent = mult.dreapta[curent];
		while (curent != -1)
		{
			S.push(curent);
			curent = mult.stanga[curent];
		}
	}

	if (!S.empty())
		curent = S.top();
	else curent = -1;
}

/*
Caz favorabil: theta(1)
Caz defavorabil: theta(n)
Overall: O(n)
*/
void IteratorMultime::prim() {
	
	while (!S.empty())
		S.pop();

	curent = mult.radacina;
	while (curent != -1)
	{
		S.push(curent);
		curent = mult.stanga[curent];
	}
	if (!S.empty())
	{
		curent = S.top();
	}
}

