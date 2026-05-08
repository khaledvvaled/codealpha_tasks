from flask import Flask, request, render_template_string, session, redirect, url_for
from markupsafe import escape
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')

    cursor.execute("SELECT * FROM users WHERE username=?", ('admin',))
    if not cursor.fetchone():
        hashed_password = generate_password_hash('admin123')
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", 
            ('admin', hashed_password)
        )

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    name = request.args.get('name', '')
    safe_name = escape(name)

    return render_template_string("""
        <h1>Welcome {{ safe_name }}</h1>
        <h2>Login</h2>
        <form method="POST" action="/login">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    """, safe_name=safe_name)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[2], password):
        session['logged_in'] = True
        session['username'] = username
        
        safe_username = escape(username)
        return f"""
        <h1>Login Successful</h1>
        <p>Welcome {safe_username}</p>
        <a href="/admin">Go to Admin Panel</a>
        """
    else:
        return """
        <h1>Login Failed</h1>
        <p>Invalid credentials.</p>
        """

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return """
        <h1>Unauthorized Access</h1>
        <p>You must be logged in to view this page.</p>
        <a href="/">Go to Login</a>
        """, 401

    return """
    <h1>Admin Panel</h1>
    <p>Confidential Data Here</p>
    """

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=False)
