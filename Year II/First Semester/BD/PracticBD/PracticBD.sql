CREATE DATABASE GestionarePauni;
GO
USE GestionarePauni;

CREATE TABLE Posesori
(
id INT IDENTITY PRIMARY KEY,
nume VARCHAR(200),
email VARCHAR(100),
data_nastere DATE,
numar_telefon VARCHAR(12) UNIQUE
)

CREATE TABLE Pauni
(
id INT IDENTITY PRIMARY KEY,
nume VARCHAR(200),
data_nastere DATE,
descriere VARCHAR(200),
posesor_id INT FOREIGN KEY REFERENCES Posesori(id)
);

CREATE TABLE Orase
(
id INT IDENTITY PRIMARY KEY,
nume VARCHAR(200),
latitudine FLOAT CHECK(-90 <= latitudine AND latitudine <=90),
longitudine FLOAT CHECK(-180 <= longitudine AND longitudine <=180),
tara VARCHAR(100)
);

CREATE TABLE Expozitii
(
id INT IDENTITY PRIMARY KEY,
denumire VARCHAR(200),
descriere VARCHAR(200),
data_expozitie DATE,
ora_inceput TIME,
ora_sfarsit TIME,
loc_desfasurare VARCHAR,
oras_id INT FOREIGN KEY REFERENCES Orase(id)
);
ALTER TABLE Expozitii
ALTER COLUMN loc_desfasurare VARCHAR(200);

CREATE TABLE ExpozitiiPauni
(
expozitie_id INT FOREIGN KEY REFERENCES Expozitii(id),
paun_id INT FOREIGN KEY REFERENCES Pauni(id),
estePrincipal BIT, -- 1 daca da, 0 daca nu
CONSTRAINT pk_expozitii_pauni PRIMARY KEY (expozitie_id, paun_id)
);

GO
INSERT INTO Posesori(nume, email, data_nastere, numar_telefon)
VALUES
('Andrei', 'andrei@gmail.com','1990-01-01','0712312345'),
('Maria', 'maria@gmail.com','1992-02-02', '0712312111'),
('Flavius', 'flavius@gmail.com','1993-03-03', '0719310101');

INSERT INTO Pauni(nume, data_nastere, descriere, posesor_id)
VALUES
('Paun', '2010-01-01', 'Paun frumos', 1),
('Paunas', '2010-02-02', 'Paun alb', 2),
('Paunel', '2011-03-03', 'Paun albastru', 2),
('Paunila', '2012-05-05', 'Paun negru', 1);

INSERT INTO Orase(nume, latitudine, longitudine, tara)
VALUES
('Oradea', 45, 100, 'Romania'),
('Bucuresti', 60, -100, 'Romania'),
('Oras', 90, 0, 'Romania');

INSERT INTO Expozitii(denumire, descriere, loc_desfasurare, data_expozitie, ora_inceput, ora_sfarsit, oras_id)
VALUES
('Expozitie1', 'Descriere1', 'Locatie1', '2023-01-01', '12:00:00', '14:00:00', 1),
('Expozitie2', 'Descriere2', 'Locatie2', '2023-02-01', '12:00:00', '14:00:00', 1),
('Expozitie3', 'Descriere3', 'Locatie3', '2023-01-02', '12:00:00', '14:00:00', 2),
('Expozitie4', 'Descriere4', 'Locatie4', '2023-03-03', '12:00:00', '14:00:00', 3);
SELECT * FROM Pauni;

INSERT INTO ExpozitiiPauni(expozitie_id, paun_id, estePrincipal)
VALUES
(3, 1, 0),
(3, 2, 1),
(3, 3, 0),
(4, 3, 1),
(5, 1, 1),
(5, 2, 0),
(6, 1, 0),
(6, 2, 1);

GO
CREATE OR ALTER PROCEDURE AddOrUpdatePaun
	@expozitie_id INT,
	@paun_id INT,
	@estePrincipal BIT
