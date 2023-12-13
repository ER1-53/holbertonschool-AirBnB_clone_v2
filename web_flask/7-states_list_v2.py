#!/usr/bin/python3
"""First flask web page """


from models import storage
from flask import Flask, render_template
from markupsafe import escape
from models.state import State
app = Flask(__name__)

@app.route("/states_list_v2", strict_slashes=False)
def states():
    """Display sentence in web page"""
    states=storage.all(State).values()
    sorted_state = sorted(states, key=lambda x: x.name) # le trie se fait dans le code python alors que dans l'autre version il se fait dans le html
    return render_template('7-states_list_v2.html', states=sorted_state)

@app.teardown_appcontext
def free(exception):
    storage.close()

if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)