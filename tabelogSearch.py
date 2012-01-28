#!/usr/bin/python
# coding:utf-8

#simple static html
from flask import render_template, request
from db_model import db, User, Restaurant, Review

def main():
  is_submit = request.args.get('subm') #ないとNoneが返る
  if is_submit: #投稿モード
    #DBの更新をする
    searchUrl = request.args.get('searchurl') #検索対象のURL
    import re
    print searchUrl
    p = re.compile("A([0-9]+)/A([0-9]+)/([0-9]+)")
    m = p.search(searchUrl)
    if m:
      name = "tA"+m.group(1)+"_A"+m.group(2)+"_"+m.group(3)
      #name = "tA1318_A131807_13122218"
    else:
      return "食べログのURL形式が不正です（東京の店しか受け付けていません） <br><a href=\".\">戻る</a>"

    print "name=|"+name+"|"

    restaurant = Restaurant.query.filter_by(name=name).first()

    authoritySum=0.0
    score=0.0
    if restaurant == None:
      return "店が見つかりませんでした <br><a href=\".\">戻る</a>"
    elif len(restaurant.reviews)==0:
      score="--"
    else:
      for review in restaurant.reviews:
        score+=review.score*review.user.authority
        authoritySum+=review.user.authority
      score/=authoritySum
    return render_template("searchForm.html", reviews=restaurant.reviews, score=score)
  else:
    return render_template("searchForm.html", reviews=[],score=None)
