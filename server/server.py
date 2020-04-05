from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

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


def add_user(firstName: str, lastName: str, email: str, type: str, password: str):
    query = "insert into Users(firstName, lastName, email, type, password) values (%s, %s, %s, %s, %s)"
    values = (firstName, lastName, email, type, password)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def check_credentials(email: str, password: str):
    query = "select password from Users where email = %s"
    values = (email,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)
    
    cursor.close()
    connection.close()


def get_trips(src: str, dest: str, day: int):
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


def buy_ticket(tripId: int):
    query = "select * from Trips where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()
    
    return result


def cancel_ticket(tripId: int):
    query = "select * from Trips where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()
    
    return result


def update_number_of_available_seats(tripId: int, opCode: str):
    if "buy" in opCode:
        query = "update Trips set numberOfAvailableSeats = numberOfAvailableSeats - 1 where tripId = %s"
    else:
        query = "update Trips set numberOfAvailableSeats = numberOfAvailableSeats + 1 where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()


@app.route('/sign_in')
def f0():
    firstName = request.args.get('fN', default = None, type = str)
    lastName = request.args.get('lN', default = None, type = str)
    email = request.args.get('e', default = None, type = str)
    type = request.args.get('t', default = None, type = str)
    passwd = request.args.get('p', default = None, type = str)
    
    add_user(firstName, lastName, email, type, passwd)
    return True

@app.route('/log_in')
def f1():
    email = request.args.get('e', default = None, type = str)
    passwd = request.args.get('p', default = None, type = str)
    
    check_credentials(email, type, passwd)
    return True

@app.route('/get_trip')
def f2():
    src = request.args.get('src', default = None, type = str)
    dest = request.args.get('dest', default = None, type = str)
    day = request.args.get('day', default = None, type = int)

    result = get_trips(src, dest, day)

    return jsonify(res=result)


@app.route('/buy_ticket')
def f3():
    tripId = request.args.get('id', default = None, type = int)

    result = buy_ticket(tripId)
    update_number_of_available_seats(tripId, "buy")

    return jsonify(res=result)


@app.route('/cancel_ticket')
def f4():
    tripId = request.args.get('id', default = None, type = int)

    result = cancel_ticket(tripId)
    update_number_of_available_seats(tripId, "cancel")

    return jsonify(res=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
