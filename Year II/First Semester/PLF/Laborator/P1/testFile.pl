sterge_aparitii(E,[],[]).
sterge_aparitii(E,[H|T],[H|Rez]) :-
    H\=E,
    write(1),
    sterge_aparitii(E,T,Rez),
    write(2),
    !.
sterge_aparitii(E,[_|T],Rez) :- sterge_aparitii(E,T,Rez).
