from booklibrary import db


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), unique=True, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)


    def __str__(self):
        # represent itself in the form of a string
        return self.book_title