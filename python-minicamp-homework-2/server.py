from flask import Flask, render_template, jsonify

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

@app.route("/sum/<number1>/<number2>")
def sum(number1, number2):
    result = int(number1) + int(number2)
    return number1 + " + " + number2 +" = " + str(result)

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    result = int(number1) * int(number2)
    return number1 + " * " + number2 + " = " + str(result)

@app.route('/subtract/<number1>/<number2>')
def subtract(number1, number2):
    result = int(number1) - int(number2)
    return number1 + " - " + number2 + " = " + str(result)

@app.route('/favoritefoods')
def favoriteFoods():
    foods = ["burrito", "pizza", "sandwiches","burgers"]
    return jsonify(foods)

if __name__=="__main__":
    app.run(debug=True)
