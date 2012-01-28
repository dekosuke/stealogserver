#/usr/bin/env python
# coding:utf-8

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master.db'

class User(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), unique=True)
  authority = db.Column(db.Float, unique=False)
  reviews = db.relationship("Review", backref=db.backref('User'))
  def __init__(self, name, authority):
    self.name = name
    self.authority = authority
  def __repr__(self):
    return '<User %r>' % self.name

class Restaurant(db.Model):
  __tablename__ = 'Restaurant'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), unique=True)
  reviews = db.relationship("Review", backref=db.backref('Restaurant'))
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return '<Restaurant %r>' % self.name

class Review(db.Model):
  __tablename__ = 'Review'
  id = db.Column(db.Integer, primary_key=True)
  score = db.Column(db.Float, unique=False)
  user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
  restaurant_id = db.Column(db.Integer, db.ForeignKey("Restaurant.id"))
  user = db.relationship("User")
  restaurant = db.relationship("Restaurant")
  def __init__(self, user, restaurant, score):
    self.user=user
    self.restaurant=restaurant
    self.score = score
  def __repr__(self):
    return '<Review %r>' % self.id

if __name__ == "__main__":
  pass
  #init_db()
