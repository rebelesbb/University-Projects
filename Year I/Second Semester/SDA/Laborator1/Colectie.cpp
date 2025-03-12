#include "Colectie.h"
#include "IteratorColectie.h"

///Pentru complexitati n = nr. de elemente distincte, nu dimensiunea

/*
 * T(n) = 1 + 1 + n + 1 + 1 = n + 4 => theta(n)
 */
void Colectie::redimensionare() {
    this->capacitate = 2 * this->capacitate;
    Pereche *colectie_noua;
    colectie_noua = new Pereche [this->capacitate];
    for(int i = 0; i < numar_valori_distincte; i++)
        colectie_noua[i] = this->colectie[i];

    delete colectie;

    colectie = colectie_noua;
}
/*
 * T(n) = 3 => theta(1)
 */
Colectie::Colectie() {
	colectie = new Pereche [this->capacitate];
    this->dimensiune = 0;
    this->numar_valori_distincte = 0;
}

/*
 * Daca elementul exista deja in colectie
 *  => T(n) = i + 3, pentru adaugarea nodului i={1, ..., n}
 *      Daca elementul e primul in colectie => T(n) = 4 => theta(1) (caz favorabil)
 * altfel (cazuri defavorbil)
 *  Daca vectorul nu necesita redimensionare
 *   => T(n) = n + 5 => theta(n)
 *  altfel (parcurgere + redimensionare)
 *   Atat => theta(n) + theta(n) = theta(n)
 *  overall: O(n)
 */
void Colectie::adauga(TElem elem) {
    bool adaugat = false;

    for(int i = 0; i < numar_valori_distincte; i++)
        if(colectie[i].element == elem) {
            colectie[i].frecventa++;
            adaugat = true;
            dimensiune++;
            break;
        }

    if(!adaugat) {
        if(numar_valori_distincte >= capacitate - 1)
            redimensionare();

        Pereche element_nou;
        element_nou.element = elem;
        element_nou.frecventa = 1;

        colectie[numar_valori_distincte] = element_nou;
        dimensiune++;
        numar_valori_distincte++;
    }
}

/*
 * Pozitia elementului in colectie influenteaza complexitatea
 * Daca elementul apare de mai multe ori (cel putin 2) in colectie decrementam frecventa
 *      => T(n) = i + 3 pentru stergerea nodului de pe pozitia i, i={1, ..., n}
 *      Daca i = 1 => T(n) = 4 => theta(1) (caz favorabil)
 *      Daca i = n => T(n) = n + 3 => theta(n) (caz defavorabil)
 * altfel => T(n) = i + 1 + 1 + (n - i) = n + 2 pentru stergerea nodului de pe pozitia i, i={1, ..., n}
 *        => theta(n)
 *        (primul i reprezinta parcurgerea primelor i elemente, urmate de mutarea urmatoarelor cu o pozitie la stanga)
 *
 * overall: O(n)
 */
bool Colectie::sterge(TElem elem) {
    for(int i = 0; i < numar_valori_distincte; i++)
        if(colectie[i].element == elem) {
            if (colectie[i].frecventa > 1) {
                colectie[i].frecventa--;
                dimensiune--;
                return true;
            } else {
                for(int j = i; j < numar_valori_distincte - 1; j++)
                    colectie[j] = colectie[j + 1];
                dimensiune--;
                numar_valori_distincte--;
                return true;
            }
        }

	return false;
}

/*
 * Daca elementul e primul in colectie => theta(1)
 * Daca elementul e ultimul in colectie => theta(n)
 *   => overall: O(n)
 */
bool Colectie::cauta(TElem elem) const {
	for(int i = 0; i < numar_valori_distincte; i++)
        if(colectie[i].element == elem)
            return true;
	return false;
}

/*
 * Daca elementul e primul in colectie => theta(1) (caz favorabil)
 * Daca elementul e ultimul in colectie => theta(n) (caz defavorabil)
 *   => overall: O(n)
 */
int Colectie::nrAparitii(TElem elem) const {
    for(int i = 0; i < numar_valori_distincte; i++)
        if(colectie[i].element == elem)
            return colectie[i].frecventa;
	return 0;
}

/*
 * T(n) = 1 => theta(1)
 */
int Colectie::dim() const {
	return this->dimensiune;
}

/*
 * T(n) = 1 => theta(1)
 */
bool Colectie::vida() const {
	if(dimensiune == 0)
        return true;
    return false;
}

/*
 * T(n) = 1 => theta(1)
 */
IteratorColectie Colectie::iterator() const {
	return  IteratorColectie(*this);
}

/*
 * T(n) = n => theta(n)
 */
Colectie::~Colectie() {
	delete this->colectie;
}


/*
 * Daca toate elementele apar o singura data doar se parcurge colectia
 *   => T(n) = n => theta(n) (caz favorabil)
 * Daca toate elementele apar de cel putin doua ori in colectie
 *   => T(n) = n * (1 + 1) = 2 * n => theta(n)
 * Overall: theta(n)
 */
int Colectie::transformaInMultime()
{
    int numar_valori_eliminate = 0;
    for(int index = 0; index < this->numar_valori_distincte; ++index)
    {
        if(this->colectie[index].frecventa > 1)
        {
            numar_valori_eliminate += (colectie[index].frecventa - 1);
            colectie[index].frecventa = 1;
        }
    }
    return numar_valori_eliminate;
}

/**
 * Subalgoritm transformaInMultime()
 *
 *      numar_valori_eliminate <- 0 {numar_valori_eliminate: int}
 *
 *      Pentru index <- 0, numar_valori_distincte executa
 *          Daca colectie[index].frecventa > 1 atunci
 *
 *              numar_valori_eliminate <- numar_valori_eliminate + (colectie[index].recventa - 1)
 *              colectie[index].frecventa <- 1
 *          SfDaca
 *      SfPentru
 *
 *      transformaInMultime <- numar_valori_eliminate
 *
 * SfSubalgoritm
 */


//next: lab3

