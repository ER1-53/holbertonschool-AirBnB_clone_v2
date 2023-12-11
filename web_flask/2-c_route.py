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

@app.route("/c/<name>", strict_slashes=False)
def c_name(name):
    """display C and <name> in arg"""
    return f"C {escape(name)}"

if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)