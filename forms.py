from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, DateField


class BookForm(FlaskForm):
  name_book = StringField('name_book')
  autor = StringField('autor') 
  discription = TextAreaField('discription')
  done = BooleanField('done', default=False)
  date = DateField('date')

  