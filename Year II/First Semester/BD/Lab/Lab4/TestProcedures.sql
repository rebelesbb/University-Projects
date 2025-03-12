USE McDonaldsDB;
SELECT * FROM Tables;
SELECT * FROM Views;
SELECT * FROM Tests;
SELECT * FROM TestTables;
SELECT * FROM TestViews;
SELECT * FROM ComenziProduseCopy;

INSERT INTO Tables(Name)
VALUES
('ClientiCopy'),
('ComenziCopy'),
('ComenziProduseCopy');

INSERT INTO TestViews(TestID, ViewID)
VALUES
(1, 1),
(1, 2),
(1, 3);

INSERT INTO Tests(Name)
VALUES
('TestInsertClientiComenziCProduse');

INSERT INTO TestTables(TestID, TableID, NoOfRows, Position)
VALUES
(1, 1, 1000, 3),
(1, 2, 1000, 2),
(1, 3, 1000, 1);

------------------------------------------------------------------

GO
ALTER PROCEDURE deleteFromTable
	@currentPosition INT
AS
BEGIN
	DECLARE @tableName VARCHAR(50);
	
	SET @tableName = (SELECT T.Name FROM Tables T WHERE T.TableID = @currentPosition);
	EXEC('DELETE FROM ' + @tableName);

	IF (OBJECTPROPERTY(OBJECT_ID(@tableName), 'TableHasIdentity') = 1) 
		DBCC CHECKIDENT(@tableName, RESEED, 0);
END;

-------------------------------------------------------------------------------------

GO
ALTER PROCEDURE insertIntoClientiCopy
	@numberOfRows INT
AS
BEGIN 

	WHILE(@numberOfRows > 0)
	BEGIN 
		INSERT INTO ClientiCopy(nume, numar_telefon)
		VALUES
		(
			'Client' + CAST(@numberOfRows AS VARCHAR(5)), 
			'07' + CAST(10000000 + CAST(FLOOR(RAND() * 10000000) AS INT) AS CHAR(8))
		);
		SET @numberOfRows = @numberOfRows - 1;
	END;

END;

-------------------------------------------------------------------------------------------

ALTER PROCEDURE insertIntoComenziCopy
	@numberOfRows INT
AS
BEGIN
	DECLARE @currentClient INT;

	DECLARE cursorClienti CURSOR FAST_FORWARD FOR
	SELECT C.cod_client FROM ClientiCopy C;

	OPEN cursorClienti;

	FETCH NEXT FROM cursorClienti INTO @currentClient;

	WHILE(@numberOfRows > 0)
	BEGIN 
		INSERT INTO ComenziCopy(cod_client, cod_angajat, data_comanda, ora_comanda, total)
		VALUES
		(@currentClient, 1000, CAST(GETDATE() AS DATE), CAST(GETDATE() AS TIME), 14);

		FETCH NEXT FROM cursorClienti INTO @currentClient;

		SET @numberOfRows = @numberOfRows - 1;
	END;

	CLOSE cursorClienti;
	DEALLOCATE cursorClienti;
END;

SELECT * FROM Produse

-------------------------------------------------------------------------------------------

GO
CREATE PROCEDURE insertIntoComenziProduseCopy
	@numberOfRows INT
AS
BEGIN

	DECLARE @comandaCurenta INT;

	DECLARE cursorComenzi CURSOR FAST_FORWARD FOR
	SELECT C.cod_comanda FROM ComenziCopy C;
	
	OPEN cursorComenzi;
	FETCH NEXT FROM cursorComenzi INTO @comandaCurenta;

	WHILE(@numberOfRows > 0)
	BEGIN 
		
		INSERT INTO ComenziProduseCopy(cod_comanda, cod_produs, cantitate, pretBucata)
		VALUES
		(@comandaCurenta, 106, 1, 14);

		FETCH NEXT FROM cursorComenzi INTO @comandaCurenta;

		SET @numberOfRows = @numberOfRows - 1;
	END;

	CLOSE cursorComenzi;
	DEALLOCATE cursorComenzi;
END;



-------------------------------------------------------------------------------------------

GO
ALTER PROCEDURE RunTest
	@testId INT
