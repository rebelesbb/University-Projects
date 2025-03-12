-- Produse --

-- Burger si pui --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Hamburger', 'mustar, ketchup, ceapa, castraveti murati, carne vita', 6),
('Cheeseburger', 'mustar, ketchup, ceapa, castraveti murati, cheddar, carne vita', 7),
('Fresh Deluxe', 'sos McChicken, ceapa, salata, castraveti, rosii, cheddar, carne vita', 18),
('Big Tasty Burger', 'sos Big Tasty, ceapa, salata, rosyy, emmentaler, carne vita', 23.5),
('Dublu Cheeseburger', 'mustar, ketchup, ceapa, castraveti murati, cheddar, carne vita', 14.5),
('Big Mac','sos Big Mac, ceapa, salata, castraveti murati, cheddar, carne vita', 14.5),
('McChicken', 'sos McChicken, salata, carne pui', 14),
('Filet-O-Fish', 'sos, cheddar, carne peste', 12),
('McToast', 'sunca, emmentaler', 5.5),
('Chicken McNuggets 6 Bucati', 'sos, carne pui', 17),
('Chicken McNuggets 9 Bucati', 'sos, carne pui', 24),
('Spicy Chicken McNuggets 6 Bucati', 'sos, carne pui', 19),
('Spicy Chicken McNuggets 9 Bucati', 'sos, carne pui', 26),
('McPuisor', 'sos McChicken, castraveti murati, carne pui', 6),
('Aripioare Pui 5 Bucati', 'carne pui', 19),
('Crispy Chicken Tenders', 'carne pui', 19.5),
('Quarter Pounder', 'mustar, ketchup, ceapa, castraveti murati, cheddar, carne vita', 16.5),
('McCrispy', 'sos McBacon, castraveti murati, cheddar, carne pui',22.5),
('Mac Jr.', 'mustar, ketchup, ceapa, castraveti murati, cheddar, carne vita', 11.50),
('Grand Big Mac', 'mustar, ketchup, ceapa, castraveti murati, cheddar, carne vita', 25);

UPDATE Produse
SET ingrediente = 'sos Big Tasty, ceapa, salata, rosii, emmentaler, carne vita'
WHERE  cod_produs = 103;

-- Salate, dressinguri, mar --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Felii de mar', 'mar', 4),
('Felie de ananas', 'ananas', 7),
('Salatzikos cu pui', 'castraveti, rosii cherry, carne pui', 25),
('Salatzikos cu telemea', 'castraveti, rosii cherry, telemea', 25),
('Coleslaw', 'varza, morcov, ceapa, mustar, maioneza, sos iaurt cu lamaie', 9),
('Sos Vinaigrette', 'apa, zahar, esenta otet, sare, ceapa, ulei, piper', 3.5),
('Sos Yogurt', 'iaurt, ulei, lamaie, usturoi, sare piper', 3.5),
('Sos 1000 Island', 'sare, ulei, otet, smantana, zahar, pasta tomante', 3.5);

-- McCafe --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('McPops gogoasa cu ciocolata si alune', 'produs congelat', 4),
('McPops gogoasa cu aroma de caise', 'produs congelat', 4),
('McPops gogoasa cu aroma de caramel', 'produs congelat', 4),
('McPops mix', 'produs congelat', 10),
('Espresso', 'cafea', 7.5),
('Espresso Macchiato', 'cafea, lapte', 7.5),
('Espresso', 'cafea', 8.5),
('Americano', 'cafea', 7.5),
('Cappucchino', 'cafea, lapte', 10.5),
('Caffe Latte', 'cafea, lapte', 10.5),
('Latte Machiatto', 'cafea, lapte', 12.5),
('Caramel Machiatto', 'cafea, lapte, sirop caramel', 13.5),
('Flat White', 'cafea, lapte', 11),
('Decaf Espresso', 'cafea', 7.5),
('Decaf Espresso Macchiato', 'cafea, lapte', 7.5),
('Decaf Espresso', 'cafea', 8.5),
('Decaf Americano', 'cafea', 7.5),
('Decaf Cappucchino', 'cafea, lapte', 10.5),
('Decaf Caffe Latte', 'cafea, lapte', 10.5),
('Decaf Latte Machiatto', 'cafea, lapte', 12.5),
('Decaf Caramel Machiatto', 'cafea, lapte', 13.5),
('Breakfast Tea', 'ceai', 7.5),
('Energy Tea', 'ceai', 7.5),
('Mocha Frappe', 'cafea, lapte, sirop, zahar, frisca', 13.5),
('Caramel Caffe Frappe', 'cafea, lapte, sirop, zahar, frisca', 13.5),
('Cocoa Frappe', 'cafea, lapte, sirop, zahar, frisca', 13.5),
('Caffe Frappe', 'cafea, lapte, sirop, zahar, frisca', 13.5),
('Fresh Portocale', 'suc portocala', 14.5),
('Fresh Grapefruit', 'suc grapefruit', 14.5),
('Limonada', 'suc lamaie', 14.5);

