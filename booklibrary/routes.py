from flask import render_template, request, redirect, url_for
from booklibrary import app, db
from booklibrary.models import Category, Book


@app.route("/")
def home(): 
    # loading the home page
    return render_template("home.html")


@app.route("/categories")
def categories():
    # displaying categories
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # creating new categories in database
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template('add_category.html')


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # updating categories
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    # deleting categories
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    # adding new books to database
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
        return redirect(url_for("home"))
    return render_template('add_book.html', categories=categories)


@app.route("/books")
def books():
    # displaying books
    books = list(Book.query.order_by(Book.book_title).all())
    return render_template("books.html", books=books)


@app.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    # editing new books to database
    book = Book.query.get_or_404(book_id)
    categories = list(Book.query.order_by(Book.book_title).all())
    if request.method == "POST":
        book.book_title = request.form.get("book_title"),
        book.book_author = request.form.get("book_author"),
        book.book_description = request.form.get("book_description"),
        book.current_status = request.form.get("current_status"),
        category_id = request.form.get("category_id"),
        db.session.commit()
    return render_template('edit_book.html', book=book, categories=categories)


