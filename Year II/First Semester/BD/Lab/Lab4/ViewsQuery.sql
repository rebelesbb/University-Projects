SELECT * FROM Locatii;

-- view pe o singura tabela
CREATE VIEW vw_Locatii
AS
SELECT L.adresa, L.program
FROM Locatii L;

GO
SELECT * FROM vw_Locatii;

-- view pe cel putin doua tabele
CREATE VIEW vw_ProductSales
AS
SELECT DISTINCT clienti.nume
FROM Clienti clienti
INNER JOIN Comenzi C ON c.cod_client = clienti.cod_client
INNER JOIN ComenziProduse CProd ON C.cod_comanda = CProd.cod_comanda
INNER JOIN Produse P ON CProd.cod_produs = P.cod_produs
WHERE P.nume = 'McPuisor';

GO
SELECT * FROM vw_ProductSales;

-- view cu group by
CREATE VIEW vw_PriceStats
AS
SELECT P.nume, SUM(CProd.cantitate * CProd.pretBucata) AS suma_obtinuta
FROM Produse P
INNER JOIN ComenziProduse CProd ON P.cod_produs = CProd.cod_produs
INNER JOIN Comenzi C ON C.cod_comanda = CProd.cod_comanda
WHERE C.data_comanda BETWEEN '2024-01-03' AND '2024-01-09'
GROUP BY P.nume;

GO
SELECT * FROM vw_PriceStats;


