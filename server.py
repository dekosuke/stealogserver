#!/usr/bin/python
# coding:utf-8

from flask import Flask,request,jsonify,Response
from jinja2 import FileSystemLoader
from functools import wraps

app = Flask(__name__)
app.jinja_loader = FileSystemLoader('./template/')

import tabelogSearch as ts

def check_auth(username, password):
  return username=="aaaa" and password=="aaaa"

def authenticate():
  """Sends a 401 response that enables basic auth"""
  return Response(
  'Could not verify your access level for that URL.\n'
  'You have to login with proper credentials', 401,
  {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
      return authenticate()
    return f(*args, **kwargs)
  return decorated

#伝票入力ページ
@app.route('/', methods=['GET', 'POST'])
@requires_auth
def input():
  auth = request.authorization
  if request.method in ['GET','POST']:
    return ts.main()
  else:
    return ts.main()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