-- Cartofi si sosuri --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Cartofi prajiti portie mica', 'cartofi, sare', 6),
('Cartofi prajiti portie medie', 'cartofi, sare', 8),
('Cartofi prajiti portie mare', 'cartofi, sare', 9.5),
('Cartofi Homestyle Dippers', 'cartofi, sare', 9.5);

INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Sos usturoi', '', 3.5);

INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Sos maioneza', '', 3.5),
('Sos dulce acrisor', '', 3.5),
('Sos sour', '', 3.5),
('Sos ketchup', '', 3.5);

-- Deserturi --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Placinta cu visine', 'aluat, crema visine', 7.5),
('Placinta cu mere si caramel', 'aluat, umplutura mere, sirop caramel', 8.5);

-- Bauturi --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Fanta Mic', '', 6),
('Fanta Mediu', '', 8),
('Fanta Mare', '', 10.5),
('Coca-Cola Mic', '', 6),
('Coca-Cola Mediu', '', 8),
('Coca-Cola Mare', '', 10.5),
('Coca-Cola Zero Mic', '', 6),
('Coca-Cola Zero Mediu', '', 8),
('Coca-Cola Zero Mare', '', 10.5),
('Sprite Mic', '', 6),
('Sprite Mediu', '', 8),
('Sprite Mare', '', 10.5),
('Lipton Mic', '', 6),
('Lipton Mediu', '', 8),
('Lipton Mare', '', 10.5),
('Suc de mere', '', 8),
('Suc de portocale', '', 8);

-- Shake-uri --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Shake Ciocolata', '', 8),
('Shake Vanilie', '', 8),
('Shake Capsuni', '', 8);

-- Inghetata --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('McSundae Ciocolata', 'inghetata vanilie, sirop ciocolata', 8),
('McSundae Caramel', 'inghetata vanilie, sirop caramel', 8),
('McSundae Capsune', 'inghetata vanilie, sirop capsune', 8),
('Cornet cu inghetata', 'inghetata vanilie', 2.5),
('McFlurry Oreo Ciocolata', 'inghetata vanilie, biscuiti Oreo, sirop ciocolata', 12),
('McFlurry Oreo Caramel', 'inghetata vanilie, biscuiti Oreo, sirop ciocolata', 12),
('McFlurry Kitkat Ciocolata', 'inghetata vanilie, bucati KitKat, sirop ciocolata', 12),
('McFlurry Kitkat Caramel', 'inghetata vanilie, bucati KitKat, sirop caramel', 12),
('McFlurry Snickers Caramel', 'inghetata vanilie, bucati Snickers, sirop caramel', 13.5),
('McFlurry Twix Ciocolata', 'inghetata vanilie, bucati Twix, sirop ciocolata', 13.5);


-- Apa --
INSERT INTO Produse(nume, ingrediente, pret)
VALUES
('Apa minerala plata', '', 8),
('Apa minerala carbogazoasa', '', 8);

-- More breakfast --

DELETE
FROM Produse
WHERE cod_produs = 132;
DELETE
FROM Produse
WHERE cod_produs = 141;

SELECT * FROM Produse;

/*
CREATE OR ALTER TRIGGER nume
ON {tabela/view}
[AFTER/INSTEAD OF] [INSERT/UPDATE/DELETE - putem seta pentru mai multe odata]
AS
BEGIN
avem deleted si inserted daca avem nevoie de date inainte si dupa modificari
pot fi folosite si in output (nu in trigger in update/delete/insert)
ex. update categorii set nume = 'pensionari'
	OUTPUT inserted.cod_categorie, deleted.nume nume_initial, inserted.nume nume_actual, GETDATE()
	WHERE nume = 'seniori'
cursoare
declare nume cursor fast_forward for {select statement}
open nume;
fetch first/next/prior/last;
close nume;
deallocate nume;
END