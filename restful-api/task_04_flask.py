"""Flask"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    """Home page"""
    return "Welcome to the Flask API!"

@app.route("/data")
def serve_json():
    """json page"""
    return jsonify()

@app.route("/status")
def status_route():
    """status page"""
    return "OK"

@app.route("/users/<username>")
def user_name():
    pass

@app.route("/add_user")
def add_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)
