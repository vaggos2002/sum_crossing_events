#!/usr/bin/python3

"""server.py: Basic framework to host a web service for calculating
the number of value crossing
"""

from flask import request, url_for, abort

from flask_api import FlaskAPI
from flask_httpauth import HTTPBasicAuth

app = FlaskAPI(__name__)
auth = HTTPBasicAuth()

users = {
    'evan': 'python3',
}


@auth.get_password
def get_pw(username):
    if users[username]:
        return users.get(username)
    return None


@app.route("/", methods=['POST'])
@auth.login_required
def get_number():
    """Get the number of value crossing"""
    signal = request.data.get('signal', '')
    value = request.data.get('value', '')

    if signal == '' or value == '':
        abort(422)

    try:
        signal = [int(n) for n in signal.split(',')]
        value = int(value)
    except ValueError:
        abort(422)

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

    if len(quant_list) == 0:
        return 0

    return len(quant_list) - 1


if __name__ == '__main__':
    app.run(debug=False)
