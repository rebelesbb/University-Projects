USE McDonaldsDB;

/*
WHERE : 8
GROUP BY : 4
DISTINCT : 2
HAVING : 2
2+ : 8
NM : 5 
*/

-- 1
-- Lista produselor care contin un anumit ingredient
SELECT * 
FROM PRODUSE P
WHERE ingrediente LIKE '%carne vita%';

-- 2
-- Meniurile vandute cu pretul mai mare de 25
SELECT DISTINCT M.nume
FROM Meniuri M
INNER JOIN ComenziMeniuri Cmeniuri ON M.cod_meniu = Cmeniuri.cod_meniu
INNER JOIN Comenzi AS C ON Cmeniuri.cod_comanda = C.cod_comanda
WHERE M.pret > 25;

-- 3
-- Produsele care apartin mai multor categorii
SELECT P.nume, COUNT(*) AS numar_categorii
FROM Categorii C 
INNER JOIN CategoriiProduse CP ON C.cod_categorie = CP.cod_categorie
INNER JOIN Produse P ON CP.cod_produs = P.cod_produs
GROUP BY P.nume HAVING COUNT(*) > 1;

-- 4
-- Clientii care au comandat un anumit produs
SELECT DISTINCT clienti.nume
FROM Clienti clienti
INNER JOIN Comenzi C ON c.cod_client = clienti.cod_client
INNER JOIN ComenziProduse CProd ON C.cod_comanda = CProd.cod_comanda
INNER JOIN Produse P ON CProd.cod_produs = P.cod_produs
WHERE P.nume = 'McPuisor';

-- 5
-- Pretul produselor dupa aplicarea unei oferte
-- (toate produsele pe care oferta se poate aplica)
SELECT P.nume, P.pret AS pret_vechi, pret_nou = P.pret - O.discount
FROM Produse P
INNER JOIN OferteProduse OP ON P.cod_produs = OP.cod_produs
INNER JOIN Oferte O ON O.cod_oferta = OP.cod_oferta
WHERE O.nume = 'Oferta produse pui'
;

-- 6
-- Suma rezultata prin vanzarea unui anumit produs
SELECT SUM(C.total) as Total
FROM Comenzi C 
INNER JOIN ComenziProduse CProd ON C.cod_comanda = CProd.cod_comanda
INNER JOIN Produse P ON CProd.cod_produs = P.cod_produs
WHERE P.nume = 'McPuisor';

-- 7
-- Clientii care au cheltuit minim o anumita suma(ex. 25) la o comanda 
-- intr-o anumita perioada
SELECT C.nume
FROM Clienti C
WHERE C.cod_client IN(
		SELECT clienti.cod_client
		FROM Clienti clienti 
		INNER JOIN Comenzi comenzi ON clienti.cod_client = comenzi.cod_client
		WHERE comenzi.data_comanda BETWEEN '2024-01-01' AND '2024-01-07'
		GROUP BY clienti.cod_client HAVING MAX(comenzi.total) >= 25);

-- 8
-- Angajatul de la o anumita locatie cu cea mai mare suma obtinuta in urma vanzarilor
SELECT TOP 1 A.cod_angajat, A.nume, A.prenume, SUM(C.total) AS suma 
FROM Comenzi C
INNER JOIN Angajati A ON C.cod_angajat = A.cod_angajat
INNER JOIN Locatii L ON L.cod_locatie = A.cod_locatie
WHERE L.adresa = 'Brasov, Bdul. Eroilor 1'
GROUP BY A.cod_angajat, A.nume, A.prenume
ORDER BY suma DESC;


-- 9
-- Produsele vandute pe o anumita perioada
-- si suma obinuta prin vanzarea fiecarui produs
SELECT P.nume, SUM(CProd.cantitate * CProd.pretBucata) AS suma_obtinuta
FROM Produse P
INNER JOIN ComenziProduse CProd ON P.cod_produs = CProd.cod_produs
INNER JOIN Comenzi C ON C.cod_comanda = CProd.cod_comanda
WHERE C.data_comanda BETWEEN '2024-01-03' AND '2024-01-09'
GROUP BY P.nume;

-- 10
-- Suma obtinuta la fiecare locatie
SELECT L.cod_locatie, L.adresa, SUM(C.total) AS suma_obtinuta
FROM Comenzi C
INNER JOIN Angajati A ON A.cod_angajat = C.cod_angajat
RIGHT OUTER JOIN Locatii L ON A.cod_locatie = L.cod_locatie
GROUP BY L.cod_locatie, L.adresa
ORDER BY suma_obtinuta DESC;


/*
-- Numarul de comenzi care contin meniuri dintr-o anumita categorie
SELECT COUNT(*) AS numar_comenzi
FROM Meniuri AS M
INNER JOIN ComenziMeniuri Cmeniuri ON M.cod_meniu = Cmeniuri.cod_meniu
WHERE EXISTS(
		SELECT *  
		FROM CategoriiMeniuri categoriiM
		INNER JOIN Categorii categorii ON categorii.cod_categorie = categoriiM.cod_categorie
		WHERE categorii.nume = 'Pui' AND M.cod_meniu = categoriiM.cod_meniu);
*/