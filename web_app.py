import os
from flask import Flask
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

@app.route('/')
def hello():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM names LIMIT 1;")
    name = cursor.fetchone()[0]
    conn.close()
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("DENTRO")
    app.run(debug=True, host='0.0.0.0')