from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/birthday')
def birthday():
    return "April 9th 1989"
