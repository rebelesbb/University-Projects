-- Comenzi Produse --

INSERT INTO ComenziProduse(cod_comanda, cod_produs, cantitate, pretBucata)
VALUES
(1, 102, 1, 18),
(2, 122, 1, 25),
(3, 123, 1, 25),
(7, 113, 2, 6),
(7, 161, 1, 9.5),
(7, 162, 1, 3.5),
(8, 160, 1, 9.5),
(14, 134, 2, 8.5),
(14, 157, 1, 14.5);

INSERT INTO ComenziProduse(cod_comanda, cod_produs, cantitate, pretBucata)
VALUES
(11, 158, 1, 6),
(11, 164, 1, 3.5);

INSERT INTO ComenziProduse(cod_comanda, cod_produs, cantitate, pretBucata)
VALUES
(11, 158, 1, 6),
(11, 164, 1, 3.5),
(14, 157, 1, 14.5),
(14, 134, 2, 8.5),
(15, 113, 3, 6);

INSERT INTO ComenziProduse(cod_comanda, cod_produs, cantitate, pretBucata)
VALUES
(16, 113, 3, 6);

INSERT INTO ComenziProduse(cod_comanda, cod_produs, cantitate, pretBucata)
VALUES
(34, 100, 1, 6),
(35, 116, 1, 16.5),
(36, 119, 1, 25),
(37, 150, 2, 7.5),
(38, 118, 1, 11.5),
(39, 100, 1, 6);


-- Comenzi Meniuri --

INSERT INTO ComenziMeniuri(cod_comanda, cod_meniu, cantitate, pretBucata)
VALUES
(4, 300, 1, 21),
(5, 301, 1, 22),
(6, 302, 1, 33),
(8, 311, 1, 34),
(9, 303, 1, 38.5),
(10, 307, 1, 27);

INSERT INTO ComenziMeniuri(cod_comanda, cod_meniu, cantitate, pretBucata)
VALUES
(12, 322, 1, 38),
(13, 308, 3, 20.5);

INSERT INTO ComenziMeniuri(cod_comanda, cod_meniu, cantitate, pretBucata)
VALUES
(12, 322, 1, 38),
(13, 308, 3, 20.5);

INSERT INTO ComenziMeniuri(cod_comanda, cod_meniu, cantitate, pretBucata)
VALUES
(17, 306, 1, 29),
(18, 309, 1, 32),
(19, 310, 1, 39),
(20, 311, 1, 34),
(21, 312, 1, 41),
(22, 306, 1, 29),
(23, 309, 1, 32),
(24, 310, 1, 39),
(25, 311, 1, 34),
(26, 312, 1, 41);

INSERT INTO ComenziMeniuri(cod_comanda, cod_meniu, cantitate, pretBucata)
VALUES
(32, 309, 1, 32),
(33, 312, 2, 41),
(39, 336, 1, 36.5),
(39, 339, 2, 45),
(40, 315, 1, 34.5),
(41, 317, 1, 37.5),
(42, 335, 1, 39.5);

INSERT INTO ComenziMeniuri(cod_comanda, cod_meniu, cantitate, pretBucata)
VALUES
(43, 317, 1, 37.5),
(44, 335, 1, 39.5),
(45, 315, 1, 34.5),
(46, 315, 1, 34.5);

SELECT * FROM ComenziProduse;
SELECT * FROM ComenziMeniuri;