from booklibrary import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=True, nullable=False)
    books = db.relationship("Task", backref="category", cascade="all, delete")
 
    def __repr__(self):
        # represent itself in the form of a string
        return self.category_name


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), unique=True, nullable=False)
    book_author = db.Column(db.String(30), nullable=False)
    current_status = db.Column(db.Boolean, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # represent itself in the form of a string
        return f"#{self.id} - Book:{self.book_title}|Author:{self.book_author}|Status:{self.current_status}"