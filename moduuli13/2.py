import mysql.connector
from flask import Flask, Response


app=Flask(__name__)

yhteys=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2244',
    autocommit=True
)
@app.route('/airport/<icao>')
def haeLentokentta(icao):
    sql='''
    SELECT name, municipality 
    FROM airport 
    WHERE ident = %s
    '''
    kursori=yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    tulos=kursori.fetchone()
    return tulos

if __name__=='__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)