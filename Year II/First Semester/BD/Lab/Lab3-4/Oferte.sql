-- OFERTE --
ALTER TABLE Oferte
ALTER COLUMN discount DECIMAL(5,2);

INSERT INTO Oferte(nume, descriere, data_inceput, data_sfarsit, discount)
VALUES
('Oferta produse pui', 'Reducere de 5 lei la toate produsele cu pui', '2024-03-01', '2024-03-07', 5),
('Oferta produse vita', 'Reducere de 5 lei la toate produsele cu vita', '2024-03-08', '2024-03-14', 5),
('Oferta meniuri McNuggets', 'Reducere 7 lei la toate meniurile McNuggets', '2024-03-08', '2024-03-14', 7);

INSERT INTO Oferte(nume, descriere, data_inceput, data_sfarsit, discount)
VALUES
('Oferta produse McNuggets', 'Reducere de 3 lei la toate produsele McNuggets', '2024-03-01', '2024-03-01', 3);

SELECT * FROM Oferte;

INSERT INTO OferteProduse(cod_oferta, cod_produs)
SELECT 1, P.cod_produs
FROM Produse P
WHERE P.ingrediente LIKE '%pui%';

INSERT INTO OferteProduse(cod_oferta, cod_produs)
SELECT 2, P.cod_produs
FROM Produse P
WHERE P.ingrediente LIKE '%vita%';

INSERT INTO OferteProduse(cod_oferta, cod_produs)
SELECT 4, P.cod_produs
FROM Produse P
WHERE P.nume LIKE '%McNuggets%';

INSERT INTO OferteMeniuri(cod_oferta, cod_meniu)
SELECT 3, M.cod_meniu
FROM Meniuri M
WHERE M.nume LIKE '%McNuggets%';

SELECT P.nume, O.nume
FROM Produse P
INNER JOIN OferteProduse OP ON P.cod_produs = OP.cod_produs
INNER JOIN Oferte O ON O.cod_oferta = OP.cod_oferta
;

SELECT M.nume, O.nume
FROM Meniuri M
INNER JOIN OferteMeniuri OM ON M.cod_meniu = OM.cod_meniu
INNER JOIN Oferte O ON O.cod_oferta = OM.cod_oferta;

