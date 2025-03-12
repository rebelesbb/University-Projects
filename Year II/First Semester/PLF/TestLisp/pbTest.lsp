#|
get_nums(l: lista)
Returneaza lista atomilor numerici dintr-o lista data
l: lista din care extragem atomi numerici 
|#

(defun get_nums(l)
    (cond
    ((LISTP l) (MAPCAN #'get_nums l))
    ((NUMBERP l) (LIST l))
    (t NIL)
    )
)

#|
atom_max(l:list max1: int|nil max2:int|nil)
Determina a doua cea mai mare valoare numerica dintr-o lista de atomi
l: lista din care vrem sa determinam a doua cea mai mare val numarica
max1, max2: variabile utilizate pentru calculul a celei de a doua valoare maxima, rezultatul se va afla in max2
Returneaza a doua cea mai mare valoare din lista data
 |#
(defun atom_max(l max1 max2)
    (cond
    ((NULL l) max2)
    ((NUMBERP (CAR l))
        (cond
        ((NULL max1) (atom_max (CDR l) (CAR l) max2))
        ((> (CAR l) max1) (atom_max (CDR l) (CAR l) max1))
        ((NULL max2) (atom_max (CDR l) max1 (CAR l)))
        ((> (CAR l) max2) (atom_max (CDR l) max1 (CAR l)))
        (t (atom_max (CDR l) max1 max2))
        )
    )
    (t (atom_max (CDR l) max1 max2))
    )
)

#|
 stergere(l: list x: atom)
Sterge aparitiile unui element dat dintr-o lista
l: lista din care se sterge elementul dat
x: elementul de sters
Returneaza lista in urma stergerii elemntului
 |#
(defun stergere(l x)
    (cond
        ((NULL l) NIL)
        ((LISTP (CAR l)) (CONS (stergere (CAR l) x) (stergere (CDR l) x)))
        ((EQUAL (CAR l) x) (stergere (CDR l) x))
        (t (CONS (CAR l) (stergere (CDR l) x)))
    )
)

#|
main(l: list)
Apelul principal. Determina a doua cea mai mare valoare din lista data si o elimina
l: lista din care se elimina
Returneaza lista in urma eliminarii
 |#
(defun main(l)
    (stergere l (atom_max (get_nums l) nil nil))
)