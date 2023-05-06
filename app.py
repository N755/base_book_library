from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean
from sqlalchemy import create_engine
from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, IntegerField, BooleanField, validators
from flask_sqlalchemy import SQLAlchemy
from database import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.app_context().push()
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
migrate = Migrate(app, db)


db.init_app(app)


class Book(db.Model):
    id = Column(Integer)
    title = Column(String, primary_key=True)
    author = Column(String)
    publisher = Column(String)
    year = Column(Integer)
    pages = Column(Integer)
    borrowed = Column(Boolean, default=False, nullable=False, autoincrement=True)

    def __repr__(self):
        return f"<book {self.title}>"


db.create_all()


class BookForm(Form):
    title = StringField("Title", [validators.Length(min=1, max=50)])
    author = StringField("Author", [validators.Length(min=1, max=50)])
    publisher = StringField("Publisher", [validators.Length(min=1, max=50)])
    year = IntegerField(
        "Year of publication", [validators.NumberRange(min=1000, max=9999)]
    )
    pages = IntegerField("Number of pages", [validators.NumberRange(min=1)])
    borrowed = BooleanField("Is borrowed?")


@app.route("/", methods=["GET", "POST"])
def add_book():
    form = BookForm()
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        publisher = request.form["publisher"]
        year = request.form["year"]
        pages = request.form["pages"]
        borrowed = request.form.get("borrowed", False, type=bool)
        db.session.add(
            Book(
                title=title,
                author=author,
                publisher=publisher,
                year=year,
                pages=pages,
                borrowed=borrowed,
            )
        )
        db.session.commit()
        flash("Book added successfully.")
        return redirect("/")
    else:
        books = Book.query.all()
    return render_template("books.html", books=books, form=form)


with app.app_context():
    if __name__ == "__main__":
        app.run(debug=True)
