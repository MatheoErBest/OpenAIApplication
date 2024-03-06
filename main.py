from flask import Flask, render_template, request, redirect, session
import pymysql
import openai

app = Flask(__name__)
app.secret_key = 'secret_key'

# Opprett forbindelse til MySQL-databasen
def connect_to_database():
    return pymysql.connect(host='your_host', user='your_username', password='your_password', database='your_database')

# Opprett en bruker i databasen
def add_user_to_db(username, password):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
            connection.commit()
    finally:
        connection.close()

# Sjekk om brukeren er i databasen
def user_exists(username):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            return result is not None
    finally:
        connection.close()

# Logg inn brukeren
def login_user(username):
    session['username'] = username

# Sjekk om brukeren er logget inn
def is_logged_in():
    return 'username' in session

# Logg ut brukeren
def logout_user():
    session.pop('username', None)

# Innloggingsside
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_exists(username):
            login_user(username)
            return redirect('/openai')
        else:
            return render_template('login.html', error='Feil brukernavn eller passord.')
    else:
        return render_template('login.html')

# Registreringsside
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not user_exists(username):
            add_user_to_db(username, password)
            return redirect('/login')
        else:
            return render_template('register.html', error='Brukernavnet eksisterer allerede.')
    else:
        return render_template('register.html')

# Logg ut
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

# OpenAI-siden
@app.route('/openai')
def openai():
    if is_logged_in():
        # Legg til OpenAI-kode her for å kalle API og hente respons
        return render_template('openai.html')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
