--comentariu--
/*
comentariu
*/

--crearea unei baze de date noi--
CREATE DATABASE [Laborator1226-1BD2024];
GO
USE [Laborator1226-1BD2024];
CREATE TABLE Persoane
(cod_p INT PRIMARY KEY IDENTITY(1,1), --IDENTITY PENTRU GENERARE AUTOMATA CHEIE, START, STEP--
nume VARCHAR(200),
data_nasterii DATE,
localitate VARCHAR(100)
);
--SPOILER INSEERT
INSERT INTO Persoane (nume, data_nasterii, localitate) VALUES
('Marcel', '1800-02-28', 'Jucu de Sus');
--SPOILER SELECT
 
/*
DELETE FROM Persoane WHERE cod_p = 1;
*/