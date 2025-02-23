"""Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

# path to choose
@app.route("/")
def home():
    """Home page"""
    return "Welcome to the Flask API!"

@app.route("/data")
def store_users():
    """json page"""
    return jsonify(list(users.keys())) # convert to json 

@app.route("/status")
def status_route():
    """status page"""
    return "OK"

@app.route("/users/<username>")
def user_name(username):
    """get username"""
    name = users.get(username)
    if bool(name):
        return name
    else:
        return {"error": "User not found"}, 404

@app.route("/add_user", methods=['POST'])
def add_user():
    """add user"""
    # JSON data from the request
    data = request.get_json()
    # check data not empty or username not in data
    if not data or "username" not in data:
        return {"error":"Username is required"}, 400
    # data[username] = username: alice, name: Alice etc.
    username = data["username"]
    # Create user with username key
    users[username] = {
        "username": data.get("username"),
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    # Return a JSON response using the jsonify() function
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
