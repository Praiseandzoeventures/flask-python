
from flask import Flask, render_template, request
import mysql.connector
import re 
app = Flask(__name__)
@app.route('/login', methods=['GET','POST'])
def login():
    msg =""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(

host='remoteysql.com',

user='Rz8hqnlk4',

password='nd6wK03xe0',

database='Rz8hqnlk4'

)
        mycursor=mydb.cursor()
       
        mycursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = mycursor.fetchone()
        if account:
            msg = 'Logged in successfully!'
            print('logged in successfully!')
            return render_template('login.html', msg=msg)
        else:
         msg = 'Incorrect username / password!'
         return render_template('login.html', msg=msg)
    else:
         return render_template('login.html', msg=msg)
    