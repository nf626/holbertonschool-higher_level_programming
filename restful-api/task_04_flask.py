"""Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route("/")
def home():
    """Home page"""
    return "Welcome to the Flask API!"

@app.route("/data")
def store_users():
    """json page"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status_route():
    """status page"""
    return "OK"

@app.route("/users/<username>")
def user_name(username):
    name = users.get(username)
    if bool(name):
        return name
    else:
        return {"error": "User not found"}

@app.route("/add_user", methods=['POST'])
def add_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)
