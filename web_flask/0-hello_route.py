#!/usr/bin/python3
"""First flask web page """


from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display sentence in web page"""
    return "Hello HBNB!"

if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)