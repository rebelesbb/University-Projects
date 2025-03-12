%sterge_aparitii(E : atom, L : lista, Rez : Lista)
%E : atomul de sters
%L : lista din care il stergem
%Rez : lista rezultata in urma stergerii aparitiilor atomului
% Predicatul presupune parcurgerea listei si construirea in rez a listei
% atomilor diferiti de atomul dat E
stergeAparitii(_,[],[]):-!.
stergeAparitii(E,[H|T],[H|Rez]) :-
    H\=E,
    !,
    stergeAparitii(E,T,Rez).
stergeAparitii(E,[E|T],Rez) :- stergeAparitii(E,T,Rez).
