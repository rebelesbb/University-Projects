% checkVale(L: list, Flag: int).
% 1 cat timp descreste
% 2 cat timp descreste
greaterThan(X, Y):-
    X > Y.

checkVale([_], 2):-!.
checkVale([L1, L2 | T], 1):-
    L1 > L2,
    checkVale([L2 | T], 1).
checkVale([L1, L2 | T], 1):-
    L1 < L2,
    checkVale([L2 | T], 2).
checkVale([L1, L2 | T], 2):-
    L1 < L2,
    checkVale([L2 | T], 2).

vale([L1, L2 | T]):-
    greaterThan(L1, L2),
    checkVale([L1, L2 | T], 1).
