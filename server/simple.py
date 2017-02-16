"""Simple temperature data endpoint."""

import json
import shelve
import base64
from io import BytesIO
from os import path
from pickle import HIGHEST_PROTOCOL

import numpy as np
import matplotlib.pyplot as plt

import flask
from flask import Flask
from flask import request
from flask import render_template_string


SHELVE_DB = 'shelve.db'

app = Flask(__name__)
app.config.from_object(__name__)


def get_db():
    db = flask.g.get("database")
    if db is None:
        db = flask.g.database = shelve.open(path.join(app.root_path,
                                                      app.config['SHELVE_DB']),
                                            protocol=HIGHEST_PROTOCOL,
                                            writeback=True)
        db.setdefault('measurements', [])
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = flask.g.get('database')
    if db is not None:
        db.close()


def _make_plot(db, key):
    obs = db['measurements']
    x = [o['time'] for o in obs]
    idx = np.argsort(x)
    x = np.array(x)
    y = np.array([o[key] for o in obs])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(x[idx], y[idx])
    ax.set_xlabel("time (s)")
    if key == 'temp':
        ax.set_ylabel("Temperature (deg C)")

    if key == 'humidity':
        ax.set_ylabel("Humidity (%)")

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = figdata_png.decode('ascii')
    return render_template_string(
        '<img src="data:image/png;base64,{{ result }}" width="500">',
        result=result)


@app.route('/temp.png')
def temperature_plot():
    db = get_db()
    return _make_plot(db, 'temp')


@app.route('/humidity.png')
def humidity_plot():
    db = get_db()
    return _make_plot(db, 'humidity')


@app.route('/dashboard')
def dashboard():
    db = get_db()

    s = _make_plot(db, 'temp')
    s += _make_plot(db, 'humidity')

    return s


@app.route('/sensor', methods=['POST'])
def post_sensor_data():
    db = get_db()
    db['measurements'].append(json.loads(request.data.decode('ascii')))
    return "OK"#json.dumps(db['measurements'])


@app.route('/data', methods=['GET'])
def get_sensor_data():
    db = get_db()
    return json.dumps(db['measurements'])
