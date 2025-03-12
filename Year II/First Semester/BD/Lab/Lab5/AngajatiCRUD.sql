USE McDonaldsDB;

select * from Locatii

-- dbo.ValidateEmployeeId(@emplyeeId INT) RETURNS VARCHAR(100)

GO
CREATE FUNCTION ValidateEmployee(@lastname VARCHAR(200),@firstname VARCHAR(200), @phoneNumber VARCHAR(200), 
								@locationId INT, @position VARCHAR(200), @salary INT, @employmentDate DATE)
	RETURNS VARCHAR(250)
AS
BEGIN
	DECLARE @errorsString VARCHAR(250) = '';
	
	IF (@lastname LIKE '%[0-9]%' OR @lastname = '')
		SET @errorsString = @errorsString + 'Nume invalid!' + CHAR(13) + CHAR(10);

	IF (@firstname LIKE '%[0-9]%' OR @firstname = '')
		SET @errorsString = @errorsString + 'Prenume invalid!' + CHAR(13) + CHAR(10);

	IF NOT(@phoneNumber LIKE '07[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
		SET @errorsString = @errorsString + 'Numar de telefon invalid!' + CHAR(13) + CHAR(10);

	IF EXISTS(SELECT * FROM Angajati WHERE numar_telefon = @phoneNumber)
		SET @errorsString = @errorsString + 'Numarul de telefon exista deja!' + CHAR(13) + CHAR(10);

	IF NOT EXISTS(SELECT * FROM Locatii WHERE cod_locatie = @locationId)
		SET @errorsString = @errorsString + 'Cod locatie invalid!' + CHAR(13) + CHAR(10);

	IF (@position != 'Manager' AND @position != 'Casier' AND @position != 'Bucatar')
		SET @errorsString = @errorsString + 'Functie invalida!' + CHAR(13) + CHAR(10);

	IF (@salary <= 0)
		SET @errorsString = @errorsString + 'Salariu invalid!' + CHAR(13) + CHAR(10);

	IF (@employmentDate > CAST(GETDATE() AS DATE))
		SET @errorsString = @errorsString + 'Data invalida!' + CHAR(13) + CHAR(10);

	RETURN @errorsString;
END;

GO 
CREATE PROCEDURE CreateEmployee
	@lastname VARCHAR(200),
	@firstname VARCHAR(200),
	@phoneNumber VARCHAR(20),
	@locationId INT,
	@position VARCHAR(100),
	@salary INT,
	@employmentDate DATE
AS
BEGIN
	DECLARE @errorsString VARCHAR(200) = dbo.ValidateEmployee(@lastname, @firstname, @phoneNumber, @locationId, @position, @salary, @employmentDate);
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	INSERT INTO Angajati(nume, prenume, cod_locatie, numar_telefon, functie, salariu, data_angajare)
	VALUES
	(@lastname, @firstname, @locationId, @phoneNumber, @position, @salary, @employmentDate);

	PRINT('Angajat adaugat cu succes!');
END;


GO
CREATE PROCEDURE GetAllEmployees
AS
BEGIN
	SELECT * FROM Angajati;
END;


GO
CREATE PROCEDURE FindOneEmployee
	@employeeId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) = dbo.ValidateEmployeeId(@employeeId);
	IF NOT(@errorsString = '')
	BEGIN
	 RAISERROR(@errorsString, 16, 1);
	 RETURN;
	END;

	SELECT * FROM Angajati WHERE cod_angajat = @employeeId;

END;

GO
CREATE PROCEDURE UpdateEmployee
	@employeeId INT,
	@newLastname VARCHAR(200),
	@newFirstname VARCHAR(200),
	@newPhoneNumber VARCHAR(20),
	@newLocationId INT,
	@newPosition VARCHAR(100),
	@newSalary INT,
	@newEmploymentDate DATE
AS
BEGIN
	DECLARE @errorsString VARCHAR(250) = dbo.ValidateEmployeeId(@employeeId);
	SET @errorsString = @errorsString + dbo.ValidateEmployee(@newLastname, @newFirstname, @newPhoneNumber, @newLocationId, @newPosition, @newSalary, @newEmploymentDate);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	UPDATE Angajati SET
	nume = @newLastname,
	prenume = @newFirstname,
	numar_telefon = @newPhoneNumber,
	cod_locatie = @newLocationId,
	functie = @newPosition,
	salariu = @newSalary,
	data_angajare = @newEmploymentDate
	WHERE cod_angajat = @employeeId;

	PRINT('Date actualizate cu succes');
END;


GO
CREATE PROCEDURE DeleteEmployee
	@employeeId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) =dbo.ValidateEmployeeId(@employeeId);	
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	DELETE FROM Angajati WHERE cod_angajat = @employeeId;

	PRINT('Angajat sters cu succes!');
END;

GO
EXEC GetAllEmployees;
EXEC CreateEmployee 'Popescu', 'David', '0798765432', 1, 'Casier', 2500, '2024-05-03';
EXEC CreateEmployee 'Pop4escu', '', '07985565432', 100, 'Caser', 0, '2025-05-03';
EXEC FindOneEmployee 1102;
EXEC UpdateEmployee 1102, 'Po4pescu', '', '07898999848', 100, 'Cas3ier', 0, '2025-07-07';
EXEC UpdateEmployee 1102, 'Popovici', 'Denis', '0789899984', 1, 'Casier', 1, '2024-07-07';
EXEC DeleteEmployee 1102;
