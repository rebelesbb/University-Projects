% areDivizori(X: int, D: int)
% Verifica daca un numar are divizori.
% Modele de flux: (i, i)
%
% X: numarul dat pentru care dorim sa verificam daca are divizori
% D: numarul curent pe care il verificam daca este divizorul lui X
areDivizori(X, D):-
    X mod D =:= 0,
    !.

areDivizori(X, D):-
    D * D =< X,
    NewD is D + 1,
    areDivizori(X, NewD).

% estePrim(X: int)
% Verifica daca un numar este prim
% Modele de flux: (i)
%
% X: numarul dat, care se verifica daca este prim
estePrim(2):-!.
estePrim(X):-
    X >= 2,
    not(areDivizori(X, 2)).


% getDivizori(X: int, D: int, Divizori: list)
% Determina lisat tuturor divizorilor unui numar dat
% Modele de flux: (i, i, o), (i, i, i)
%
% X: numarul a carui lista de divizori dorim sa o determinam
% D: numarul curent pe care il verificam daca este divizor al lui X
% Divizori: lista divizorilor numarului dat
getDivizori(0, 1, []):-!.
getDivizori(X, X, [X]):-!.
getDivizori(X, D, [D | Divs]):-
    D =< X,
    X mod D =:= 0,
    !,
    NewD is D + 1,
    getDivizori(X, NewD, Divs).
getDivizori(X, D, Divs):-
    D =< X,
    NewD is D + 1,
    getDivizori(X, NewD, Divs).

% adaugaLaLista(ListaDeAdaugat: list, ListaInitiala: lista,
% ListaFinala: list)
% Adauga elementele unei liste la o alta lista
% Modele de flux: (i, i, o), (i, i, i)
%
% ListaDeAdaugat: lista a carei elemente dorim sa le adaugam la o alta
% lista
% ListaInitiala: lista initiala la care dorim sa adaugam elementele
% celeilalte lista
% ListaFinala: lista rezultata in urma adaugarii elementelor
adaugaLaLista([], L, L):-!.
adaugaLaLista([H | T], L, [H | Result]):-
    adaugaLaLista(T, L, Result).


% adaugaDupaNeprim(ListaInitiala: list, ListaFinala: list)
% Adauga dupa fiecare numar dintr-o lista, care nu este prim, toti
% divizorii acestuia
% Modele de flux: (i, i), (i, o)
%
% ListaInitiala: lista data in care se vor adauga divizorii numerelor
% care nu sunt prime, dupa acestea
% ListaFinala: lista rezultata in urma adaugarii divizorilor numerelor
% care nu sunt prime dupa acesteaa
adaugaDupaNeprim([], []):-!.
adaugaDupaNeprim([H | T], [H | ListaNoua]):-
    not(estePrim(H)),
    !,
    getDivizori(H, 1, Divizori),
    adaugaDupaNeprim(T, ListaPrec),
    adaugaLaLista(Divizori, ListaPrec, ListaNoua).
adaugaDupaNeprim([H | T], [H | ListaPrec]):-
    adaugaDupaNeprim(T, ListaPrec).
