USE McDonaldsDB;

-- dbo.ValidateClientId(clientId)

GO
ALTER FUNCTION ValidateEmployeeId(@employeeId INT)
	RETURNS VARCHAR(100)
AS
BEGIN
	IF (@employeeId IS NULL OR NOT EXISTS(SELECT * FROM Angajati WHERE cod_angajat = @employeeId))
		RETURN 'Nu exista un angajat cu id-ul dat' + CHAR(13) + CHAR(10);
	RETURN '';
END;


GO
ALTER FUNCTION ValidateOrderId(@orderId INT)
	RETURNS VARCHAR(100)
AS
BEGIN
	IF (@orderId IS NULL OR NOT EXISTS(SELECT * FROM Comenzi WHERE cod_comanda = @orderId))
		RETURN 'Nu exista o comanda cu id-ul dat!' + CHAR(13) + CHAR(10);
	RETURN '';
END;


GO
ALTER FUNCTION ValidateOrder(@clientId INT, @employeeId INT, @date DATE, @time TIME, @price DECIMAL)
	RETURNS VARCHAR(150)
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateClientId(@clientId);
	SET @errorsString = @errorsString + dbo.ValidateEmployeeId(@employeeId);

	IF (@date IS NULL OR @date > CAST(GETDATE() AS DATE))
		SET @errorsString = @errorsString + 'Data invalida!' + CHAR(13) + CHAR(10);

	IF (@time IS NULL OR @date IS NULL OR (@date = CAST(GETDATE() AS DATE) AND @time > CAST(GETDATE() AS TIME)))
		SET @errorsString = @errorsString + 'Timp invalid!' + CHAR(13) + CHAR(10);

	IF (@price IS NULL OR @price < 0)
		SET @errorsString = @errorsString + 'Pret invalid!' + CHAR(13) + CHAR(10);

	RETURN @errorsString;
END;


GO
ALTER PROCEDURE CreateOrder
	@clientId INT,
	@employeeID INT,
	@date DATE,
	@time TIME,
	@price DECIMAL
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateOrder(@clientId, @employeeId, @date, @time, @price);
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
	VALUES
	(@clientId, @employeeId, @date, @time, @price);

	PRINT 'Comanda adaugata cu succes!';
END;


GO
CREATE PROCEDURE GetAllOrders
AS
BEGIN
	SELECT * FROM Comenzi;
END;


GO
ALTER PROCEDURE FindOneOrder
	@orderId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) = dbo.ValidateOrderId(@orderId);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	SELECT * FROM Comenzi WHERE cod_comanda = @orderId;
END;


GO
ALTER PROCEDURE UpdateOrder
	@orderId INT,
	@newClientId INT,
	@newEmployeeID INT,
	@newDate DATE,
	@newTime TIME,
	@newPrice DECIMAL
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateOrderId(@orderId);
	SET @errorsString = @errorsString + dbo.ValidateOrder(@newClientID, @newEmployeeId, @newDate, @newTime, @newPrice);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	UPDATE Comenzi SET
	cod_client = @newClientId,
	cod_angajat = @newEmployeeID,
	data_comanda = @newDate,
	ora_comanda = @newTime,
	total = @newPrice
	WHERE cod_comanda = @orderId;

	PRINT('Date actualizate cu succes!');
END;


GO
ALTER PROCEDURE DeleteOrder
	@orderId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) = dbo.ValidateOrderId(@orderId);
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	DELETE FROM Comenzi
	WHERE cod_comanda = @orderId;

	PRINT('Comanda stearsa cu succes!');
END;

GO
SELECT * FROM Angajati;
SELECT * FROM Comenzi;
EXEC CreateOrder 30, 1016, '2024-12-09', '02:15:00', 100;
EXEC GetAllOrders;
EXEC FindOneOrder 52;
EXEC FindOneOrder 50;
EXEC UpdateOrder 52, 29, 1001, '2024-12-09', '23:12:00', 100;
EXEC DeleteOrder 52;
