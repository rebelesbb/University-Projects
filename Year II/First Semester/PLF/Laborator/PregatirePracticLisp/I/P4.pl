% substitute(L: list, Elem: list, LForReplace: list, Result: list)
substitute([], _, _, []):-!.
substitute([E | T], E, L, [L | Res]):-
    !,
    substitute(T, E, L, Res).
substitute([H | T], E, L, [H | Res]):-
    substitute(T, E, L, Res).

%----------------------------------------------------------------

deleteN([_ | T], Pos, Pos, T):-!.
deleteN([H | T], CurrentPos, Pos, [H | Res]):-
    NextCurrentPos is CurrentPos + 1,
    deleteN(T, NextCurrentPos, Pos, Res).

deleteFromPosition(L, Pos, Res):-
    deleteN(L, 1, Pos, Res).
