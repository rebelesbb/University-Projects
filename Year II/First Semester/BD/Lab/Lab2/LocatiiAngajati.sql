ALTER TABLE Angajati
ADD CONSTRAINT UQ_Angajati_Telefon UNIQUE (numar_telefon);

--LOCATII
INSERT INTO Locatii (adresa, program) 
VALUES 
('Bucuresti, Bdul. Nicolae Titulescu 25', '08:00 - 22:00'),
('Bucuresti, Calea Victoriei 39', '09:00 - 23:00'),
('Cluj-Napoca, Bdul. Eroilor 2', '10:00 - 21:00'),
('Timisoara, Str. Marasesti 16', '09:30 - 22:30'),
('Iasi, Bdul. Stefan cel Mare 9', '08:00 - 21:00'),
('Brasov, Bdul. Eroilor 1', '10:00 - 23:00'),
('Constanta, Bdul. Mamaia 100', '09:00 - 24:00'),
('Bucuresti, Str. Mihai Eminescu 1', '09:00 - 22:30'),
('Sibiu, Str. Balea 4', '09:00 - 23:00'),
('Bucuresti, Calea Dorobantilor 12', '10:00 - 23:00'),
('Ploiesti, Bdul. Republicii 56', '08:00 - 22:00'),
('Bacau, Str. Nicu Enea 15', '10:00 - 22:00'),
('Oradea, Str. Traian Mosoiu 14', '09:00 - 21:30'),
('Arad, Str. Revolutiei 5', '08:00 - 22:00'),
('Targu Mures, Bdul. 1 Decembrie 1918 7', '09:30 - 23:00'),
('Galati, Str. Traian 24', '09:00 - 22:00'),
('Craiova, Str. Iona Mincu 11', '10:00 - 23:30'),
('Buzau, Str. Unirii 12', '08:30 - 22:30'),
('Satu Mare, Str. 1 Decembrie 1918 10', '09:00 - 21:00'),
('Drobeta-Turnu Severin, Bdul. Carol I 8', '09:00 - 23:00');

SELECT *
FROM Locatii;

DELETE FROM Locatii;

DBCC CHECKIDENT ('Locatii', RESEED, 0); -- CA SA SE RESETEZE VALOAREA DE LA PRIMARYKEY
 
INSERT INTO Angajati (nume, prenume, cod_locatie, numar_telefon, functie, salariu, data_angajare) 
VALUES 
('Andreev', 'Mihail', 1, '0734567890', 'Manager', 3600, '2021-03-01'),
('Ionescu', 'Sonia', 1, '0734567891', 'Casier', 2400, '2022-04-15'),
('Popescu', 'Elena', 1, '0734567892', 'Bucatar', 2800, '2023-05-10'),
('Radu', 'Cristian', 1, '0734567893', 'Bucatar', 2800, '2022-06-20'),
('Dumitrescu', 'Maria', 1, '0734567894', 'Vanzator', 2500, '2020-07-05'),

('Marinescu', 'Ion', 2, '0734567895', 'Manager', 3600, '2021-02-10'),
('Stanescu', 'Adriana', 2, '0734567896', 'Casier', 2400, '2020-03-15'),
('Vasilescu', 'Florin', 2, '0734567897', 'Bucatar', 2800, '2023-04-22'),
('Dima', 'Raluca', 2, '0734567898', 'Bucatar', 2800, '2022-05-30'),
('Cristea', 'George', 2, '0734567899', 'Vanzator', 2500, '2023-06-15'),

('Petrescu', 'Mihai', 3, '0734567801', 'Manager', 3600, '2020-01-05'),
('Sava', 'Andreea', 3, '0734567802', 'Casier', 2400, '2021-02-18'),
('Nica', 'Daniel', 3, '0734567803', 'Bucatar', 2800, '2023-03-12'),
('Radu', 'Simona', 3, '0734567804', 'Bucatar', 2800, '2021-04-25'),
('Oprea', 'Carmen', 3, '0734567805', 'Vanzator', 2500, '2022-05-30'),

('Dumitru', 'Mihai', 4, '0734567806', 'Manager', 3600, '2022-01-10'),
('Ilie', 'Ioana', 4, '0734567807', 'Casier', 2400, '2021-02-20'),
('Barbu', 'Vasile', 4, '0734567808', 'Bucatar', 2800, '2023-03-15'),
('Cojocaru', 'Elena', 4, '0734567809', 'Bucatar', 2800, '2020-04-30'),
('Racovita', 'Anca', 4, '0734567810', 'Vanzator', 2500, '2021-05-15'),

