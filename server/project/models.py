from server.project import db


class User(db.Model):
  table_name = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  userName = db.Column(db.String(255), nullable=False, unique=True)
  password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  phone = db.Column(db.String(10), nullable=True)
  role = db.Column(db.String(10), nullable=False)

  def __init__(self, userName, email, password, phone, role):
    self.userName = userName
    self.password = password
    self.email = email
    self.phone = phone
    self.role = role

  def __repr__(self):
    return f'User ({self.userName})'



