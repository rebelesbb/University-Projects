USE McDonaldsDB;

GO
ALTER FUNCTION ValidateProductOrder(@productId INT, @orderId INT, @quantity INT)
	RETURNS VARCHAR(150)
AS
BEGIN
	
	DECLARE @errorsString VARCHAR(150) = '';
	
	SET @errorsString = dbo.ValidateProductId(@productId);
	SET @errorsString = @errorsString + dbo.ValidateOrderId(@orderId);

	IF EXISTS(SELECT * FROM ComenziProduse WHERE cod_produs = @productId AND cod_comanda = @orderId)
		SET @errorsString = @errorsString + 'Comanda corespunzatoare produsului a fost deja inregistrata!';

	IF (@quantity IS NULL OR @quantity <= 0)
		SET @errorsString = @errorsString + 'Cantitate invalida!';
	
	RETURN @errorsString;
END;

GO
CREATE FUNCTION ValidateProductOrderId(@productId INT, @orderId INT)
	RETURNS VARCHAR(100)
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) = dbo.ValidateProductId(@productId) + dbo.ValidateOrderId(@orderId);
	IF NOT(@errorsString = '')
		RETURN @errorsString;

	IF NOT EXISTS(SELECT * FROM ComenziProduse WHERE cod_produs = @productId AND cod_comanda = @orderId)
		RETURN 'Produsul nu se afla in comanda precizata!';
	RETURN '';
END;

GO 
ALTER FUNCTION ValidateUpdatedProductOrder(@productId INT, @orderId INT, @quantity INT)
	RETURNS	VARCHAR(150)
AS
BEGIN
	DECLARE @errorsString VARCHAR(150);

	SET @errorsString = dbo.ValidateProductOrderId(@productId, @orderId);
	IF NOT(@errorsString = '')
		RETURN @errorsString;

	IF (@quantity <= 0)
		RETURN 'Cantitate invalida!';
	
	RETURN '';
END;

GO
ALTER PROCEDURE CreateProductOrder
	@productId INT,
	@orderId INT,
	@quantity INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateProductOrder(@productId, @orderId, @quantity);
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	DECLARE @price INT;
	SET @price = (SELECT pret FROM Produse WHERE cod_produs = @productId);

	INSERT INTO ComenziProduse(cod_produs, cod_comanda, cantitate, pretBucata)
	VALUES
	(@productId, @orderId, @quantity, @price);
END;

GO
CREATE PROCEDURE GetAllProductOrders
AS
BEGIN
	SELECT * FROM ComenziProduse;
END;

GO
CREATE PROCEDURE FindOneProductOrder
	@productId INT,
	@orderId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(100) = dbo.ValidateProductOrderId(@productId, @orderId);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	SELECT * FROM ComenziProduse WHERE cod_produs = @productId AND cod_comanda = @orderId;
END;


GO
CREATE PROCEDURE UpdateProductOrder
	@productId INT,
	@orderId INT,
	@newQuantity INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateUpdatedProductOrder(@productId, @orderId, @newQuantity);
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	DECLARE @newPrice DECIMAL(5,2);
	SET @newPrice = (SELECT pretBucata FROM ComenziProduse WHERE cod_produs = @productId AND cod_comanda = @orderId);

	UPDATE ComenziProduse SET
	cantitate = @newQuantity,
	pretBucata = @newPrice
	WHERE cod_produs = @productId AND cod_comanda = @orderId;

	PRINT('Date actualizate cu succes!');

END;

GO
CREATE PROCEDURE DeleteProductOrder
	@productId INT,
	@orderId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateProductOrderId(@productId, @orderId);
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	DELETE FROM ComenziProduse
	WHERE cod_produs = @productId AND cod_comanda = @orderId;

	PRINT('Produs eliminat cu succes din comanda precizata!');
END;

GO
EXEC GetAllProductOrders;
EXEC GetAllOrders; -- 49
EXEC GetAllClients;
EXEC GetAllProducts;
EXEC CreateOrder 1, 1001, '2024-02-02', '12:12:12', 12;
EXEC CreateProductOrder 101, 51, 1;
PRINT dbo.ValidateOrderId(492);
EXEC FindOneProductOrder 1001, 449;
EXEC FindOneProductOrder 101, 51;
EXEC FindOneProductOrder 100, 49;
EXEC UpdateProductOrder 101, 51, 2;
EXEC DeleteProductOrder 101, 51;
