% checkEvenS(L: list, isEven: int)
% Verifica daca o lista data are numar par de elemente
% Modele de flux: (i, i), (i, o)
%
% L: lista data, pentru care verificam daca are numar
%    par de elemente
% isEven: valoare intreaga cu scop de flag, avand valorile:
%    - 1, daca lista are numar par de elemente
%    - 0, altfel
checkEvenS([], 1):-!.
checkEvenS([_ | T], 1):-
    !,
    checkEvenS(T, 0).
checkEvenS([_ | T], 0):-
    checkEvenS(T, 1).

% checkEvenSize(L: list)
% Verifica daca o lista data are numar par de elemente
% Modele de flux: (i)
%
% L: lista data, pentru care verificam daca are numar
%    par de elemente
checkEvenSize(L):-
    checkEvenS(L, 1).

%----------------------------------------------------------------------

% minOf(X: int, Y: int, Result: int)
% Determina valoarea minima dintre doua valori intregi date
% Modele de flux: (i, i, o), (i, i, i)
%
% X: prima valoare data, de comparat
% Y: a doua valoare data, de comparat
% Result: valoarea mai mare (maxima) dintre cele doua valori date
minOf(X, Y, X):-
    X < Y,
    !.
minOf(_, Y, Y).

% minOfList(L: list, Min: int)
% Determina elementul minim dintr-o lista de valori intregi
% Modele de flux: (i, o), (i, i)
%
% L: lista din care vrem sa determinam elementul cu valoarea minima
% Min: elementul cu valoarea minima din lista data
minOfList([InitMin], InitMin):-!.
minOfList([H | T], Min):-
    minOfList(T, PreviousMin),
    minOf(H, PreviousMin, Min).

% deleteFirst(L: list, Elem: int, Result: list)
% Sterge prima apaitie a unui element dintr-o lista de numere intregi
% Modele de flux: (i, i, o), (i, i, i), (i, o, i).
%
% L: lista din care se va sterge prima apraitie a elementului
% Elem: elementul a carui prima aparitie dorim sa o stergem
% Result: lista rezultata in urma stergerii
deleteFirst([E | T], E, T):-!.
deleteFirst([H | T], E, [H | Res]):-
    deleteFirst(T, E, Res).

% deleteFirstOfMin(L: list, Result: list)
% Sterge prima aparitie a elementului minim dintr-o lista
% Modele de flux: (i, o), (i, i)
deleteFirstOfMin(L, Res):-
    minOfList(L, Min),
    deleteFirst(L, Min, Res).
