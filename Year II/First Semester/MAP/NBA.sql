create table teams
(
id bigserial primary key,
name varchar(100)
);

select * from teams

delete from teams;

insert into teams(name)
values
('Houston Rockets'),
('Los Angeles Lakers'),
('LA Clippers'),
('Chicago Bulls'),
('Cleveland Cavaliers'),
('Utah Jazz'),
('Brooklyn Nets'),
('New Orleans Pelicans'),
('Indiana Pacers'),
('Toronto Raptors'),
('Charlottes Hornets'),
('Phoenix Suns'),
('Portland TrailPlazers'),
('Golden State Warriors'),
('Washington Wizards'),
('San Antonio Spurs'),
('Orlando Magic'),
('Denver Nuggets'),
('Detroit Pistons'),
('Atlanta Hawks'),
('Dallas Mavericks'),
('Sacramento Kings'),
('Oklahoma City Thunder'),
('Boston Celtics'),
('New York Kniks'),
('Minnesota Timberwolves'),
('Miami Heat'),
('Milwaukee Bucks');

create table students
(
id bigserial primary key,
name varchar(200),
school varchar(200)
);

-- Insert 17 students for "Scoala Gimnaziala 'Horea'"
INSERT INTO students (name, school)
VALUES 
('Popescu Andrei', 'Scoala Gimnaziala "Horea"'),
('Ionescu Maria', 'Scoala Gimnaziala "Horea"'),
('Dumitrescu Mihai', 'Scoala Gimnaziala "Horea"'),
('Stan Elena', 'Scoala Gimnaziala "Horea"'),
('Radu Ioana', 'Scoala Gimnaziala "Horea"'),
('Matei Alexandru', 'Scoala Gimnaziala "Horea"'),
('Constantinescu Gabriela', 'Scoala Gimnaziala "Horea"'),
('Gheorghe Cristian', 'Scoala Gimnaziala "Horea"'),
('Pop Ana', 'Scoala Gimnaziala "Horea"'),
('Tudor Adrian', 'Scoala Gimnaziala "Horea"'),
('Moldovan Roxana', 'Scoala Gimnaziala "Horea"'),
('Marin Bianca', 'Scoala Gimnaziala "Horea"'),
('Iliescu Sorin', 'Scoala Gimnaziala "Horea"'),
('Enescu Nicoleta', 'Scoala Gimnaziala "Horea"'),
('Avram Daniel', 'Scoala Gimnaziala "Horea"'),
('Voicu Cristina', 'Scoala Gimnaziala "Horea"'),
('Balint Andreea', 'Scoala Gimnaziala "Horea"');

-- Insert 17 students for "Scoala Gimnaziala 'Octavian Goga'"
INSERT INTO students (name, school)
VALUES 
('Popescu Radu', 'Scoala Gimnaziala "Octavian Goga"'),
('Ionescu Claudia', 'Scoala Gimnaziala "Octavian Goga"'),
('Dumitrescu Alin', 'Scoala Gimnaziala "Octavian Goga"'),
('Stan Diana', 'Scoala Gimnaziala "Octavian Goga"'),
('Radu Vlad', 'Scoala Gimnaziala "Octavian Goga"'),
('Matei Ioana', 'Scoala Gimnaziala "Octavian Goga"'),
('Constantinescu Mihai', 'Scoala Gimnaziala "Octavian Goga"'),
('Gheorghe Simona', 'Scoala Gimnaziala "Octavian Goga"'),
('Pop Darius', 'Scoala Gimnaziala "Octavian Goga"'),
('Tudor Larisa', 'Scoala Gimnaziala "Octavian Goga"'),
('Moldovan Cristina', 'Scoala Gimnaziala "Octavian Goga"'),
('Marin Adrian', 'Scoala Gimnaziala "Octavian Goga"'),
('Iliescu Gabriela', 'Scoala Gimnaziala "Octavian Goga"'),
('Enescu Teodora', 'Scoala Gimnaziala "Octavian Goga"'),
('Avram Robert', 'Scoala Gimnaziala "Octavian Goga"'),
('Voicu Denisa', 'Scoala Gimnaziala "Octavian Goga"'),
('Balint Sebastian', 'Scoala Gimnaziala "Octavian Goga"');

select * from students

create table players
(
student_id bigint,
team_id bigint,
foreign key (team_id) references teams(id),
foreign key (student_id) references students(id),
primary key (student_id)
)

select * from players
drop table players;

-- Insert the first 15 students from "Scoala Gimnaziala 'Horea'" to team 1
INSERT INTO players (student_id, team_id)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1);

