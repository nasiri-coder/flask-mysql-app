import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="",        
        database="flaskdb",
        port=3307
    )
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES;")
    data = cursor.fetchall()
    return f"Bases disponibles : {data}"

if __name__ == '__main__':
    app.run(debug=True)
