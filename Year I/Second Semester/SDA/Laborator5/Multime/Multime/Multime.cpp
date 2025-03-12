#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>

using namespace std;

//o posibila relatie
bool rel(TElem e1, TElem e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

// theta(1)
int Multime::aloca()
{
	int i = primLiber;
	primLiber = stanga[primLiber];
	return i;
}

// theta(1)
void Multime::dealoca(int i)
{
	stanga[i] = primLiber;
	dreapta[i] = -1;
	primLiber = i;
}

//theta(n)
void Multime::redimensionare()
{
	while (1)
		cout << "REDIM";
	int* elemRedim = new int[2 * capacitate];
	int* drRedim = new int[2 * capacitate];
	int* stRedim = new int[2 * capacitate];

	for (int i = 0; i < capacitate; ++i)
	{
		elemRedim[i] = elemente[i];
		stRedim[i] = stanga[i];
		drRedim[i] = dreapta[i];
	}
	for (int i = capacitate; i < 2 * capacitate - 1; ++i)
		stRedim[i] = i + 1, drRedim[i] = -1;

	stRedim[2 * capacitate - 1] = drRedim[2 * capacitate - 1] = -1;
	primLiber = capacitate;
	capacitate *= 2;

	delete[] stanga;
	delete[] dreapta;
	delete[] elemente;

	elemente = elemRedim;
	stanga = stRedim;
	dreapta = drRedim;
}

// theta(n)
Multime::Multime() {

	dimensiune = 0;
	capacitate = 100000;
	elemente = new int[capacitate];
	dreapta = new int[capacitate];
	stanga = new int[capacitate];

	// vom folosi lista stanga si pentru a gestiona spatiul liber
	for (int i = 0; i < capacitate - 1; ++i)
		stanga[i] = i + 1, dreapta[i] = -1;

	//NIL
	dreapta[capacitate - 1] = stanga[capacitate - 1] = -1;

	primLiber = 0;

	radacina = -1;
}

void Multime::afisareCapete()
{
	for (int i = 0; i < 200; ++i)
		cout << i << ": " << elemente[i] << ' ' << stanga[i] << ' ' << dreapta[i] << '\n';
}

/*
Daca adaugam primul element => theta(1)
Daca avem un arbore in care nodul ar trebui adaugat in continuarea celei mai din stanga frunze => theta(n)
Overall:theta(n)
*/
bool Multime::adauga(TElem elem) {

	if (dimensiune == capacitate)
		redimensionare();

	// daca multimea e vida
	if (dimensiune == 0)
	{
		int i = aloca();
		radacina = i;

		elemente[i] = elem;
		stanga[i] =  dreapta[i] = -1;

		dimensiune++;
		return true;
	}

	int p = radacina, prec = -1;

	while (p != -1) 
	{
		if (elemente[p] == elem)
			return false;

		if (rel(elem, elemente[p]))
				prec = p, p = stanga[p]; // daca e mai mic continuam in subarborele stang
		else prec = p, p = dreapta[p]; // daca e mai mare continuam in cel drept
	}

	// daca am parcurs tot arborele inseamna ca nu am gasit elementul, nu a mai fost adaugat
	// deci il adaugam

	int i = aloca();

	// facem lagaturile
	if (rel(elem, elemente[prec]))
		stanga[prec] = i;
	else dreapta[prec] = i;

	elemente[i] = elem;
	stanga[i] = dreapta[i] = -1;

	dimensiune++;
	return true;

}

/*
Deoarece refacerea lagaturilor se executa in timp constant complexitatea tine doar de cautarea elementului de sters
Caz favorabil: theta(1)
Caz defavorabil: theta(n)
Overall: O(n)
*/
bool Multime::sterge(TElem elem) {
	// daca multimea e vida
	if (dimensiune == 0)
		return false;

	int p = radacina, prec = -1;
	while (p != -1) {
		if (elemente[p] == elem) 
		{
			if (dreapta[p] == -1 && stanga[p] != -1) // nu exista subarbore drept
			{ 
				if (prec != -1) { // daca nu este radacina
					if (stanga[prec] == p)
						stanga[prec] = stanga[p];
					else
						dreapta[prec] = stanga[p];
				}
				else {
					radacina = stanga[p]; // daca este radacina
				}
				dealoca(p);
			}
			else if (stanga[p] == -1 && dreapta[p] != -1) { // nu exista subarbore stang
				if (prec != -1) { // daca nu este radacina
					if (stanga[prec] == p)
						stanga[prec] = dreapta[p];
					else
						dreapta[prec] = dreapta[p];
				}
				else {
					radacina = dreapta[p];
				}
				dealoca(p);
			}
			else if (stanga[p] == -1 && dreapta[p] == -1) { // nu exista niciun subarbore
				if (prec == -1) { // daca e radacina
					radacina = -1;
					primLiber = 0;
				}
				else {
					if (stanga[prec] == p)
						stanga[prec] = -1;
					else
						dreapta[prec] = -1;
				}
				dealoca(p);
			}
			else { // exista atat subarbore stang cat si subarbore drept
				// cautam valoarea minima din subarborele drept al elementului pe care il stergem
				int k = dreapta[p], precK = p;
				while (stanga[k] != -1) {
					precK = k;
					k = stanga[k];
				}
				// mutam valoarea în locul lui p
				elemente[p] = elemente[k];

				// stergem valoarea de pe pozitia initiala
				if (dreapta[k] != -1) {
					if (precK == p)
						dreapta[precK] = dreapta[k];
					else
						stanga[precK] = dreapta[k];
				}
				else {
					if (precK == p)
						dreapta[precK] = -1;
					else
						stanga[precK] = -1;
				}
				dealoca(k);
			}

			dimensiune--;
			return true;
		}

		prec = p;
		if (rel(elem, elemente[p]))
			p = stanga[p];
		else
			p = dreapta[p];
	}

	return false;

	/*
	// daca multimea e vida nu exista elemente
	if (dimensiune == 0)
		return false;

	int p = radacina, prec = -1;

	while (p != -1)
	{
		if (elemente[p] == elem)
		{
			if(dreapta[p] == -1 && stanga[p] != -1) // nu exista subarbore drept
			{
				cout << "a";
				if (prec != -1) // daca nu este radacina
					stanga[prec] = stanga[p];
				else  radacina = stanga[p]; // daca este radacina

				dealoca(p);
			}
			else if (stanga[p] == -1 && dreapta[p] != -1) // nu exista subarbore stang
			{
				cout << "b";
				if (prec != -1) // daca nu este radacina
					dreapta[prec] = dreapta[p];
				else radacina = dreapta[p];

				dealoca(p);
			}
			else if (stanga[p] == -1 and dreapta[p] == -1) // nu exista niciun subarbore
			{
				if (prec == -1) // daca e radacina
				{
					cout << "r";
					radacina = -1;
					primLiber = 0;
					dealoca(p);
					dimensiune--;
					return true;
				}
				else { // altfel
					if (rel(elemente[p], elemente[prec]))
						stanga[prec] = -1;
					else dreapta[prec] = -1;
					cout << "c " <<p<<' '<<prec << ' ' << elemente[prec] << ' ' << stanga[prec] << ' ' << dreapta[prec] << '\n';
					dealoca(p);
				}
			}
			else // daca exista atat subarbore stang cat si drept
			{
				cout << "x";
				// cautam valoarea minima din subarborele drept
				//cout << "p: " << p << '\n';
				int k = dreapta[p], precK = p;
				//cout << "k = " << k <<'\n';
				while (stanga[k] != -1)
				{
					precK = k, k = stanga[k]; // valoarea minima va fi mereu pe o ramura care porneste spre stanga
				}

				// mutam valoarea in locul lui p
				elemente[p] = elemente[k];

				//stergem valoarea de pe pozitia initiala
				if (dreapta[k] != -1)
					if (precK == p)
						dreapta[precK] = dreapta[k];
					else stanga[precK] = dreapta[k];
				dealoca(k);
			}

			dimensiune--;
			return true;
		}

		if (rel(elem, elemente[p]))
			prec = p, p = stanga[p];
		else prec = p, p = dreapta[p];
	}

	return false;*/
}

/*
Daca elementul este radacina => theta(1)
Daca elementul este frunza si este cel mai mare sau cel mai mic=> theta(n)
Overall: O(n)
*/
bool Multime::cauta(TElem elem) const {
	
	if (dimensiune == 0)
		return false;

	int p = radacina;
	while (p != -1)
	{
		if (elemente[p] == elem)
			return true;
		if (rel(elem, elemente[p]))
			p = stanga[p];
		else p = dreapta[p];
	}

	return false;
}

// theta(1)
int Multime::dim() const {
	return dimensiune;
}


// theta(1)
bool Multime::vida() const {
	if(dimensiune == 0) 
		return true;
	return false;
}

// Daca arborele are un singur element sau e vid => theta(1)
// Daca avem un arbore cu toate elementele pe subarbori din stanga sau din dreapta => theta(n) ex daca adaugam 5 4 3 2 1 in aceasta ordine
int Multime::diferentaMaxMin() const
{
	if (vida())
		return -1;

	int indexMin = radacina, indexMax = radacina;

	// valoarea minima este de fapt cea mai din stanga frunza a arborelui
	while (stanga[indexMin] != -1)
		indexMin = stanga[indexMin];
	
	// valoarea maxima este de fapt cea mai din dreapta frunza a arborelui
	while (dreapta[indexMax] != -1)
		indexMax = dreapta[indexMax];

	return elemente[indexMax] - elemente[indexMin];
}
/*
Subalgoritm diferentaMaxMin()
	Daca vida() = true atunci
		diferentaMaxMin <- -1
	SfDaca

	indexMin <- radacina
	indexMax <- radacina

	Cat timp stanga[indexMin] != -1 executa
		indexMin = stanga[indexMin]
	SfCatTimp

	Cat timp dreapta[indexMax] != -1 executa
		indexMax = dreapta[indexMax]
	SfCatTimp

	diferentaMaxMin <- (elemente[indexMax] - elemente[indexMin])
*/

// crearea iteratorului dureaza theta(log2(n)) => theta(log2(n))
IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

// theta(n)
Multime::~Multime() {
	delete[] elemente;
	delete[] dreapta;
	delete[] stanga;
}






