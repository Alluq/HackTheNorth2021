from . import authentication
from .user_repo import UserRepo
import os
from flask import Flask, make_response, request, jsonify
import uuid

db_user = UserRepo()
app = Flask("app")
os.makedirs("../uploads", exists_ok=True)


# @app.route("/api/access")

@app.route("/api/delete_user", methods=["POST"])
def delete_user():
    if "username" in request.form and "password" in request.form:
        username, password = request.form["username"], request.form["password"]
        if db_user.authenticate(username, password):
            db_user.delete_user(username)
            return {"status": "success"}, 200
        else:
            return {"status": "unauthorized"}, 401
    else:
        return {"status": "bad request"}, 400


@app.route("/api/create_user", methods=["POST"])
def create_user():
    if "username" in request.form and "password" in request.form:
        username, password = request.form["username"], request.form["password"]
        if db_user.check_user(username):
            db_user.create_user(username, password)
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "user already exists"}), 401
    else:
        return jsonify({"status": "bad request"}, 400)


@app.route("/api/auth/")
def auth_check():
    if "token" not in request.cookies:
        return jsonify({"status": "bad request"}), 400
    id = authentication.verify_data(request.cookies["token"])
    if id[1]:
        return jsonify({"status": "authenticated"}), 200
    return jsonify({"status": "authenticated"}), 200


@app.route("/api/login/", methods=["POST"])
def login():
    if "username" in request.form and "password" in request.form:
        username, password = request.form["username"], request.form["password"]
        auth_val = db_user.authenticate(username, password)
        if auth_val:
            token_val = authentication.get_token(auth_val)
            response = make_response(jsonify({"status": "success"}))
            response.set_cookie("token", token_val, httponly=True)
            return response
        else:
            return {"status": "invalid user"}, 401
    else:
        return {"response", "bad request"}, 400


@app.route("/api/upload", methods=["POST"])
def upload_api():
    if request.files:
        saved_file = request.files["upload"]
        saved_file.save(os.path.join("../uploads", uuid.uuid4().hex))
        return {"status": "success"}, 200
    return {"status": "bad request"}, 400
