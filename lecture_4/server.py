from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/new-friend', methods = ['POST'])
def new_friend():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    name = request.form['name']
    age = request.form['age']
    try:
        cursor.execute('INSERT INTO friends(name, age) VALUES (?,?)', (name, age))
        connection.commit()
        message = 'Successfully inserted into friends table'
    except:
        connection.rollback()
        message = 'Failed to insert data.'
    finally:
        connection.close()
        return message



app.run(debug = True)
