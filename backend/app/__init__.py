import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
import json


from api.v1.consume_itunes import get_response

app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
app.config["MONGO_URI"] = "mongodb://localhost:27017/Database"
mongo = PyMongo(app)


@app.route("/")
def index():
    users = mongo.db.Users
    users.insert(
        {
            # "Email": request.form["Email"],
            "Email": 0,
        }
    )
    return "yes"
    # return render_template("Login.html", title="Home", url=os.getenv("URL"))


@app.route("/browse")
def contact():
    return render_template("Browse.html", title="Browse", url=os.getenv("URL"))


@app.route("/review")
def projects():
    return render_template("Review.html", title="Review", url=os.getenv("URL"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.Users
        existing_user = users.find_one({"Username": request.form["username"]})
        password = request.form.get("password")

        # Check if the user does not exist and register it
        if existing_user is None:
            # Hash the password
            hashpass = generate_password_hash(password)

            # Insert in name username, and password the hash password
            # Since the password is hashed, it becomes a byte object, we need to transform it to string, therefore we decode it
            users.insert(
                {
                    # "Email": request.form["Email"],
                    "Email": 0,
                    "Username": request.form["username"],
                    "Password": hashpass,
                }
            )
            return redirect(url_for("login"))
        # Existing user was not none
        return "That username already exists!"

    return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        users = mongo.db.Users
        error = None
        user = users.find_one({"Username": request.form["username"]})

        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

        if error is None:
            return "Login Successful", 200
        else:
            return error, 418

    return render_template("login.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        query = request.form["search"]

        ok, response = get_response(query=query)

        return json.dumps(response), 200

    return render_template("search.html", title="Search", url=os.getenv("URL"))


@app.route("/health")
def health():
    return "it has health", 200
