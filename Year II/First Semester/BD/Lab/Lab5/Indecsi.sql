USE McDonaldsDB;

GO

CREATE NONCLUSTERED INDEX IX_Produse_codProdus_asc ON Produse(cod_produs ASC)
INCLUDE (nume);
CREATE NONCLUSTERED INDEX IX_ComenziProduse_codProdus_asc_codComanda_asc ON ComenziProduse (cod_produs ASC, cod_comanda ASC);
CREATE NONCLUSTERED INDEX IX_Comenzi_codComanda_asc ON Comenzi(cod_comanda ASC) 
INCLUDE (total); -- nu ajuta la al doilea view sa includ codul angajatului, considera ca e mai simplu sa faca scan pe idx clustered


GO
CREATE VIEW vw_TotalProductSales
AS
SELECT SUM(C.total) as Total
FROM Comenzi C 
INNER JOIN ComenziProduse CProd ON C.cod_comanda = CProd.cod_comanda
INNER JOIN Produse P ON CProd.cod_produs = P.cod_produs
WHERE P.nume = 'McPuisor';

GO
SELECT * FROM vw_TotalProductSales;

GO
CREATE NONCLUSTERED INDEX IX_Angajati_codAngajat ON Angajati(cod_angajat ASC)
INCLUDE(cod_locatie, nume, prenume);
CREATE NONCLUSTERED INDEX IX_Locatii_codLocatie_asc ON Locatii(cod_locatie ASC)
INCLUDE(adresa);
CREATE NONCLUSTERED INDEX IX_Comenzi_codAngajat_asc_total_desc ON Comenzi(cod_angajat ASC, total DESC);

GO
CREATE VIEW vw_BestEmployee
AS
SELECT TOP 1 A.cod_angajat, A.nume, A.prenume, SUM(C.total) AS suma 
FROM Comenzi C
INNER JOIN Angajati A ON C.cod_angajat = A.cod_angajat
INNER JOIN Locatii L ON L.cod_locatie = A.cod_locatie
WHERE L.adresa = 'Brasov, Bdul. Eroilor 1'
GROUP BY A.cod_angajat, A.nume, A.prenume
ORDER BY suma DESC;

GO
SELECT * FROM vw_BestEmployee;


----------------------------------------------------------------------------------------
CREATE NONCLUSTERED INDEX IX_Produse_codProdus_asc_pret_desc ON Produse(pret DESC)
INCLUDE(cod_produs, nume);

GO
CREATE VIEW view_
AS
SELECT cod_produs, nume, pret FROM Produse
ORDER BY pret DESC;
