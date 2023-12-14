#!/usr/bin/python3
"""First flask web page """
from models import storage
from flask import Flask, render_template, abort
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def free(exception):
    """use methode close for free"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """Display sentence in web page"""
    states = storage.all(State).values()
    if id is None:
        return render_template('9-states.html', html_states=states, id=None)

    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state, state_id=id)
    return render_template('9-states.html', id=0)


if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)
