#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """ display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ display “HBNB” """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display “Python ”, followed by the value of the text"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """display n only if it's an integer"""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
