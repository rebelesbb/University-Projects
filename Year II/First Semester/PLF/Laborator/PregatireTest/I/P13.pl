isMember(X, [X | _]):-!.
isMember(X, [_ | T]):-
    isMember(X, T).

% convert(L: list, CurrentResult: list, Result: list)
convert([], []):-!.
convert([H | T], [H | Res]):-
    convert(T, Res),
    not(isMember(H, Res)),
    !.

convert([_ | T], Res):-
    convert(T, Res).

