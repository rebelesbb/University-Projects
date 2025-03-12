#include "MD.h"
#include "IteratorMD.h"
#include <exception>
#include <iostream>

using namespace std;

/**
 * m - capcaitatea initiala
 * T(m) = 5 + m + 2 = m + 7 => theta(m)
 */
MD::MD() {
	capacitate = 1;
	elemente = new TElem[capacitate];
	lungime = 0;
	
	urm = new int[capacitate];
	prec = new int[capacitate];

	/// prim = 0 => tot spatiul e liber
	initSpatiuLiber(0);

	prim = ultim = -1;
}

/**
 * m - capacitatea
 * T(m) = 3 + m + 2 + 2 * m + 2 * m + m = 5 * m + 5 => theta(m)
 *	      eliberarea spatiului--^--  -^--initializare spatiu liber
 */
void MD::redimensionare()
{
	int capacitateVeche = capacitate;
	capacitate = 2 * capacitate;
	TElem* elementeRedim = new TElem[capacitate];

	for (int index = 0; index < capacitateVeche; ++index)
	{
		elementeRedim[index] = elemente[index];
	}
	delete[] elemente;
	elemente = elementeRedim;

	int *urmRedim, *precRedim;
	urmRedim = new int[capacitate];
	precRedim = new int[capacitate];

	for (int index = 0; index < capacitateVeche; ++index)
	{
		urmRedim[index] = urm[index];
		precRedim[index] = prec[index];
	}
	delete[] urm;
	delete[] prec;

	urm = urmRedim;
	prec = precRedim;

	/// se initializeaza spatiul liber
	/// adica cel de la capacitatea veche pana la cea noua
	initSpatiuLiber(capacitateVeche);

}

/**
 * Daca consideram m capacitatea dictionarului => T(m) = m + 2 => theta(m)  
 */
void MD::initSpatiuLiber(int primL)
{
	/// initializarea spatiului liber

	/// am adaugat parametrul prim pentru a putea 
	/// utiliza functia in cazul redimensionarii putin mai optim
	for (int i = primL; i < capacitate - 1; ++i)
	{
		urm[i] = i + 1;
	}

	urm[capacitate - 1] = -1;

	primLiber = primL;
}

/**
 * theta(1) 
 */
int MD::aloca()
{
	int index = primLiber;
	primLiber = urm[primLiber];
	return index;
}

/**
 * theta(1)
 */
void MD::dealoca(int index)
{
	urm[index] = primLiber;
	primLiber = index;
}

/**
 * n - dimensiune/lungime 
 * Caz favorabil: nu este nevoie de redimensionare => theta(1) (ramane constant chiar si daca trebuie sa adaugam primul element)
 * Caz defavorabil: dictionarul necesita redimensionare ( n == m )
 *		=> T(n) = n + 9 => theta(n)
 * Overall: O(n)
 */
void MD::adauga(TCheie c, TValoare v) 
{		

	if (lungime == capacitate)
		redimensionare();

	TElem nod;
	nod.first = c, nod.second = v;

	int nodNou = aloca();
	elemente[nodNou] = nod;
	prec[nodNou] = -1;
	urm[nodNou] = prim;

	// adaugam la inceput

	// in cazul in care se adauga primul nod
	// setam si valoarea lui ultim catre acelasi nod
	if (prim == -1)
	{
		ultim = nodNou;
	}
	else {
		prec[prim] = nodNou;
	}
	
	prim = nodNou;
	lungime++;

}

/**
 * Caz favorabil: elementul care trebuie sters este primul sau ultimul din dictionar => theta(1)
 * Caz defavorabil: elementul n - 1 trebuie sters => T(n) = (n - 1) + 4 = n + 3 => theta(n)
 * Overall: O(n)
 */
bool MD::sterge(TCheie c, TValoare v) {

	int index = prim;
	while (index != -1 && !(elemente[index].first == c && elemente[index].second == v))
		index = urm[index];

	if (index != -1)
	{

		if (index == prim)
		{
			if (lungime != 1) {
				prim = urm[prim];
				prec[prim] = -1;
			}
			else prim = ultim = -1;
		}
		else if (index == ultim)
		{
			ultim = prec[ultim];
			urm[ultim] = -1;
		}
		else {
			urm[prec[index]] = urm[index];
			prec[urm[index]] = prec[index];
		}
		dealoca(index);
		lungime--;
		return true;
	}
	return false;
	
}

/**
 * Indiferent de pozitionarea elementului in dictionar, este necesara parcurgerea intregului continut
 *   => theta(n)
 */
vector<TValoare> MD::cauta(TCheie c) const {
	vector<TValoare> valoriAsociate;
	
	int index = prim;
	
	while (index != -1)
	{
		if (elemente[index].first == c)
			valoriAsociate.push_back(elemente[index].second);
		index = urm[index];
	}
	
	return valoriAsociate;
}

/**
 * theta(1)
 */
int MD::dim() const {
	return lungime;
}

/**
 * theta(1)
 */
bool MD::vid() const {
	if(!lungime)
		return true;
	return false;
}

/**
 * theta(1)
 */
IteratorMD MD::iterator() const {
	return IteratorMD(*this);
}

/**
 * theta(3)
 */
MD::~MD() {
	delete[] elemente;
	delete[] prec;
	delete[] urm;
}

/**
 * m - dimensiunea lui d
 * n - dimensiunea dictionarului nostru
 * Caz favorabil: theta(m) - daca d are acelasi element, pe prima pozitie in md
 * Caz defavorabil: theta(n*m) - daca niciun element din d nu exista in md
 * Overall: O(n*m)
 */
int MD::adaugaInexistente(MD& d)
{
	int cnt = 0;
	IteratorMD dIt = d.iterator();

	while (dIt.valid())
	{
		TElem element = dIt.element();
		int index = prim;
		bool exista = false;
		while (index != -1)
		{
			if (elemente[index].first == element.first && elemente[index].second == element.second)
			{
				exista = true;
				break;
			}
			index = urm[index];
		}

		if (!exista)
			this->adauga(element.first, element.second), cnt++;
		dIt.urmator();
	}

	return cnt;
}

/*
Subalgoritm adaugaInexistente(d)
	{ element : Telem, dIt: IteratorMD}
	cnt <- 0;
	dIt <- d.iterator();

	Cat timp dIt.valid() executa
		element <- dIt.element()
		index <- prim
		exista <- false
		Cat timp index != -1 executa
			Daca ( elemente[index].c = element.c ) si ( elemente[index].c = element.c ) atunci
			{
				exista = true;
				break;
			}
			index = urm[index];
		}

		if (!exista)
			this->adauga(element.first, element.second), cnt++;
		dIt.urmator();
	}

	return cnt;
	


*/


