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


def search(src: str, dest: str, day: int):
    query = "select * from Trips where src = %s and dest = %s and dayOfLeaving = %s"
    values = (src, dest, day)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()

    return result


def add_to_cart(email:str, tripId: int):
    query = "insert into Cart (email, tripid, ticketType) values (%s, %s, %s)"
    values = (email, tripId, "reserved")

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def check_cart(email: str):
    query = "select tripId, ticketType from Cart where email = %s"
    values = (email,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()

    return result

def delete_from_cart(email: str, tripId: int):
    query = "delete from Cart where email = %s and tripId = %s"
    values = (email, tripId)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return True


def update_ticket_status(email: str, tripId: int):
    query = "update Cart set ticketType = %s where email = %s and tripId = %s"
    values = ("bought", email, tripId)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()


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


def check_if_ticket_is_reserved(email: str, tripId: int):
    query = "select ticketType from Cart where email = %s and tripId = %s"
    values = (email, tripId)

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
    query = "update Trips set numberOfAvailableSeats = numberOfAvailableSeats - 1 where tripId = %s"
    values = (tripId,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)
    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()


def check_if_email_exists(email: str):
    query = "select * from Users where email = %s"
    values = (email,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()

    return result

def sign_in(fN: str, lN: str, email: str, passwd: str):
    query = "insert into Users (firstName, lastName, email, password)" \
            "values (%s, %s, %s, %s) "
    values = (fN, lN, email, passwd)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def get_password(email: str):
    query = "select password from Users where email = %s"
    values = (email,)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)

    result = []
    [result.append(line) for line in cursor]

    cursor.close()
    connection.close()

    return result


def delete_account(email: str, passwd: str):
    query = "delete from Users where email = %s and password = %s"
    values = (email, passwd)

    connection = get_sql_connection()
    cursor = get_cursor(connection)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return True


@app.route('/search')
def f0():
    src = request.args.get('src', default=None, type=str)
    dest = request.args.get('dest', default=None, type=str)
    day = request.args.get('day', default=None, type=int)

    result = search(src, dest, day)
    return jsonify(trips=result)


@app.route('/add_to_cart')
def f1():
    email = request.args.get('e', default=None, type=str)
    id = request.args.get('id', default=None, type=int)

    add_to_cart(email, id)
    result = check_cart(email)

    return jsonify(ticket=result)


@app.route('/buy_ticket')
def f2():
    email = request.args.get('e', default=None, type=str)
    trip_id = request.args.get('id', default=None, type=int)

    update_number_of_available_seats(trip_id, "buy")
    update_ticket_status(email, trip_id)

    result = check_cart(email)

    return jsonify(ticket=result)


@app.route('/delete_from_cart')
def f3():
    email = request.args.get('e', default=None, type=str)
    id = request.args.get('id', default=None, type=int)

    ticketType = check_if_ticket_is_reserved(email, id)

    if ticketType.pop(0)[0] == "bought":
        return jsonify(ticket="The ticket has been already bought")

    delete_from_cart(email, id)
    result = check_cart(email)

    return jsonify(ticket=result)


@app.route('/sign_in')
def f4():
    fN = request.args.get('fN', default=None, type=str)
    lN = request.args.get('lN', default=None, type=str)
    email = request.args.get('e', default=None, type=str)
    passwd = request.args.get('p', default=None, type=str)

    sign_in(fN, lN, email, passwd)
    return jsonify(sign_in=True)


@app.route('/log_in')
def f5():
    email = request.args.get('e', default=None, type=str)
    passwd = request.args.get('p', default=None, type=str)

    result = get_password(email).pop(0)[0]
    if passwd == result:
        return jsonify(log_in=True)
    else:
        return jsonify(log_in=False)


@app.route('/delete_account')
def f6():
    email = request.args.get('e', default=None, type=str)
    passwd = request.args.get('p', default=None, type=str)

    result = delete_account(email, passwd)

    return jsonify(delete_account=result)


@app.route('/check_cart')
def f7():
    email = request.args.get('e', default=None, type=str)

    result = check_cart(email)

    return jsonify(ticket=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
