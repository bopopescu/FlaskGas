import mysql.connector as mariadb
from flask import render_template
from flask import flash, redirect, url_for, request
import time
from datetime import date
from datetime import datetime
from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    SITE_NAME='GasCalculate'
))

def dblog():
    global cursor
    global mariadb_connection
    mariadb_connection = mariadb.connect(
        user='root',
        password='piotr',
        database='db')


@app.route('/home', methods=['GET', 'POST'])
def home():

    return render_template('home.html')
a= ''

@app.route('/calc',methods=['GET', 'POST'])
def Calculate():
    if request.method == 'POST':
        global date
        valuePage = request.form['zadanie'].strip()
        if len(valuePage) > 0 :
            dblog()
            date=date.today()
            timestamp=str(round(time.time()))

            cursor = mariadb_connection.cursor()
            cursor.execute("SELECT * FROM jeden ORDER BY id DESC LIMIT 1")
            dbResult = cursor.fetchone()
            dbValue = dbResult[1];dbDate = dbResult[2];dbTimestamp = dbResult[3]

            valuePage=int(valuePage);dbValue=int(dbValue)
            value = valuePage-dbValue
            price = round(value*2.31)

            timestamp=int(timestamp);dbTimestamp=int(dbTimestamp)
            lapsing = round(timestamp-dbTimestamp)
            lapsing = round(lapsing/86400)


            cursor = mariadb_connection.cursor()
            cursor.execute('INSERT INTO jeden (value, date, time) VALUES (%s, %s, %s)', (valuePage,date,timestamp))
            mariadb_connection.commit()

        price=str(price);lapsing=str(lapsing);dbDate=str(dbDate);value=str(value)
        flash('Przez ostatnie '+lapsing+' dni (liczone od '+dbDate+'), zostalo zuzyte '+value+' kubikow gazu.(Co kosztowalo nas '
          +price+' zl)')
    return render_template('calc.html')


@app.route('/DataBase',methods=['GET', 'POST'])
def dbList():
    dblog()
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT * FROM jeden ORDER BY value DESC LIMIT 10")
    dbResultlist = cursor.fetchall()
    i=0
    while i <len(dbResultlist):
        flash(dbResultlist[i][2]+'-->'+dbResultlist[i][1])
        i+=1
    return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)