import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Finance Tracker!"

def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

init_db()

if __name__ == '__main__':
    app.run(debug=True)