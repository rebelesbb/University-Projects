#include "TestScurt.h"
#include <assert.h>
#include "Multime.h"
#include "IteratorMultime.h"

void testReuniune()
{
	Multime m;
	
	// intitial m vida
	Multime b1;
	for (int i = 1; i <= 10; ++i)
		b1.adauga(i);
	assert(b1.dim() == 10);
	m.reuniune(b1);
	assert(m.dim() == 10);

	// adaugam in m care nu mai e vida elemente inexistante in ea
	Multime b2;
	for (int i = 11; i <= 20; ++i)
		b2.adauga(i);
	assert(b2.dim() == 10);
	m.reuniune(b2);
	assert(m.dim() == 20);

	// adaugam doar elemente deja existente
	m.reuniune(b1);
	assert(m.dim() == 20);
	m.reuniune(b2);
	assert(m.dim() == 20);

	//adaugam atat elemente existente cat si inexistente
	for (int i = 21; i <= 30; ++i)
		b2.adauga(i);
	assert(b2.dim() == 20);
	m.reuniune(b2);
	assert(m.dim() == 30);
}

void testAll() { //apelam fiecare functie sa vedem daca exista
	Multime m;
	assert(m.vida() == true);
	assert(m.dim() == 0); //adaug niste elemente
	assert(m.adauga(5)==true);
	assert(m.adauga(1)==true);
	assert(m.adauga(10)==true);
	assert(m.adauga(7)==true);
	assert(m.adauga(1)==false);
	assert(m.adauga(10)==false);
	assert(m.adauga(-3)==true);
	assert(m.dim() == 5);
	assert(m.cauta(10) == true);
	assert(m.cauta(16) == false);
	assert(m.sterge(1) == true);
	assert(m.sterge(6) == false);
	assert(m.dim() == 4);

	
	IteratorMultime im = m.iterator();
	im.prim();
	int s = 0;
	while (im.valid()) {
		TElem e = im.element();
		s += e;
		im.urmator();
	}
	assert(s == 19);
}
