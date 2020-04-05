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


def add_trip(src: str, dest: str, day: str, leaveHour: str, arriveHour: str, numberOfAvailableSeats: str,
             price: str, tripId: str):
    query = "insert into Trips(src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId)" \
            "values (%s, %s, %s, %s, %s, %s, %s, %s) "
    values = (src, dest, day, leaveHour, arriveHour, numberOfAvailableSeats, price, tripId)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def add_seat_into_trip(tripId: str):
    query = "update Trips set numberOfAvailableSeats = numberOfAvailableSeats + 1 where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def delete_seat_from_trip(tripId: str):
    query = "update Trips set numberOfAvailableSeats = numberOfAvailableSeats - 1 where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def get_trips(src: str, dest: str, day: str):
    query = "select * from Trips where src = %s and dest = %s and day = %s"
    values = (src, dest, day)
    
    connection = get_sql_connection()
    cursor = get_cursor(connection)
    
    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()
    return result


def get_users():
    query = "select * from Users"

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    
    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()
    return result

def main():
    while True:
        command = input("Enter a command: ")
        arguments = input("Enter the arguments: ").split()

        if "add_trip" in command:
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

        if "delete_seat" in command:
            delete_seat_from_trip(arguments[0])

        if "add_seat" in command:
            delete_seat_into_trip(arguments[0])

        if "get_trips" in command:
            get_trip(arguments[0], arguments[1], arguments[2])

        if "get_users" in command:
            get_users()

if __name__ == '__main__':
    main()
