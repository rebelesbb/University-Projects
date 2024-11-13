isMember(X, [X | _]):-!.
isMember(X, [_ | T]):-
    isMember(X, T).


% setDifference(A: list, B: list, D: list)
% Computes the set difference of two sets
setDifference(A, _, A):-!.
setDifference([H | T], B, D):-
    isMember(H, B),
    !,
    setDifference(T, B, D).
setDifference([H | T], B, [H | D]):-
    setDifference(T, B, [H | D]).


%-----------------------------------------------------------

isEven(X):- X mod 2 =:= 0.

% addAfterEven(L: list, Res: list)
% Adds one after each even value
addAfterEven([],[]).
addAfterEven([H | T], [H, 1 | Res]):-
    isEven(H),
    !,
    addAfterEven(T, Res).
addAfterEven([H | T], [H | Res]):-
    addAfterEven(T, Res).