AS
BEGIN
	IF NOT EXISTS(SELECT * FROM Tests T WHERE T.TestID = @testId)
	BEGIN
		PRINT('No test with given id found.')
		RETURN;
	END;

	DECLARE @testStartTime DATETIME;
	DECLARE @insertStartTime DATETIME;
	DECLARE @viewStartTime DATETIME;
	DECLARE @testRunId INT;

	INSERT INTO TestRuns(Description, StartAt, EndAt)
	VALUES 
	('Running test with id ' + CAST(@testId AS CHAR(5)),
	GETDATE(),
	NULL);

	SET @testRunId = (SELECT MAX(TR.TestRunID) FROM TestRuns TR);
	print ('Current test run ' + CAST(@testRunId AS CHAR(5)));

	DECLARE tablesCursor CURSOR FAST_FORWARD FOR
	SELECT TT.TableID, T.Name, TT.NoOfRows FROM 
	Tables T INNER JOIN TestTables TT ON T.TableID = TT.TableID
	WHERE TT.TestID = @testId
	ORDER BY TT.Position;

	DECLARE @currentTableId INT;
	DECLARE @currentTableName VARCHAR(50);
	DECLARE @currentTableRows INT;
	DECLARE @currentViewId INT;
	DECLARE @currentViewName VARCHAR(50);

	OPEN tablesCursor;
	FETCH NEXT FROM tablesCursor INTO @currentTableId, @currentTableName, @currentTableRows;

	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT ('Deleted from table ' + @currentTableName);

		EXEC('deleteFromTable ' + @currentTableId);

		FETCH NEXT FROM tablesCursor INTO @currentTableId, @currentTableName, @currentTableRows;
	END;

	CLOSE tablesCursor;
	DEALLOCATE tablesCursor;


	-- declaram cursorul tablesCursor, de data aceasta avand rezultatul sortat in ordine inversa
	-- campului position
	DECLARE tablesCursor CURSOR FAST_FORWARD FOR
	SELECT TT.TableID, T.Name, TT.NoOfRows FROM 
	Tables T INNER JOIN TestTables TT ON T.TableID = TT.TableID
	WHERE TT.TestID = @testId
	ORDER BY TT.Position DESC;

	OPEN tablesCursor
	FETCH NEXT FROM tablesCursor INTO @currentTableId, @currentTableName, @currentTableRows;

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @insertStartTime = GETDATE();

		EXEC('insertInto' + @currentTableName + ' ' + @currentTableRows);

		INSERT INTO TestRunTables(TestRunID, TableID, StartAt, EndAt)
		VALUES
		(@testRunId, @currentTableId, @insertStartTime, GETDATE());

		FETCH NEXT FROM tablesCursor INTO @currentTableId, @currentTableName, @currentTableRows;

	END;

	CLOSE tablesCursor;
	DEALLOCATE tablesCursor;

	DECLARE viewsCursor CURSOR FAST_FORWARD FOR
	SELECT V.ViewID, V.Name 
	FROM Views V INNER JOIN TestViews TV ON V.ViewID = TV.ViewID
	WHERE TV.TestID = @testId;

	OPEN viewsCursor;

	FETCH NEXT FROM viewsCursor INTO @currentViewId, @currentViewName;

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @viewStartTime = GETDATE();
		
		EXEC('SELECT * FROM dbo.' + @currentViewName)

		INSERT INTO TestRunViews(TestRunID, ViewID, StartAt, EndAt)
		VALUES
		(@testRunId, @currentViewId, @viewStartTime, GETDATE());

		FETCH NEXT FROM viewsCursor INTO @currentViewId, @currentViewName;

	END;

	CLOSE viewsCursor;
	DEALLOCATE viewsCursor;

	-- Setam momentul la care testul se termina
	UPDATE TestRuns SET EndAt = GETDATE()
	WHERE TestRunID = @testRunId;
END;






go
SELECT TT.TableID, TT.Position, TT.NoOfRows FROM 
Tables T INNER JOIN TestTables TT ON T.TableID = TT.TableID
WHERE TT.TestID = 1
ORDER BY TT.Position DESC;

SELECT * FROM ClientiCopy;
SELECT * FROM ComenziCopy;
SELECT * FROM ComenziProduseCopy;

SELECT * FROM TestRuns;
SELECT * FROM TestRunTables;
SELECT * FROM TestRunViews;
DELETE FROM TestRuns;
DELETE FROM TestRunTables;

SELECT * FROM dbo.vw_Locatii;
SELECT * FROM Views;

DELETE FROM TestRuns;

GO
EXEC RunTest 1;
