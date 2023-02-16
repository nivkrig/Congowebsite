import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology


# Configure application
app = Flask(__name__)

# Custom filter


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///finance.db")
#  connect to sqlite database

#create a cursor object that sends commands to SQL


# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Show portfolio of stocks"""
    return render_template("index.html")


@app.route("/ONUC", methods=["GET", "POST"])
def ONUC():
    """Buy shares of stock"""
    return render_template("ONUC.html")

@app.route("/MON")
def MON():
    """Show history of transactions"""
    return render_template("MON.html")

@app.route("/cite")
def cite():
    """Show history of transactions"""
    return render_template("cite.html")
        