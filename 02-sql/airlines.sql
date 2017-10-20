CREATE DATABASE airlines;

\connect airlines;

CREATE TABLE IF NOT EXISTS crewmember (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	dob DATE);

CREATE TABLE IF NOT EXISTS aircraft (
	id SERIAL PRIMARY KEY,
	model VARCHAR (50) NOT NULL,
	model_count INTEGER
);

/* we can also create this table without composed primary key */
CREATE TABLE IF NOT EXISTS flight_exp (
	aircraft_id INTEGER NOT NULL REFERENCES aircraft ON DELETE CASCADE,
	crewman_id  INTEGER NOT NULL REFERENCEs crewmember ON DELETE CASCADE,
	flight_hours INTEGER,
	PRIMARY KEY (aircraft_id, crewman_id)
);

/*default data*/
INSERT INTO crewmember VALUES (DEFAULT, 'Veljko', 'Srdarevic', '1987-09-15');
INSERT INTO crewmember VALUES (DEFAULT, 'John', 'Johnovic', '1976-11-20');
INSERT INTO crewmember VALUES (DEFAULT, 'Amelia', 'Eearhart','1897-07-24');
INSERT INTO crewmember VALUES (DEFAULT, 'Charles', 'Lindbergh','1902-02-04');
INSERT INTO crewmember VALUES (DEFAULT, 'Manfred', 'von Richtofen', '1892-05-02');

INSERT INTO aircraft VALUES (DEFAULT, 'Fokker Dr.I',5);
INSERT INTO aircraft VALUES (DEFAULT, 'Fokker DR.VII',2);
INSERT INTO aircraft VALUES (DEFAULT, '594 Avian III',3);
INSERT INTO aircraft VALUES (DEFAULT, 'Spirit of St. Louis', 1);
INSERT INTO aircraft VALUES (DEFAULT, 'Duglas DC-8',8);
INSERT INTO aircraft VALUES (DEFAULT, 'de Havilland Comet',5);
INSERT INTO aircraft VALUES (DEFAULT, 'Cessna 172',25);
INSERT INTO aircraft VALUES (DEFAULT, 'Boeing 747', 13);

INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (1,7,100);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (2,7,134);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (2,5,3043);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (2,6,2764);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (2,8,359);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (3,3,4034);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (4,4,3579);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (5,1,6231);
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours) VALUES (5,2,39);
/*Let's presume that we don't know which id is which person/aircraft*/
INSERT INTO flight_exp (crewman_id, aircraft_id, flight_hours)
			VALUES (
					(SELECT id FROM crewmember where last_name = 'Srdarevic' and first_name='Veljko'),
					(SELECT id FROM aircraft where model = 'Duglas DC-8'),

					32);

/* First approach, select within WHERE clause */
SELECT first_name,last_name FROM crewmember WHERE dob = (SELECT MIN(dob) from crewmember);
/*second approach, order by, limit */
SELECT first_name,last_name FROM crewmember ORDER BY dob LIMIT 1;
/* n-th oldest crewmember, using offset */
SELECT first_name,last_name FROM crewmember ORDER BY dob OFFSET 2 LIMIT 1;
/*most experienced crewmember*/
SELECT first_name,last_name FROM crewmember JOIN flight_exp on crewmember.id = crewman_id GROUP_BY first_name, last_name ORDER_BY COUNT(*) DESC LIMIT 1;
/* least experienced crewmember */
SELECT first_name,last_name FROM crewmember JOIN flight_exp on crewmember.id = crewman_id GROUP_BY first_name, last_name ORDER_BY COUNT(*) LIMIT 1;
