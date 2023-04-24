from flask import render_template
from booklibrary import app, db
from booklibrary.models import Books


@app.route("/")
def home():
    return render_template("base.html")