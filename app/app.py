import os
import time
import mysql.connector
from flask import Flask

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "flaskdb")

def get_db_connection(retries=5, delay=3):
    for i in range(retries):
        try:
            return mysql.connector.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
        except mysql.connector.Error as e:
            print(f"MySQL not ready, retrying in {delay} sec... ({i+1}/{retries})")
            time.sleep(delay)
    raise Exception("Could not connect to MySQL after several retries")

@app.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return f"Users : {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
