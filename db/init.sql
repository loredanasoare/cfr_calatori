create database CFR;

use CFR;

create table Users(
    firstName varchar(30),
    lastName varchar(30),
    email varchar(30),
    password varchar(30)
);

create table Trips(
    src varchar(30),
    dest varchar(30),
    dayOfLeaving int,
    leaveHour int,
    arriveHour int,
    numberOfAvailableSeats int,
    price int,
    tripId int
);

create table Cart(
    email varchar(30),
    tripId int,
    ticketType varchar(30)
);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Pitesti', 'Bucuresti', 1, 8, 10, 100, 25, 0);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Pitesti', 'Bucuresti', 1, 12, 14, 50, 15, 1);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Pitesti', 'Bucuresti', 1, 16, 18, 150, 30, 2);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Pitesti', 'Bucuresti', 1, 18, 20, 100, 15, 3);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Pitesti', 'Bucuresti', 1, 20, 22, 100, 20, 4);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Bucuresti', 'Pitesti', 1, 9, 11, 50, 15, 5);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Bucuresti', 'Pitesti', 1, 13, 15, 100, 15, 6);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Bucuresti', 'Pitesti', 1, 14, 16, 100, 20, 7);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Bucuresti', 'Pitesti', 1, 17, 19, 150, 25, 8);

INSERT INTO Trips (src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId) VALUES ('Bucuresti', 'Pitesti', 1, 20, 22, 50, 20, 9);


INSERT INTO Users (firstName, lastName, email, password) VALUES ('Loredana', 'Soare', 'ls@gmail.com', 'root');

INSERT INTO Users (firstName, lastName, email, password) VALUES ('Iulia', 'Popescu', 'ip@gmail.com', 'root');

INSERT INTO Users (firstName, lastName, email, password) VALUES ('Andrei', 'Constantin', 'ac@gmail.com', 'root');

INSERT INTO Users (firstName, lastName, email, password) VALUES ('Alexandru', 'Miron', 'am@gmail.com', 'root');

INSERT INTO Users (firstName, lastName, email, password) VALUES ('Gabriel', 'Iancu', 'gi@gmail.com', 'root');
