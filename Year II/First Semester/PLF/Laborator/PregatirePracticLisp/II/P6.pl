%addElements(ListToAdd: list, L: list, Result: list)

addElements([], L, L).
addElements([H | T], L, [H | Res]):-
    addElements(T, L, Res).

%replace(L: list, Elem: int, LToAdd: list, Result)
replace([], _, _, []):-!.
replace([H | T], H, L, NewRes):-
    !,
    replace(T, H, L, Res),
    addElements(L, Res, NewRes).
replace([H | T], Elem, L, [H | Res]):-
    replace(T, Elem, L, Res).
