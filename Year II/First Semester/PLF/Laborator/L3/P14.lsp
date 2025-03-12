;;;;path: "C:/Users/Bogdan Rebeles/Desktop/University-Projects/Year II/First Semester/PLF/Laborator/L3/P14.lsp"
#|
depth(v: list|atom)
Determina adancimea unui arbore n-ar

v: (initial) lista nodurilor arborelui reprezentata sub forma
(radacina lista-subarb_1 ... lista_subarb_n)
|#
(defun depth (v)
	(cond
		((AND (LISTP v) (NOT (NULL (CDR v)))) (+ 1 (APPLY #'MAX (MAPCAR #'depth v) ) ) )
		(T 0)
	)
)
