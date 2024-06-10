from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

app.secret_key = "abc"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nico_!1303'
app.config['MYSQL_DB'] = 'login_db'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

def sjekk_db_tilkobling():
    with app.app_context():
        try:
            mysql.connection.ping()
            print("Tilkobling til databasen er vellykket!")
        except Error as e:
            print("Feil ved tilkobling til databasen:", e)

sjekk_db_tilkobling()

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            if not username or not password:
                mesage = 'Username and password cannot be empty!'
                return render_template('login.html', mesage=mesage)
            print(f"Username: {username}, Password: {password}")  # Debug: Log input values
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
            user = cursor.fetchone()
            print(f"User: {user}")  # Debug: Log fetched user
            if user:
                session['loggedin'] = True
                session['userid'] = user['id']
                session['username'] = user['username']
                print("User logged in successfully!")  # Debug: Log successful login
                mesage = 'Logged in successfully!'
                return render_template('user.html', mesage=mesage)
            else:
                mesage = 'Please enter correct username / password!'
        else:
            mesage = 'Please enter both username and password!'
    return render_template('login.html', mesage=mesage)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Her kan du legge til logikk for å håndtere registrering
    return "Registreringsside kommer snart!"

if __name__ == '__main__':
    app.run(debug=True, port=5500)
