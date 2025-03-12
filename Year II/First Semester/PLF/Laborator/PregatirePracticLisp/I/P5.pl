% deleteAllOf(L: list, Elem: atom, Result: list)
% Sterge toate aparitiile unui element dat dintr-o lista
% Modele de input: (i, i, o), (i, i, i)
%
% L: lista din care se sterg aparitiile elementului dat
% Elem: elementul ale carui aparitii dorim sa le stergem
% Result: lista rezultata in urma stergerii aparitiilor elementului
deleteAllOf([], _, []):-!.
deleteAllOf([E | T], E, Res):-
    !,
    deleteAllOf(T, E, Res).
deleteAllOf([H | T], E, [H | Res]):-
    deleteAllOf(T, E, Res).

% countNum(L: list, Num: atom, Count: int)
% Determina numarul de aparitii a unui atom dat intr-o lista
% Modele de flux: (i, i, o), (i, i, i)
%
% L: lista in care numaram numarul de aparitii a numarului dat
% Num: elementul a carui numar de aparitii in lista dorim sa il
%     determinam
% Count: numarul de aparitii a elementului in lista
countNum([], _, 0):-!.
countNum([Num | T], Num, Count):-
    !,
    countNum(T, Num, PreviousCount),
    Count is PreviousCount + 1.
countNum([_ | T], Num, Count):-
    countNum(T, Num, Count).

% createElFrList(L: list, PartialList: list, Result: list)
% Returneaza o lista cu elemente de forma [element, frecventa], cu
% elementele din lista furnizata ca parametru
% Modele de input: (i, i, o), (i, i, i)
%
% L: lista initiala cu elementele careia se va crea lista de forma
%     [element, frecventa]
% PartialList: lista partiala, obinuta pana intr-un anumit punct, de
%     elemente [el, fr]
% Result: lista finala de elemente de forma [el, fr] formata cu
% elementele listei date initial
createElFrList([], Result, Result).
createElFrList([H | T], PartList, Res):-
    countNum([H | T], H, Fr),
    deleteAllOf([H | T], H, UpdatedList),
    createElFrList(UpdatedList, [[H , Fr] | PartList], Res).

% elementFrequencyOf(L: list, Result: list)
% Returneaza o lista cu elemente de forma [el, fr], unde el apartine
% listei initiale L
% Modele de input: (i, i), (i, o)
%
% L: lista cu elementele careia dorim sa cream noua lista
% Res: lista rezultata de [el, fr]

elementFrequencyOf(L, Res):-
    createElFrList(L, [], ReversedRes),
    reverseList(ReversedRes, [], Res).

% reverseList(L: list, PartRes: list, Res: list)
% Inverseaza o lista
% Modele de flux: (i, i, o), (i, i, i), (o, i, i)
%
%
reverseList([], Res, Res):-!.
reverseList([H | T], PartRes, Res):-
    reverseList(T, [H | PartRes], Res).


