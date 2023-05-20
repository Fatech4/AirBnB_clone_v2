#!/usr/bin/python3
""" A script that starts a Flask web application: """
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """ A function that returns a string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display2():
    """ A function that returns "HBNB" """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display3(text):
    """ A function that returns 'C' followed by the escaped text """
    str = text.replace('_', ' ')
    return 'C %s' % escape(str)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display4(text='is cool'):
    """ A function that returns 'Python' followed by the escaped text """
    str = text.replace('_', ' ')
    return 'Python %s' % escape(str)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
