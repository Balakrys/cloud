from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def new_student():
    """Function."""
    return render_template('hlog.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    """Function to insert the details."""
    if request.method == 'POST':
        nm = request.form['nm']
        print "test",request
        mail = request.form['mail']
        password = request.form['password']
        confirm = request.form['confirm']
        gender = request.form['gender']
        with sql.connect("datbas.db") as con:
            cur = con.cursor()
            cur.execute ( "INSERT INTO LOGI( name,mail,password,confirm,gender) VALUES ( ?, ?,  ?, ?,? )", ( nm, mail,password,confirm,gender) )
            
            print 


            con.commit()
            con = sql.connect("datbas.db")
            con.row_factory = sql.Row
             
            cur = con.cursor()
            cur.execute("SELECT * from LOGI")
             
            rows = cur.fetchall();
            return render_template("listt.html",rows = rows) 
                  

            
        
@app.route('/listt')
def list():
  con = sql.connect("datbas.db")
  con.row_factory = sql.Row
   
  cur = con.cursor()
  cur.execute("SELECT * from LOGI")
   
  rows = cur.fetchall();
  return render_template("listt.html",rows = rows)  
@app.route("/upda") 
def upda():
  con=sql.connect("datbas.db")
  con.row_factory=sql.Row
  cur=con.cursor()
  rows=cur.fetchall();
  cur.execute("SELECT * from LOGI where name = '%s' "%nm )

    # if request.method == 'POST':
     # nm = request.form['nm']
  #   print nm.upper()
    # a=addrec()
    # print a
    
  return render_template("upda.html",rows=rows)           

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2001)
