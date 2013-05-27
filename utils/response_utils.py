from flask import jsonify


def json_response(obj):
    return jsonify(obj)


def json_success(**kwargs):
    response = kwargs
    if 'status' not in response:
        response['status'] = 'success'

    return json_response(response)


def json_failure(message="", **kwargs):
    response = {
        'status': 'failure',
        'message': message
    }
    response.update(kwargs)
    return json_response(response)
