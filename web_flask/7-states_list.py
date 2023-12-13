#!/usr/bin/python3
"""First flask web page """
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """Display sentence in web page"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def free(exception):
    """use methode close for free"""
    storage.close()


if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)
