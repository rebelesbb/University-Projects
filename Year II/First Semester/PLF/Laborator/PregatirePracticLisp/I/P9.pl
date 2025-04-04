is_member(X, [X | _]):-!.
is_member(X, [_ | T]):-
    is_member(X, T).

% add_to_set(L: list, CurrentSet: list, Set: list)
add_to_set([], Set, Set):-!.
add_to_set([H | T], CurrentSet, Set):-
    not(is_member(H, CurrentSet)),
    !,
    add_to_set(T, [H | CurrentSet], Set).
add_to_set([_ | T], CurrentSet, Set):-
    add_to_set(T, CurrentSet, Set).

reverseL([], Res, Res):-!.
reverseL([H | T], CurrentL, Res):-
    reverseL(T, [H | CurrentL], Res).


% reunion(A: list, B: list, Res: list)
reunion(A, B, Res):-
    add_to_set(A, [], PartialResA),
    add_to_set(B, PartialResA, PartialResB),
    reverseL(PartialResB, [], Res).

