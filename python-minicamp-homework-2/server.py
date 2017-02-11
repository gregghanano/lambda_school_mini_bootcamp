from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return "April 9th 1989"

@app.route("/greeting/<name>")
def greeting(name):
    return "Hello {}!".format(name)
