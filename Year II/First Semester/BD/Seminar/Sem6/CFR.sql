CREATE DATABASE CFRdatabase;
GO
USE CFRdatabase;

CREATE TABLE Tip
(
cod_t INT IDENTITY PRIMARY KEY,
descriere VARCHAR(100)
);

CREATE TABLE Trenuri
(
cod_tr INT IDENTITY PRIMARY KEY,
nume VARCHAR(100),
cod_t INT FOREIGN KEY REFERENCES Tip(cod_t)
);

CREATE TABLE Rute
(
cod_r INT IDENTITY PRIMARY KEY,
nume VARCHAR(100),
cod_tr INT FOREIGN KEY REFERENCES Trenuri(cod_tr)
);

CREATE TABLE Statii
(
cod_s INT IDENTITY PRIMARY KEY,
nume VARCHAR(100)
);

CREATE TABLE StatiiRute
(
cod_r INT FOREIGN KEY REFERENCES Rute(cod_r),
cod_s INT FOREIGN KEY REFERENCES Statii(cod_s),
ora_sosire TIME,
ora_plecare TIME,
CONSTRAINT pk_StatiiRute PRIMARY KEY (cod_r, cod_s)
);


-- Insert records into Tip table
INSERT INTO Tip (descriere) VALUES ('Rapid');
INSERT INTO Tip (descriere) VALUES ('Intercity');
INSERT INTO Tip (descriere) VALUES ('Personal');
INSERT INTO Tip (descriere) VALUES ('International');
INSERT INTO Tip (descriere) VALUES ('Expres');

-- Insert records into Trenuri table
INSERT INTO Trenuri (nume, cod_t) VALUES ('Train Alpha', 1);
INSERT INTO Trenuri (nume, cod_t) VALUES ('Train Beta', 2);
INSERT INTO Trenuri (nume, cod_t) VALUES ('Train Gamma', 3);
INSERT INTO Trenuri (nume, cod_t) VALUES ('Train Delta', 4);
INSERT INTO Trenuri (nume, cod_t) VALUES ('Train Epsilon', 5);

-- Insert records into Rute table
INSERT INTO Rute (nume, cod_tr) VALUES ('Route 101', 1);
INSERT INTO Rute (nume, cod_tr) VALUES ('Route 202', 2);
INSERT INTO Rute (nume, cod_tr) VALUES ('Route 303', 3);
INSERT INTO Rute (nume, cod_tr) VALUES ('Route 404', 4);
INSERT INTO Rute (nume, cod_tr) VALUES ('Route 505', 5);

-- Insert records into Statii table
INSERT INTO Statii (nume) VALUES ('Station A');
INSERT INTO Statii (nume) VALUES ('Station B');
INSERT INTO Statii (nume) VALUES ('Station C');
INSERT INTO Statii (nume) VALUES ('Station D');
INSERT INTO Statii (nume) VALUES ('Station E');

-- Insert records into StatiiRute table
INSERT INTO StatiiRute (cod_r, cod_s, ora_sosire, ora_plecare) VALUES (1, 1, '08:00:00', '08:15:00');
INSERT INTO StatiiRute (cod_r, cod_s, ora_sosire, ora_plecare) VALUES (1, 2, '08:45:00', '09:00:00');
INSERT INTO StatiiRute (cod_r, cod_s, ora_sosire, ora_plecare) VALUES (2, 3, '10:00:00', '10:15:00');
INSERT INTO StatiiRute (cod_r, cod_s, ora_sosire, ora_plecare) VALUES (2, 4, '10:45:00', '11:00:00');
INSERT INTO StatiiRute (cod_r, cod_s, ora_sosire, ora_plecare) VALUES (3, 5, '12:00:00', '12:15:00');

GO
CREATE PROCEDURE upsert_StatiiRute
	@cod_r INT,
	@cod_s INT,
	@ora_sosire TIME,
	@ora_plecare TIME
AS
BEGIN
	IF EXISTS(SELECT * FROM StatiiRute WHERE cod_s = @cod_s AND cod_r = @cod_r)
		BEGIN
			UPDATE StatiiRute SET
			ora_sosire = @ora_sosire,
			ora_plecare = @ora_plecare
			WHERE  cod_r = @cod_r AND cod_s = @cod_s;
			PRINT('Date actualizate!');
		END;
	ELSE
		BEGIN
			INSERT INTO StatiiRute(cod_r, cod_s, ora_sosire, ora_plecare)
			VALUES
			(@cod_r, @cod_s, @ora_sosire, @ora_plecare);
			PRINT('Statie introdusa!');
		END;

END;

SELECT * FROM StatiiRute;

EXEC upsert_StatiiRute 2, 2, '09:45:00', '09:50:00';
EXEC upsert_StatiiRute 1, 5, '11:45:00', '11:50:00';

GO
CREATE OR ALTER VIEW vw_RuteToateStatiile
AS
SELECT DISTINCT 
R.nume FROM Rute R
WHERE (SELECT COUNT(cod_s) FROM Statii) = (SELECT COUNT(*) FROM StatiiRute SR_ WHERE SR_.cod_r = R.cod_r);

GO
CREATE VIEW wv_RuteToateStatiile2
AS
SELECT R.nume FROM Rute R
INNER JOIN StatiiRute SR ON SR.cod_r = R.cod_r
GROUP BY R.cod_r, R.nume HAVING COUNT(*) = (SELECT COUNT(*) FROM Statii); 

select * from dbo.vw_RuteToateStatiile;
select * from dbo.wv_RuteToateStatiile2;

SELECT * FROM Statii;
DELETE FROM Statii WHERE cod_s >= 6;
DELETE FROM StatiiRute WHERE cod_s = 2 AND cod_r = 2;