CREATE TABLE Users
(
	id SERIAL PRIMARY KEY,
	firstname VARCHAR(100),
	lastname VARCHAR(100),
	email VARCHAR(150) UNIQUE NOT NULL,
	password VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO Users(firstname, lastname, email, password)
VALUES
('Andrei', 'Popescu', 'andrei.popescu@gmail.com', 'andrei123'),
('Mihai', 'Ionescu', 'mihai.ionescu@gmail.com', 'm1ha1_2023'),
('Maria', 'Georgescu', 'maria.georgescu@gmail.com', 'maria@pw!'),
('Ana', 'Popa', 'ana.popa@gmail.com', 'ana#456'),
('Ion', 'Dumitrescu', 'ion.dumitrescu@gmail.com', 'ion_secure12'),
('Raluca', 'Stanciu', 'raluca.stanciu@gmail.com', 'raluca*99'),
('Daniel', 'Marinescu', 'daniel.marinescu@gmail.com', 'daniel2023'),
('Alexandra', 'Enache', 'alexandra.enache@gmail.com', 'alex#pw'),
('George', 'Nistor', 'george.nistor@gmail.com', 'george_pw01'),
('Cristina', 'Matei', 'cristina.matei@gmail.com', 'cristina01'),
('Victor', 'Vasile', 'victor.vasile@gmail.com', 'victor$pass'),
('Diana', 'Constantinescu', 'diana.constantinescu@gmail.com', 'd1ana_pw'),
('Florin', 'Serban', 'florin.serban@gmail.com', 'florin123!'),
('Roxana', 'Petrescu', 'roxana.petrescu@gmail.com', 'rox@pw2023'),
('Claudiu', 'Nicolae', 'claudiu.nicolae@gmail.com', 'clau_pw34'),
('Elena', 'Sandu', 'elena.sandu@gmail.com', 'elena!pass'),
('Adrian', 'Neagu', 'adrian.neagu@gmail.com', 'adr!an_pw'),
('Larisa', 'Luca', 'larisa.luca@gmail.com', 'larisa_pw01'),
('Razvan', 'Stoica', 'razvan.stoica@gmail.com', 'raz_pw2023'),
('Carmen', 'Tanase', 'carmen.tanase@gmail.com', 'carmen@pass'),
('Dragos', 'Simion', 'dragos.simion@gmail.com', 'drago5!23'),
('Gabriela', 'Mircea', 'gabriela.mircea@gmail.com', 'gab_pw_07'),
('Robert', 'Stan', 'robert.stan@gmail.com', 'rob_stan23'),
('Bianca', 'Preda', 'bianca.preda@gmail.com', 'bianca2023'),
('Sebastian', 'Grigore', 'sebastian.grigore@gmail.com', 'sebas*123'),
('Violeta', 'Voicu', 'violeta.voicu@gmail.com', 'vio_pass!'),
('Marcel', 'Ilie', 'marcel.ilie@gmail.com', 'marc_pw1'),
('Teodora', 'Ene', 'teodora.ene@gmail.com', 'teodora_07'),
('Cosmin', 'Dobre', 'cosmin.dobre@gmail.com', 'cos_pw2023'),
('Lavinia', 'Radu', 'lavinia.radu@gmail.com', 'lavi_pw!02');

SELECT * FROM Users;