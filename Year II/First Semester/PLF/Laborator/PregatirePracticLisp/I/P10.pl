% insertNum/4
% insertNum(X: integer, N: integer, L: list, Res: list)
% Inserts X on the n-th position into the list

insertNum(X, 1, L, [X | L]):-!.
insertNum(X, N, [H | T], [H | Result]):-
    NewN is N - 1,
    insertNum(X, NewN, T, Result).

%----------------------------------------------------------
%GCD(a,b):
% a, b = 0
% GCD(b, a mod b)
gcd(A, 0, A):-!.
gcd(A, B, D):-
    NewB is A mod B,
    gcd(B, NewB, D).

gcdList([L1], L1):-!.
gcdList([H | T], CurrentGCD):-
    gcdList(T, OldGCD),
    gcd(OldGCD, H, CurrentGCD).
