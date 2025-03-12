% pre(X: List, Transport: int, PartRes: list, Res: list).

pre([0 | Tail], _, [9 | Res]):-
    !,
    pre(Tail, 1, Res).

pre([H | Tail], T, [NewH | Tail]):-
    NewH is H - T.

reverseList([], ReversedList, ReversedList):-!.
reverseList([H | T], PReversedList, ReversedList):-
    reverseList(T, [H | PReversedList], ReversedList).


predecesor(L, Res):-
    reverseList(L, [], ReversedL),
    pre(ReversedL, 1, ReversedRes),
    reverseList(ReversedRes, [], Res).
