% LeastCommonMultiple

% LCM(A: int, B:int, Result: int)
% Uses GCD(A, B)
gcd(A, 0, A):-!.
gcd(A, B, Res):-
    NewB is A mod B,
    NewA is B,
    gcd(NewA, NewB, Res).

lcm(0, _, 0):-!.
lcm(_, 0, 0):-!.
lcm(A, B, Res):-
    A > B,
    !,
    gcd(A, B, GCD),
    Res is (A div GCD) * B.
lcm(A, B, Res):-
    gcd(A, B, GCD),
    Res is (B div GCD) * A.

% lcmList(L: list, currentLcm: int, Result: int)
lcmList([], 0):-!.
lcmList([H], H):-!.
lcmList([H | T], Res):-
    lcmList(T, PreviousRes),
    lcm(H, PreviousRes, Res).

%------------------------------------------------------------------

% addAfterTwo(L: list, V: int, CurrentPosition: int, PositonToAddAfter:int, Result: list).
addAfterTwo([],_,_,_,[]).
addAfterTwo([H | T], V, CurrPos, Pos, [H, V | Res]):-
    CurrPos = Pos,
    !,
    NewPos is Pos * 2,
    NewCurrPos is CurrPos + 1,
    addAfterTwo(T, V, NewCurrPos, NewPos, Res).
addAfterTwo([H | T], V, CurrPos, Pos, [H | Res]):-
    NewCurrPos is CurrPos + 1,
    addAfterTwo(T, V, NewCurrPos, Pos, Res).

addAfterPowOfTwo(L, V, Res):-
    addAfterTwo(L, V, 1, 1, Res).
