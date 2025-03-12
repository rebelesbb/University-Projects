CREATE DATABASE Sem4;

USE Sem4;

CREATE TABLE Sectiuni
(
cod_s INT IDENTITY PRIMARY KEY,
nume VARCHAR(100),
descriere VARCHAR(200)
);

GO
CREATE TABLE Atractii
(
cod_a INT IDENTITY PRIMARY KEY,
nume VARCHAR(100),
descriere VARCHAR(200),
varsta_min INT,
cod_s INT FOREIGN KEY (cod_s) REFERENCES Sectiuni(cod_s)
);

CREATE TABLE Categorii
(
cod_c INT IDENTITY PRIMARY KEY,
nume VARCHAR(100)
);

CREATE TABLE Vizitatori
(
cod_v INT IDENTITY PRIMARY KEY,
nume VARCHAR(100),
email VARCHAR(100),
cod_c INT FOREIGN KEY (cod_c) REFERENCES Categorii(cod_c)
);

CREATE TABLE Note
(
cod_a INT FOREIGN KEY (cod_a) REFERENCES Atractii(cod_a),
cod_v INT FOREIGN KEY (cod_v) REFERENCES Vizitatori(cod_v),
nota INT,
CONSTRAINT pk_note PRIMARY KEY (cod_a, cod_v)
);

-- Inserare date in tabelul Sectiuni
INSERT INTO Sectiuni (nume, descriere)
VALUES 
('Sectiune 1', 'Descriere sectiune 1'),
('Sectiune 2', 'Descriere sectiune 2'),
('Sectiune 3', 'Descriere sectiune 3'),
('Sectiune 4', 'Descriere sectiune 4'),
('Sectiune 5', 'Descriere sectiune 5'),
('Sectiune 6', 'Descriere sectiune 6'),
('Sectiune 7', 'Descriere sectiune 7'),
('Sectiune 8', 'Descriere sectiune 8');

INSERT INTO Sectiuni (nume, descriere)
VALUES 
('Carusel', 'askjbdjas');
 
-- Inserare date in tabelul Atractii
INSERT INTO Atractii (nume, descriere, varsta_min, cod_s)
VALUES 
('Atractie 1', 'Descriere atractie 1', 10, 1),
('Atractie 2', 'Descriere atractie 2', 12, 2),
('Atractie 3', 'Descriere atractie 3', 8, 3),
('Atractie 4', 'Descriere atractie 4', 6, 1),
('Atractie 5', 'Descriere atractie 5', 14, 2),
('Atractie 6', 'Descriere atractie 6', 9, 3),
('Atractie 7', 'Descriere atractie 7', 12, 4),
('Atractie 8', 'Descriere atractie 8', 5, 5),
('Atractie 9', 'Descriere atractie 9', 8, 6),
('Atractie 10', 'Descriere atractie 10', 7, 7),
('Atractie 11', 'Descriere atractie 11', 13, 8);
 
-- Inserare date in tabelul Categorii
INSERT INTO Categorii (nume)
VALUES 
('Categorie 1'),
('Categorie 2'),
('Categorie 3'),
('Categorie 4'),
('Categorie 5'),
('Categorie 6'),
('Categorie 7'),
('Categorie 8');
 
-- Inserare date in tabelul Vizitatori
INSERT INTO Vizitatori (nume, email, cod_c)
VALUES 
('Vizitator 1', 'vizitator1@example.com', 1),
('Vizitator 2', 'vizitator2@example.com', 2),
('Vizitator 3', 'vizitator3@example.com', 3),
('Vizitator 4', 'vizitator4@example.com', 1),
('Vizitator 5', 'vizitator5@example.com', 4),
('Vizitator 6', 'vizitator6@example.com', 5),
('Vizitator 7', 'vizitator7@example.com', 6),
('Vizitator 8', 'vizitator8@example.com', 7),
('Vizitator 9', 'vizitator9@example.com', 8),
('Vizitator 10', 'vizitator10@example.com', 4);
 
-- Inserare date in tabelul Note
INSERT INTO Note (cod_a, cod_v, nota)
VALUES 
(1, 1, 5),
(2, 2, 4),
(3, 3, 3),
(4, 4, 4),
(1, 2, 5),
(2, 3, 4),
(5, 1, 3),
(6, 2, 4),
(7, 3, 5),
(8, 4, 4),
(9, 5, 3),
(10, 6, 5),
(11, 7, 4),
(1, 8, 5),
(2, 9, 3),
(3, 10, 4),
(4, 1, 5),
(5, 2, 2),
(6, 3, 4);


CREATE FUNCTION GetCod(@nume VARCHAR(100))
RETURNS INT 
AS
BEGIN
	IF(EXISTS(SELECT C.cod_c FROM Categorii C WHERE C.nume = @nume))
		RETURN (SELECT C.cod_c FROM Categorii C WHERE C.nume = @nume)
	RETURN -1
END;

PRINT dbo.GetCod('Categorie 1000');
PRINT dbo.GetCod('Categorie 5');

/*
GO
CREATE FUNCTION GetCodCategorie(@nume VARCHAR(70))
RETURNS INT AS
BEGIN
	IF(EXISTS(SELECT C.cod_c FROM Categorii C WHERE C.nume = @nume))
		RETURN(SELECT C.cod_c FROM Categorii C WHERE C.nume = @nume);
	RETURN -1;
END;

DROP FUNCTION dbo.GetCodCategorie;

PRINT dbo.GetCodCategorie('Categorie 100');*/

GO
CREATE TRIGGER ImpiedicaEliminare
ON Categorii
INSTEAD OF DELETE
AS
BEGIN
	PRINT 'Momentan nu se pot sterge categorii :('
END

DELETE FROM Categorii;
SELECT * FROM Categorii;

INSERT INTO Categorii(nume)
VALUES
('pensionari'),
('copii');

GO
CREATE VIEW vw_CategoriiPensionari
AS
SELECT C.cod_c, C.nume FROM Categorii C WHERE C.nume = 'pensionari' OR C.nume = 'copii';

GO
SELECT * FROM vw_CategoriiPensionari;

GO
CREATE VIEW vw_Sectiuni
AS
SELECT cod_s, nume, descriere FROM Sectiuni WHERE nume LIKE 'C%';

GO
SELECT * FROM vw_Sectiuni;