#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import render_template
from flask import Flask
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_filter():
    """display the filter"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
