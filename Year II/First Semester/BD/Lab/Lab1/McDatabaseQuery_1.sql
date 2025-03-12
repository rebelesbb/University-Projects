CREATE DATABASE McDonaldsDB;
GO
USE McDonaldsDB;

CREATE TABLE Produse
(
cod_produs INT IDENTITY(100,1),
nume VARCHAR(100),
ingrediente VARCHAR(200),
pret INT,
CONSTRAINT pk_produse PRIMARY KEY (cod_produs)
);

CREATE TABLE Categorii
(
cod_categorie INT IDENTITY(200,1),
nume VARCHAR(100)
CONSTRAINT pk_categorie PRIMARY KEY (cod_categorie)
);

-- Tabel de legatura intre produse si categorii
/*
	O categorie poate avea mai multe produse: Bauturi racoritoare -> Cola, Fanta, ...
	Un produs poate apartine mai multori categorii: Burgeri pui, Oferte limitate -> McCrispy
*/
CREATE TABLE CategoriiProduse
(
cod_categorie INT,
cod_produs INT,
CONSTRAINT fk_categoriiProduse_categorie FOREIGN KEY (cod_categorie) REFERENCES Categorii(cod_categorie) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT fk_categoriiProduse_produs FOREIGN KEY (cod_produs) REFERENCES Produse(cod_produs) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT pk_categoriiProduse PRIMARY KEY (cod_categorie,cod_produs)
);

drop table CategoriiProduse;

CREATE TABLE Locatii
(
cod_locatie INT IDENTITY,
adresa VARCHAR(200),
program  VARCHAR(100)
CONSTRAINT pk_locatii PRIMARY KEY (cod_locatie)
);

CREATE TABLE Angajati
(
cod_angajat INT IDENTITY(1000,1),
nume VARCHAR(200),
prenume VARCHAR(200),
cod_locatie INT,
numar_telefon VARCHAR(20),
functie VARCHAR(100),
salariu INT,
data_angajare DATE,
CONSTRAINT pk_angajati PRIMARY KEY (cod_angajat),
CONSTRAINT fk_locatiiAngajati FOREIGN KEY (cod_locatie) REFERENCES Locatii(cod_locatie) ON UPDATE CASCADE
);

CREATE TABLE Clienti
(
cod_client INT IDENTITY,
nume VARCHAR(200),
CONSTRAINT pk_clienti PRIMARY KEY (cod_client)
);

/*
	Un client poate avea mai multe comenzi.
	Un angajat poate pregati mai multe comenzi.
*/
CREATE TABLE Comenzi
(
cod_comanda INT IDENTITY,
cod_client INT,
cod_angajat INT,
data_comanda DATE,
ora_comanda TIME,
total INT,
CONSTRAINT pk_comenzi PRIMARY KEY (cod_comanda),
CONSTRAINT fk_comenziAngajati FOREIGN KEY (cod_angajat) REFERENCES Angajati(cod_angajat) ON UPDATE CASCADE,
CONSTRAINT fk_comenziClienti FOREIGN KEY (cod_client) REFERENCES Clienti(cod_client) ON UPDATE CASCADE
)

CREATE TABLE ComenziProduse
(
cod_comanda INT,
cod_produs INT,
cantitate INT,
CONSTRAINT fk_comenziProduse_comanda FOREIGN KEY (cod_comanda) REFERENCES Comenzi(cod_comanda) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT fk_comenziProduse_produs FOREIGN KEY (cod_produs) REFERENCES Produse(cod_produs) ON UPDATE CASCADE,
CONSTRAINT pk_comenziProduse PRIMARY KEY (cod_comanda,cod_produs)
);

CREATE TABLE Meniuri
(
cod_meniu INT IDENTITY(300,1),
nume VARCHAR(100),
descriere VARCHAR(200),
CONSTRAINT pk_meniuri PRIMARY KEY (cod_meniu)
);

CREATE TABLE ComenziMeniuri
(
cod_comanda INT,
cod_meniu INT,
CONSTRAINT fk_comenziMeniuri_comanda FOREIGN KEY (cod_comanda) REFERENCES Comenzi(cod_comanda) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT fk_comenziMeniuri_meniu FOREIGN KEY (cod_meniu) REFERENCES Meniuri(cod_meniu) ON UPDATE CASCADE,
CONSTRAINT pk_comenziMeniuri PRIMARY KEY (cod_comanda,cod_meniu)
);

CREATE TABLE Oferte
(
cod_oferta INT IDENTITY,
nume VARCHAR(100),
descriere VARCHAR(200),
data_inceput DATE,
data_sfarsit DATE,
discount INT,
CONSTRAINT pk_oferte PRIMARY KEY (cod_oferta)
);

CREATE TABLE OferteProduse
(
cod_oferta INT,
cod_produs INT,
CONSTRAINT fk_oferteProduse_oferta FOREIGN KEY (cod_oferta) REFERENCES Oferte(cod_oferta),
CONSTRAINT fk_oferteProduse_produs FOREIGN KEY (cod_produs) REFERENCES Produse(cod_produs),
CONSTRAINT pk_oferteProduse PRIMARY KEY (cod_oferta,cod_produs)
);

CREATE TABLE OferteMeniuri
(
cod_oferta INT,
cod_meniu INT,
CONSTRAINT fk_oferteMeniuri_oferta FOREIGN KEY (cod_oferta) REFERENCES Oferte(cod_oferta),
CONSTRAINT fk_oferteMeniuri_meniu FOREIGN KEY (cod_meniu) REFERENCES Meniuri(cod_meniu),
CONSTRAINT pk_oferteMeniuri PRIMARY KEY (cod_oferta,cod_meniu)
);

-- Modificari --
-- meniu -- pret
ALTER TABLE Meniuri ADD pret INT;
ALTER TABLE Meniuri ALTER COLUMN pret DECIMAL(5,2);
ALTER TABLE Produse ALTER COLUMN pret DECIMAL(5,2);
ALTER TABLE Comenzi ALTER COLUMN total DECIMAL(10,2);

-- comenzi -- pret
ALTER TABLE ComenziProduse ADD pretBucata DECIMAL(5,2);

ALTER TABLE ComenziMeniuri ADD cantitate INT;
ALTER TABLE ComenziMeniuri ADD pretBucata DECIMAL(5,2);

-- client -- email, nr.
ALTER TABLE Clienti ADD numar_telefon VARCHAR(20);

-- C.total -- initial value = 0
ALTER TABLE Comenzi
ADD CONSTRAINT DF_Value_Total DEFAULT 0 FOR total;


