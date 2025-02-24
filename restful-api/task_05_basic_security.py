"""Security"""
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    else:
        return "Invalid username and password", 401

@app.route("/basic-protected")
@auth.login_required
def basic_auth():
    return "Basic Auth: Access Granted"

if __name__ == "__main__":
    app.run(debug=True)
