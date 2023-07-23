from flask import render_template, request, redirect, url_for
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
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template('add_category.html')