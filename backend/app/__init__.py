
import os
import pickle
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from api.v1.consume_itunes import get_response, send_data_cache, get_data_cache, check_data_cache

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Database"
mongo = PyMongo(app)



@app.route("/")
def index():
    return render_template("index.html", title="Welcome", url=os.getenv("URL")), 200


@app.route("/browse")
def browse():
    return render_template("Browse.html", title="Browse", url=os.getenv("URL"))


@app.route("/review")
def review():
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

        password = request.form.get("password")
        error = None

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["Password"], password):
            error = "Incorrect password."

        if error is None:
            return "Login Successful", 200
        else:
            return error, 418

    return render_template("login.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    results = None
    if request.method == "GET":
        return render_template("search.html", title="Search", url=os.getenv("URL"))
        
    if request.method == "POST":
        query = request.form["search"]
        response = check_data_cache(query)
        result = response['results']
        if response is None:
            return render_template("404.html", title="Error", url=os.getenv("URL"))

       
    return render_template("results.html", title="Results", url=os.getenv("URL"), result=result)


@app.route("/health")
def health():
    return "it has health"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Login"), 404
