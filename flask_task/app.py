from flask import Flask, request, jsonify

app = Flask(__name__)

users = dict()  # Dictionary to store user credentials


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    if username and password:
        if username not in users:
            users[username] = password
            return jsonify({"message": "User registration successful."}), 200
        else:
            return jsonify({"message": "Username already exists."}), 400
    else:
        return jsonify({"message": "Invalid username or password."}), 400


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username and password:
        if username in users and users[username] == password:
            return jsonify({"message": "Access granted."}), 200
        else:
            return jsonify({"message": "Access denied."}), 401
    else:
        return jsonify({"message": "Invalid username or password."}), 400


if __name__ == "__main__":
    app.run()