AS
BEGIN
	DECLARE @errorsString VARCHAR(200) = '';

	IF @expozitie_id NOT IN(SELECT id FROM Expozitii)
		SET @errorsString += 'Expozitia nu exista!' + CHAR(13) + CHAR(10);
	IF @paun_id NOT IN(SELECT id FROM Pauni)
		SET @errorsString += 'Paunul nu exista!';

	IF (@errorsString <> '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	IF EXISTS(SELECT * FROM ExpozitiiPauni WHERE expozitie_id = @expozitie_id AND paun_id = @paun_id)
	BEGIN
		-- Actualizare
		UPDATE ExpozitiiPauni
		SET estePrincipal = @estePrincipal
		WHERE expozitie_id = @expozitie_id AND paun_id = @paun_id;

		PRINT('Date despre paun in cadrul expozitiei actualizate!');
	END;
	ELSE
	BEGIN
		-- Adaugare
		INSERT INTO ExpozitiiPauni(expozitie_id, paun_id, estePrincipal)
		VALUES 
		(@expozitie_id, @paun_id, @estePrincipal);

		PRINT('Paun adaugat in cadrul expozitiei!');
	END;
END;

GO
SELECT * FROM Pauni;
SELECT * FROM Expozitii;
SELECT * FROM ExpozitiiPauni;

-- Date invalide
EXEC AddOrUpdatePaun 100, 100, 1;

-- Adaugare paun
EXEC AddOrUpdatePaun 3, 4, 0;

-- Actualizare paun
EXEC AddOrUpdatePaun 4, 2, 1;

GO
CREATE OR ALTER VIEW vw_Pauni
AS
SELECT Po.numar_telefon, Pa.nume as nume_paun, Pa.data_nastere as data_nastere_paun
FROM Posesori Po
INNER JOIN Pauni Pa ON Po.id = Pa.posesor_id
WHERE Pa.id IN 
	(SELECT Pa2.id 
	FROM Pauni Pa2
	INNER JOIN ExpozitiiPauni EP ON Pa2.id = EP.paun_id
	INNER JOIN Expozitii E ON EP.expozitie_id = E.id
	INNER JOIN Orase O ON E.oras_id = O.id
	WHERE O.nume LIKE 'O%')
	AND
	Pa.id IN 
	(SELECT Pa2.id 
	FROM Pauni Pa2
	INNER JOIN ExpozitiiPauni EP ON Pa2.id = EP.paun_id
	INNER JOIN Expozitii E ON EP.expozitie_id = E.id
	INNER JOIN Orase O ON E.oras_id = O.id
	WHERE 45 <= O.latitudine AND O.latitudine <= 60);

GO

SELECT * FROM dbo.vw_Pauni;

SELECT * 
FROM Posesori Po
INNER JOIN Pauni Pa ON Po.id = Pa.posesor_id
INNER JOIN ExpozitiiPauni EP ON Pa.id = EP.paun_id
INNER JOIN Expozitii E ON EP.expozitie_id = E.id
INNER JOIN Orase O ON E.oras_id = O.id;


SELECT * FROM Expozitii;
SELECT * FROM Pauni;

INSERT INTO Pauni(nume, data_nastere, descriere, posesor_id)
VALUES
('Paunescu', '2010-01-01', 'Paun', 1);

INSERT INTO Pauni(nume, data_nastere, descriere, posesor_id)
VALUES
('Paun1', '2010-01-01', 'Paun', 1),
('Paun2', '2010-01-01', 'Paun', 1);

/*
INSERT INTO Orase(nume, latitudine, longitudine, tara)
VALUES
('Oradea', 45, 100, 'Romania'),
('Bucuresti', 60, -100, 'Romania'),
('Oras', 90, 0, 'Romania');


INSERT INTO Expozitii(denumire, descriere, loc_desfasurare, data_expozitie, ora_inceput, ora_sfarsit, oras_id)
VALUES
('Expozitie1', 'Descriere1', 'Locatie1', '2023-01-01', '12:00:00', '14:00:00', 1),
('Expozitie2', 'Descriere2', 'Locatie2', '2023-02-01', '12:00:00', '14:00:00', 1),
('Expozitie3', 'Descriere3', 'Locatie3', '2023-01-02', '12:00:00', '14:00:00', 2),
('Expozitie4', 'Descriere4', 'Locatie4', '2023-03-03', '12:00:00', '14:00:00', 3);
SELECT * FROM Pauni;
*/

INSERT INTO ExpozitiiPauni(expozitie_id, paun_id, estePrincipal)
VALUES
(5, 5, 0),
(6, 5, 0);

INSERT INTO ExpozitiiPauni(expozitie_id, paun_id, estePrincipal)
VALUES
(5, 6, 0),
(6, 7, 0);