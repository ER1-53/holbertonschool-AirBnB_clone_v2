#!/usr/bin/python3
"""First flask web page """


from models import storage
from flask import Flask, render_template, abort
from markupsafe import escape
from models.state import State
app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states():
    """Display sentence in web page"""
    return render_template('7-states_list.html', states=storage.all(State).values() )

@app.teardown_appcontext
def free(exception):
    storage.close()

if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)
