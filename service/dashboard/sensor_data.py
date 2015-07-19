# -*- coding: utf-8 -*-

import sqlite3

from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

app = Flask(__name__)
app.static_url_path=''
app.debug = True

class DataBaseWrapper():
    def __init__(self, db_file='db.sqlite3'):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    #c.execute()
    #conn.commit()

#@app.route('/')
#def root():
#    print('foobar')
#    return app.send_static_file('index.html')

@app.route('/')
def root():
    with open('index.html', 'r', encoding='utf-8') as fp:
        html = response=fp.read()
    resp = Response(html, status=200)
    return resp

# constant sound speed: us per cm
k = 29.104

# total height in centimeters
total_height = 50.

# air gap level when the tank is full in centimeters
full_airgap = 20.7

water_level = lambda h: ((total_height - float(h/(k*2))) /
        (total_height - full_airgap))


#@app.route('/api', methods=['GET'])
#def get_reading():
#    mydb = DataBaseWrapper()
#    query = 'SELECT * FROM sensor_data;'
#    mydb.cursor.execute(query)
#    list_readings = mydb.cursor.fetchall()
#    dict_response = [
#            {"timestamp": r[2],
#             "reading": r[1],
#             "water_level": water_level(r[1])
#            }  for r in list_readings]
#
#    resp = Response(response=str(dict_response).replace("'",'"'),
#                    status=200,
#                    mimetype='application/json')
#    return resp

@app.route('/api/<interval>', methods=['GET'])
def get_reading_month(interval='day'):

    mydb = DataBaseWrapper()
    if interval == 'day':
        query = "SELECT * FROM sensor_data WHERE time_point BETWEEN datetime('now', \
                    '-1 days') AND datetime('now', 'localtime');"
        mydb.cursor.execute(query)
        list_readings = mydb.cursor.fetchall()

    if interval == 'week':
        query = "SELECT * FROM sensor_data WHERE time_point BETWEEN datetime('now', \
                    '-6 days') AND datetime('now', 'localtime');"
        mydb.cursor.execute(query)
        list_readings = mydb.cursor.fetchall()[::4]

    if interval == 'month':
        query = "SELECT * FROM sensor_data WHERE time_point BETWEEN datetime('now', \
                    '-30 days') AND datetime('now', 'localtime');"
        mydb.cursor.execute(query)
        list_readings = mydb.cursor.fetchall()[::4*10]

    dict_response = [
            {"timestamp": r[2],
             "reading": r[1],
             "water_level": water_level(r[1])
            }  for r in list_readings]

    resp = Response(response=str(dict_response).replace("'",'"'),
                    status=200,
                    mimetype='application/json')
    return resp

@app.route('/api', methods=['POST'])
def post_reading():
    mydb = DataBaseWrapper()
    # Post Request Example: http://127.0.0.1:5000/?reading=1234
    reading = request.form.get('reading')
    query = 'INSERT INTO sensor_data (reading) VALUES (%s);'
    mydb.cursor.execute(query % reading)
    mydb.connection.commit()
    return '{"status": "ok"}'

if __name__ == '__main__':
    app.run(debug=True)
