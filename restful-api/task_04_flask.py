from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    """Home page"""
    return "Welcome to the Flask API!"

@app.route("/data")
def serve_json():
    """json page"""
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify()

@app.route("/status")
def status_route():
    """status page"""
    return "OK"

if __name__ == "__main__":
    app.run()
