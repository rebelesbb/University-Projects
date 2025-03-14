isMember(X, [X | _]):-!.
isMember(X, [_ | T]):-
    isMember(X, T).

%convert(L: list, PartialSet: list, Result: list)

convert([], Res, Res):-!.
convert([H | T], PartSet, Res):-
    not(isMember(H, PartSet)),
    !,
    convert(T, [H | PartSet], Res).
convert([_ | T], PartSet, Res):-
    convert(T, PartSet, Res).

reverseL([], ReversedL, ReversedL).
reverseL([H | T], PartReversedL, ReversedL):-
    reverseL(T, [H | PartReversedL], ReversedL).

toSet(L, Res):-
    convert(L, [], ReversedRes),
    reverseL(ReversedRes, [], Res).

%-------------------------------------------------------------------
toEvenUneven([], 0, 0, [[],[]]):-!.
toEvenUneven([H | T], NewEvenCnt, UnevenCnt, [[H | LEven], LUneven]):-
    H mod 2 =:= 0,
    !,
    toEvenUneven(T, EvenCnt, UnevenCnt, [LEven, LUneven]),
    NewEvenCnt is EvenCnt + 1.
toEvenUneven([H | T], EvenCnt, NewUnevenCnt, [LEven, [H | LUneven]]):-
    toEvenUneven(T, EvenCnt, UnevenCnt, [LEven, LUneven]),
    NewUnevenCnt is UnevenCnt + 1.
