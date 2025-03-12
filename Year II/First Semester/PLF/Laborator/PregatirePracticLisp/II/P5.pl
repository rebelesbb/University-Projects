% maxOf(X: int, Y: int, Result: int)
% Determina valoarea maxima (mai mare), dintre doua valori date
% Modele de flux: (i, i, i), (i, i, o)
%
% X: prima valoare de comparat
% Y: a doua valoare de comaparat
% Result: valoarea mai mare dintre cele doua valori furnizare
maxOf(X, Y, X):-
    X > Y,
    !.
maxOf(_, Y, Y).


% maxim(L: list, Max: int)
% Determina valoarea elemetului maxim dintr-o lissta de numere intregi
% Modele de flux: (i, o), (i, i)
%
% L: lista din care dorim sa determinam valoarea maxima
% Max: valoarea elementului maxim din lista data
%
maxim([InitMax], InitMax):-!.
maxim([H | T], Max):-
    maxim(T, PreviousMax),
    maxOf(H, PreviousMax, Max).

% positions(L: list, Elem: int, Count: int, Positions: list)
% Determina pozitiile unui element intreg dat intr-o lista de intregi
% Modele de flux: (i, i, i, o), (i, i, i, i), (i, o, i, i)?
%
% L: lista din care determinam pozitiile elementului dat
% Elem: elementul ale carui pozitii in lista data dorim sa le aflam
% Positions: pozitiile elementului in lista
%
positions([], _, _, []):-!.
positions([E | T], E, Count, [Count | Res]):-
    !,
    NewCount is Count + 1,
    positions(T, E, NewCount, Res).
positions([_ | T], E, Count, Res):-
    NewCount is Count + 1,
    positions(T, E, NewCount, Res).

% maxPositions(L: list, Positions: list)
% Determina pozitiile elementului maxim dintr-o lista
% Modele de flux: (i, o), (i, i)
%
% L: lista in care dorim determinarea pozitiilor elementului maxim
% Positions: pozitiile elementului maxim in lista

maxPositions(L, Positions):-
    maxim(L, Max),
    positions(L, Max, 1, Positions).
