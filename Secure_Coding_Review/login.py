from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

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

    cursor.execute(
        "INSERT INTO users (username, password) VALUES ('admin', 'admin123')"
    )

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():

    name = request.args.get('name', '')

    return render_template_string(f"""
        <h1>Welcome {name}</h1>

        <h2>Login</h2>

        <form method="POST" action="/login">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
    """)

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    print("[DEBUG] Executing Query:", query)

    cursor.execute(query)

    user = cursor.fetchone()

    conn.close()

    if user:
        return f"""
        <h1>Login Successful</h1>
        <p>Welcome {username}</p>
        """
    else:
        return """
        <h1>Login Failed</h1>
        """

@app.route('/admin')
def admin():

    return """
    <h1>Admin Panel</h1>
    <p>Confidential Data Here</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
