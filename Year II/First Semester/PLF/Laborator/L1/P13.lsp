#|
interclasareElem(L: list, elem: atom, poz: int)
Interclaseaza un element pe o pozitie data intr-o lista.
Functia returneaza lista rezultata in urma interclasarii elementului pe pozitia data.

L: lista liniara, in care elementul va fi introdus
elem: elementul de interclasat in lista
poz: positia pe care elementul urmeaza sa fie interclasat in lista
|#

(defun interclasareElem(lista elem poz)
	(cond 

	((AND (NULL lista) (NOT (= poz 1))) NIL)
	((= poz 1) 
		(APPEND (LIST elem) lista))
	(T (APPEND (LIST (CAR lista)) (interclasareElem (CDR lista) elem (- poz 1))))

	)
)

;;----------------------------------------------------------------------------------

#|
suma(L: lista)
Calculeaza suma tuturor atomilor numerici de la toate nivelurile unei liste eterogene
Functia returneaza aceasta suma.

L: lista pentru care se doreste calcularea sumei atomilor numerici de la toate nivelurile
|#

(defun suma(lista)
	(cond

	((NULL lista) 0)
	((NUMBERP (CAR lista)) 
		(+ (CAR lista) (suma (CDR lista))))
	((LISTP (CAR lista)) 
		(+ (suma (CAR lista)) (suma (CDR lista))))
	(T (suma (CDR lista)))

	)
)

;;-----------------------------------------------------------------------------------

#|
subliste(L: list)
Determina toate sublistele unei liste date, de pe toate nivelele.
Functia returneza lista formata din sublistele gasite.

L: lista a carei subliste dormi sa le determinam
|#

(defun subliste(lista)
	(cond

	((NULL lista) NIL)
	((LISTP (CAR lista)) 
		(APPEND (LIST (CAR lista)) (subliste (CAR lista)) (subliste (CDR lista))))
	(T (subliste (CDR lista)))

	)
)

;;-----------------------------------------------------------------------------------

#|
apartine(M: list, elem: atom)
Determina daca un element apartine unei multimi.
Functia returneaza adevarat daca elementul apartine mmiltimii date,
fals altfel.

M: multimea de elemente, unde verificam prezenta elementului dat
elem: elemmentul a carui prezenta in multime dorim sa o verificam
|#

(defun apartine(multime elem)
	(cond
	
	((NULL multime) NIL)
	((= elem (CAR multime)) T)
	(T(apartine (CDR multime) elem))

	)
)

#|
esteInclusa(M1: list, M2: list)
Verifica daca o multime este inclusa in alta.
Functia returneaza adevarat daca multimea data este inclusa in cealalta multime data,
fals altfel.

M1: multimea care verificam daca este inclusa in cealalta multime
M2: 
|#

(defun esteInclusa(m1 m2)
	(cond

	((NULL m1) T)
	((NOT (apartine m2 (CAR m1))) NIL)
	(T (esteInclusa (CDR m1) m2))

	)
)

#|
suntMultimiEgale(M1: list M2: list)
Verifica daca doua multimi sunt egale.
Functia returneaza "true" daca cele doua multimi sunt egale,
"false" altfel.

M1, M2: cele doua multimi a caror egalitate se verifica
|#

(defun suntMultimiEgale(m1 m2)
	(cond

	((AND (esteInclusa m1 m2) (esteInclusa m2 m1)) 'true)
	(T 'false)

	)
)









