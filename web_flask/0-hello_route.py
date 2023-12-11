#!/usr/bin/python3
"""First flask web page """


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Display sentence in web page"""
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)