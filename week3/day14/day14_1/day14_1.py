from flask import Flask,request,render_template, redirect
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():

    conn = sqlite3.connect('week3/day14/day14_1/test.db')
    cursor = conn.cursor()
    cursor.execute(" select title,lastname,firstname,country,city from employees ")
    emp = cursor.fetchall()
    conn.close()
    return render_template('sqlite_index.html',emp = emp)

@app.route('/albums')
def albums():
    conn = sqlite3.connect('week3/day14/day14_1/test.db')
    cursor = conn.cursor()
    cursor.execute("select albumid,name ,composer,bytes from tracks limit 20")
    albums = cursor.fetchall()
    conn.close()
    return render_template('albums.html',albums=albums)
@app.route('/inPerson')
def inPerson():
    return render_template('inPerson.html')

@app.route('/person')
def person():
    conn = sqlite3.connect('week3/day14/day14_1/test.db')
    cursor = conn.cursor()
    cursor.execute('select * from persons')
    person = cursor.fetchall()
    return render_template('person.html',person=person)

@app.route('/create',methods=['POST'])
def create():
    username = request.form['name']
    userage = request.form['age']
    gender = request.form['gender']
    major = request.form['major']
    conn = sqlite3.connect('week3/day14/day14_1/test.db')
    cursor = conn.cursor()
    sql = 'insert into persons values(?,?,?,?)'
    cursor.execute(sql,(username,userage,gender,major))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

