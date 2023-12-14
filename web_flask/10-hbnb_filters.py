#!/usr/bin/python3
"""First flask web page """
from models import storage
from flask import Flask, render_template, abort
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def free(exception):
    """use methode close for free"""
    storage.close()



@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """Display sentence in web page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    return render_template(
        '10-hbnb_filters.html', html_states=states, amenities=amenities)


if __name__ == '__main__':
    """execute this info only at script execution
    in other case dont execte this"""
    app.run(host='0.0.0.0', port=5000)
