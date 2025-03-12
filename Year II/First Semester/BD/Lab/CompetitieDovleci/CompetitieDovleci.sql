CREATE DATABASE Competitie_dovleci;
GO
USE Competitie_dovleci;

CREATE TABLE Participanti
(
cod_participant INT IDENTITY PRIMARY KEY,
nume VARCHAR(200),
numar_telefon VARCHAR(15),
adresa VARCHAR(200)
);

CREATE TABLE Dovleci
(
cod_dovleac INT IDENTITY PRIMARY KEY,
descriere VARCHAR(200),
data_decorare DATE,
timp_minute INT,
finalizare VARCHAR(20),
CONSTRAINT check_finalizare_constraint CHECK (finalizare = 'Da' Or finalizare = 'Nu')
)

CREATE TABLE Evaluatori
(
cod_evaluator INT IDENTITY PRIMARY KEY,
nume VARCHAR(200),
email VARCHAR(100),
data_nasterii DATE,
);

CREATE TABLE Decorari
(
cod_dovleac INT FOREIGN KEY REFERENCES Dovleci(cod_dovleac),
cod_participant INT FOREIGN KEY REFERENCES Participanti(cod_participant),
descriere VARCHAR(200),
CONSTRAINT pk_Decorari PRIMARY KEY (cod_dovleac, cod_participant)
);



CREATE TABLE Note
(
cod_evaluator INT FOREIGN KEY REFERENCES Evaluatori(cod_evaluator),
cod_dovleac INT FOREIGN KEY REFERENCES Dovleci(cod_dovleac),
nota INT,
CONSTRAINT check_nota_constraint CHECK (1 <= nota AND nota <= 10),
CONSTRAINT pk_note PRIMARY KEY (cod_evaluator, cod_dovleac)
);

-- Adaugă participanți
INSERT INTO Participanti (nume, numar_telefon, adresa)
VALUES
('Andrei Popescu', '0721123456', 'Strada Primaverii 10'),
('Maria Ionescu', '0732456789', 'Strada Libertatii 5'),
('Cristian Mihai', '0743567890', 'Strada Victoriei 20');

-- Adaugă dovleci
INSERT INTO Dovleci (descriere, data_decorare, timp_minute, finalizare)
VALUES
('Dovleac clasic cu decoratiuni colorate', '2025-01-10', 120, 'Da'),
('Dovleac sculptat in forma de pisica', '2025-01-11', 150, 'Nu'),
('Dovleac pictat cu peisaj de toamna', '2025-01-12', 180, 'Da');

INSERT INTO Dovleci (descriere, data_decorare, timp_minute, finalizare)
VALUES
('Dovleac pictat cu peisaj de iarna', '2025-01-12', 180, 'Da');

-- Adaugă evaluatori
INSERT INTO Evaluatori (nume, email, data_nasterii)
VALUES
('Roxana Stan', 'roxana.stan@example.com', '1985-04-15'),
('Alexandru Marin', 'alexandru.marin@example.com', '1990-08-22'),
('Ioana Cristea', 'ioana.cristea@example.com', '1982-12-01');

-- Adaugă decorări
INSERT INTO Decorari (descriere, cod_participant, cod_dovleac)
VALUES
('Dovleac clasic cu decoratiuni colorate', 1, 1),
('Dovleac sculptat in forma de pisica', 2, 2),
('Dovleac pictat cu peisaj de toamna', 3, 3);

-- Adaugă note
INSERT INTO Note (nota, cod_evaluator, cod_dovleac)
VALUES
(8, 1, 1),
(9, 2, 1),
(7, 3, 1),
(10, 1, 3),
(9, 2, 3),
(8, 3, 3);

GO
CREATE OR ALTER PROCEDURE CreateOrAlterDecorare
	@cod_participant INT,
	@cod_dovleac INT,
	@descriere VARCHAR(200)
AS
BEGIN
	IF NOT EXISTS (SELECT * FROM Participanti AS P WHERE P.cod_participant = @cod_participant)
	BEGIN
		RAISERROR('Eroare! Cod participant invalid!', 16, 1);
		RETURN;
	END;

	IF NOT EXISTS (SELECT * FROM Dovleci AS D WHERE D.cod_dovleac = @cod_dovleac)
	BEGIN
		RAISERROR('Eroare! Cod dovleac invalid!', 16, 1);
		RETURN;
	END;

	IF EXISTS(SELECT * FROM Decorari AS D 
	WHERE D.cod_participant = @cod_participant AND D.cod_dovleac = @cod_dovleac)
	BEGIN
		--Actualizam descrierea
		UPDATE Decorari
		SET descriere = @descriere
		WHERE cod_participant = @cod_participant AND cod_dovleac = @cod_dovleac;
		PRINT('Descriere actualizata!');
		RETURN;
	END;
	ELSE
	BEGIN
		INSERT INTO Decorari(cod_participant, cod_dovleac, descriere)
		VALUES
		(@cod_participant, @cod_dovleac, @descriere);
		PRINT('Decorare adaugata!');
		RETURN;
	END;
END;

INSERT INTO Participanti (nume, numar_telefon, adresa)
VALUES
('Andrei Muresan', '0721123456', 'Strada Primaverii 10'),
('Maria Rusu', '0732456789', 'Strada Libertatii 5'),
('Cristian Minune', '0743567890', 'Strada Victoriei 20');

SELECT * FROM Decorari;
SELECT * FROM Dovleci;
SELECT * FROM Participanti;

GO
EXEC CreateOrAlterDecorare 2, 4, 'Dovleac pictat';

GO
CREATE OR ALTER VIEW vw_bestParticipant 
AS
SELECT TOP 1 P.nume FROM
Participanti AS P 
INNER JOIN Decorari AS De ON P.cod_participant = De.cod_participant
INNER JOIN Dovleci AS D ON De.cod_dovleac = D.cod_dovleac
WHERE D.finalizare = 'Da'
GROUP BY P.nume, P.cod_participant
ORDER BY COUNT(P.nume) DESC;

GO
SELECT * FROM vw_bestParticipant;

SELECT * FROM Decorari
ORDER BY cod_dovleac
OFFSET 2 ROWS
FETCH NEXT 2 ROWS ONLY;


