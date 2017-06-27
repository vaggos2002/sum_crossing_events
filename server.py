#!/usr/bin/python3

"""server.py: Basic framework to host a web service for calculating
the number of value crossing
"""

import sqlite3
from flask import g
from flask import request, url_for
from flask.ext.api import FlaskAPI

app = FlaskAPI(__name__)


DATABASE = '/path/to/database.db'


def retrieveUsers():
    """Retrieve users from the database"""
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM users")
    users = cur.fetchall()
    con.close()
    return users


@app.route("/", methods=['POST'])
def get_number():
    """Get the number of value crossing"""
    signal = request.data.get('signal', '')
    signal = [int(n) for n in signal.split(',')]
    value = int(request.data.get('value', ''))
    crossing_number = get_number_of_value_crossings(signal, value)
    return {'crossing_number': crossing_number}


def get_number_of_value_crossings(signal, value):
    """Return the number of value crossings"""

    quant_list = []

    for i in signal:

        # Signal quantization to 1 and 0
        if i > value:
            quat_i = 0
        elif i < value:
            quat_i = 1

        # Signal compression
        if len(quant_list) >= 1 and i != value and quat_i != quant_list[-1]:
            quant_list.append(quat_i)
        elif len(quant_list) == 0:
            quant_list.append(quat_i)

    return len(quant_list) - 1



if __name__ == '__main__':
    app.run(debug=False)
