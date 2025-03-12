INSERT INTO Views(Name)
VALUES
('vw_Locatii'),
('vw_PriceStats'),
('vw_ProductSales');

--tabele folosite:
-- doar pk: clienti
-- pk si minim un fk: comenzi
-- pk compus: comenzi produse

-- copie la tabele

-- Copie 
CREATE TABLE ClientiCopy
(
cod_client INT IDENTITY,
nume VARCHAR(200),
CONSTRAINT pk_clientiCopy PRIMARY KEY (cod_client)
);

ALTER TABLE ClientiCopy ADD numar_telefon VARCHAR(20);

INSERT INTO ClientiCopy(nume, numar_telefon)
SELECT C.nume, C.numar_telefon
FROM Clienti C;

SELECT * FROM ClientiCopy;
SELECT * FROM Clienti;

go
CREATE TABLE ComenziCopy
(
cod_comanda INT IDENTITY,
cod_client INT,
cod_angajat INT,
data_comanda DATE,
ora_comanda TIME,
total DECIMAL(10,2),
CONSTRAINT pk_comenziCopy PRIMARY KEY (cod_comanda),
CONSTRAINT fk_comenziAngajatiCopy FOREIGN KEY (cod_angajat) REFERENCES Angajati(cod_angajat) ON UPDATE CASCADE,
CONSTRAINT fk_comenziClientiCopy FOREIGN KEY (cod_client) REFERENCES ClientiCopy(cod_client) ON UPDATE CASCADE,
)
ALTER TABLE ComenziCopy
ADD CONSTRAINT DF_Value_TotalCopy DEFAULT 0 FOR total;

INSERT INTO ComenziCopy(cod_client, cod_angajat, data_comanda, ora_comanda, total)
SELECT C.cod_client, C.cod_angajat, C.data_comanda, C.ora_comanda, C.total
FROM Comenzi C;

SELECT * FROM ComenziCopy;

go
CREATE TABLE ComenziProduseCopy
(
cod_comanda INT,
cod_produs INT,
cantitate INT,
pretBucata DECIMAL(5,2),
CONSTRAINT fk_comenziProduse_comandaCopy FOREIGN KEY (cod_comanda) REFERENCES ComenziCopy(cod_comanda) ON UPDATE CASCADE ON DELETE CASCADE,
CONSTRAINT fk_comenziProduse_produsCopy FOREIGN KEY (cod_produs) REFERENCES Produse(cod_produs) ON UPDATE CASCADE,
CONSTRAINT pk_comenziProduseCopy PRIMARY KEY (cod_comanda,cod_produs)
);

INSERT INTO ComenziProduseCopy(cod_comanda, cod_produs, cantitate, pretBucata)
SELECT C.cod_comanda, C.cod_produs, C.cantitate, C.pretBucata
FROM ComenziProduse C;

SELECT * FROM ComenziProduseCopy;

drop table ComenziProduseCopy;
drop table ComenziCopy;

