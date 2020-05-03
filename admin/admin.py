import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'CFR'
}


def get_sql_connection():
    return mysql.connector.connect(**config)


def get_cursor(connection):
    return connection.cursor()


def get_users():
    query = "select firstName, lastName, email from Users"

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()

    return result


def add_trip(src: str, dest: str, day: int, leaveHour: str, arriveHour: str, numberOfAvailableSeats: str,
             price: str, tripId: str):
    query = "insert into Trips(src, dest, dayOfLeaving, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId)" \
            "values (%s, %s, %s, %s, %s, %s, %s, %s) "
    values = (src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def add_seat_into_trip(tripId: int):
    query = "update Trips set numberOfAvailableSeats = numberOfAvailableSeats + 1 where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def delete_trip(tripId: int):
    query = "delete from Trips where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def delete_seat_from_trip(tripId: int):
    query = "update Trips set numberOfAvailableSeats = numberOfAvailableSeats - 1 where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def get_trips():
    query = "select * from Trips"

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()

    return result


def main():
    while True:
        command = input("Enter a command:\n"
                        "add_trip\n"
                        "add_seat_into_trip\n"
                        "delete_trip\n"
                        "delete_seat_from_trip\n"
                        "get_trips\n"
                        "get_users\n")

        if "add_trip" in command:
            arguments = input(""
                              "Enter the arguments: Source Destination Day LeaveHour ArriveHour"
                              "AvailableSeats Price TripId\n").split()
            add_trip(
                arguments[0],
                arguments[1],
                arguments[2],
                arguments[3],
                arguments[4],
                arguments[5],
                arguments[6],
                arguments[7]
            )

        if "add_seat_into_trip" in command:
            arguments = input("Enter the arguments: TripId\n").split()
            add_seat_into_trip(int(arguments[0]))

        if "delete_trip" in command:
            arguments = input("Enter the arguments: TripId\n").split()
            delete_trip(int(arguments[0]))

        if "delete_seat_from_trip" in command:
            arguments = input("Enter the arguments: TripId\n").split()
            delete_seat_from_trip(int(arguments[0]))

        if "get_trips" in command:
            trips = get_trips()
            [print(
                f"Source: {trip[0]} | Destination: {trip[1]} | Day: {trip[2]} | LeaveHour: {trip[3]}"
                f"| ArriveHour: {trip[4]} | AvailableSeats: {trip[5]} | Price: {trip[6]} | TripId: {trip[7]}")
                for trip in trips
            ]

        if "get_users" in command:
            users = get_users()
            [print(
                f"First Name: {user[0]} | Last Name: {user[1]} | Email: {user[2]}")
                for user in users
            ]


if __name__ == '__main__':
    main()
