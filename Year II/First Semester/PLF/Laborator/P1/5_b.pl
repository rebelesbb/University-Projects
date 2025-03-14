%adauga(E : atom, L : lista, Rez : lista)
%  Predicatul verifica daca atomul E exista in lista de perechi si
%  incrementeaza valoarea frecventei daca da, sau adauga o pereche noua
%  [E, 1] daca nu
%
% L : lista de perechi
% E : atomul de adaugat in lista de
% perechi
% Rez : lista rezultata in urma adaugarii lui E
%
adauga(E,[],[[E,1]]) :- !.
adauga(E,[[E,Fr]| T],[[E,FrN] | T]) :-
    FrN is Fr+1,
    !.
adauga(E,[H | T], [H | L]) :-
    adauga(E, T, L).


%creareLista(LI : lista, LF : lista)
%  Predicatul parcurge lista initiala adaugand pe rand fiecare element
%  in lista finala de tipul atom : n (utilizeaza predicatul adauga)
%
% LI : lista initiala de elemente
% LF : lista finala de tipul atom : n (element : frecventa)


creareLista([],L, L) :- !.
creareLista([H | T], L, Rez) :-
    adauga(H, L, LNou),
    creareLista(T, LNou, Rez).

%anumar(L : lista, X : lista)
% Produce o lista de perechi [atom, n], unde atom apartine listei L
%
% L : Lista initiala de atomi
% X : lista produsa de perechi atom : n
numar(L,X) :- creareLista(L,[],X).






% ----------------------------------------------------------------------


/*
creareLista([],[]) :- !.
creareLista([H | T], RezN) :-
    creareLista(T, Rez),
    adauga(H,Rez,RezN).

numar(L,X) :- creareLista(L,X).
*/
