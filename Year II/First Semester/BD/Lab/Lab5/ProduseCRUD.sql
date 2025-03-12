USE McDonaldsDB;

SELECT * FROM Produse

GO
CREATE FUNCTION ValidateProduct(@productName VARCHAR(100), @ingredients VARCHAR(200), @price DECIMAL(5,2))
	RETURNS VARCHAR(150)
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = '';

	IF(@productName IS NULL OR @productName = '')
		SET @errorsString = @errorsString + 'Nume invalid!' + CHAR(13) + CHAR(10);
	IF(@ingredients IS NULL)
		SET @errorsString = @errorsString + 'Ingrediente invalide!' + CHAR(13) + CHAR(10)
	IF(@price IS NULL OR @price < 0)
		SET @errorsString = @errorsString + 'Pret invalid!' + CHAR(13) + CHAR(10)
	RETURN @errorsString;
END;

GO
CREATE FUNCTION ValidateProductId(@productId INT)
	RETURNS VARCHAR(150)
AS
BEGIN
	IF NOT EXISTS(SELECT * FROM Produse WHERE cod_produs = @productId)
		RETURN 'Nu exista un produs cu id-ul dat!' + CHAR(13) + CHAR(10);
	RETURN '';
END;

GO
CREATE PROCEDURE CreateProduct
	@productName VARCHAR(100),
	@ingredients VARCHAR(200),
	@price DECIMAL(5,2)
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateProduct(@productName, @ingredients, @price);
	
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	INSERT INTO Produse(nume, ingrediente, pret)
	VALUES
	(@productName, @ingredients, @price);

	PRINT('Produs adaugat cu succes!');
END;

GO
CREATE PROCEDURE GetAllProducts
AS
BEGIN
	SELECT * FROM Produse;
END;

GO 
CREATE PROCEDURE FindOneProduct 
	@productId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateProductId(@productId);

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	SELECT * FROM Produse WHERE cod_produs = @productId;
END;

GO
CREATE PROCEDURE UpdateProduct
	@productId INT,
	@newProductName VARCHAR(100),
	@newIngredients VARCHAR(200),
	@newPrice DECIMAL(5,2)
AS
BEGIN
	DECLARE @errorsString VARCHAR(200) = dbo.ValidateProductId(@productId);
	
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	SET @errorsString = @errorsString + dbo.ValidateProduct(@newProductName, @newIngredients, @newPrice)

	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	UPDATE Produse SET
	nume = @newProductName,
	ingrediente = @newIngredients,
	pret = @newPrice
	WHERE cod_produs = @productId;

	PRINT('Date actualizat cu succes!');
END;

GO
CREATE PROCEDURE DeleteProduct
	@productId INT
AS
BEGIN
	DECLARE @errorsString VARCHAR(150) = dbo.ValidateProductId(@productId);
	
	IF NOT(@errorsString = '')
	BEGIN
		RAISERROR(@errorsString, 16, 1);
		RETURN;
	END;

	DELETE FROM Produse WHERE cod_produs = @productId;

	PRINT('Produs sters cu succes!');
END;

GO
EXEC GetAllProducts;
EXEC CreateProduct 'Produs Nou', 'Ingredient1, Ingredient2', 12;
EXEC CreateProduct '', NULL, -13;
EXEC FindOneProduct 204;
EXEC UpdateProduct 204, 'Produs', 'Ingredient1, Ingredient3, Ingredient5', 0;
EXEC UpdateProduct 201, '', NULL, -1;
EXEC UpdateProduct 203, '', NULL, -1;
EXEC DeleteProduct 204;



