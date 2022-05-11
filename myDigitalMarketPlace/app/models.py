from app import db
from datetime import datetime
#from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post')#, backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.username} {self.email}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body= db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<User ID: {self.user_id} {self.body}>'


class Product1(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  productname = db.Column(db.String(64),unique = False)
  productprice = db.Column(db.Float,unique = False)
  productdescription = db.Column(db.String(500),unique=False)
  productimage = db.Column(db.String(500),unique=False)
  def __repr__(self):
      return f'<Product: {self.productname}>'

class Cart(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  productname = db.Column(db.String(64),unique = False)
  productprice = db.Column(db.Float,unique = False)
  productimage = db.Column(db.String(500),unique=False)
  def __repr__(self):
      return f'<Product: {self.productname}>'
