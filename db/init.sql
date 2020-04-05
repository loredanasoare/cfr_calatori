create database CFR;
use CFR;

create table Users(
    firstName varchar(30),
    lastName varchar(30),
    email varchar(30),
    type varchar(30),
    password varchar(30)
);

create table Trips(
    src varchar(30),
    dest varchar(30),
    day int,
    leaveHour int,
    arriveHour int,
    numberOfAvailableSeats int,
    price int,
    tripId int
);


INSERT INTO Trips (src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Bucuresti', 'Constanta', 1, 20, 23, 100, 100, 0);


INSERT INTO Trips (src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Pitesti', 'Constanta', 1, 20, 23, 100, 100, 1);


INSERT INTO Trips (src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Pitesti', 'Bucuresti', 1, 20, 23, 100, 100, 2);


INSERT INTO Trips (src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Craiova', 'Timisoara', 1, 20, 23, 100, 100, 3);


INSERT INTO Trips (src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Bucuresti', 'Iasi', 1, 20, 23, 100, 100, 4);
