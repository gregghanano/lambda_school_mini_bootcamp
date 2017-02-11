from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('home.html');

#this is a comment

@app.route('/about')
def about():
    return app.send_static_file('about.html');

# @app.route('/something')
# def something():
#     return '<h1>This is a big h1 headline</h1><p>This is a paragraph</p><h2>this is an h2 header</h2>'

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html');


@app.route('/post/<postnum>')
def post(postnum):
    return 'this is post ' + postnum
