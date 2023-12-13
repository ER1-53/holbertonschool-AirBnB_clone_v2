#!/usr/bin/python3
"""First flask web page """
from flask import Flask, abort, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display sentence in web page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """display only HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display C and <text> in arg"""
    return f"C {escape(text)}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """display python and <text> in arg"""
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def only_n(n):
    """display <n> if is an integer"""
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)
