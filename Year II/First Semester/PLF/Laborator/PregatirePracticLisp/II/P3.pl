%insertElem(Elem: int, L: list, Result: list)
insertElem(X, [], [X]):-!.
insertElem(X, [H | T], [X, H | T]):-
    X < H,
    !.
insertElem(X, [H | T], [H | T]):-
    X = H,
    !.
insertElem(X, [H | T], [H | Res]):-
    X > H,
    insertElem(X, T, Res).

insertionSort([],[]).
insertionSort([H | T], SortedList):-
    insertionSort(T, SortedTail),
    insertElem(H,SortedTail, SortedList).


