USE McDonaldsDB;

CREATE TABLE VersiuneCurenta
(
cod_v INT PRIMARY KEY IDENTITY,
numar INT
)

INSERT INTO VersiuneCurenta(numar) VALUES(0);

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

GO
CREATE PROCEDURE Undo_V1
AS
BEGIN
	DROP TABLE Reviews;
END;


GO 
CREATE PROCEDURE V2
AS
BEGIN 
	ALTER TABLE Reviews 
	ADD CONSTRAINT df_date_constraint
	DEFAULT CONVERT(date, GETDATE()) FOR data_review;
END;

GO
CREATE PROCEDURE Undo_V2
AS 
BEGIN
	ALTER TABLE Reviews
	DROP CONSTRAINT df_date_constraint
END;


GO
CREATE PROCEDURE V3
AS
BEGIN
	ALTER TABLE Reviews
	ALTER COLUMN descriere NVARCHAR(200);
END;

GO 
CREATE PROCEDURE Undo_V3
AS
BEGIN
	ALTER TABLE Reviews
	ALTER COLUMN descriere VARCHAR(200);
END;


GO
CREATE PROCEDURE V4
AS
BEGIN
	ALTER TABLE Reviews
	ADD cod_comanda INT;
END;

GO
CREATE PROCEDURE Undo_V4
AS
BEGIN
	ALTER TABLE Reviews
	DROP COLUMN cod_comanda;
END;


GO
CREATE PROCEDURE V5
AS
BEGIN
	ALTER TABLE Reviews
	ADD CONSTRAINT fk_comanda_constraint FOREIGN KEY (cod_comanda) REFERENCES Comenzi(cod_comanda);
END;

GO
ALTER PROCEDURE Undo_V5
AS
BEGIN
	ALTER TABLE Reviews
	DROP CONSTRAINT fk_comanda_constraint;
END;

GO
ALTER PROCEDURE GestionareVersiuneTest
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
END;


GO
EXEC GestionareVersiuneTest 0;

SELECT * FROM VersiuneCurenta;


INSERT INTO Reviews(nota, cod_client, descriere)
VALUES
(3,1,'Meh');

SELECT * FROM Reviews;
SELECT * FROM VersiuneCurenta;
DELETE FROM Reviews;

UPDATE VersiuneCurenta
SET numar = 0;