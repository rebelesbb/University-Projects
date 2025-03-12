#pragma once
#include "Lista.h"

class IteratorLP{
	friend class Lista;
private:

	Nod* curent;

	IteratorLP(Lista& lista);

	//contine o referinta catre containerul pe care il itereaza
	Lista& lista;

	/* aici e reprezentarea  specifica a iteratorului */

	
public:

		//reseteaza pozitia iteratorului la inceputul containerului
		void prim();

		//muta iteratorul in container
		// arunca exceptie daca iteratorul nu e valid
		void urmator();

		//verifica daca iteratorul e valid (indica un element al containerului)
		bool valid() const;

		//returneaza valoarea elementului din container referit de iterator
		//arunca exceptie daca iteratorul nu e valid
		TElem element() const;

        //elimina si returneaza elementul curent referit de iterator
        //arunca exceptie daca it invalid
        TElem elimina();

};