-- Insert the first 15 students from "Scoala Gimnaziala 'Octavian Goga'" to team 2
INSERT INTO players (student_id, team_id)
VALUES
(18, 2),
(19, 2),
(20, 2),
(21, 2),
(22, 2),
(23, 2),
(24, 2),
(25, 2),
(26, 2),
(27, 2),
(28, 2),
(29, 2),
(30, 2),
(31, 2),
(32, 2);


create table games 
(
id bigserial primary key,
first_team_id bigint,
second_team_id bigint,
game_date timestamp,
foreign key (first_team_id) references teams(id),
foreign key (second_team_id) references teams(id),
check (first_team_id != second_team_id)
);

drop table games;

select S.id, S.name, S.school, P.team_id
from students S inner join players P on S.id = P.student_id;

insert into games(first_team_id, second_team_id, game_date)
values
(1, 2, '2023-10-10 14:30:00'),
(1, 2, '2024-11-11 12:45:00');

select * from games;

create table active_players
(
player_id bigint,
game_id bigint,
scored_points bigint,
player_type varchar(20),
foreign key (player_id) references players(student_id),
foreign key (game_id) references games(id),
primary key (player_id, game_id),
check (player_type = 'Rezerva' or player_type = 'Participant')
);

-- Insert active players for the first game (game_id = 1)
INSERT INTO active_players (player_id, game_id, scored_points, player_type)
VALUES
-- Team 1 (players 1 to 15, omit player_id = 1, set player_id = 3 and player_id = 6 as "Rezerva")
(2, 1, 10, 'Participant'),
(3, 1, 0, 'Rezerva'),
(4, 1, 8, 'Participant'),
(5, 1, 14, 'Participant'),
(6, 1, 0, 'Rezerva'),
(7, 1, 13, 'Participant'),
(8, 1, 6, 'Participant'),
(9, 1, 11, 'Participant'),
(10, 1, 7, 'Participant'),
(11, 1, 15, 'Participant'),
(12, 1, 20, 'Participant'),
(13, 1, 18, 'Participant'),
(14, 1, 5, 'Participant'),
(15, 1, 4, 'Participant'),

-- Team 2 (players 18 to 32, omit player_id = 18, set player_id = 20 and player_id = 23 as "Rezerva")
(19, 1, 9, 'Participant'),
(20, 1, 0, 'Rezerva'),
(21, 1, 7, 'Participant'),
(22, 1, 11, 'Participant'),
(23, 1, 0, 'Rezerva'),
(24, 1, 14, 'Participant'),
(25, 1, 8, 'Participant'),
(26, 1, 10, 'Participant'),
(27, 1, 12, 'Participant'),
(28, 1, 15, 'Participant'),
(29, 1, 13, 'Participant'),
(30, 1, 17, 'Participant'),
(31, 1, 4, 'Participant'),
(32, 1, 6, 'Participant');

-- Insert active players for the second game (game_id = 2)
INSERT INTO active_players (player_id, game_id, scored_points, player_type)
VALUES
-- Team 1 (players 1 to 15, omit player_id = 2, set player_id = 4 and player_id = 7 as "Rezerva")
(1, 2, 10, 'Participant'),
(3, 2, 14, 'Participant'),
(4, 2, 0, 'Rezerva'),
(5, 2, 11, 'Participant'),
(6, 2, 8, 'Participant'),
(7, 2, 0, 'Rezerva'),
(8, 2, 6, 'Participant'),
(9, 2, 15, 'Participant'),
(10, 2, 7, 'Participant'),
(11, 2, 18, 'Participant'),
(12, 2, 5, 'Participant'),
(13, 2, 20, 'Participant'),
(14, 2, 4, 'Participant'),
(15, 2, 12, 'Participant'),

-- Team 2 (players 18 to 32, omit player_id = 19, set player_id = 21 and player_id = 25 as "Rezerva")
(18, 2, 8, 'Participant'),
(20, 2, 14, 'Participant'),
(21, 2, 0, 'Rezerva'),
(22, 2, 9, 'Participant'),
(23, 2, 15, 'Participant'),
(24, 2, 11, 'Participant'),
(25, 2, 0, 'Rezerva'),
(26, 2, 12, 'Participant'),
(27, 2, 7, 'Participant'),
(28, 2, 5, 'Participant'),
(29, 2, 18, 'Participant'),
(30, 2, 4, 'Participant'),
(31, 2, 20, 'Participant'),
(32, 2, 13, 'Participant');

select * from active_players
delete from active_players