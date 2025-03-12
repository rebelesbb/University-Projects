%divizori(N: integer, D: integer)
%Determina daca un numar are divizori proprii
%Modele de flux: (i, o), (i, i)
%
% N: numarul a pentru care cautam existenta divizorilor
% D: numarul
% curent pentru care verificam daca este sau nu divizor
divizori(N,D):-
    N mod D =:= 0,
    !.
divizori(N,D):-
    D*D=<N,
    NewD is D + 1,
    divizori(N,NewD).

% areDivizori(N: integer)
% Determina daca un numar are divizori proprii
% Modele de flux: (i)
%
% N: numarul a pentru care cautam existenta divizorilor
areDivizori(N):-
    divizori(N,2).

% prim(N: integer)
% Determina daca un numar este prim
% Modele de flux: (i)
%
% N: numarul dat, pentru care verificam conditia de numar prim
prim(2):-!.
prim(N):-
    N > 2,
    not(areDivizori(N)).

% descompune(N: integer, P: integer, Desc: list)
% Returneaza toate descompunerile in suma de numere prime distincte a
% unui numar dat.
% Modele de flux: (i, i, o), (i, i, i)
%
% N: numarul a carui descompuneri in suma de numere prime distincte
% dorim a le determina
% P: numarul curent in descompunerea curenta, care se verifica daca
% este prim si daca poate fi termen in descompunerea lui N
% Desc: descompunerea curenta
descompune(0,_,[]).
descompune(N,P,[P | Descompunere]):-
    P =< N,
    prim(P),
    NewN is N - P,
    NewP is P + 1,
    descompune(NewN,NewP,Descompunere).
descompune(N,P,Descompunere):-
    P =< N,
    NewP is P + 1,
    descompune(N,NewP,Descompunere).

% descompunere(N: integer, Desc: list)
% Returneaza toate descompunerile in suma de numere prime distincte a
% unui numar dat.
% Modele de flux: (i, o), (i, i)
%
% N: numarul a carui descompuneri in suma de numere prime distincte
% dorim a le determina
% este prim si daca poate fi termen in descompunerea lui N
% Desc: descompunerea curenta
descompunere(Numar, Descompunere):-
    descompune(Numar,2,Descompunere).
