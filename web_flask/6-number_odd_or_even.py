#!/usr/bin/python3
"""First flask web page """


from flask import Flask, render_template, abort
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

@app.route("/number_template/<int:n>", strict_slashes=False)
def display_page_if_intn(n):
    """display thml page if <n> is an integer"""
    return render_template('5-number.html', my_number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_odd(n):
    """display thml page if <n> is an integer"""
    if n % 2 == 0:
        result = 'even'
    elif n % 2 != 0:
        result = 'odd'
    return render_template('6-number_odd_or_even.html', my_number=n, result=result)

if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)
