import sqlite3

from flask import Flask
from flask import jsonify

app = Flask(__name__)

class DataBaseWrapper():
    def __init__(self, db_file='db.sqlite3'):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    #c.execute()
    #conn.commit()

mydb = DataBaseWrapper()

@app.route("/", methods=["GET"])
def get_reading():
    query = 'SELECT * FROM sensor_data_sensorreading;'
    mydb.cursor.execute(query % reading)
    list_readings = mydb.cursor.fetchall()
    return jsonify(list_readings)

@app.route("/", methods=["POST"])
def post_reading():
    reading = request.form['reading']
    query = 'INSERT INTO sensor_data_sensorreading (reading) VALUE (%s)'
    mydb.cursor.execute(query % reading)
    return '{"status": "ok"}'

if __name__ == "__main__":
    app.run()
