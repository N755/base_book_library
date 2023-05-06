from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, IntegerField, validators
from flask_sqlalchemy import SQLAlchemy
from database import db

app = Flask(__name__)
app.app_context().push()
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

class Book(db.Model):
    title = Column(String, primary_key=True)
    author = Column(String)
    publisher = Column(String)
    year = Column(Integer)
    pages = Column(Integer)

    def __repr__(self):
        return f'<book {self.title}>'

db.create_all()

class BookForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=50)])
    author = StringField('Author', [validators.Length(min=1, max=50)])
    publisher = StringField('Publisher', [validators.Length(min=1, max=50)])
    year = IntegerField('Year of publication', [validators.NumberRange(min=1000, max=9999)])
    pages = IntegerField('Number of pages', [validators.NumberRange(min=1)])

@app.route('/', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publisher = request.form['publisher']
        year = request.form['year']
        pages = request.form['pages']
        db.session.add(Book(title=title, author=author, publisher=publisher, year=year, pages=pages))
        db.session.commit()
        flash('Book added successfully.')
        return redirect('/')
    else:
        books = Book.query.all()
        return render_template('books.html', form=form, books=books)


with app.app_context():
    if __name__ == '__main__':
        app.run(debug=True)


# @app.route('/', methods=['GET'])
# def get_books():
#     form = BookForm(request.form)
#     books = get_books_from_csv()
#     return render_template('books.html', books=books, form=form)


