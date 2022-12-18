from flask import (
    request,
    jsonify
)

def get_from_request(name):
    return request.json.get(name,None)

def set_response(data, index=200):
    return jsonify(data), index 

def get_from_intention(intention, name:str) -> list:
    return intention[name]

def get_max_score(scores:list[float]) -> int:
    return max(enumerate(scores), key=lambda x: x[1])[0]

def get_labels() -> list[str]:
    return ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]