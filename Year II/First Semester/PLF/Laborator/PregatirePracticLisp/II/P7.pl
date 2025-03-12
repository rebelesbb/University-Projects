%reverseL(L: list, PartialRevL: list, RevL: list)
reverseL([], RevL, RevL):-!.
reverseL([H | T], PartialRevL, RevL):-
    reverseL(T, [H | PartialRevL], RevL).

% multiply(Num: list, Digit: int, Transport: int, PartialRes:list,
% Result: list)
multiply([_ | _], 0, _, [0]):-!.
multiply([], _, 0, []):-!.
multiply([], _, Tr, [Tr]):-!.
multiply([H | T], D, Tr, [ComputedD | Res]):-
    ComputedD is (H * D + Tr) mod 10,
    ComputedTr is (H * D + Tr) div 10,
    multiply(T, D, ComputedTr, Res).


multiplication(L, D, Res):-
    reverseL(L, [], ReversedList),
    multiply(ReversedList, D, 0, ReversedRes),
    reverseL(ReversedRes, [], Res).
