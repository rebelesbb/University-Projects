CREATE DATABASE GestionareDeserturi;
GO
USE GestionareDeserturi;

CREATE TABLE Producatori
(
id INT IDENTITY PRIMARY KEY,
nume VARCHAR(100),
site_web VARCHAR(200)
);

CREATE TABLE TipuriDesert
(
id INT IDENTITY PRIMARY KEY,
nume VARCHAR(100)
);

CREATE TABLE Deserturi
(
id INT IDENTITY PRIMARY KEY,
nume VARCHAR(100),
mod_preparare VARCHAR(300),
pret FLOAT,
numar_calorii INT,
producator_id INT FOREIGN KEY REFERENCES Producatori(id),
tip_id INT FOREIGN KEY REFERENCES TipuriDesert(id)
);

CREATE TABLE Clienti
(
id INT IDENTITY PRIMARY KEY,
nume VARCHAR(200),
email VARCHAR(100),
data_nasterii DATE
);

CREATE TABLE Achizitii
(
desert_id INT FOREIGN KEY REFERENCES Deserturi(id),
client_id INT FOREIGN KEY REFERENCES Clienti(id),
cantitate INT,
CONSTRAINT pk_achizitii PRIMARY KEY (desert_id, client_id)
);

INSERT INTO Producatori(nume, site_web)
VALUES
('Prod 1', 'www.site1.com'),
('Prod 2', 'www.site2.com'),
('Prod 3', 'www.site3.com');

INSERT INTO TipuriDesert(nume)
VALUES
('Tip1'),
('Tip2'),
('Tip3');

INSERT INTO Deserturi(nume, mod_preparare, pret, numar_calorii, producator_id, tip_id)
VALUES
('Desert1', 'ModPreparare1', 22.5, 200, 1, 1),
('Desert2', 'ModPreparare2', 20.7, 300, 1, 2),
('Desert3', 'ModPreparare3', 35.0, 420, 1, 3),
('Desert4', 'ModPreparare4', 10.0, 100, 2, 1),
('Desert5', 'ModPreparare5', 23.9, 500, 2, 2),
('Desert6', 'ModPreparare6', 40.45, 380, 2, 3),
('Desert7', 'ModPreparare7', 30.15, 250, 3, 1),
('Desert8', 'ModPreparare8', 20.75, 175, 3, 3);

INSERT INTO Clienti(nume, email, data_nasterii)
VALUES
('Ana', 'ana@gmail.com', '2000-01-10'),
('Maria', 'maria@gmail.com', '1990-02-12'),
('Marian', 'marian@gmail.com', '1998-03-13'),
('Alex', 'alex@gmail.com', '2001-04-11');

INSERT INTO Achizitii(desert_id, client_id, cantitate)
VALUES
(1, 1, 2),
(4, 1, 3),
(2, 2, 1),
(1, 3, 4),
(7, 3, 5),
(3, 4, 1),
(5, 4, 2),
(6, 4, 3);


ALTER TABLE Clienti
ADD CONSTRAINT uq_email UNIQUE (email);

GO 
CREATE FUNCTION ValidateClientId(@clientId INT)
	RETURNS BIT
AS 
BEGIN
	IF @clientId NOT IN (SELECT id FROM Clienti)
		RETURN 0;
	RETURN 1;
END;

GO 
CREATE FUNCTION ValidateDesertId(@desertId INT)
	RETURNS BIT
AS 
BEGIN
	IF @desertId NOT IN (SELECT id FROM Deserturi)
		RETURN 0;
	RETURN 1;
END;

GO
CREATE OR ALTER PROCEDURE CreateOrUpdateAchizitie
	@client_id INT,
	@desert_id INT,
	@cantitate INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(200) = '';
	IF(dbo.ValidateClientId(@client_id) = 0)
		SET @errorsString += 'Clientul nu exista!' + CHAR(13) + CHAR(10);

	IF(dbo.ValidateDesertId(@desert_id) = 0)
		SET @errorsString += 'Desertul nu exista!';

	IF(@errorsString <> '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	IF EXISTS(SELECT * FROM Achizitii WHERE client_id = @client_id AND desert_id = @desert_id)
	BEGIN
		--Actualizam
		UPDATE Achizitii
		SET cantitate = @cantitate
		WHERE client_id = @client_id AND desert_id = @desert_id;
		PRINT('Achizitie actualizata');
	END
	ELSE
	BEGIN
		INSERT INTO Achizitii(client_id, desert_id, cantitate)
		VALUES
		(@client_id, @desert_id, @cantitate);
		PRINT('Achizitie adaugata');
	END
END;

-- invalid
EXEC CreateOrUpdateAchizitie 100, 100, 1;
EXEC CreateOrUpdateAchizitie 1, 100, 1;
EXEC CreateOrUpdateAchizitie 100, 1, 1;

SELECT * FROM Achizitii;
--actualizare
EXEC CreateOrUpdateAchizitie 1, 1, 10;
--adaugare
EXEC CreateOrUpdateAchizitie 1, 7, 20;

GO
CREATE FUNCTION GetClientsWithA()
	RETURNS TABLE
AS
	RETURN SELECT P.nume AS nume_producator, D.nume AS nume_desert, D.numar_calorii, A.cantitate, C.nume AS nume_client 
		FROM Producatori P
		INNER JOIN Deserturi D ON P.id = D.producator_id
		INNER JOIN Achizitii A ON D.id = A.desert_id
		INNER JOIN Clienti C ON A.client_id = C.id
		WHERE C.nume LIKE 'A%';

GO
SELECT * FROM dbo.GetClientsWithA();