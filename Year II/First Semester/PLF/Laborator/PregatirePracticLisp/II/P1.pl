%revList(L: list, ReversedL: list)
revList([],RL, RL).
revList([H | T], CurrentRL, RL):-
    revList(T, [H | CurrentRL], RL).

reverseList(L, RL):-
    revList(L, [], RL).

% suma(N1: list, N2: list, R: int, TPartial: list, Total: list)
suma([], [], 0, T, T):-!.
suma([], [], R, TP, [R | TP]):-!.
suma([H1 | T1], [], R, TP, T):-
    !,
    HSum is (H1 + R) mod 10,
    NewR is (H1 + R) div 10,
    suma(T1, [], NewR, [HSum | TP], T).

suma([], [H2 | T2], R, TP, T):-
    !,
    HSum is (H2 + R) mod 10,
    NewR is (H2 + R) div 10,
    suma([], T2, NewR, [HSum | TP], T).

suma([H1 | T1], [H2 | T2], R, TP, T):-
    HSum is (H1 + H2 + R) mod 10,
    NewR is (H1 + H2 + R) div 10,
    suma(T1, T2, NewR, [HSum | TP], T).

aduna(N1, N2, T):-
    reverseList(N1, NewN1),
    reverseList(N2, NewN2),
    suma(NewN1, NewN2, 0, [], T).
