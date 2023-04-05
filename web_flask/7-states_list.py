#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import render_template
from flask import Flask
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_session():
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
