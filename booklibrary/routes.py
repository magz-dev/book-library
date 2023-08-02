from flask import render_template, request, redirect, url_for
from booklibrary import app, db
from booklibrary.models import Category, Book

    # route

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template('add_category.html')


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        book = Book(
            book_title=request.form.get("book_title"),
            book_author=request.form.get("book_author"),
            book_description=request.form.get("book_description"),
            current_status=request.form.get("current_status"),
            category_id=request.form.get("category_id"),

        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("books"))
    return render_template('add_book.html', categories=categories)


@app.route("/books")
def books():
    books = list(Book.query.order_by(Book.book_title).all())
    return render_template("books.html", books=books)

    