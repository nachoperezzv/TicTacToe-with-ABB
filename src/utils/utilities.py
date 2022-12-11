from flask import (
    request,
    jsonify
)

def get_from_request(name):
    return request.json.get(name,None)

def set_response(data, index=200):
    return jsonify(data), index 