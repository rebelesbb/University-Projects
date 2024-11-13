USE McDonaldsDB;

-- CATEGORII --

DBCC CHECKIDENT('Categorii',RESEED, 199);

INSERT INTO Categorii (nume) 
VALUES
('Pui'),
('Vita'),
('Porc'),
('Peste'),
('Cartofi'),
('Bauturi'),
('Deserturi'),
('Salate'),
('Happy Meal'),
('Meniuri'),
('Sosuri'),
('Cafea McCafe'),
('Bauturi Calde McCafe'),
('Bauturi Reci McCafe'),
('Editie Limitata');

INSERT INTO Categorii (nume) 
VALUES
('Mic Dejun'),
('Fructe');

Select * FROM Categorii;
SELECT * FROM Meniuri;

CREATE TABLE CategoriiMeniuri
(
cod_categorie INT,
cod_meniu INT,
CONSTRAINT fk_categoriiMeniuri_categorie FOREIGN KEY (cod_categorie) REFERENCES Categorii(cod_categorie) ON UPDATE CASCADE,
CONSTRAINT fk_categoriiMeniuri_meniu FOREIGN KEY (cod_meniu) REFERENCES Meniuri(cod_meniu) ON UPDATE CASCADE,
CONSTRAINT pk_categoriiMeniuri PRIMARY KEY (cod_categorie, cod_meniu)
);