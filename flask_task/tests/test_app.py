import json
import pytest
import random
import string
from app import app, users


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def generate_random_username():
    # Generate a random username
    return "".join(random.choice(string.ascii_lowercase) for _ in range(6))


def test_register_success(client):
    username = generate_random_username()
    response = client.post(
        "/register", json={"username": username, "password": "password123"}
    )
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["message"] == "User registration successful."
    assert username in users


def test_register_duplicate_username(client):
    username = generate_random_username()
    users[username] = "password123"  # Simulate existing user
    response = client.post(
        "/register", json={"username": username, "password": "password123"}
    )
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["message"] == "Username already exists."
    assert users[username] == "password123"  # User should not be overwritten


def test_register_missing_fields(client):
    response = client.post("/register", json={"username": generate_random_username()})
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data["message"] == "Invalid username or password."
    assert "john" not in users  # User should not be added


def test_login_success(client):
    username = generate_random_username()
    users[username] = "password123"  # Add user for testing
    response = client.post(
        "/login", json={"username": username, "password": "password123"}
    )
    data = json.loads(response.data)
    assert response.status_code == 200
