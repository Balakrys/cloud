"""Basic program."""
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def new_student():
    """Function."""
    return render_template('heello.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    """Function to insert the details."""
    if request.method == 'POST':
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        blood_group = request.form['blood_group']
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute ( "INSERT INTO student ( name, addr, city, pin ,blood_group) VALUES ( ?, ?,  ?, ? ,? )", ( nm, addr, city, pin ,blood_group) )
            con.commit()
        return render_template("result.html",msg = "msg")
        con.close()
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from student")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)            



if __name__ == '__main__':
    app.run(host='192.168.0.105', port=2005)