('Matei', 'Florin', 5, '0734567811', 'Manager', 3600, '2023-02-01'),
('Grigore', 'Alina', 5, '0734567812', 'Casier', 2400, '2021-03-15'),
('Nicolescu', 'Teodor', 5, '0734567813', 'Bucatar', 2800, '2022-04-10'),
('Tudor', 'Raluca', 5, '0734567814', 'Bucatar', 2800, '2023-05-20'),
('Enescu', 'Cecilia', 5, '0734567815', 'Vanzator', 2500, '2020-06-25');


INSERT INTO Angajati (nume, prenume, cod_locatie, numar_telefon, functie, salariu, data_angajare) 
VALUES 
('Vasilescu', 'Florentina', 6, '0751234560', 'Manager', 3600, '2015-03-01'),
('Balan', 'Tiberiu', 6, '0751234561', 'Casier', 2400, '2013-04-15'),
('Cristea', 'Lavinia', 6, '0751234562', 'Bucatar', 2800, '2018-05-10'),
('Serban', 'Ionut', 6, '0751234563', 'Bucatar', 2800, '2016-06-20'),
('Nicolescu', 'Roxana', 6, '0751234564', 'Vanzator', 2500, '2017-07-05'),

('Petrescu', 'Mihai', 7, '0751234565', 'Manager', 3600, '2012-02-10'),
('Stanescu', 'Adriana', 7, '0751234566', 'Casier', 2400, '2014-03-15'),
('Vasilescu', 'Florin', 7, '0751234567', 'Bucatar', 2800, '2019-04-22'),
('Dima', 'Raluca', 7, '0751234568', 'Bucatar', 2800, '2011-05-30'),
('Cristea', 'George', 7, '0751234569', 'Vanzator', 2500, '2013-06-15'),

('Albu', 'Stefan', 8, '0751234570', 'Manager', 3600, '2014-01-05'),
('Grigore', 'Ana', 8, '0751234571', 'Casier', 2400, '2015-02-18'),
('Tudor', 'Vasile', 8, '0751234572', 'Bucatar', 2800, '2017-03-12'),
('Nica', 'Ioana', 8, '0751234573', 'Bucatar', 2800, '2018-04-25'),
('Costea', 'Simona', 8, '0751234574', 'Vanzator', 2500, '2016-05-30'),

('Pavel', 'Dan', 9, '0751234575', 'Manager', 3600, '2011-01-10'),
('Enescu', 'Bianca', 9, '0751234576', 'Casier', 2400, '2018-02-20'),
('Dobre', 'Radu', 9, '0751234577', 'Bucatar', 2800, '2013-03-15'),
('Pop', 'Adriana', 9, '0751234578', 'Bucatar', 2800, '2019-04-25'),
('Fodor', 'Alexandra', 9, '0751234579', 'Vanzator', 2500, '2015-06-30'),

('Neagu', 'Florin', 10, '0751234580', 'Manager', 3600, '2016-02-01'),
('Barbu', 'Monica', 10, '0751234581', 'Casier', 2400, '2017-03-15'),
('Matei', 'Iulia', 10, '0751234582', 'Bucatar', 2800, '2014-04-10'),
('Danciu', 'Cristian', 10, '0751234583', 'Bucatar', 2800, '2012-05-20'),
('Vlad', 'Carmen', 10, '0751234584', 'Vanzator', 2500, '2019-06-25');


INSERT INTO Angajati (nume, prenume, cod_locatie, numar_telefon, functie, salariu, data_angajare) 
VALUES 
('Moldovan', 'Cristian', 11, '0771234561', 'Manager', 3600, '2014-01-15'),
('Panaite', 'Elena', 11, '0771234562', 'Casier', 2400, '2011-02-20'),
('Lazar', 'Andreea', 11, '0771234563', 'Bucatar', 2800, '2013-03-10'),
('Florea', 'Sorin', 11, '0771234564', 'Bucatar', 2800, '2015-04-25'),
('Matei', 'Florin', 11, '0771234565', 'Vanzator', 2500, '2017-05-30'),

('Sima', 'Iulia', 12, '0771234566', 'Manager', 3600, '2018-02-01'),
('Radu', 'Mihai', 12, '0771234567', 'Casier', 2400, '2016-03-15'),
('Popescu', 'Denisa', 12, '0771234568', 'Bucatar', 2800, '2014-04-20'),
('Barbu', 'Roxana', 12, '0771234569', 'Bucatar', 2800, '2013-05-25'),
('Gheorghe', 'Alex', 12, '0771234570', 'Vanzator', 2500, '2010-06-10'),

