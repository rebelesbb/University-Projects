% stergeSecvente(L: list, DeSters: integer, Rez: list)
% Sterge secventele de valori consecutive din lista data.
% Modele de flux: (i, i, o), (i, i, i).
%
% L: lista initiala de valori
% DeSters: valoare intreaga cu scop de flag, avand valorile:
%          1 daca valoarea precedenta celei curente a fost stearsa
%          0 altfel
% Rez: lista rezultata in urma stergerii secventelor
%
stergeSecvente([],_,[]):-!.
stergeSecvente([_],1,[]):-!.
stergeSecvente([H],0,[H]):-!.

stergeSecvente([L1, L2| T],_,Rez):-
    L2 =:= L1 + 1,
    !,
    stergeSecvente([L2 | T], 1, Rez).

stergeSecvente([L1, L2 | T], 0, [L1 | Rez]):-
    L2 =\= L1 + 1,
    !,
    stergeSecvente([L2 | T], 0, Rez).

stergeSecvente([L1, L2 | T], 1, Rez):-
    L2 =\= L1 + 1,
    stergeSecvente([L2 | T], 0, Rez).

% sterge(L: list, Rez: list)
% Sterge secventele de valori consecutive din lista data.
% Modele de flux: (i, o), (i, i)
%
% L: lista din care se sterg secventele de valori consecutive
% Rez: lista rezultata in urma stergerii secventelor de valori
% consecutive
%
sterge(L, Rez):-
    stergeSecvente(L, 0, Rez).

% -----------------------------------------------------------------

% stergeDinSubliste(L: list, Rez: list)
% Sterge secventele de valori crescatoare din toate sublistele listei
% date.
% Modele de flux: (i, o), (i, i).
%
% L: lista eterogena de numere intregi si liste de numere intregi
% Rez: lista rezultata in urma stergerii secventelor de valori
% crescatoare din sublistele lui L
%
stergeDinSubliste([], []):-!.
stergeDinSubliste([H | T], [H | Rez]):-
    not(is_list(H)),
    !,
    stergeDinSubliste(T, Rez).
stergeDinSubliste([H | T], [NewH | Rez]):-
    is_list(H),
    !,
    sterge(H, NewH),
    stergeDinSubliste(T, Rez).
