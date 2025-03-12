#pragma once

typedef int TElem;

typedef bool(*Relatie)(TElem, TElem);

//in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorMultime;

class Multime {

	friend class IteratorMultime;

private:
	/* aici e reprezentarea */
	int capacitate, dimensiune;

	int radacina;
	
	int* elemente;
	int* stanga;
	int* dreapta;

	int primLiber;

	// furnizeaza indicele unei locatii de spatiu libere
	// actualizeaza lista spatiului liber
	int aloca();

	// trece pozitia i in lista spatiului liber
	// aceasta se adauga la inceputul listei sptiului liber
	void dealoca(int i);

	// se ocupa de redimensionarea multimii
	// mai exact a vectorilor stanga, drapta si elemente
	void redimensionare();


public:
		//constructorul implicit
		Multime();

		void afisareCapete();

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

		int diferentaMaxMin() const;

		//returneaza un iterator pe multime
		IteratorMultime iterator() const;

		// destructorul multimii
		~Multime();

};

