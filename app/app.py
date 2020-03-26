from flask import Flask, request, render_template
import mysql.connector
import socket

app = Flask(__name__)

config = {
	'user': 'root',
        'password': 'lori!',
        'host': 'mysql_db',
        'port': '3306',
        'database': 'CFR'
    }

def getMySQLConnection():
    return mysql.connector.connect(**config)

#@app.route('/', methods=['GET', 'POST'])
#def test1():
#    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def test2():
    if request.method == "POST":
        information = request.form
        
        firstname = information['firstname']
        lastname = information['lastname']
        email = information['email']
        
        mysqlConn = getMySQLConnection()
        cursor = mysqlConn.cursor()
        query = "insert into Users(firstname, lastname, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (firstname, lastname, email))
        mysql.connection.commit()
        cursor.close()
        return "success"
    return render_template('index.html')

if __name__ =="__main__":
    app.run(host="0.0.0.0", debug=True)
