% properDivisors(X: int, D: int, Divs: list)
properDivisors(X, D, []):-
    D > X div 2,
    !.
properDivisors(X, D, [D | Divs]):-
    X mod D =:= 0,
    !,
    NewD is D + 1,
    properDivisors(X, NewD, Divs).
properDivisors(X, D, Divs):-
    NewD is D + 1,
    properDivisors(X, NewD, Divs).

% addList(ListToAdd: list, ListToAddTo: list, Result: list)
addList([], L, L):-!.
addList([H | T], L, [H | Res]):-
    addList(T, L, Res).

% addDivisors(L: list, Result: list)
addDivisors([],[]):-!.
addDivisors([H | T], [H | Res]):-
    properDivisors(H, 2, Divs),
    addDivisors(T, PreviousRes),
    addList(Divs, PreviousRes, Res).
