
import mysql.connector as mariadb
from flask import render_template
from flask import request, redirect, url_for, flash
import os
from flask import app,config
from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    SITE_NAME='GasCalculate'
))

def dblog():
    global cursor
    global mariadb_connection
    mariadb_connection = mariadb.connect(user='root',
        password='piotr',
        database='db')
dblog()

cursor = mariadb_connection.cursor()
# cursor.execute('INSERT INTO jeden (value, date, time) VALUES (%s, %s, %s)', (value,date,time))
# mariadb_connection.commit()

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calc')

def Calculate():
    return render_template('calc.html')

if __name__ == '__main__':
    app.run(debug=True)