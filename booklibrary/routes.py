from flask import render_template
from booklibrary import app, db
from booklibrary.models import Category, Book



@app.route("/")
def home():
    return render_template("home.html")

    
@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    return render_template('add_category.html')