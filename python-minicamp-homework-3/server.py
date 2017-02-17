from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/enternew')
def food():
    return render_template('food.html')

@app.route('/addfood', methods=['POST'])
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        is_vegetarian = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']
        cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name, calories, cuisine, is_vegetarian, is_gluten_free))
        connection.commit()
        message = 'Records successfully added'
    except:
        connection.rollback()
        message = 'error in insert operation'
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM foods WHERE name = "pizza"')
        #print(cursor.fetchone())
        connection.commit()
    except:
        connection.rollback()
        message = 'error in selecting favorite foods'
    finally:
        return jsonify(cursor.fetchone())
        connection.close()
