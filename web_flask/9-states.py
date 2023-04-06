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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id=None):
    """display cities by states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_is(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
