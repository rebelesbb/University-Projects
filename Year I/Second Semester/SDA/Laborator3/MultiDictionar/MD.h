#pragma once
#include<vector>
#include<utility>

using namespace std;

typedef int TCheie;
typedef int TValoare;

typedef std::pair<TCheie, TValoare> TElem;

class IteratorMD;

class MD
{
	friend class IteratorMD;

private:
	TElem* elemente;
	int capacitate;
	int lungime;

	int prim;
	int ultim;

	int primLiber;
	int* prec;
	int* urm;

	void initSpatiuLiber(int prim);
	void redimensionare();

	// furnizeaza un spatiu liber, returneaza indexul corespunzator
	int aloca();

	// trece pozitia index in lista spatiului liber
	void dealoca(int index);


public:
	// constructorul implicit al MultiDictionarului
	MD();

	// adauga o pereche (cheie, valoare) in MD	
	void adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza vectorul de valori asociate
	vector<TValoare> cauta(TCheie c) const;

	//sterge o cheie si o valoare 
	//returneaza adevarat daca s-a gasit cheia si valoarea de sters
	bool sterge(TCheie c, TValoare v);

	//returneaza numarul de perechi (cheie, valoare) din MD 
	int dim() const;

	//verifica daca MultiDictionarul e vid 
	bool vid() const;

	// se returneaza iterator pe MD
	IteratorMD iterator() const;

	int adaugaInexistente(MD& d);

	// destructorul MultiDictionarului	
	~MD();



};

