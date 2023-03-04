import json


class Books:
  def __init__(self):
    try:
      with open("books.json", "r") as f:
        self.books = json.load(f)
    except FileNotFoundError:
      self.books = []

  def all(self):
    return self.books

  def get(self, id):
    return self.books[id]

  def create(self, data):
    self.books.append(data)

  def save_all(self):
    with open("books.json", "w") as f:
      json.dump(self.books, f)

  def update(self, id, data):
    data.pop('csrf_token')
    self.book[id] = data
    self.save_all()


books = Books()

books.create(
  data={
      'name_book': 'Изучаем Python',
      'autor': 'Марк Лутц',
      'discription': '',
      'done': False,
      'date': '01.05.2023'
    }
)
books.create(
  data={
      'name_book': 'Автоматизация рутинных задач с помощью Python',
      'autor': 'Эл Свейгарт',
      'discription': '',
      'done': False,
      'date': '01.06.2023'
    }
)
books.create(
  data={ 
      'name_book': 'Python. Книга рецептов',
      'autor': 'Бизли и Джонс',
      'discription': '',
      'done': False,
      'date': '01.07.2023'
    }
 )