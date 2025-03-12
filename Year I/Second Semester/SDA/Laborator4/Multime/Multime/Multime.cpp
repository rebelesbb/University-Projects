#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>

/**
 * theta(1)
 */
int Multime::d(int c) const
{
	return abs(c%m); // dispersie prin diviziune
}

/**
 * theta(m)
 */
Multime::Multime(){
	m = 3;
	elems = new int[m];
	urm = new int[m];
	for (int i = 0; i < m; ++i)
	{
		elems[i] = NULL_TELEM;
		urm[i] = -1;
		// initializam spatiul liber
	}
	primLiber = 0;
}

/**
 * theta(m)
 */
void Multime::redimensionare()
{
	int* elemsRedim = new int[2 * m];
	int* urmRedim = new int[2 * m];


	for (int i = 0; i < 2 * m; ++i) {
		urmRedim[i] = -1;
		elemsRedim[i] = NULL_TELEM;
	}

	delete[] urm;

	urm = urmRedim;

	int mV = m;
	primLiber = 0;
	m *= 2;
	for (int i = 0; i < mV; ++i) {
		int j = d(elems[i]);
		if (elemsRedim[j] == NULL_TELEM)
		{
			elemsRedim[j] = elems[i];
			if(j == primLiber)
			{
				primLiber++;
				while (primLiber < m and elemsRedim[primLiber] != NULL_TELEM)
					primLiber++;
			}
		}
		else {
			int k = -1;
			while (j != -1 and elemsRedim[j] != elems[i])
				k = j, j = urm[j];
			urm[k] = primLiber;
			elemsRedim[primLiber] = elems[i];
			
			primLiber++;
			while (primLiber < m and elemsRedim[primLiber] != NULL_TELEM)
				primLiber++;
			
		}
	}
	delete[] elems;
	elems = elemsRedim;
}

/**
 * m - capacitatea tabelei de dispersie
 * Caz favorabil: theta(1)
 * Caz defavorabil: theta(m)
 * Overall: O(m)
 */
void Multime::actualizarePrimLiber()
{
	primLiber++;
	while (primLiber < m and elems[primLiber] != NULL_TELEM)
		primLiber++;
}

/**
 * Caz favorabil: theta(1) primLiber == d(elem)
 * Caz defavorabil: theta(m) 
 *	exemplu: vrem da adaugam valoarea 0 iar tabela are o sg locatie libera, si toate celelalte m-1 elemente au valoarea de dispersie 0
 * Overall: O(m)
 * Conform SUH: theta(1)
 */
bool Multime::adauga(TElem elem) {
	if (primLiber == m)
		redimensionare();

	int i = d(elem); // valoarea de dispersie a elementului

	if (elems[i] == NULL_TELEM) // locatie libera
	{
		elems[i] = elem;
		if (i == primLiber)
			actualizarePrimLiber();
	}
	else if (elems[i] == elem)
		return false;
	else
	{
		int j = -1;
		while (i != -1)
			if (elems[i] != elem)
				j = i, i = urm[i];
			else break;
		if (i != -1)
			return false;
		urm[j] = primLiber;
		elems[primLiber] = elem;
		actualizarePrimLiber();
	}
	dimensiune++;
	//std::cout << elem << '\n';
	return true;
}

/**
 * Caz favorabil: theta(1) 
 *	Exemple: - elementul nu exista in multime si nu exista nicio alta valoare pe pozitia corespunazatoare valorii
 *			 sale de dispersie
 *			 - elementul se afla chiar pe pozitia de dispersie si nu mai exista alte elemente care sa aiba valoarea resp de disp
 * Caz defavorabil: theta(m) daca toate elementele au aceeasi valoare de dispersie dar sunt distincte
 *			iar elementul e ultimul adaugat
 * Overall: O(m)
 * Conform SUH: theta(1)
 */
bool Multime::sterge(TElem elem) {
	int i = d(elem); // valoarea de dispersie a elementului
	int j = -1; // anteriorul elementului elem

	while (i != -1 and elems[i] != elem)
		j = i, i = urm[i];
	if (i == -1) // elementul nu exista in multime
	{
		return false;
	}
	else {
		bool gata = false;
		do {
			int p = urm[i], pp = i;
			while(p != -1 and d(elems[p]) != i)
			{
				pp = p;
				p = urm[p];
			}
			if (p == -1)
				gata = true;
			else {
				elems[i] = elems[p];
				i = p;
				j = pp;
			}
		} while (!gata);

		if (j == -1)
		{
			int k = 0;
			while (k < m and urm[k] != i)
				k++;
			if (k < m)
				j = k;
		}

		if (j != -1)
			urm[j] = urm[i];
		elems[i] = NULL_TELEM;
		urm[i] = -1;
		

		if (i < primLiber) primLiber = i;
	}
	dimensiune--;
	return true;
}

/**
 * Caz favorabil: theta(1) elem se afla pe val de disp sau -1 acolo
 * Caz defavorabil: theta(m)daca toate elementele au aceeasi valoare de dispersie dar sunt distincte
 *			iar elementul e ultimul adaugat
 * Overall: O(m)
 * Conform SUH: theta(1) 
 */
bool Multime::cauta(TElem elem) const {
	int i = d(elem);
	if (!dimensiune) return false;
	while (i != -1)
		if (elems[i] == elem)
			return true;
		else i = i[urm];
	return false;
}

/**
 * theta(1) 
 */
int Multime::dim() const {
	return dimensiune;
}

/**
 * theta(1) 
 */
bool Multime::vida() const {
	return dimensiune == 0;
}

/**
 * theta(n)
 */
Multime::~Multime() {
	delete[] elems;
	delete[] urm;
}

/**
 * Complexitatea operatiei tine de complexitatea op de adaugare
 * n - dimensiunea lui b
 * Caz favorabil: theta(n)
 * Caz defavorabil: theta(m*n)
 * Overall: O(m*n)
 */
void Multime::reuniune(const Multime& b)
{
	IteratorMultime itB = b.iterator();
	while (itB.valid())
	{
		TElem elem = itB.element();
		adauga(elem);
		itB.urmator();
	}
}

/*
Subalgoritm reuniune(b: multime)
	itB <- b.iterator()
	Cat Timp itB.valid() executa
		elem <- itB.element()
		adauga(elem) {functia de adaugare din multimea curenta}
		itB.urmator()
	SfCatTimp
*/


IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

