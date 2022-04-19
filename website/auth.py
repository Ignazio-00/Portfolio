from crypt import methods
from unicodedata import name
from wsgiref.simple_server import WSGIRequestHandler
from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")


@auth.route("/home", methods=["GET", "POST"])
def home():
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    print(email)
    print(username)
    print(password1)
    print(password2)
    return render_template("home.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("views.index"))
