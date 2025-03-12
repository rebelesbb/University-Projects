% addAfter(Elem: int, Count: int, positionToAdd: int, L: list,
% ModifiedList: list, Res: list)

addAfter(_, _, _, [], []):-!.
addAfter(E, Count, Pos, [H | T], [H, E |Res]):-
    Count = Pos,
    !,
    NewCount is Count + 1,
    NewPos is 2 * Pos + 1,
    addAfter(E, NewCount, NewPos, T, Res).
addAfter(E, Count, Pos, [H | T], [H | Res]):-
    NewCount is Count + 1,
    addAfter(E, NewCount, Pos, T, Res).


addElementAfter(E, L, Res):-
    addAfter(E, 1, 1, L,Res).
