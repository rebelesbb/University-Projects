#pragma once

#define NULL_TELEM -2000000000
typedef int TElem;

class IteratorMultime;

class Multime {
	friend class IteratorMultime;

    private:
		int m; // dimensiunea tabelei de dispersie (cheile din reprezentare)
		int d(int c) const; // functia de dispersie
		int* elems; // valorile efective memorate in multime
		int* urm; // reprezinta spatiul alocat 
		int primLiber; // prima locatie de memorie libera

		void redimensionare();
		void actualizarePrimLiber();

		int dimensiune = 0;

    public:
 		//constructorul implicit
		Multime();

		//adauga un element in multime
		//returneaza adevarat daca elementul a fost adaugat (nu exista deja in multime)
		bool adauga(TElem e);

		//sterge un element din multime
		//returneaza adevarat daca elementul a existat si a fost sters
		bool sterge(TElem e);

		//verifica daca un element se afla in multime
		bool cauta(TElem elem) const;

		//intoarce numarul de elemente din multime;
		int dim() const;

		//verifica daca multimea e vida;
		bool vida() const;

		//adauga toate elementele din multimea b in multimea curenta
		void reuniune(const Multime& b);

		//returneaza un iterator pe multime
		IteratorMultime iterator() const;

		// destructorul multimii
		~Multime();
};




