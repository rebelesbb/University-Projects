ALTER TABLE Clienti
ADD CONSTRAINT UQ_Clienti_Telefon UNIQUE (numar_telefon);


-- CLIENTI

INSERT INTO Clienti (nume, numar_telefon) VALUES
('Popescu Andrei', '0712345670'),
('Ionescu Maria', '0712345671'),
('Dumitru Sorin', '0712345672'),
('Pavel Elena', '0712345673'),
('Radu Bianca', '0712345674'),
('Mihaila Paul', '0712345675'),
('Vasile Alina', '0712345676'),
('Cristea Florin', '0712345677'),
('Marin Oana', '0712345678'),
('Petrescu Radu', '0712345679'),
('Nicolescu Andreea', '0712345680'),
('Barbu Adrian', '0712345681'),
('Georgescu Raluca', '0712345682'),
('Dima Alin', '0712345683'),
('Serban Irina', '0712345684'),
('Popa Ionut', '0712345685'),
('Enescu Camelia', '0712345686'),
('Matei Daniel', '0712345687'),
('Moraru Simona', '0712345688'),
('Panaite Victor', '0712345689'),
('Rusu Mihai', '0712345691');


INSERT INTO Clienti (nume, numar_telefon) VALUES
('Neagu Cristina', '0712345690');
INSERT INTO Clienti (nume, numar_telefon) VALUES
('Sava Anca', '0712345692'),
('Hodorogea Ovidiu', '0712345693'),
('Grigore Larisa', '0712345694'),
('Toma Radu', '0712345695'),
('Lazar Claudia', '0712345696'),
('Marinescu Florin', '0712345697'),
('Dragan Denisa', '0712345698'),
('Popescu Victor', '0712345699');

/*
('Cojocaru Iulia', '0712345700'),
('Sinescu Cristian', '0712345701'),
('Vasile Gabriela', '0712345702'),
('Tudor Andrei', '0712345703'),
('Dumitrescu Loredana', '0712345704'),
('Radu Marius', '0712345705'),
('Buzescu Corina', '0712345706'),
('Dima Alina', '0712345707'),
('Nica Emil', '0712345708'),
('Popescu Sorina', '0712345709'),
('Filimon George', '0712345710'),
('Gheorghe Elena', '0712345711'),
('Moldovan Raluca', '0712345712'),
('Mateescu Paul', '0712345713'),
('Dumitru Radu', '0712345714'),
('Vlad Ioana', '0712345715'),
('Toma Adrian', '0712345716'),
('Lazar Oana', '0712345717'),
('Mihaila Sorin', '0712345718'),
('Hodoroaga Biancă', '0712345719'),
('Rasdan Alin', '0712345720'),
('Neagu Ion', '0712345721'),
('Cristea Raluca', '0712345722'),
('Sava Dan', '0712345723'),
('Nistor Elena', '0712345724'),
('Filipescu Ionuț', '0712345725'),
('Pavel Gabriela', '0712345726'),
('Balan Vasile', '0712345727'),
('Grigore Simona', '0712345728'),
('Rusu Petru', '0712345729'),
('Ilie Irina', '0712345730'),
('Moldovan Radu', '0712345731'),
('Sinescu Daniel', '0712345732'),
('Cristea Maria', '0712345733'),
('Tudor Alina', '0712345734'),
('Popescu Ion', '0712345735'),
('Radu Alina', '0712345736'),
('Panaite Adrian', '0712345737'),
('Dumitrescu Vlad', '0712345738'),
('Neagu Florin', '0712345739'),
('Marin Iulia', '0712345740'),
('Popescu Mircea', '0712345741'),
('Dragan Raluca', '0712345742'),
('Toma Paul', '0712345743'),
('Grigore Andreea', '0712345744'),
('Hodorogea Ionut', '0712345745'),
('Nicolescu Simona', '0712345746'),
('Vlad Mihai', '0712345747'),
('Dima Bianca', '0712345748'),
('Marinescu Andreea', '0712345749'),
('Popescu Marius', '0712345750'),
('Cojocaru Vlad', '0712345751'),
('Sava Gabriela', '0712345752'),
('Vasile Florin', '0712345753'),
('Neagu Radu', '0712345754'),
('Dragan Elena', '0712345755'),
('Barbu Ion', '0712345756'),
('Gheorghe Cristian', '0712345757'),
('Marin Andreea', '0712345758'),
('Mateescu George', '0712345759'),
('Toma Mihai', '0712345760'),
('Radu Andreea', '0712345761');
*/
DELETE FROM Clienti;

DBCC CHECKIDENT ('Clienti', RESEED, 0); -- CA SA SE RESETEZE VALOAREA DE LA PRIMARYKEY

DELETE FROM Clienti
WHERE cod_client IN(
		SELECT C.cod_client
		FROM Clienti C
		LEFT OUTER JOIN Comenzi CO ON C.cod_client = CO.cod_client
		WHERE CO.cod_comanda IS NULL);


DELETE FROM Clienti
WHERE cod_client >= 93;

DBCC CHECKIDENT ('Clienti', RESEED, 22);

SELECT * FROM Clienti;  