from flask import render_template
from booklibrary import app, db
from booklibrary.models import Category, Book


@app.route("/")
def home():
    return render_template("books.html")