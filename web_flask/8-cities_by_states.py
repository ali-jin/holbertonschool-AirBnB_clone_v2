#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import render_template
from flask import Flask
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities():
    """display cities by states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
