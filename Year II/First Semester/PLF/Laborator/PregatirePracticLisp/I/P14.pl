% isMember/2
% isMember(X: integer, L: list)
% Checks is X exists in L
isMember(X, [X | _]):-!.
isMember(X, [_ | T]):-
    isMember(X, T).


% isSubset/2
% isSubset(A: list, B: list)
% Checks if a set is a subset of another one
isSubset([],_).
isSubset([H | T], B):-
    isMember(H, B),
    isSubset(T, B).

% areEqual/2
% areEqual(A: list, B: list)
% Checks if two sets are equal
areEqual(A, B):-
    isSubset(A, B),
    isSubset(B, A).

%-----------------------------------------------------------------------

% getMemberN/2
% getMemberN(X: integer , N: integer, L: list)
% Returns the value from the N-th position from a list
getMemberN(X, 1, [X | _]):-!.
getMemberN(X, N, [_ | T]):-
    NewN is N - 1,
    getMemberN(X, NewN, T).
