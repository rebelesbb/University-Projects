#pragma once

#define NULL_TELEM -1
typedef int TElem;

class IteratorColectie;

typedef struct{
    TElem element;
    int frecventa;
}Pereche;

class Colectie
{
	friend class IteratorColectie;

private:
    int capacitate = 10;
    int dimensiune;
    int numar_valori_distincte;
	Pereche *colectie;
    void redimensionare();
public:
		//constructorul implicit
		Colectie();

		//adauga un element in colectie
		void adauga(TElem e);

		//sterge o aparitie a unui element din colectie
		//returneaza adevarat daca s-a putut sterge
		bool sterge(TElem e);

		//verifica daca un element se afla in colectie
		bool cauta(TElem elem) const;

		//returneaza numar de aparitii ale unui element in colectie
		int nrAparitii(TElem elem) const;

		//intoarce numarul de elemente din colectie;
		int dim() const;

		//verifica daca colectia e vida;
		bool vida() const;

        //pastreaza doar o aparitie a tuturor elementelor din colectie
        //returneaza numarul de elemente eliminate
        int transformaInMultime();

		//returneaza un iterator pe colectie
		IteratorColectie iterator() const;

		// destructorul colectiei
		~Colectie();

};

