#!/usr/bin/python3
""" This module starts a Flask web application
listening on 0.0.0.0, port 5000
Routes:
    /hbnb_filters: display a HTML page: (inside the tag BODY)
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filter_hbnb_filters():
    """
    Display a HTML page: (inside the tag BODY)
    """
    state_list = storage.all(State).values()
    amenity_list = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", state_list=state_list, amenity_list=amenity_list)


@app.teardown_appcontext
def shutdown_session(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
