-- COMENZI --

INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
VALUES
(1, 1002, '2024-01-01', '10:15', 18), -- 102
(2, 1003, '2024-01-02', '11:45', 25), -- 122
(3, 1004, '2024-01-03', '12:30', 25), -- 123
(4, 1007, '2024-01-04', '13:00', 21), -- 300
(5, 1008, '2024-01-05', '14:15', 22), -- 301
(6, 1009, '2024-01-06', '15:30', 33), -- 302
(7, 1012, '2024-01-07', '16:45', 25), -- 113 113 161 162
(8, 1013, '2024-01-08', '17:00', 43.5), -- 311 160
(9, 1014, '2024-01-09', '18:30', 38.5), -- 303
(10, 1017, '2024-01-10', '10:30', 27); -- 307

INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
VALUES
(11, 1018, '2024-01-11', '11:00', 9.5), -- 158, 164
(12, 1019, '2024-01-12', '12:15', 38), --322
(13, 1022, '2024-01-13', '13:45', 61.5), -- 308 308 308
(14, 1023, '2024-01-14', '14:30', 31.5), -- 157 134 134
(15, 1024, '2024-01-04', '15:00', 18); -- 113 113 113 

INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
VALUES
(15, 1024, '2024-01-15', '15:00', 18); -- 113 113 113

SELECT * FROM CategoriiMeniuri;

INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
VALUES
(16, 1027, '2024-01-16', '16:15', 29), -- 306
(17, 1028, '2024-01-17', '17:30', 32), -- 309
(18, 1029, '2024-01-18', '18:00', 39), -- 310
(19, 1032, '2024-01-19', '10:45', 34), -- 311
(20, 1033, '2024-01-20', '11:15', 41); -- 312

INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
VALUES
(13, 1027, '2024-01-16', '16:15', 29), -- 306
(1, 1028, '2024-01-17', '17:30', 32), -- 309
(18, 1029, '2024-01-18', '18:00', 39), -- 310
(9, 1032, '2024-01-19', '10:45', 34), -- 311
(22, 1033, '2024-01-20', '11:15', 41); -- 312


SELECT * from Clienti;
SELECT * from Comenzi;
SELECT * FROM Produse;
SELECT * FROM Meniuri;
SELECT * FROM Angajati;

INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
VALUES
(21, 1034, '2024-01-21', '12:30', 32), --309
(23, 1039, '2024-01-24', '15:30', 82), --312 312
(24, 1043, '2024-01-26', '17:00', 6), -- 100
(25, 1049, '2024-01-30', '12:15', 16.5), -- 116
(26, 1057, '2024-02-03', '16:15', 25), --119
(27, 1063, '2024-02-07', '11:15', 15), --150 150
(28, 1068, '2024-02-10', '14:15', 11.5), --118
(29, 1074, '2024-02-14', '18:30', 132.5), --336 339 339 100
(30, 1093, '2024-02-25', '11:15', 34.5), -- 315
(20, 1084, '2024-02-20', '15:00', 37.5), -- 317
(30, 1087, '2024-02-21', '16:15', 39.5); -- 335

INSERT INTO Comenzi(cod_client, cod_angajat, data_comanda, ora_comanda, total)
VALUES
(1, 1052, '2024-01-31', '13:45', 37.5), -- 317
(12, 1053, '2024-02-01', '14:30', 39.5), -- 335
(26, 1077, '2024-02-15', '10:30', 34.5), -- 315
(17, 1078, '2024-02-16', '11:00', 34.5); -- 315

/*

(22, 1037, '2024-01-22', '13:00', ),
(23, 1038, '2024-01-23', '14:15', ),

(25, 1042, '2024-01-25', '16:45', ),

(27, 1044, '2024-01-27', '18:30', ),
(28, 1047, '2024-01-28', '10:30', ),
(29, 1048, '2024-01-29', '11:00', ),


(33, 1054, '2024-02-02', '15:00', ),

(35, 1058, '2024-02-04', '17:30', ),
(36, 1059, '2024-02-05', '18:00', ),
(37, 1062, '2024-02-06', '10:45', ),

(39, 1064, '2024-02-08', '12:30', ),
(40, 1067, '2024-02-09', '13:00', ),

(42, 1069, '2024-02-11', '15:30', ),
(43, 1072, '2024-02-12', '16:45', ),
(44, 1073, '2024-02-13', '17:00', ),


(48, 1079, '2024-02-17', '12:15', ),
(49, 1082, '2024-02-18', '13:45', ),
(50, 1083, '2024-02-19', '14:30', ),

(53, 1088, '2024-02-22', '17:30', ),
(54, 1089, '2024-02-23', '18:00', ),
(55, 1092, '2024-02-24', '10:45', ),

(57, 1094, '2024-02-26', '12:30', ),
(58, 1097, '2024-02-27', '13:00', ),
(59, 1098, '2024-02-28', '14:15', ),
(60, 1099, '2024-03-01', '15:30', ),
*/

/*
(61, 1002, '2024-03-02', '16:45', ),
(62, 1003, '2024-03-03', '17:00', ),
(63, 1004, '2024-03-04', '18:30', ),
(64, 1007, '2024-03-05', '10:30', ),
(65, 1008, '2024-03-06', '11:00', ),
(66, 1009, '2024-03-07', '12:15', ),
(67, 1012, '2024-03-08', '13:45', ),
(68, 1013, '2024-03-09', '14:30', ),
(69, 1014, '2024-03-10', '15:00', ),
(70, 1017, '2024-03-11', '16:15', ),
(71, 1018, '2024-03-12', '17:30', ),
(72, 1019, '2024-03-13', '18:00', ),
(73, 1022, '2024-03-14', '10:45', ),
(74, 1023, '2024-03-15', '11:15', ),
(75, 1024, '2024-03-16', '12:30', ),
(76, 1027, '2024-03-17', '13:00', ),
(77, 1028, '2024-03-18', '14:15', ),
(78, 1029, '2024-03-19', '15:30', ),
(79, 1032, '2024-03-20', '16:45', ),
(80, 1033, '2024-03-21', '17:00', ),
(81, 1034, '2024-03-22', '18:30', ),
(82, 1037, '2024-03-23', '10:30', ),
(83, 1038, '2024-03-24', '11:00', ),
(84, 1039, '2024-03-25', '12:15', ),
(85, 1042, '2024-03-26', '13:45', ),
(86, 1043, '2024-03-27', '14:30', ),
(87, 1044, '2024-03-28', '15:00', ),
(88, 1047, '2024-03-29', '16:15', ),
(89, 1048, '2024-03-30', '17:30', ),
(90, 1049, '2024-03-31', '18:00', ),
(91, 1052, '2024-04-01', '10:45', ),
(92, 1053, '2024-04-02', '11:15', );
*/