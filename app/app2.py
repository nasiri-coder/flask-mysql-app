import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

# Connexion MySQL via Docker Compose service name
DB_HOST = os.getenv("DB_HOST", "db")  # <-- ici "db" et non 127.0.0.1
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "flaskdb")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

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
    # Écoute sur toutes les interfaces dans le conteneur
    app.run(host='0.0.0.0', port=5000, debug=True)
