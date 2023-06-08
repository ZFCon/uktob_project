import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_sum_numbers():
    numbers = [1, 2, 3, 4, 5]
    payload = json.dumps({"numbers": numbers})
    response = client.post("/sum", data=payload)
    assert response.status_code == 200
    assert response.json() == {"sum": sum(numbers)}

def test_sum_numbers_invalid_input():
    payload = json.dumps({"numbers": [1, 2, "gg", 4, 5]})
    response = client.post("/sum", data=payload)
    assert response.status_code == 422

def test_concatenate_strings():
    strings = ["Hello", " ", "World"]
    payload = json.dumps({"strings": strings})
    response = client.post("/concatenate", data=payload)
    assert response.status_code == 200
    assert response.json() == {"concatenated_string": "".join(strings)}
