#/usr/bin/python
# coding:utf-8

#DB再構築するよ
import sys, os, unittest
from db_model import db, User, Restaurant, Review

def makeDB(filename):
  try:
    os.remove("master.db") #DB削除
  except:
    print "failed to delete master.db"
  db.create_all() #DB初期化
  restaurants = {}
  users = {}
  reviews = {}
  lines = [l.strip() for l in file(filename, "r").readlines()]
  i=0
  uu,dupu=0,0
  for line in lines:
    elems = line.split(":")
    if i%1000 == 0:
      print elems
    if elems[0]=="shop":
      name = elems[1]
      restaurants[name] = Restaurant(name)
      db.session.add(restaurants[name])
    elif elems[0]=="authority":
      name = elems[1]
      authority = elems[2]
      if users.has_key(name):
        dupu+=1
      else:
        uu+=1
        users[name] = User(name, authority)
        db.session.add(users[name])
    elif elems[0]=="review":
      username = elems[2]
      restaurantname = elems[1]
      score = elems[3]
      review = Review(users[username], restaurants[restaurantname], score)
      db.session.add(review)
    i+=1
  print "user=",uu, "dupuser=",dupu
  print "writing on db..."
  db.session.commit()
  print u"DBの再初期化が完了しました" 

if __name__ == "__main__":
  makeDB(sys.argv[1])
