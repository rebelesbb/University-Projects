USE McDonaldsDB;


GO
ALTER FUNCTION ValidateClient(@name VARCHAR(200), @phone_number VARCHAR(20))
	RETURNS VARCHAR(100)
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) = '';

	IF (@name IS NULL OR @name LIKE '%[0-9]%' OR @name = '')
		SET @errorsString = @errorsString + 'Nume invalid!' + CHAR(13) + CHAR(10);
	IF NOT(@phone_number IS NULL OR @phone_number LIKE '07[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
		SET @errorsString = @errorsString + 'Numar de telefon invalid!' + CHAR(13) + CHAR(10);
	
	RETURN @errorsString;
END;


GO
ALTER FUNCTION ValidateClientId(@clientId INT)
	RETURNS VARCHAR(100)
AS
BEGIN
	IF (@clientId IS NULL OR NOT EXISTS(SELECT * FROM Clienti WHERE cod_client = @clientId))
		RETURN 'Nu exista un client cu id-ul dat!' + CHAR(13) + CHAR(10);
	RETURN '';
END


GO
CREATE PROCEDURE CreateClient
	@nume VARCHAR(200),
	@numar_telefon VARCHAR(20)
AS
BEGIN
	DECLARE @errorsString VARCHAR(100);
	SET @errorsString = dbo.ValidateClient(@nume, @numar_telefon);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1)
		RETURN;
	END;

	INSERT INTO Clienti(nume, numar_telefon)
	VALUES
	(@nume, @numar_telefon);

	PRINT('Client adaugat cu succes!');
END;


GO
CREATE PROCEDURE GetAllClients
AS
BEGIN
	SELECT * FROM Clienti;
END;


GO
CREATE PROCEDURE FindOneClient
	@clientId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) = dbo.ValidateClientId(@clientId);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;
	SELECT * FROM Clienti WHERE cod_client = @clientId;
END;


GO
ALTER PROCEDURE UpdateClient 
	@clientId INT,
	@newName VARCHAR(200),
	@newPhoneNumber VARCHAR(20)
AS
BEGIN
	DECLARE	@errorsString VARCHAR(200) = '';
	SET @errorsString = @errorsString + dbo.ValidateClientId(@clientId);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	SET @errorsString = @errorsString + dbo.ValidateClient(@newName, @newPhoneNumber);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	UPDATE Clienti SET
	nume = @newName,
	numar_telefon = @newPhoneNumber
	WHERE cod_client = @clientId;

	PRINT('Date actualizate cu succes!');
END;

GO
CREATE PROCEDURE DeleteClient
	@clientId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(200) = dbo.ValidateClientId(@clientId);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	DELETE FROM Clienti
	WHERE cod_client = @clientId;

	PRINT('Client sters cu succes!');

END;

GO
EXEC GetAllClients;
EXEC FindOneClient 40;
EXEC CreateClient 'Nume', '0722232222';
EXEC UpdateClient 40, 'Jabsd', '0722232229';
EXEC DeleteClient 40;