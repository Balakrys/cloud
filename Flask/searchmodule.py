"""Basic program."""
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def new_student():
    """Function."""
    return render_template('se.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    """Function to get the information to search."""
    if request.method == 'POST':
        statename = request.form['state_name']
        cityname = request.form['city_name']
        blood = request.form['blood']
        print statename,cityname,blood
        with sql.connect("database.db") as con:
        	cur = con.cursor()
        	cur.execute ( "Select * from donar where city = '%s' "%cityname);
        	# for row in cur.fetchall():
        	# 	print row
        	a=str(cur.fetchall())
        	print a
        	return a


        	con.commit()
    	return "cityname"

        	
        	
	    	



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2006,debug=True)
