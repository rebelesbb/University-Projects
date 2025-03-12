USE McDonaldsDB;

-- Creare tabela cu Versiune
CREATE TABLE VersiuneCurenta
(
cod_v INT PRIMARY KEY IDENTITY,
numar INT
)

-- Setare versiune la 0
INSERT INTO VersiuneCurenta(numar) VALUES(0);

-- Versiunea 1
-- Creare tabela noua, Reviews
GO
CREATE PROCEDURE V1
AS
BEGIN
	CREATE TABLE Reviews
	(
	cod_review INT IDENTITY PRIMARY KEY,
	nota INT CHECK (0 < nota AND nota <= 5),
	cod_client INT,
	descriere VARCHAR(200),
	data_review DATE,
	CONSTRAINT fk_reviews FOREIGN KEY (cod_client) REFERENCES Clienti(cod_client)
	);
END;

-- Revenire din Versiunea 1
-- Stergere tabela
GO
CREATE PROCEDURE Undo_V1
AS
BEGIN
	DROP TABLE Reviews;
END;

-- Versiunea 2
-- Adaugare constrangere default pentru campul data_review
GO 
CREATE PROCEDURE V2
AS
BEGIN 
	ALTER TABLE Reviews 
	ADD CONSTRAINT df_date_constraint
	DEFAULT CONVERT(date, GETDATE()) FOR data_review;
END;

-- Revenire din Versiunea 2
-- Stergere constrangere default
GO
CREATE PROCEDURE Undo_V2
AS 
BEGIN
	ALTER TABLE Reviews
	DROP CONSTRAINT df_date_constraint
END;


-- Versiunea 3
-- Modificare tip coloana varchar -> nvarchar
GO
CREATE PROCEDURE V3
AS
BEGIN
	ALTER TABLE Reviews
	ALTER COLUMN descriere NVARCHAR(200);
END;

-- Revenire din Versiunea 3
-- Modificare tip coloana nvarchar -> varchar
GO 
CREATE PROCEDURE Undo_V3
AS
BEGIN
	ALTER TABLE Reviews
	ALTER COLUMN descriere VARCHAR(200);
END;


-- Versiunea 4
-- Adaugare camp nou cod_comanda
GO
CREATE PROCEDURE V4
AS
BEGIN
	ALTER TABLE Reviews
	ADD cod_comanda INT;
END;


-- Revenire din Versiunea 4
-- Stergere camp cod_comanda
GO
CREATE PROCEDURE Undo_V4
AS
BEGIN
	ALTER TABLE Reviews
	DROP COLUMN cod_comanda;
END;

-- Versiunea 5
-- Adaugare constrangere de cheie straina
GO
CREATE PROCEDURE V5
AS
BEGIN
	ALTER TABLE Reviews
	ADD CONSTRAINT fk_comanda_constraint FOREIGN KEY (cod_comanda) REFERENCES Comenzi(cod_comanda);
END;


-- Revenire din Versiunea 5
-- Stergere constrangere de cheie straina
GO
ALTER PROCEDURE Undo_V5
AS
BEGIN
	ALTER TABLE Reviews
	DROP CONSTRAINT fk_comanda_constraint;
END;

-- Procedura de schimbare a versiunilor
GO
ALTER PROCEDURE GestionareVersiune
	@ver INT
AS
BEGIN 
	IF (0 <= @ver AND @ver <= 5)
	BEGIN
		DECLARE @vCurenta INT;
		SELECT @vCurenta = (SELECT TOP 1 numar FROM VersiuneCurenta);
		
		WHILE(@vCurenta != @ver)
		BEGIN
			IF(@vCurenta < @ver) ---5 4
				BEGIN

				IF(@vCurenta = 0) EXEC V1;
				IF(@vCurenta = 1) EXEC V2;
				IF(@vCurenta = 2) EXEC V3;
				IF(@vCurenta = 3) EXEC V4;
				IF(@vCurenta = 4) EXEC V5;

				SET @vCurenta = @vCurenta + 1;

				END;
			ELSE
				BEGIN

				IF(@vCurenta = 5) EXEC Undo_V5;
				IF(@vCurenta = 4) EXEC Undo_V4;
				IF(@vCurenta = 3) EXEC Undo_V3;
				IF(@vCurenta = 2) EXEC Undo_V2;
				IF(@vCurenta = 1) EXEC Undo_V1;

				SET @vCurenta = @vCurenta - 1;

				END;
		END;
		UPDATE VersiuneCurenta
		SET numar = @vCurenta
	END;

	ELSE
	BEGIN
		PRINT('Valoare invalida')
	END;
END;


GO
EXEC GestionareVersiune 7;

SELECT * FROM VersiuneCurenta;