('Neacsu', 'Andrei', 13, '0771234571', 'Manager', 3600, '2012-01-20'),
('Buzescu', 'Laura', 13, '0771234572', 'Casier', 2400, '2017-02-28'),
('Filimon', 'Daniel', 13, '0771234573', 'Bucatar', 2800, '2018-03-15'),
('Sinescu', 'Adriana', 13, '0771234574', 'Bucatar', 2800, '2011-04-25'),
('Mateescu', 'Sergiu', 13, '0771234575', 'Vanzator', 2500, '2016-05-30'),

('Cristea', 'Simona', 14, '0771234576', 'Manager', 3600, '2019-02-15'),
('Dumitru', 'Florin', 14, '0771234577', 'Casier', 2400, '2015-03-10'),
('Iliescu', 'Carmen', 14, '0771234578', 'Bucatar', 2800, '2014-04-20'),
('Vasile', 'Ionut', 14, '0771234579', 'Bucatar', 2800, '2013-05-30'),
('Rasdan', 'Alina', 14, '0771234580', 'Vanzator', 2500, '2012-06-25'),

('Hodoroaga', 'Victor', 15, '0771234581', 'Manager', 3600, '2016-01-05'),
('Neagu', 'Bianca', 15, '0771234582', 'Casier', 2400, '2018-02-15'),
('Vlad', 'Teodor', 15, '0771234583', 'Bucatar', 2800, '2010-03-20'),
('Dima', 'Raluca', 15, '0771234584', 'Bucatar', 2800, '2017-04-25'),
('Ion', 'Cecilia', 15, '0771234585', 'Vanzator', 2500, '2011-05-30');


INSERT INTO Angajati (nume, prenume, cod_locatie, numar_telefon, functie, salariu, data_angajare) 
VALUES 
('Marinescu', 'Gabriel', 16, '0781234561', 'Manager', 3600, '2014-01-15'),
('Toma', 'Elena', 16, '0781234562', 'Casier', 2400, '2013-02-20'),
('Pavel', 'Sorin', 16, '0781234563', 'Bucatar', 2800, '2011-03-10'),
('Cojocaru', 'Raluca', 16, '0781234564', 'Bucatar', 2800, '2016-04-25'),
('Iliescu', 'Andreea', 16, '0781234565', 'Vanzator', 2500, '2018-05-30'),

('Neagu', 'Mihai', 17, '0781234566', 'Manager', 3600, '2012-02-01'),
('Barbu', 'Ana', 17, '0781234567', 'Casier', 2400, '2017-03-15'),
('Vasilescu', 'Carmen', 17, '0781234568', 'Bucatar', 2800, '2015-04-20'),
('Dima', 'Florin', 17, '0781234569', 'Bucatar', 2800, '2010-05-30'),
('Grigore', 'Alex', 17, '0781234570', 'Vanzator', 2500, '2014-06-10'),

('Popescu', 'Ioana', 18, '0781234571', 'Manager', 3600, '2019-01-05'),
('Filipescu', 'Denisa', 18, '0781234572', 'Casier', 2400, '2016-02-20'),
('Moldovan', 'Teodor', 18, '0781234573', 'Bucatar', 2800, '2013-03-15'),
('Sinescu', 'Raluca', 18, '0781234574', 'Bucatar', 2800, '2011-04-25'),
('Catu', 'Gabriel', 18, '0781234575', 'Vanzator', 2500, '2015-05-30'),

('Tudor', 'Sergiu', 19, '0781234576', 'Manager', 3600, '2012-01-10'),
('Vasile', 'Anca', 19, '0781234577', 'Casier', 2400, '2014-02-15'),
('Lazar', 'Cristina', 19, '0781234578', 'Bucatar', 2800, '2017-03-20'),
('Cristea', 'Iulia', 19, '0781234579', 'Bucatar', 2800, '2018-04-25'),
('Cojocaru', 'Mihai', 19, '0781234580', 'Vanzator', 2500, '2019-05-30'),

('Dragan', 'Florin', 20, '0781234581', 'Manager', 3600, '2016-01-05'),
('Panaite', 'Simona', 20, '0781234582', 'Casier', 2400, '2015-03-10'),
('Nistor', 'Ovidiu', 20, '0781234583', 'Bucatar', 2800, '2013-04-20'),
('Sava', 'Denisa', 20, '0781234584', 'Bucatar', 2800, '2010-05-30'),
('Cristea', 'Raluca', 20, '0781234585', 'Vanzator', 2500, '2018-06-25');

SELECT * FROM Angajati;


-- reset the key wronG (starting from value one)
DELETE FROM Angajati;

DBCC CHECKIDENT('Angajati', RESEED, 999);

UPDATE Angajati
SET functie = 'Bucatar'
WHERE functie = 'Vanzator';
