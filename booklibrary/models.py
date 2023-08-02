from booklibrary import db


class Category(db.Model):
    # schema for the category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=True, nullable=False)
    books = db.relationship("Book", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # represent itself in the form of a string
        return self.category_name


class Book(db.Model):
    # schema for the book model
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(45), unique=True, nullable=False)
    book_author = db.Column(db.String(60), nullable=False)
    book_description = db.Column(db.Text, nullable=False)
    current_status = db.Column(db.String(15), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # represent itself in the form of a string
        return f"#{self.id} - Book:{self.book_title} | Author:{self.book_author} | Status:{self.current_status}"
