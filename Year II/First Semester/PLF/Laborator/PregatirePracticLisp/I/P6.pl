countElement([], _, 0):-!.
countElement([X | T], X, Count):-
    !,
    countElement(T, X, PreviousCount),
    Count is PreviousCount + 1.
countElement([_ | T], X, Count):-
    countElement(T, X, Count).


deleteMA(_, [], []):-!.
deleteMA(L, [H | T], [H | Result]):-
    countElement(L, H, Count),
    1 is Count,
    !,
    deleteMA(L, T, Result).
deleteMA(L, [_ | T], Result):-
    deleteMA(L, T, Result).

deleteMultipleAppearance(L, Result):-
    deleteMA(L, L, Result).
